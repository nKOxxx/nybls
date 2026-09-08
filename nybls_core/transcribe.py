"""Transcript: platform captions when they exist, local whisper only when they don't.

Captions cover the large majority of YouTube videos and cost nothing but the
fetch, so whisper is a fallback rather than a requirement. Models are downloaded
on demand, and the default is small on purpose: a 1.5 GB download before a tool
does anything is an adoption tax most people decline to pay.
"""
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

MODEL_DIR = Path.home() / ".nybls" / "models"
BASE_URL = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main"

# name -> (file, approx MB, note) , sizes verified against the CDN 2026-09-02
MODELS = {
    "tiny":   ("ggml-tiny.en.bin", 74, "fastest, English only"),
    "base":   ("ggml-base.en.bin", 141, "default, good balance, English only"),
    "small":  ("ggml-small.en.bin", 465, "more accurate, English only"),
    "turbo":  ("ggml-large-v3-turbo.bin", 1549, "most accurate, all languages"),
}
DEFAULT_MODEL = "base"
MIN_WORDS_PER_MIN = 30.0      # below this the audio is silent or near-silent
MIN_DISTINCT_PER_MIN = 9.0    # enough words but no vocabulary means the model is inventing

TAG_RE = re.compile(r"<[^>]+>")
TS_LINE_RE = re.compile(r"(\d+):(\d+):(\d+)\.\d+\s+-->")


def _fmt(seconds: float) -> str:
    return f"[{int(seconds // 60):02d}:{int(seconds % 60):02d}]"


def have_whisper() -> bool:
    return shutil.which("whisper-cli") is not None


def model_path(name: str = DEFAULT_MODEL, autodownload: bool = True) -> Path:
    if name not in MODELS:
        raise ValueError(f"unknown model {name!r}; choose from {', '.join(MODELS)}")
    fname, size_mb, _ = MODELS[name]
    dest = MODEL_DIR / fname
    if dest.exists():
        return dest
    if not autodownload:
        raise FileNotFoundError(f"model {name} not downloaded")
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    print(f"this video has no captions, so it needs local transcription.\n"
          f"downloading the '{name}' speech model once ({size_mb} MB)...", file=sys.stderr)
    tmp = dest.with_suffix(".part")
    r = subprocess.run(["curl", "-fL", "--progress-bar", "-o", str(tmp), f"{BASE_URL}/{fname}"])
    if r.returncode != 0 or not tmp.exists():
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"model download failed; retry, or fetch {BASE_URL}/{fname} manually")
    tmp.rename(dest)
    return dest


# ── captions ─────────────────────────────────────────────────────────────────

def _pick_vtt(vtts: list[Path]) -> Path:
    """Prefer English; alphabetical order is not a language policy."""
    for v in vtts:
        if ".en" in v.name:
            return v
    return vtts[0]


def condense_vtt(vtt: Path) -> list[tuple[float, str]]:
    """Parse VTT into (start_seconds, text), dropping rolling-caption repeats."""
    segs: list[tuple[float, str]] = []
    start = None
    seen_tail = ""
    for line in vtt.read_text(errors="replace").splitlines():
        m = TS_LINE_RE.match(line.strip())
        if m:
            h, mi, s = (int(x) for x in m.groups())
            start = h * 3600 + mi * 60 + s
            continue
        # VTT carries HTML entities, and YouTube's auto-captions use "&gt;&gt;"
        # as a speaker marker. Left raw, 288 of 1,666 segments in one real
        # 67-minute transcript read as "&gt;&gt;" instead of ">>", which is
        # noise in every quote and in anything the verifier matches against.
        text = html.unescape(TAG_RE.sub("", line)).strip()
        if not text or start is None or text.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        if text in seen_tail:
            continue
        segs.append((float(start), text))
        seen_tail = text
    return segs


# ── whisper fallback ─────────────────────────────────────────────────────────

def whisper(video: Path, out_dir: Path, model: str = DEFAULT_MODEL, lang: str = "auto") -> list[tuple[float, str]]:
    wav = out_dir / "audio16k.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-ar", "16000", "-ac", "1", str(wav)],
        check=True, timeout=600,
    )
    r = subprocess.run(
        ["whisper-cli", "-m", str(model_path(model)), "-f", str(wav), "-l", lang, "-np"],
        capture_output=True, text=True, timeout=3600,
    )
    wav.unlink(missing_ok=True)
    segs = []
    for line in r.stdout.splitlines():
        m = re.match(r"\[(\d+):(\d+):(\d+)\.\d+ -->.*?\]\s+(.*)", line)
        if m:
            h, mi, s, text = int(m[1]), int(m[2]), int(m[3]), m[4].strip()
            if text:
                segs.append((float(h * 3600 + mi * 60 + s), text))
    return segs


# Words that carry no information about a video's subject. Same list the
# modality benchmark used, so the guard below is measured on the same terms.
_STOP = {"the", "and", "for", "you", "your", "this", "that", "with", "from", "are",
         "was", "not", "but", "have", "has", "had", "can", "will", "all", "its",
         "it's", "they", "them", "their", "our", "out", "get", "got", "one", "two",
         "new", "now", "how", "why", "what", "when", "who"}


def word_rates(segs: list[tuple[float, str]], duration_s: float) -> tuple[float, float]:
    """Words per minute, and distinct informative words per minute.

    Two numbers because whisper fails in two opposite ways and neither number
    catches both. Silence produces almost no words at all. A hallucinating model
    produces plenty, at a normal rate, but keeps circling a tiny vocabulary, so
    it hides inside the first number and only shows up in the second.
    """
    total = 0
    seen: set[str] = set()
    for _, text in segs:
        toks = re.sub(r"[^a-z0-9']+", " ", text.lower()).split()
        total += len(toks)
        for w in toks:
            if len(w) >= 3 and w not in _STOP:
                seen.add(w)
    mins = max(duration_s, 1.0) / 60.0
    return total / mins, len(seen) / mins


