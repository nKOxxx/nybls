"""Cumulative spend ledger, the piece nothing else on the market has.

Each vendor counts image tokens differently, so the ledger stores every image's
pixel size and recomputes tokens for whichever model the reader is billed on.
Prices and formulas below were read from the vendors' documentation on
2026-09-15; the source for each is named so a reader can re-check it.
"""
import json
import math
import os
from pathlib import Path

from PIL import Image

from .store import utc_now

DEFAULT_MODEL = "sonnet-5"


# ── token formulas, one per vendor ───────────────────────────────────────────

def _cells(w: float, h: float) -> int:
    return math.ceil(w / 28) * math.ceil(h / 28)


def _anthropic(w: int, h: int, spec: dict) -> int:
    """Anthropic: ceil(w/28) * ceil(h/28), after the tier's downscale.

    Each tier has a long-edge limit and a visual-token cap; larger images are
    scaled down, aspect preserved, to the largest size that fits both. Standard
    tier (models before Claude 4.7): 1568 px, 1568 tokens. High-resolution tier
    (Claude 4.7 and later): 2576 px, 4784 tokens. Checked against the worked
    table in Anthropic's vision docs, 2026-09-15.
    """
    edge, cap = spec["max_edge"], spec["max_tokens"]
    scale = min(1.0, edge / max(w, h))
    if _cells(w * scale, h * scale) > cap:
        scale = min(scale, math.sqrt(cap * 784 / (w * h)))
        while _cells(w * scale, h * scale) > cap:
            scale *= 0.995
    return _cells(w * scale, h * scale)


def _patches(w: float, h: float) -> int:
    return math.ceil(w / 32) * math.ceil(h / 32)


def _openai_patch(w: int, h: int, spec: dict) -> int:
    """OpenAI patch models: 32px patches times a per-model multiplier, after
    scaling to the model's maximum dimension and patch budget (detail=high).
    Billable tokens are the patch count times the multiplier, rounded up, at
    the model's text input price. OpenAI images-vision guide, 2026-09-15.
    """
    scale = min(1.0, spec["max_edge"] / max(w, h))
    if _patches(w * scale, h * scale) > spec["patch_cap"]:
        scale = min(scale, math.sqrt(spec["patch_cap"] * 1024 / (w * h)))
        while _patches(w * scale, h * scale) > spec["patch_cap"]:
            scale *= 0.995
    return math.ceil(_patches(w * scale, h * scale) * spec["multiplier"])


def _openai_tile(w: int, h: int, spec: dict) -> int:
    """OpenAI tile models: fit in 2048 square, shortest side to 768, 512px tiles."""
    scale = min(1.0, 2048 / max(w, h))
    w, h = w * scale, h * scale
    short = min(w, h)
    if short > 768:
        w, h = w * 768 / short, h * 768 / short
    tiles = math.ceil(w / 512) * math.ceil(h / 512)
    return spec["base"] + spec["per_tile"] * tiles


FORMULAS = {"anthropic": _anthropic, "openai-patch": _openai_patch, "openai-tile": _openai_tile}

# name -> vendor formula, USD per 1M input tokens, formula parameters, source.
A_HI = {"formula": "anthropic", "max_edge": 2576, "max_tokens": 4784,
        "source": "Anthropic vision docs + pricing, 2026-09-15"}
A_STD = {"formula": "anthropic", "max_edge": 1568, "max_tokens": 1568,
         "source": "Anthropic vision docs + pricing, 2026-09-15"}
OA = "OpenAI images-vision guide + pricing, 2026-09-15"

MODELS: dict[str, dict] = {
    "sonnet-5":  {**A_HI, "usd_per_mtok": 2.00},
    "opus-5":    {**A_HI, "usd_per_mtok": 5.00},
    "fable-5.1": {**A_HI, "usd_per_mtok": 10.00},
    "haiku-4.5": {**A_STD, "usd_per_mtok": 1.00},
    "gpt-5.5": {"formula": "openai-patch", "usd_per_mtok": 5.00, "multiplier": 1.2,
                "max_edge": 2048, "patch_cap": 2500, "source": OA},
    "gpt-5.4": {"formula": "openai-patch", "usd_per_mtok": 2.50, "multiplier": 1.2,
                "max_edge": 2048, "patch_cap": 2500, "source": OA},
    "gpt-5.2": {"formula": "openai-patch", "usd_per_mtok": 1.75, "multiplier": 1.2,
                "max_edge": 2048, "patch_cap": 6144, "source": OA},
    "gpt-5.1": {"formula": "openai-tile", "usd_per_mtok": 1.25, "base": 70, "per_tile": 140, "source": OA},
    "gpt-5":   {"formula": "openai-tile", "usd_per_mtok": 1.25, "base": 70, "per_tile": 140, "source": OA},
    "gpt-4.1": {"formula": "openai-tile", "usd_per_mtok": 2.00, "base": 85, "per_tile": 170, "source": OA},
    "gpt-4o":  {"formula": "openai-tile", "usd_per_mtok": 2.50, "base": 85, "per_tile": 170, "source": OA},
    # xAI publishes the price but, on every page reachable on 2026-09-15, no
    # image token formula. The token count below is a stand-in and says so.
    "grok-4.6": {"formula": "openai-patch", "usd_per_mtok": 2.00, "multiplier": 1.0,
                 "max_edge": 2048, "patch_cap": 2500,
                 "unverified": "xAI publishes no image token formula; 32px patches used as a stand-in",
                 "source": "docs.x.ai grok-4.6 model page, 2026-09-15 (price only)"},
}


