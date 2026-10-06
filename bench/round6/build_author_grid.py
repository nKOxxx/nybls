"""Author reference grid for round 6: one 1024-wide frame every INTERVAL seconds, where
INTERVAL = max(10, ceil(duration_s / 120)) (PROTOCOL.md). Also copies the transcript.
Usage: build_author_grid.py <media_id> <author_dir>. Prints the interval used.
"""
import json, math, os, subprocess, sys

def main():
    vid, out = sys.argv[1], sys.argv[2]
    st = os.path.expanduser(f"~/.nybls/store/{vid}")
    dur = json.load(open(f"{st}/manifest.json"))["duration_s"]
    interval = max(10, math.ceil(dur / 120))
    video = next(p for p in os.listdir(st) if p.startswith("video.") and p.rsplit(".", 1)[-1] in ("mp4", "webm", "mkv"))
    os.makedirs(f"{out}/grid", exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{st}/{video}", "-vf",
                    f"fps=1/{interval},scale=1024:-2", "-start_number", "0", f"{out}/grid/tmp_%05d.png"], check=True, timeout=3600)
    n = 0
    for f in sorted(os.listdir(f"{out}/grid")):
        if f.startswith("tmp_"):
            i = int(f[4:9]); ts = i * interval
            os.rename(f"{out}/grid/{f}", f"{out}/grid/g_{ts:05d}s.png"); n += 1
    subprocess.run(["cp", f"{st}/transcript.txt", f"{out}/transcript.txt"], check=True)
    json.dump({"video": vid, "duration_s": dur, "interval_s": interval, "frames": n}, open(f"{out}/grid_meta.json", "w"), indent=1)
    print(vid, "interval", interval, "frames", n)

if __name__ == "__main__":
    main()
