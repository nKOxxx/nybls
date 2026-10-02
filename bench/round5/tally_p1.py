"""Tally round 5 Part 1 verdicts against the 56 audited questions in bench/SCORES.md."""
import json, re, sys, collections
S = sys.argv[1]
mapping = json.load(open(f"{S}/judge/MAPPING.json"))
rec = collections.defaultdict(dict)  # (vid,q) -> {"A":a,"B":b}
for ln in open("bench/SCORES.md"):
    m = re.match(r"\|\s*(\d)\s*\|\s*(\S+)\s*\|\s*(\d)\s*\|\s*(-?\d)\s*\|\s*(-?\d)\s*\|", ln)
    if m:
        rnd, vid, q, a, b = m.groups()
        rec[(vid, int(q))] = {"round": int(rnd), "A": int(a), "B": int(b)}
tot = collections.Counter(); out = collections.Counter(); r4 = collections.Counter()
rows = []
for vid, letters in mapping.items():
    v = json.load(open(f"{S}/judge/{vid}/verdict.json"))
    for it in v["items"]:
        q = int(it["q"])
        if (vid, q) not in rec:
            continue  # voided
        r = rec[(vid, q)]
        row = {"vid": vid, "q": q, "round": r["round"], "A_rec": r["A"], "B_rec": r["B"]}
        for L, arm in letters.items():
            s = it["arms"][L]["score"]; o = it["arms"][L]["outcome"]
            row[arm] = s; row[arm + "_o"] = o
            out[(arm, o)] += 1
            if arm in "NT":
                tot[arm] += s
                if r["round"] == 4:
                    r4[arm] += s
            else:
                r4[arm + "_rejudge"] += s
        tot["A"] += r["A"]; tot["B"] += r["B"]
        if r["round"] == 4:
            r4["A"] += r["A"]; r4["B"] += r["B"]
        rows.append(row)
n = len(rows)
print(f"items {n}, points {2*n}")
for a in "NTAB":
    print(a, tot[a], f"{100*tot[a]/(2*n):.1f}%")
print("round4 (40 pts):", dict(r4))
print("outcomes:", {f"{k[0]}:{k[1]}": v for k, v in sorted(out.items())})
json.dump(rows, open(f"{S}/judge/p1_rows.json", "w"), indent=1)
