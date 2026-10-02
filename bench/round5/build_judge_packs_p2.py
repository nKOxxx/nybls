"""Blind judge packs for round 5 Part 2: the author's ground truth + the four arms, anonymised."""
import json, os, random, re, sys

S, vids = sys.argv[1], sys.argv[2].split(",")
out = f"{S}/judge_p2"
mp_path = f"{out}/MAPPING.json"
mapping = json.load(open(mp_path)) if os.path.exists(mp_path) else {}
for vid in vids:
    random.seed(f"p2-{vid}")
    arms = {}
    for a in "NTAB":
        t = open(f"{S}/p2/{vid}/{a}/answers.md").read()
        t = re.sub(r"(?ims)^\W*(nybls ledger|watched \d+ min|frames examined|i examined).*\Z", "", t)
        t = re.sub(r"(?im)^\W*(arm|condition|evidence available)\b.*$", "", t)
        arms[a] = t.strip() + "\n"
    keys = list(arms)
    random.shuffle(keys)
    d = f"{out}/{vid}"
    os.makedirs(d, exist_ok=True)
    open(f"{d}/ground_truth.md", "w").write(open(f"{S}/p2/{vid}/author/ground_truth.md").read())
    for L, k in zip("WXYZ", keys):
        open(f"{d}/{L}.md", "w").write(arms[k])
    mapping[vid] = dict(zip("WXYZ", keys))
json.dump(mapping, open(mp_path, "w"), indent=1)
print({v: mapping[v] for v in vids})
