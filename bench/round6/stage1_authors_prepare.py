"""Stage 1 prep: for every video in VIDEOS.json whose store entry has a manifest and a
transcript, build the author directory (grid at the registered interval + transcript) under
<scratch>/r6/<vid>/author, and record per-video status to <scratch>/r6/STATUS.json.
Nothing here calls a model. Usage: stage1_authors_prepare.py <scratch_root>
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.expanduser("~/.nybls/store")

def main():
    root = sys.argv[1]; os.makedirs(f"{root}/r6", exist_ok=True)
    vids = json.load(open(f"{HERE}/VIDEOS.json")); status = {}
    for vid in vids:
        st = f"{STORE}/{vid}"
        if not (os.path.exists(f"{st}/manifest.json") and os.path.exists(f"{st}/transcript.txt")):
            status[vid] = "NOT PROBED"; print(vid, "not probed"); continue
        out = f"{root}/r6/{vid}/author"
        if os.path.exists(f"{out}/grid_meta.json"):
            status[vid] = "ready"; continue
        r = subprocess.run([sys.executable, f"{HERE}/build_author_grid.py", vid, out], capture_output=True, text=True)
        status[vid] = "ready" if r.returncode == 0 else f"GRID FAILED: {r.stderr[-200:]}"
        print(vid, r.stdout.strip() or status[vid])
    json.dump(status, open(f"{root}/r6/STATUS.json", "w"), indent=1)
    print(sum(v == "ready" for v in status.values()), "of", len(vids), "author dirs ready")

if __name__ == "__main__":
    main()
