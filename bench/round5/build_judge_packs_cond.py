"""Blind judge packs for round 5 Parts 1b/1c: ground truth + whichever arms the condition ran."""
import json, os, random, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_judge_packs import gt  # noqa: E402

S, cond, vids = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
random.seed(f"{cond}-20261002")
out = f"{S}/judge_{cond}"
mp_path = f"{out}/MAPPING.json"
mapping = json.load(open(mp_path)) if os.path.exists(mp_path) else {}
for vid in vids:
    arms = {}
    for a in "NTB":
        p = f"{S}/{cond}/{vid}/{a}/answers.md"
        if os.path.exists(p):
            t = open(p).read()
            t = re.sub(r"(?ims)^\W*(nybls ledger|watched \d+ min).*\Z", "", t)  # drop ledger tail
            arms[a] = t.strip() + "\n"
    keys = list(arms); random.shuffle(keys)
    d = f"{out}/{vid}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/ground_truth.md", "w").write(gt(vid))
    letters = "WXY"[: len(keys)]
    for L, k in zip(letters, keys):
        open(f"{d}/{L}.md", "w").write(arms[k])
    mapping[vid] = dict(zip(letters, keys))
json.dump(mapping, open(mp_path, "w"), indent=1)
print({v: mapping[v] for v in vids})
