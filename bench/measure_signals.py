"""Measure candidate change-detection signals against an independent reference.

The claim under test is a design decision inside nybls: a perceptual hash is the
wrong signal for detecting that a video's *content* changed, and mean absolute
pixel difference is the right one. That claim was originally made from a single
observation on one chess lesson. This script tests it properly.

Method. Probe each video on a fixed clock. From each probe compute two candidate
cheap signals against the previous probe:

  phash  - Hamming distance between 64-bit perceptual hashes (the signal nybls
           originally used, and still uses for near-duplicate detection)
  pixdiff- mean absolute difference of 192px grayscale pixels (the replacement)

Neither is the ground truth. The reference signal is independent of both: the
set of words Apple Vision OCR reads on screen, compared between consecutive
probes by Jaccard distance. On instructional, screen-capture and title-card
content, the on-screen text changing IS the information changing, and OCR knows
nothing about either candidate signal. A pair is labelled a CONTENT CHANGE when
its OCR Jaccard distance exceeds --ocr-threshold.

We then ask of each candidate: how well does it rank content changes above
non-changes? Reported as AUC (probability that a randomly chosen changed pair
scores above a randomly chosen unchanged pair; 0.5 = coin flip), computed from
the Mann-Whitney U statistic with no external dependency.

Usage:  python bench/measure_signals.py <media_id> [--every 10] [--out results.json]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import imagehash  # reference implementation; install with `pip install nybls[bench]`
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nybls_core.store import read_manifest, workspace  # noqa: E402


def _video_path(ws: Path) -> Path:
    vids = [p for p in list(ws.glob("video.*")) + list(ws.glob("media*"))
            if p.suffix.lower() in {".mp4", ".webm", ".mkv", ".mov", ".m4v"}]
    if not vids:
        raise SystemExit(f"no video file in {ws}")
    return vids[0]


def _ocr_words(img_path: Path) -> set[str]:
    from ocrmac import ocrmac
    try:
        res = ocrmac.OCR(str(img_path), language_preference=["en-US"]).recognize()
    except Exception:
        return set()
    words = set()
    for item in res:
        text = item[0] if isinstance(item, (list, tuple)) else str(item)
        conf = item[1] if isinstance(item, (list, tuple)) and len(item) > 1 else 1.0
        if isinstance(conf, (int, float)) and conf < 0.5:
            continue
        for w in str(text).lower().split():
            w = "".join(c for c in w if c.isalnum())
            if len(w) >= 3:
                words.add(w)
    return words


def _jaccard_distance(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 0.0
    return 1.0 - len(a & b) / len(a | b)


def auc(pos: list[float], neg: list[float]) -> float:
    """AUC via Mann-Whitney U, ties counted as half. No sklearn dependency."""
    if not pos or not neg:
        return float("nan")
    wins = 0.0
    for p in pos:
        for n in neg:
            wins += 1.0 if p > n else (0.5 if p == n else 0.0)
    return wins / (len(pos) * len(neg))


def run(media_id: str, every: float, ocr_threshold: float, probe_w: int = 640) -> dict:
    ws = workspace(media_id)
    man = read_manifest(media_id)
    dur = float(man["duration_s"])
    video = _video_path(ws)
    tmp = ws / "_measure"
    tmp.mkdir(exist_ok=True)

    stamps = [t for t in np.arange(every / 2, dur, every)]
    prev_gray = prev_hash = prev_words = None
    rows = []
    for ts in stamps:
        f = tmp / f"m_{int(ts * 1000)}.png"
        try:
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}", "-i", str(video),
                 "-frames:v", "1", "-vf", f"scale={probe_w}:-2", str(f)],
                check=True, timeout=120,
            )
        except subprocess.CalledProcessError:
            continue
        img = Image.open(f)
        gray = np.asarray(img.convert("L").resize((192, 108)), dtype=np.float32)
        ph = imagehash.phash(img)
        words = _ocr_words(f)
        if prev_gray is not None:
            rows.append({
                "t": round(float(ts), 1),
                "phash_hamming": int(ph - prev_hash),
                "pixdiff": round(float(np.abs(gray - prev_gray).mean()), 4),
                "ocr_jaccard": round(_jaccard_distance(prev_words, words), 4),
                "ocr_words_now": len(words),
            })
        prev_gray, prev_hash, prev_words = gray, ph, words
        f.unlink(missing_ok=True)
    for leftover in tmp.glob("*.png"):
        leftover.unlink(missing_ok=True)
    tmp.rmdir()

    # only pairs where OCR saw text on at least one side can serve as reference
    usable = [r for r in rows if r["ocr_words_now"] > 0]
    pos = [r for r in usable if r["ocr_jaccard"] > ocr_threshold]
    neg = [r for r in usable if r["ocr_jaccard"] <= ocr_threshold]

    ph_all = [r["phash_hamming"] for r in rows]
    px_all = [r["pixdiff"] for r in rows]
    scenes = json.loads((ws / "scenes.json").read_text()) if (ws / "scenes.json").exists() else []

    def q(v, p):
        return round(float(np.percentile(v, p)), 4) if v else None

    return {
        "media_id": media_id,
        "title": man.get("title", ""),
        "duration_s": round(dur, 1),
        "probe_every_s": every,
        "n_pairs": len(rows),
        "n_usable_ocr_pairs": len(usable),
        "n_content_changes": len(pos),
        "n_non_changes": len(neg),
        "ocr_threshold": ocr_threshold,
        "scene_cuts": len(scenes),
        "scene_cuts_per_min": round(len(scenes) / (dur / 60), 2),
        "phash": {"median": q(ph_all, 50), "p90": q(ph_all, 90), "max": q(ph_all, 100),
                  "auc_vs_ocr": round(auc([r["phash_hamming"] for r in pos],
                                          [r["phash_hamming"] for r in neg]), 4)},
        "pixdiff": {"median": q(px_all, 50), "p90": q(px_all, 90), "max": q(px_all, 100),
                    "auc_vs_ocr": round(auc([r["pixdiff"] for r in pos],
                                            [r["pixdiff"] for r in neg]), 4)},
        "rows": rows,
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("media_id")
    ap.add_argument("--every", type=float, default=10.0)
    ap.add_argument("--ocr-threshold", type=float, default=0.5)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    res = run(a.media_id, a.every, a.ocr_threshold)
    out = Path(a.out) if a.out else Path(__file__).parent / "round2" / f"signals_{a.media_id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=1))
    slim = {k: v for k, v in res.items() if k != "rows"}
    print(json.dumps(slim, indent=1))
