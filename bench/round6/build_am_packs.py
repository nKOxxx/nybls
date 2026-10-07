"""Round 6 cost-matched control (arm AM): per video, a uniform grid of exactly as many
1568-wide frames as arm B's ledger records (images), plus transcript and questions, under
<scratch>/r6/<vid>/AM/. A video where B spent 0 images gets 0 frames (AM then equals T by
construction; reported, not adjusted). Writes am_counts.json here (committed).
Usage: build_am_packs.py <scratch_root>
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.expanduser("~/.nybls/store")

def main():
    root = sys.argv[1]; vids = json.load(open(f"{HERE}/VIDEOS.json")); counts = {}
    for vid in vids:
        lp = f"{STORE}/{vid}/ledger.json"; bdir = f"{root}/r6/{vid}/B"
        if not (os.path.exists(f"{bdir}/answers.md")): continue
        n = json.load(open(lp))["images"] if os.path.exists(lp) else 0
        counts[vid] = n
        d = f"{root}/r6/{vid}/AM"; os.makedirs(f"{d}/frames", exist_ok=True)
        if os.path.exists(f"{d}/index.json"): continue
        dur = json.load(open(f"{STORE}/{vid}/manifest.json"))["duration_s"]
        video = next(p for p in os.listdir(STORE + "/" + vid) if p.startswith("video.") and p.rsplit(".", 1)[-1] in ("mp4", "webm", "mkv"))
        idx = []
        for i in range(n):
            ts = dur * (i + 0.5) / n
            out = f"{d}/frames/am{i:02d}_{int(ts)}s.png"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{ts:.3f}", "-i", f"{STORE}/{vid}/{video}",
                            "-frames:v", "1", "-vf", "scale=1568:-2", out], check=True, timeout=300)
            idx.append({"i": i, "ts": round(ts, 3), "file": os.path.basename(out)})
        json.dump({"video": vid, "n": n, "width": 1568, "frames": idx}, open(f"{d}/index.json", "w"), indent=1)
        subprocess.run(["cp", f"{STORE}/{vid}/transcript.txt", f"{d}/transcript.txt"], check=True)
        subprocess.run(["cp", f"{root}/r6/{vid}/author/questions.md", f"{d}/questions.md"], check=True)
        print(vid, n)
    json.dump(counts, open(f"{HERE}/am_counts.json", "w"), indent=1)
    print(len(counts), "AM packs; total frames", sum(counts.values()), "; zero-frame videos:", [k for k, v in counts.items() if v == 0])

if __name__ == "__main__":
    main()
