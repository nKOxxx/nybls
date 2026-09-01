"""Transcript: prefer downloaded subtitles (condensed), fall back to whisper.cpp."""
import re
import subprocess
from pathlib import Path

MODEL = Path.home() / ".nybls" / "models" / "ggml-large-v3-turbo.bin"
TAG_RE = re.compile(r"<[^>]+>")
TS_LINE_RE = re.compile(r"(\d+):(\d+):(\d+)\.\d+\s+-->")


def _fmt(seconds: float) -> str:
    return f"[{int(seconds // 60):02d}:{int(seconds % 60):02d}]"


def condense_vtt(vtt: Path) -> list[tuple[float, str]]:
    """Parse VTT into (start_seconds, text) segments, deduping rolling captions."""
    segs: list[tuple[float, str]] = []
    start = None
    seen_tail = ""
    for line in vtt.read_text(errors="replace").splitlines():
        m = TS_LINE_RE.match(line.strip())
        if m:
            h, mi, s = (int(x) for x in m.groups())
            start = h * 3600 + mi * 60 + s
            continue
        text = TAG_RE.sub("", line).strip()
        if not text or start is None or text.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        if text in seen_tail:  # rolling-caption duplicate
            continue
        segs.append((float(start), text))
        seen_tail = text
    return segs


def whisper(video: Path, out_dir: Path, lang: str = "auto") -> list[tuple[float, str]]:
    wav = out_dir / "audio16k.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-ar", "16000", "-ac", "1", str(wav)],
        check=True, timeout=600,
    )
    r = subprocess.run(
        ["whisper-cli", "-m", str(MODEL), "-f", str(wav), "-l", lang, "-np"],
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


def _pick_vtt(vtts: list[Path]) -> Path:
    """Prefer English, then anything else (alphabetical is not a language policy)."""
    for v in vtts:
        if ".en" in v.name:
            return v
    return vtts[0]


def build_transcript(video_id: str, ws: Path, video: Path) -> tuple[Path | None, str]:
    vtts = sorted(ws.glob("*.vtt"))
    if vtts:
        vtt = _pick_vtt(vtts)
        segs, source = condense_vtt(vtt), f"subtitles:{vtt.name}"
    else:
        segs, source = whisper(video, ws), "whisper:large-v3-turbo"
    if not segs:
        return None, "none"
    out = ws / "transcript.txt"
    out.write_text("\n".join(f"{_fmt(t)} {text}" for t, text in segs))
    return out, source
