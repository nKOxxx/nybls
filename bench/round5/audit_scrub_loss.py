"""Committed audit: per-answer text loss introduced by the re-judging scrub (D9).

Lists every (video, arm, question) where the rejudge pack retains less than 60% of the
source answer's characters. Robust section splitter: numbered headings in #, ##, bold,
or bare forms.
"""
import json, os, re

BENCH = os.path.dirname(os.path.abspath(__file__))

def sections(text):
    out, cur = {}, None
    for ln in text.splitlines():
        m = re.match(r"^(?:#{1,3}\s*)?(?:\*\*)?(?:Q(?:uestion)?\s*)?([1-8])[.):\s]", ln)
        if m:
            cur = int(m.group(1))
            out.setdefault(cur, 0)
        if cur is not None:
            out[cur] += len(ln) + 1
    return out

def main():
    mp = json.load(open(f"{BENCH}/rejudge/MAPPING.json"))
    rows = []
    for vid, m in mp.items():
        for L, arm in m.items():
            src = sections(open(f"{BENCH}/data/p2/{vid}/{arm}/answers.md").read())
            pk = sections(open(f"{BENCH}/rejudge/{vid}/{L}.md").read())
            for q, s in src.items():
                p = pk.get(q, 0)
                if s > 0 and p < 0.6 * s:
                    rows.append({"video": vid, "arm": arm, "q": q, "src_chars": s, "pack_chars": p})
    rows.sort(key=lambda r: (r["video"], r["arm"], r["q"]))
    json.dump(rows, open(f"{BENCH}/rejudge/scrub_loss_audit.json", "w"), indent=1)
    for r in rows:
        print(r)
    print(len(rows), "items with >40% loss")

if __name__ == "__main__":
    main()
