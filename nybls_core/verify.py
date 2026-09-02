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
    status: str          # verified | weak | unsupported | out-of-range
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


def verify_claim(segs: list[tuple[float, str]], claim: str, at: float) -> Verdict:
    if not segs or at > segs[-1][0] + WINDOW_AFTER or at < -1:
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
    mark = {"verified": "✓", "weak": "~", "unsupported": "✗", "out-of-range": "?"}
    lines = []
    for v in verdicts:
        ts = f"{int(v.at // 60):02d}:{int(v.at % 60):02d}"
        lines.append(f"  {mark[v.status]} [{ts}] {v.coverage:>4.0%}  {v.claim[:66]}")
        if v.status in ("weak", "unsupported") and v.missing:
            lines.append(f"        not found near this timestamp: {', '.join(v.missing[:8])}")
    n = len(verdicts) or 1
    ok = sum(1 for v in verdicts if v.status == "verified")
    weak = sum(1 for v in verdicts if v.status == "weak")
    bad = n - ok - weak
    lines.append(f"\n  {ok}/{n} verified · {weak} weak · {bad} unsupported "
                 f"({ok / n:.0%} clean)")
    return "\n".join(lines)


def to_json(verdicts: list[Verdict]) -> str:
    return json.dumps([asdict(v) for v in verdicts], indent=1)
