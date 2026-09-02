"""How long is an event actually on screen? Measured, not assumed.

The uniform-grid capture probability vN/D depends on v, the seconds an event is
visible. Estimating v by eye would make the whole analysis an assumption, so we
measure it: sample densely around the known event time, OCR each sample, and
report the longest contiguous run of frames carrying the event's signature text.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nybls_core.store import read_manifest, workspace  # noqa: E402


def ocr_text(p: Path) -> str:
    from ocrmac import ocrmac
    try:
        return " ".join(str(i[0]) for i in ocrmac.OCR(str(p), language_preference=["en-US"]).recognize()).lower()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("media_id")
    ap.add_argument("--center", type=float, required=True)
    ap.add_argument("--window", type=float, default=30.0)
    ap.add_argument("--step", type=float, default=0.5)
    ap.add_argument("--signature", required=True, help="comma-separated; a frame matches if ANY appears")
    a = ap.parse_args()

    ws = workspace(a.media_id)
    vids = [p for p in list(ws.glob("video.*")) + list(ws.glob("media*"))
            if p.suffix.lower() in {".mp4", ".webm", ".mkv", ".mov", ".m4v"}]
    tmp = ws / "_persist"; tmp.mkdir(exist_ok=True)
    sigs = [s.strip().lower() for s in a.signature.split(",")]

    hits, t = [], a.center - a.window
    while t <= a.center + a.window:
        f = tmp / f"e_{int(t*1000)}.png"
        try:
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.3f}",
                            "-i", str(vids[0]), "-frames:v", "1", "-vf", "scale=960:-2", str(f)],
                           check=True, timeout=60)
        except subprocess.CalledProcessError:
            t += a.step; continue
        txt = ocr_text(f)
        hits.append((round(t, 2), any(s in txt for s in sigs)))
        f.unlink(missing_ok=True)
        t += a.step
    for leftover in tmp.glob("*.png"):
        leftover.unlink(missing_ok=True)
    tmp.rmdir()

    best = cur = 0; best_start = cur_start = None
    for ts, hit in hits:
        if hit:
            if cur == 0: cur_start = ts
            cur += 1
            if cur > best: best, best_start = cur, cur_start
        else:
            cur = 0
    dur = float(read_manifest(a.media_id)["duration_s"])
    v = best * a.step
    res = {"media_id": a.media_id, "signature": sigs, "center_s": a.center,
           "step_s": a.step, "n_samples": len(hits), "n_matching": sum(1 for _, h in hits if h),
           "longest_run_frames": best, "measured_visible_s": round(v, 2),
           "run_starts_s": best_start, "duration_s": round(dur, 1),
           "capture_prob_uniform_30": round(min(1.0, v * 30 / dur), 4) if v else 0.0,
           "frames_needed_even_odds": int(dur / (2 * v)) if v else None}
    print(json.dumps(res, indent=1))
    out = Path(__file__).parent / "round2" / f"persist_{a.media_id}_{int(a.center)}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
