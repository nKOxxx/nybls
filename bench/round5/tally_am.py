"""Tally the cost-matched control (arm AM) against the re-judged B and A of record."""
import collections, json, os

BENCH = os.path.dirname(os.path.abspath(__file__))
VIDS = "bNpx7gpSqbY oQtzvzKP5Q0 7R-CfL21zIY dwwhwVaI6vg txspjbMw6ks p09i_hoFdd0 WDAmjfQAkvk jtl4KKRIheo".split()
B_OF_RECORD, A_OF_RECORD = 125, 115
B_V, A_V = 38, 31  # of 40, re-judged with the relabel

def main():
    tot = 0; out = collections.Counter(); per = {}
    lab_t = collections.Counter(); lab_n = collections.Counter(); silent = 0
    for vid in VIDS:
        v = json.load(open(f"{BENCH}/am/{vid}/verdict.json"))
        labels = {int(k): x["final_label"] for k, x in json.load(open(f"{BENCH}/data/p2/{vid}/labels.json")).items()}
        s = 0
        for it in v["items"]:
            a = it["arms"]["AM"]; q = int(it["q"])
            s += a["score"]; out[a["outcome"]] += 1
            lab_t[labels[q]] += a["score"]; lab_n[labels[q]] += 1
        per[vid] = s; tot += s
        if vid in ("txspjbMw6ks", "p09i_hoFdd0"): silent += s
    print("AM per video:", per)
    print(f"AM total: {tot}/128 = {100*tot/128:.1f}%   (B {B_OF_RECORD}, A {A_OF_RECORD})")
    print("outcomes:", dict(out))
    for lab in "SBV":
        print(f"label {lab}: {lab_t[lab]}/{2*lab_n[lab]}")
    print("silent:", silent, "/32")
    print("P16 (AM < B):", tot < B_OF_RECORD)
    print("P17 (AM < A):", tot < A_OF_RECORD)
    print(f"P18 (AM V <= B_V - 4 = {B_V-4}):", lab_t["V"] <= B_V - 4, f"(AM V = {lab_t['V']})")
    json.dump({"per_video": per, "total": tot, "by_label": {k: lab_t[k] for k in "SBV"}}, open(f"{BENCH}/am/tally.json", "w"), indent=1)

if __name__ == "__main__":
    main()