def _mostly_unspaced_script(segs: list[tuple[float, str]]) -> bool:
    """Chinese, Japanese and Thai do not put spaces between words, so counting
    them would report a near-zero rate for a perfectly good transcript. The rate
    guard is validated on space-separated scripts only, so skip those.
    """
    text = "".join(t for _, t in segs)
    if not text:
        return False
    cjk = sum(1 for ch in text if "\u3040" <= ch <= "\u9fff" or "\u0e00" <= ch <= "\u0e7f")
    return cjk / len(text) > 0.15


def looks_degenerate(segs: list[tuple[float, str]]) -> str | None:
    """Whisper on audio it cannot handle does not fail, it loops.

    Run an English-only model over Hindi, or any model over music, and it emits
    the same line hundreds of times and reports success. Measured on a real
    25-minute video: one identical line repeated for 23 of them, presented as a
    healthy transcript. A silent wrong answer is worse than a loud failure, so
    detect the loop and say so.
    """
    words = sum(len(t.split()) for _, t in segs)
    dur = (segs[-1][0] - segs[0][0]) if len(segs) > 1 else 0.0

    # A near-empty transcript is the other half of the same failure. Fed silence
    # or music, whisper does not return nothing - it returns a stock politeness.
    # Four real Instagram reels, all silent screen recordings, produced exactly
    # one line each: "Thank you.", "We'll see you next time.", "We'll be right
    # back.", and a Spanish request to subscribe. All were reported as healthy.
    joined = " ".join(t.strip().lower() for _, t in segs)
    HALLUCINATED = (
        "thank you", "thanks for watching", "we'll see you next time",
        "we'll be right back", "subscribe", "suscr\u00edbete", "bye",
        "please subscribe", "you", "\u266a",
    )
    stripped = joined.strip(" .!?\u00a1\u00bf,")
    if words <= 12 and any(stripped == h or stripped.startswith(h) for h in HALLUCINATED):
        return (f"the entire transcript is {words} words of stock filler "
                f"({joined[:48]!r}), the audio is almost certainly silent or music only")

    if len(segs) < 20:
        return None
    lines = [t.strip().lower() for _, t in segs]
    unique = len(set(lines))
    if unique / len(lines) < 0.25:
        return (f"only {unique} distinct lines in {len(lines)}, the model looped, "
                f"which usually means the audio is not the model's language")
    longest = worst = 1
    for a, b in zip(lines, lines[1:]):
        longest = longest + 1 if a == b else 1
        worst = max(worst, longest)
    if worst >= 12:
        return f"one line repeated {worst} times consecutively, the model looped"

    # These go last because they are the general case and the checks above are
    # specific. They catch what those cannot: a transcript of varied nonsense
    # that never repeats, and one where every line is unique only because each
    # carries its own timestamp. Both scored a perfect 1.000 on the line ratio
    # and were reported healthy.
    #
    # Thresholds measured across 24 videos of at least 30 seconds. Real speech
    # runs 119 to 249 words per minute; the sparsest genuine narration we have,
    # a teardown with long silent stretches and a deliberately quiet coding
    # stream, still reach 49 and 63, while every silent video sits at 14 or
    # below. The vocabulary check is the tighter of the two: a real ASR failure
    # sits at 7.5 distinct words per minute and the nearest healthy video at
    # 11.2, so 9 splits a gap of only 1.5x. Long videos on one narrow subject
    # push this number down honestly, which is why it only applies when the
    # model produced a normal volume of words in the first place.
    if not _mostly_unspaced_script(segs) and dur >= 30:
        wpm, distinct = word_rates(segs, dur)
        if wpm < MIN_WORDS_PER_MIN:
            return (f"only {wpm:.0f} words per minute, against {MIN_WORDS_PER_MIN:.0f} for "
                    f"the sparsest real narration we have measured. The audio is silent or "
                    f"nearly so, and the frames are the only place the content exists")
        if distinct < MIN_DISTINCT_PER_MIN:
            return (f"{wpm:.0f} words per minute but only {distinct:.1f} distinct content "
                    f"words per minute. The model produced fluent text from audio it could "
                    f"not hear; treat none of it as evidence")
    return None


def build_transcript(media_id: str, ws: Path, video: Path,
                     model: str = DEFAULT_MODEL) -> tuple[Path | None, str]:
    vtts = sorted(ws.glob("*.vtt"))
    if vtts:
        vtt = _pick_vtt(vtts)
        segs, source = condense_vtt(vtt), f"captions:{vtt.name}"
    elif not have_whisper():
        return None, ("none, no captions on this video, and whisper-cli is not installed. "
                      "Frames still work; for speech install it with: brew install whisper-cpp")
    else:
        segs, source = whisper(video, ws, model), f"whisper:{model}"
    if not segs:
        return None, "none"
    out = ws / "transcript.txt"
    out.write_text("\n".join(f"{_fmt(t)} {text}" for t, text in segs))

    if source.startswith("whisper"):
        problem = looks_degenerate(segs)
        if problem:
            hint = ""
            if MODELS[model][0].endswith(".en.bin"):
                hint = (f"  The '{model}' model is English-only. For other languages "
                        f"re-run with --model turbo.")
            source = f"{source}, UNRELIABLE: {problem}.{hint}"
    return out, source
