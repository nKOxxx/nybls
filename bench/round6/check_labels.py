"""Round 6 mechanical label check, as round 5's check_labels.py but Unicode-aware: round 5
normalised with [^a-z0-9], which deletes every Arabic or accented character and would make
the transcript re-check vacuous on genres 3 and 4. Here normalisation lowercases and keeps
every Unicode word character. Relabel-safe via the "note" field, as in round 5.
Usage: check_labels.py <data_root> <vid>   (reads <data_root>/<vid>/author/{ground_truth.md,transcript.txt})
"""
import json, os, re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[\u064b-\u0652\u0670]", "", s)          # Arabic short vowels / tanween
    return " " + re.sub(r"[^\w]+", " ", s, flags=re.UNICODE).strip() + " "

def parse(gt):
    secs = re.split(r"(?m)^##\s+Q(?:uestion)?\s*(\d+)", gt)
    items = {}
    for i in range(1, len(secs), 2):
        q, body = int(secs[i]), secs[i + 1]
        m = re.search(r"Label:?\**\s*\**\s*([SVB])\b", body)
        kt = re.search(r"(?im)^\**Key terms:?\**(.*)$", body)
        terms = re.findall(r'["“«]([^"”»]+)["”»]', kt.group(1)) if kt else []
        items[q] = {"label": m.group(1) if m else None, "terms": terms}
    return items

root, vid = sys.argv[1], sys.argv[2]
d = f"{root}/{vid}/author"
items = parse(open(f"{d}/ground_truth.md").read())
tr = norm(re.sub(r"\[\d\d:\d\d(:\d\d)?\]", " ", open(f"{d}/transcript.txt").read()))
out = {}
for q, it in sorted(items.items()):
    hits = [t for t in it["terms"] if norm(t).strip() and norm(t) in tr]
    final = it["label"]
    if it["label"] == "V" and hits:
        final = "S" if len(hits) == len(it["terms"]) else "B"
    out[q] = {"author_label": it["label"], "final_label": final, "terms": it["terms"], "transcript_hits": hits}
lp = f"{root}/{vid}/labels.json"
if os.path.exists(lp):
    prev = json.load(open(lp))
    for q in out:
        if str(q) in prev and "note" in prev[str(q)]:
            out[q] = prev[str(q)]
json.dump(out, open(lp, "w"), indent=1, ensure_ascii=False)
print(vid, " ".join(f"Q{q}:{v['author_label']}->{v['final_label']}{'*' if v['transcript_hits'] else ''}" for q, v in out.items()))
