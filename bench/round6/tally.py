"""Round 6 tally: per arm, per stratum, per genre, per label, per video; outcomes;
cluster bootstrap 95% intervals by video; prediction checks P23 to P31.
Reads judge/<vid>/verdict.json + judge/MAPPING.json, data/<vid>/labels.json, VIDEOS.json
(id -> {stratum, genre, duration_s}). Writes tally.json. Asserts nothing until all 32 are in.
"""
import collections, json, os, random, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ARMS = ["T", "B", "AM", "BF"]  # BF only on the 8-video Fable subset

def load():
    vids = json.load(open(f"{HERE}/VIDEOS.json"))
    mapping = json.load(open(f"{HERE}/judge/MAPPING.json"))
    per = {}
    for vid, meta in vids.items():
        vp = f"{HERE}/judge/{vid}/verdict.json"
        if not os.path.exists(vp): continue
        inv = mapping[vid]
        labels = {int(k): x["final_label"] for k, x in json.load(open(f"{HERE}/data/{vid}/labels.json")).items()}
        items = []
        for it in json.load(open(vp))["items"]:
            q = int(it["q"])
            items.append({"q": q, "label": labels.get(q), **{inv[k]: v for k, v in it["arms"].items()}})
        per[vid] = {"meta": meta, "items": items}
    return per

def pts(per, vids, arm, label=None):
    return sum(it[arm]["score"] for v in vids for it in per[v]["items"] if arm in it and (label is None or it["label"] == label))

def mx(per, vids, label=None, arm="B"):
    return 2 * sum(1 for v in vids for it in per[v]["items"] if arm in it and (label is None or it["label"] == label))

def pct(per, vids, arm, label=None):
    m = mx(per, vids, label, arm); return 100 * pts(per, vids, arm, label) / m if m else float("nan")

def boot(per, vids, a, b, reps=20000, seed=7):
    random.seed(seed); gs = []
    for _ in range(reps):
        s = [random.choice(vids) for _ in vids]
        gs.append(pct(per, s, b) - pct(per, s, a))
    gs.sort(); return round(gs[int(.025 * reps)], 1), round(gs[int(.975 * reps)], 1)

def spearman(x, y):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
        for k, i in enumerate(order): r[i] = k
        return r
    rx, ry = rank(x), rank(y); n = len(x)
    return 1 - 6 * sum((a - b) ** 2 for a, b in zip(rx, ry)) / (n * (n * n - 1))

def main():
    per = load(); vids = sorted(per)
    print(f"videos judged: {len(vids)}")
    out = {"n_videos": len(vids), "pooled": {}, "strata": {}, "genres": {}, "labels": {}, "per_video": {}, "outcomes": {}}
    for a in ARMS:
        out["pooled"][a] = {"points": pts(per, vids, a), "max": mx(per, vids, None, a), "pct": round(pct(per, vids, a), 1)}
        out["outcomes"][a] = dict(collections.Counter(it[a]["outcome"] for v in vids for it in per[v]["items"] if a in it))
    print("pooled:", {a: f"{d['points']}/{d['max']} ({d['pct']}%)" for a, d in out["pooled"].items()})
    print("outcomes:", out["outcomes"])
    for s in ("N", "S"):
        sv = [v for v in vids if per[v]["meta"]["stratum"] == s]
        if sv: out["strata"][s] = {a: round(pct(per, sv, a), 1) for a in ARMS}; out["strata"][s]["n"] = len(sv)
    print("strata:", out["strata"])
    genres = sorted({per[v]["meta"]["genre"] for v in vids if per[v]["meta"]["stratum"] == "S"})
    for g in genres:
        gv = [v for v in vids if per[v]["meta"].get("genre") == g]
        out["genres"][g] = {a: pts(per, gv, a) for a in ARMS}; out["genres"][g]["max"] = mx(per, gv)
    for lab in "SBV":
        out["labels"][lab] = {a: f"{pts(per, vids, a, lab)}/{mx(per, vids, lab, a)}" for a in ARMS}
    print("labels:", out["labels"])
    for v in vids:
        out["per_video"][v] = {a: pts(per, [v], a) for a in ARMS}
    if len(vids) >= 2:
        out["bootstrap_95"] = {f"{b}-{a}": boot(per, vids, a, b) for a, b in [("T", "B"), ("AM", "B")]}
        print("bootstrap 95% (pp):", out["bootstrap_95"])
    # predictions (reported whenever computable; of record only at 32 videos)
    P = {}
    P["P23"] = pct(per, vids, "B") - pct(per, vids, "T") >= 20
    P["P24"] = pct(per, vids, "B") - pct(per, vids, "AM") >= 8
    P["P25"] = sum(1 for v in vids if pts(per, [v], "B") < 14.4) >= 2
    bf = [v for v in vids if per[v]["meta"].get("bf_subset") and any("BF" in it for it in per[v]["items"])]
    if bf:
        P["P26"] = pts(per, bf, "B") >= 0.85 * pts(per, bf, "BF") and out["outcomes"]["B"].get("fabricated", 0) <= 2
        out["bf_subset"] = {"n": len(bf), "B": pts(per, bf, "B"), "BF": pts(per, bf, "BF"), "T": pts(per, bf, "T"), "AM": pts(per, bf, "AM"), "max": mx(per, bf)}
    if "N" in out["strata"] and "S" in out["strata"]:
        gN = out["strata"]["N"]["B"] - out["strata"]["N"]["T"]; gS = out["strata"]["S"]["B"] - out["strata"]["S"]["T"]
        P["P27"] = gS >= gN - 10
    ne = [v for v in vids if per[v]["meta"].get("genre") in (3, 4)]
    if ne: P["P28"] = pct(per, ne, "T", "S") >= 90 and pct(per, ne, "B", "V") >= 75
    if len(vids) >= 5:
        P["P29"] = spearman([per[v]["meta"]["duration_s"] for v in vids], [pts(per, [v], "B") - pts(per, [v], "AM") for v in vids]) > 0
    P["P30"] = out["outcomes"]["T"].get("fabricated", 0) == 0 and out["outcomes"]["B"].get("fabricated", 0) <= 1
    if genres:
        P["P31"] = all(out["genres"][g]["B"] > out["genres"][g]["T"] for g in genres) and sum(out["genres"][g]["B"] > out["genres"][g]["AM"] for g in genres) >= 9
    out["predictions"] = P; print("predictions:", P, "(of record only at 32 videos)")
    json.dump(out, open(f"{HERE}/tally.json", "w"), indent=1)

if __name__ == "__main__":
    main()
