"""Mechanical citation verification.

The research is blunt about this: frontier models score ~8% on evidence
grounding while being ~45% right, and every large quality gain in the literature
came from adding a separate checking step rather than from better prompting. So
a claim's citation is never trusted because a model asserted it — it is checked
against the transcript window it points at.

The check is deliberately fuzzy. ASR output is not verbatim, so exact string
matching would fail on correct claims. Instead: take the claim's content words,
look for them in a window around the cited timestamp, and report the fraction
found. Fuzzy overlap in a window is evidence; it is not proof, and the verdicts
are named to keep that distinction visible.
"""
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

WINDOW_BEFORE = 45.0    # generous: speakers introduce a term before defining it
WINDOW_AFTER = 120.0
STRONG, WEAK = 0.55, 0.30   # fraction of content words found in the window
STOP = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "that", "this",
    "these", "those", "is", "are", "was", "were", "be", "been", "being", "to",
    "of", "in", "on", "at", "for", "with", "from", "by", "as", "it", "its",
    "you", "your", "he", "his", "she", "her", "they", "them", "their", "we",
    "our", "i", "my", "not", "no", "do", "does", "did", "can", "will", "would",
    "should", "could", "have", "has", "had", "what", "when", "where", "which",
    "who", "how", "why", "all", "any", "each", "more", "most", "other", "some",
    "such", "only", "own", "same", "so", "up", "out", "about", "into", "over",
}
TS_RE = re.compile(r"^\[(\d+):(\d+)\]\s*(.*)$")


@dataclass
class Verdict:
    claim: str
    at: float
    status: str          # verified | weak | unsupported | out-of-range | no-speech
    coverage: float
    found: list[str]
    missing: list[str]


def load_transcript(path: Path) -> list[tuple[float, str]]:
    segs = []
    for line in path.read_text(errors="replace").splitlines():
        m = TS_RE.match(line.strip())
        if m:
            segs.append((float(int(m[1]) * 60 + int(m[2])), m[3]))
    return segs


def _stem(w: str) -> str:
    """Crude suffix stripping. ASR output and a written claim rarely agree on
    word form ("ask"/"asking", "save"/"saves"), and penalising that produces
    false negatives on claims that are perfectly well supported."""
    for suf in ("ing", "ed", "es", "s"):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def _normalise(text: str) -> str:
    """A transcript writes 90%; a claim writes '90 percent'. Same fact."""
    return text.lower().replace("%", " percent ")


def _content_words(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9']+", _normalise(text))
    return [_stem(w) for w in words if len(w) >= 4 and w not in STOP]


def window_text(segs: list[tuple[float, str]], at: float) -> str:
    lo, hi = at - WINDOW_BEFORE, at + WINDOW_AFTER
    return " ".join(t for ts, t in segs if lo <= ts <= hi)


def _no_usable_speech(segs: list[tuple[float, str]]) -> bool:
    """Distinguish "the video said something else" from "the video said nothing".

    A silent screen recording yields one line of whisper filler. Scoring a claim
    against that returns 0% coverage, which reads identically to a fabrication —
    so the verifier would mark a claim that is plainly true on screen as
    unsupported, and an honest agent would delete it. Measured: a correct claim
    about a medallion pipeline scored 0.0 against a one-line transcript.
    """
    from .transcribe import looks_degenerate
    if not segs:
        return True
    return looks_degenerate(segs) is not None


def verify_claim(segs: list[tuple[float, str]], claim: str, at: float) -> Verdict:
    if _no_usable_speech(segs):
        # Not a failure of the claim — a failure of this method to apply. The
        # claim needs a frame citation, which the transcript can never supply.
        return Verdict(claim, at, "no-speech", 0.0, [], [])
    if at > segs[-1][0] + WINDOW_AFTER or at < -1:
        return Verdict(claim, at, "out-of-range", 0.0, [], [])
    words = _content_words(claim)
    if not words:
        return Verdict(claim, at, "unsupported", 0.0, [], [])
    hay = " ".join(_stem(w) for w in re.findall(r"[a-z0-9']+", _normalise(window_text(segs, at))))
    found = [w for w in words if w in hay]
    cov = len(found) / len(words)
    status = "verified" if cov >= STRONG else ("weak" if cov >= WEAK else "unsupported")
    return Verdict(claim, at, status, round(cov, 2), found,
                   [w for w in words if w not in found])


def verify_file(transcript: Path, claims_path: Path) -> list[Verdict]:
    """claims.json: [{"claim": "...", "at": 242.0}, ...] — `at` in seconds."""
    segs = load_transcript(transcript)
    claims = json.loads(claims_path.read_text())
    return [verify_claim(segs, c["claim"], float(c["at"])) for c in claims]


def report(verdicts: list[Verdict]) -> str:
    mark = {"verified": "✓", "weak": "~", "unsupported": "✗",
            "out-of-range": "?", "no-speech": "▣"}
    lines = []
    for v in verdicts:
        ts = f"{int(v.at // 60):02d}:{int(v.at % 60):02d}"
        lines.append(f"  {mark[v.status]} [{ts}] {v.coverage:>4.0%}  {v.claim[:66]}")
        if v.status in ("weak", "unsupported") and v.missing:
            lines.append(f"        not found near this timestamp: {', '.join(v.missing[:8])}")
        if v.status == "no-speech":
            lines.append("        no usable speech in this video — speech cannot "
                         "confirm or deny this; cite a frame instead")
    n = len(verdicts) or 1
    ok = sum(1 for v in verdicts if v.status == "verified")
    weak = sum(1 for v in verdicts if v.status == "weak")
    mute = sum(1 for v in verdicts if v.status == "no-speech")
    bad = n - ok - weak - mute
    tail = f" · {mute} not checkable by speech" if mute else ""
    denom = n - mute
    if denom <= 0:
        # Everything was unjudgeable. Printing "0/1 verified · 0% clean" here
        # reads as total failure when the truth is that this method does not
        # apply at all to this material.
        lines.append(f"\n  0 of {n} claims can be judged by speech — this video has "
                     f"none. Verify these against frames.")
    else:
        lines.append(f"\n  {ok}/{denom} verified · {weak} weak · {bad} unsupported{tail} "
                     f"({ok / denom:.0%} clean of what speech can judge)")
    return "\n".join(lines)


def to_json(verdicts: list[Verdict]) -> str:
    return json.dumps([asdict(v) for v in verdicts], indent=1)
