"""Tally round 5 verdicts. Usage: tally.py <scratch> p1b|p1c|p2"""
import json, re, sys, collections
S, cond = sys.argv[1], sys.argv[2]
mp = json.load(open(f"{S}/judge_{cond}/MAPPING.json"))
audited = set()
for ln in open("../SCORES.md"):
    m = re.match(r"\|\s*\d\s*\|\s*(\S+)\s*\|\s*(\d)\s*\|", ln)
    if m: audited.add((m.group(1), int(m.group(2))))
score = collections.Counter(); n = collections.Counter(); out = collections.Counter()
bylab = collections.defaultdict(collections.Counter); nlab = collections.defaultdict(collections.Counter)
silent = {"92gQUnMCA08", "QtqYNyBv9r8", "Wlu4MsBnjuk", "vxP2PTA1GEk", "txspjbMw6ks", "p09i_hoFdd0"}
for vid, letters in mp.items():
    try: v = json.load(open(f"{S}/judge_{cond}/{vid}/verdict.json"))
    except FileNotFoundError: print("no verdict", vid); continue
    labels = {}
    if cond == "p2":
        labels = {int(k): x["final_label"] for k, x in json.load(open(f"{S}/p2/{vid}/labels.json")).items()}
    for it in v["items"]:
        q = int(it["q"])
        if cond != "p2" and (vid, q) not in audited: continue
        for L, arm in letters.items():
            a = it["arms"].get(L)
            if a is None: continue
            s, o = a["score"], a["outcome"]
            score[arm] += s; n[arm] += 1; out[(arm, o)] += 1
            if vid in silent: score[arm + "@silent"] += s; n[arm + "@silent"] += 1
            if labels: bylab[labels.get(q)][arm] += s; nlab[labels.get(q)][arm] += 1
for k in sorted(n):
    print(f"{k:10s} {score[k]:4d}/{2*n[k]:4d} = {100*score[k]/(2*n[k]):5.1f}%")
print("outcomes:", {f"{a}:{o}": c for (a, o), c in sorted(out.items())})
for lab in sorted(bylab, key=str):
    print("label", lab, {a: f"{bylab[lab][a]}/{2*nlab[lab][a]}" for a in sorted(bylab[lab])})