def budget_for(duration_s: float) -> int:
    return max(8, min(math.ceil(duration_s / 60 * 4), 200))


def image_dims(img_path: Path) -> tuple[int, int]:
    return Image.open(img_path).size


def tokens_for(w: int, h: int, model: str = DEFAULT_MODEL) -> int:
    spec = MODELS[model]
    return FORMULAS[spec["formula"]](w, h, spec)


def est_tokens(img_path: Path, model: str = DEFAULT_MODEL) -> int:
    w, h = image_dims(img_path)
    return tokens_for(w, h, model)


def resolve_model(name: str | None) -> str:
    """Explicit flag, then NYBLS_MODEL, then the default. Unknown names fail loudly."""
    chosen = name or os.environ.get("NYBLS_MODEL") or DEFAULT_MODEL
    if chosen not in MODELS:
        raise ValueError(f"unknown model {chosen!r}; run `nybls ledger --models` for the list")
    return chosen


def record(ws: Path, cmd: str, images: list[Path]) -> dict:
    p = ws / "ledger.json"
    led = json.loads(p.read_text()) if p.exists() else {"entries": [], "images": 0, "tokens": 0}
    dims = [image_dims(i) for i in images]
    tokens = sum(tokens_for(w, h) for w, h in dims)
    led["entries"].append({"utc": utc_now(), "cmd": cmd, "images": len(images),
                           "tokens": tokens, "dims": dims})
    led["images"] += len(images)
    led["tokens"] += tokens
    p.write_text(json.dumps(led, indent=1))
    return led


def _tokens_for_model(led: dict, model: str) -> tuple[int, bool]:
    """Recompute from stored dims. Entries written before dims were stored can
    only be priced at the default model's count; the caller is told."""
    total, exact = 0, True
    for e in led.get("entries", []):
        if "dims" in e:
            total += sum(tokens_for(w, h, model) for w, h in e["dims"])
        else:
            total += e.get("tokens", 0)
            exact = False
    return total, exact


def summary(ws: Path, duration_s: float, total_frames_hint: int | None = None,
            model: str | None = None) -> str:
    p = ws / "ledger.json"
    led = json.loads(p.read_text()) if p.exists() else {"images": 0, "tokens": 0, "entries": []}
    model = resolve_model(model)
    spec = MODELS[model]
    budget = budget_for(duration_s)
    mins = duration_s / 60
    frames_total = total_frames_hint or int(duration_s * 25)
    tokens, exact = _tokens_for_model(led, model)
    cost = tokens / 1_000_000 * spec["usd_per_mtok"]
    note = ""
    if spec.get("unverified"):
        note = " [token formula UNVERIFIED]"
    elif not exact and model != DEFAULT_MODEL:
        note = " [older entries counted at the default model's rate]"
    return (
        f"watched {mins:.0f} min · examined {led['images']} images "
        f"(~{tokens:,} visual tokens, ≈${cost:.2f} at {model} input rate{note}) "
        f"of ~{frames_total:,} total frames · budget {led['images']}/{budget} units"
    )


def models_table() -> str:
    rows = ["model         $/Mtok  image tokens                        source"]
    for name, s in MODELS.items():
        how = {"anthropic": f"28px cells, cap {s.get('max_tokens')} tok",
               "openai-patch": f"32px patches x{s.get('multiplier')}, cap {s.get('patch_cap')}",
               "openai-tile": f"{s.get('base')} + {s.get('per_tile')}/512px tile"}[s["formula"]]
        flag = "  UNVERIFIED" if s.get("unverified") else ""
        rows.append(f"{name:<13} {s['usd_per_mtok']:>6.2f}  {how:<35} {s['source']}{flag}")
    rows.append(f"\ndefault: {DEFAULT_MODEL}. Set NYBLS_MODEL or pass --model. Estimates use each "
                "vendor's published input-token formula and text input rate; they are not invoices.")
    return "\n".join(rows)
