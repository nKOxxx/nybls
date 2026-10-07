"""Copy the round 6 record from the scratchpad into bench/round6/data/<vid>/: author files
(questions, ground truth, transcript, grid_meta), labels.json, and each arm's answers.md
(T, B, AM, BF where present). Grids, frames and store copies are not committed. Idempotent.
Usage: collect_data.py <scratch_root>
"""
import json, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def main():
    root = sys.argv[1]; n = 0
    for vid in json.load(open(f"{HERE}/VIDEOS.json")):
        src = f"{root}/r6/{vid}"; dst = f"{HERE}/data/{vid}"
        os.makedirs(f"{dst}/author", exist_ok=True)
        for f in ("questions.md", "ground_truth.md", "transcript.txt", "grid_meta.json"):
            if os.path.exists(f"{src}/author/{f}"): shutil.copy(f"{src}/author/{f}", f"{dst}/author/{f}")
        if os.path.exists(f"{src}/labels.json"): shutil.copy(f"{src}/labels.json", f"{dst}/labels.json")
        for arm in ("T", "B", "AM", "BF"):
            if os.path.exists(f"{src}/{arm}/answers.md"):
                os.makedirs(f"{dst}/{arm}", exist_ok=True); shutil.copy(f"{src}/{arm}/answers.md", f"{dst}/{arm}/answers.md"); n += 1
        if os.path.exists(f"{src}/AM/index.json"): shutil.copy(f"{src}/AM/index.json", f"{dst}/AM/frames_index.json")
    print(n, "arm answer files collected")
if __name__ == "__main__": main()
