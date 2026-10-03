"""Build the cost-matched control (arm AM) evidence packs: per video, a uniform grid of
exactly as many full-resolution frames as arm B was served (PREDICTIONS_ADDENDUM.md),
plus the transcript and the author's questions. Frames are 1568 wide (882 high for the
16:9 sources used), the one-shot pack's width, so each costs 1,792 visual tokens under
the ledger formula: 68 frames = 121,856, recorded in am/tokens.json.

Usage: build_am_packs.py <out_root>. Reads the store under ~/.nybls/store/<vid>/.
This is the method of record; the PNGs themselves are not committed (size), the per-video
index.json (timestamps) is, under am/<vid>/frames_index.json.
"""
import json, os, subprocess, sys

BENCH = os.path.dirname(os.path.abspath(__file__))
COUNTS = {"bNpx7gpSqbY": 4, "oQtzvzKP5Q0": 10, "7R-CfL21zIY": 4, "dwwhwVaI6vg": 3,
          "txspjbMw6ks": 17, "p09i_hoFdd0": 20, "WDAmjfQAkvk": 8, "jtl4KKRIheo": 2}

def main():
    out_root = sys.argv[1]
    for vid, n in COUNTS.items():
        st = os.path.expanduser(f"~/.nybls/store/{vid}")
        dur = json.load(open(f"{st}/manifest.json"))["duration_s"]
        video = next(p for p in os.listdir(st) if p.startswith("video.") and p.rsplit(".", 1)[-1] in ("mp4", "webm", "mkv"))
        d = f"{out_root}/{vid}/frames"; os.makedirs(d, exist_ok=True)
        idx = []
        for i in range(n):
            ts = dur * (i + 0.5) / n
            out = f"{d}/am{i:02d}_{int(ts)}s.png"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}", "-i", f"{st}/{video}",
                            "-frames:v", "1", "-vf", "scale=1568:-2", out], check=True, timeout=120)
            idx.append({"i": i, "ts": round(ts, 3), "file": os.path.basename(out)})
        json.dump({"video": vid, "n": n, "width": 1568, "frames": idx}, open(f"{out_root}/{vid}/index.json", "w"), indent=1)
        subprocess.run(["cp", f"{st}/transcript.txt", f"{out_root}/{vid}/"], check=True)
        subprocess.run(["cp", f"{BENCH}/data/p2/{vid}/author/questions.md", f"{out_root}/{vid}/"], check=True)
        print(vid, n, "ok")

if __name__ == "__main__":
    main()
