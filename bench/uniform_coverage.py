"""What a uniform frame grid can and cannot reach, in closed form.

The one-shot baseline samples N frames at t_i = D(i+0.5)/N. Two consequences
follow from that formula alone, before any model is involved:

1. DEAD ZONES. The first sample is at D/2N and the last at D - D/2N, so the
   opening and closing D/2N seconds of every video are outside the evidence
   window. No amount of careful reasoning recovers content there.

2. CAPTURE PROBABILITY. An event visible for v seconds, at an arbitrary offset,
   is captured with probability min(1, vN/D). To make a transient event likely
   to be caught you need N >= D/v frames -- which for a 3-second title card in
   an 80-minute video is 1,616 frames, roughly 2.9M visual tokens at Claude API
   rates, about 300x the budget an adaptive pass actually spends.

This is not a claim about which method reasons better. It is arithmetic about
where the evidence is, and it is the reason a fixed grid fails on the specific
questions it fails on.

Visual-token estimate follows the Claude API's documented ceil(w/28)*ceil(h/28).
"""
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nybls_core.store import read_manifest  # noqa: E402

CORPUS = ["LP10_YdKEPw", "g9xUu2StOYg", "5oNHF72wbmI", "jgN4XWFUSb4",
          "OngJKc-FAS0", "F2FmTdLtb_4", "aircAruvnKk", "f1wnYdLEpgI",
          "8NSyI-npJCU", "N--Mj95mAYI"]

# Events with a known on-screen time, from the pre-registered ground truth of
# rounds 1 and 2. Duration is the observed on-screen persistence in seconds.
EVENTS = [
    ("LP10_YdKEPw", "mid-video title card", 521.0, 3.0),
    ("LP10_YdKEPw", "closing subscribe/thanks cards", 1185.0, 15.0),
    ("g9xUu2StOYg", "race results graphic", 162.0, 4.0),
    ("5oNHF72wbmI", "iMessage screenshot", 2532.0, 5.0),
]


def tokens(w=1568, h=882):
    return math.ceil(w / 28) * math.ceil(h / 28)


def grid(duration, n=30):
    return [duration * (i + 0.5) / n for i in range(n)]


def main():
    n = 30
    per_img = tokens()
    out = {"n_frames": n, "visual_tokens_per_frame": per_img, "videos": [], "events": []}

    for mid in CORPUS:
        try:
            m = read_manifest(mid)
        except Exception:
            continue
        d = float(m["duration_s"])
        dead = d / (2 * n)
        out["videos"].append({
            "media_id": mid, "title": m.get("title", "")[:50], "duration_s": round(d, 1),
            "grid_interval_s": round(d / n, 1),
            "dead_zone_each_end_s": round(dead, 1),
            "unreachable_fraction": round(2 * dead / d, 4),
            "frames_needed_for_3s_event": math.ceil(d / 3.0),
            "visual_tokens_for_that": math.ceil(d / 3.0) * per_img,
        })

    for mid, name, t, vis in EVENTS:
        d = float(read_manifest(mid)["duration_s"])
        g = grid(d, n)
        nearest = min(g, key=lambda s: abs(s - t))
        captured = any(abs(s - t) <= vis / 2 for s in g)
        out["events"].append({
            "media_id": mid, "event": name, "t_s": t, "visible_s": vis,
            "nearest_uniform_sample_s": round(nearest, 1),
            "gap_to_nearest_s": round(abs(nearest - t), 1),
            "captured_by_uniform_30": captured,
            "capture_probability": round(min(1.0, vis * n / d), 4),
            "frames_needed_for_even_odds": math.ceil(d / (2 * vis)),
        })

    p = Path(__file__).parent / "round2" / "uniform_coverage.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
