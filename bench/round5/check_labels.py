"""Registered mechanical check: a V item whose key terms appear in the normalised transcript
is relabelled (B if some terms hit, S if all hit). Normalisation as in QUESTION_AUDIT."""
import json, re, sys

def norm(s):
    return " " + re.sub(r"[^a-z0-9]+", " ", s.lower()).strip() + " "

def parse(gt):
    secs = re.split(r"(?m)^##\s+Q(?:uestion)?\s*(\d+)", gt)
    items = {}
    for i in range(1, len(secs), 2):
        q, body = int(secs[i]), secs[i + 1]
        m = re.search(r"Label:?\**\s*\**\s*([SVB])\b", body)
        kt = re.search(r"(?im)^\**Key terms:?\**(.*)$", body)
        terms = re.findall(r'["“]([^"”]+)["”]', kt.group(1)) if kt else []
        items[q] = {"label": m.group(1) if m else None, "terms": terms}
    return items

root, vid = sys.argv[1], sys.argv[2]
d = f"{root}/p2/{vid}/author"
items = parse(open(f"{d}/ground_truth.md").read())
tr = norm(re.sub(r"\[\d\d:\d\d(:\d\d)?\]", " ", open(f"{d}/transcript.txt").read()))
out = {}
for q, it in sorted(items.items()):
    hits = [t for t in it["terms"] if norm(t).strip() and norm(t) in tr]
    final = it["label"]
    if it["label"] == "V" and hits:
        final = "S" if len(hits) == len(it["terms"]) else "B"
    out[q] = {"author_label": it["label"], "final_label": final, "terms": it["terms"], "transcript_hits": hits}
json.dump(out, open(f"{root}/p2/{vid}/labels.json", "w"), indent=1)
print(vid, " ".join(f"Q{q}:{v['author_label']}->{v['final_label']}{'*' if v['transcript_hits'] else ''}" for q, v in out.items()))
