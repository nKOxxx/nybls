"""Cumulative spend ledger — the piece nothing else on the market has."""
import json
import math
from pathlib import Path

from PIL import Image

from .store import utc_now


def budget_for(duration_s: float) -> int:
    return max(8, min(math.ceil(duration_s / 60 * 4), 200))


def est_tokens(img_path: Path) -> int:
    w, h = Image.open(img_path).size
    return math.ceil(w / 28) * math.ceil(h / 28)


def record(ws: Path, cmd: str, images: list[Path]) -> dict:
    p = ws / "ledger.json"
    led = json.loads(p.read_text()) if p.exists() else {"entries": [], "images": 0, "tokens": 0}
    tokens = sum(est_tokens(i) for i in images)
    led["entries"].append({"utc": utc_now(), "cmd": cmd, "images": len(images), "tokens": tokens})
    led["images"] += len(images)
    led["tokens"] += tokens
    p.write_text(json.dumps(led, indent=1))
    return led


def summary(ws: Path, duration_s: float, total_frames_hint: int | None = None) -> str:
    p = ws / "ledger.json"
    led = json.loads(p.read_text()) if p.exists() else {"images": 0, "tokens": 0, "entries": []}
    budget = budget_for(duration_s)
    mins = duration_s / 60
    frames_total = total_frames_hint or int(duration_s * 25)
    cost_sonnet = led["tokens"] / 1_000_000 * 2.0  # $/Mtok input, Sonnet 5
    return (
        f"watched {mins:.0f} min · examined {led['images']} images "
        f"(~{led['tokens']:,} visual tokens, ≈${cost_sonnet:.2f} at Sonnet input rate) "
        f"of ~{frames_total:,} total frames · budget {led['images']}/{budget} units"
    )
