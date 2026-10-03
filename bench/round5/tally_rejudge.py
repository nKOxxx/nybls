"""Committed tally for the D9 re-judging: reproduces the of-record Part 2 numbers."""
import collections, json, os

BENCH = os.path.dirname(os.path.abspath(__file__))

def main():
    mp = json.load(open(f"{BENCH}/rejudge/MAPPING.json"))
    tot = collections.Counter(); out = collections.Counter()
    lab_t = collections.defaultdict(collections.Counter); lab_n = collections.defaultdict(collections.Counter)
    silent = {"txspjbMw6ks", "p09i_hoFdd0"}; sil = collections.Counter()
    for vid, m in mp.items():
        v = json.load(open(f"{BENCH}/rejudge/{vid}/verdict.json"))
        labels = {int(k): x["final_label"] for k, x in json.load(open(f"{BENCH}/data/p2/{vid}/labels.json")).items()}
        for it in v["items"]:
            q = int(it["q"])
            for L, a in it["arms"].items():
                arm = m[L]
                tot[arm] += a["score"]; out[(arm, a["outcome"])] += 1
                lab_t[labels[q]][arm] += a["score"]; lab_n[labels[q]][arm] += 1
                if vid in silent: sil[arm] += a["score"]
    print("totals (of 128):", {k: tot[k] for k in "NTAB"})
    print("outcomes:", {f"{a}:{o}": c for (a, o), c in sorted(out.items())})
    for lab in "SBV":
        print(f"label {lab} ({lab_n[lab]['B']} items):", {a: f"{lab_t[lab][a]}/{2*lab_n[lab][a]}" for a in "NTAB"})
    print("silent (of 32):", {k: sil[k] for k in "NTAB"})
    assert {k: tot[k] for k in "NTAB"} == {"N": 28, "T": 79, "A": 115, "B": 125}, "of-record mismatch"
    print("of-record numbers reproduced")

if __name__ == "__main__":
    main()
