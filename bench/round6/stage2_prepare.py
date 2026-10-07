"""Stage 2 prep: for each video whose author output is complete, run the label check, copy
questions into T/ and B/ (and BF/ for the Fable subset) under <scratch>/r6/<vid>/, copy the
transcript into T/, and for the BF subset clone the store entry to <vid>_bf so the two nybls
arms never share a ledger (round 5 D5). Idempotent. No model calls.
Usage: stage2_prepare.py <scratch_root>
"""
import json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.expanduser("~/.nybls/store")


def header_label(header):
    """Last standalone S, V or B token in a question header line, e.g. "## Q1 - label S",
    "## Q1: V", "## Q1 (V)", "## Q1. Title — **B** (mostly visual)"."""
    toks = [t.strip("*()[]:.,;") for t in header.split()]
    toks = [t for t in toks if t in ("S", "V", "B")]
    return toks[-1] if toks else None

def complete(d):
    q, g = f"{d}/questions.md", f"{d}/ground_truth.md"
    if not (os.path.exists(q) and os.path.exists(g)): return False
    nq = len(re.findall(r"(?m)^\s*\**\d+[.)]", open(q).read()))
    gt = open(g).read()
    secs = re.split(r"(?m)^##\s+(?:Q(?:uestion)?\s*)?(\d+)", gt)
    nl = sum(1 for i in range(2, len(secs), 2) if re.search(r"Label:?\**\s*\**[SVB]\b", secs[i]) or header_label(secs[i].split("\n", 1)[0]))
    return nq >= 8 and nl >= 8

def main():
    root = sys.argv[1]; vids = json.load(open(f"{HERE}/VIDEOS.json")); ready = []
    for vid, meta in vids.items():
        a = f"{root}/r6/{vid}/author"
        if not complete(a): continue
        subprocess.run([sys.executable, f"{HERE}/check_labels.py", f"{root}/r6", vid], check=True)
        for arm in ["T", "B"] + (["BF"] if meta.get("bf_subset") else []):
            d = f"{root}/r6/{vid}/{arm}"; os.makedirs(d, exist_ok=True)
            shutil.copy(f"{a}/questions.md", f"{d}/questions.md")
        shutil.copy(f"{STORE}/{vid}/transcript.txt", f"{root}/r6/{vid}/T/transcript.txt")
        if meta.get("bf_subset") and not os.path.exists(f"{STORE}/{vid}_bf/manifest.json"):
            shutil.copytree(f"{STORE}/{vid}", f"{STORE}/{vid}_bf", symlinks=True)
            m = json.load(open(f"{STORE}/{vid}_bf/manifest.json")); m["id"] = f"{vid}_bf"
            json.dump(m, open(f"{STORE}/{vid}_bf/manifest.json", "w"), indent=1)
            for f in ("ledger.json",):
                p = f"{STORE}/{vid}_bf/{f}"
                if os.path.exists(p): os.remove(p)
        ready.append(vid)
    json.dump(ready, open(f"{root}/r6/STAGE2_READY.json", "w"), indent=1)
    print(len(ready), "videos ready for arms")

if __name__ == "__main__":
    main()
