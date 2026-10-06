"""Round 6 blind judge packs: four arms (T, B, B2, AM) per video, anonymised W/X/Y/Z,
scrubbed with round 5's D9 blocklist and REDACT list (copied, with "sonnet", "fable",
"_s55" and "claude" added to the blocklist since B2 differs from B only by model), and
mechanically verified. Sources: data/<vid>/{T,B,B2,AM}/answers.md; output judge/<vid>/.
Usage: build_judge_packs.py <vid> [<vid> ...]
"""
import json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARMS = ["T", "B", "B2", "AM"]
BLOCK = re.compile(
    r"nybls|ledger|oneshot|watch protocol|\barm\b|no-video|transcript-only|"
    r"uniform grid|uniform stills|\d+ stills|evidence available|"
    r"frames? examined|files? (i )?read|i examined|modif(y|ied) no|did not modify|"
    r"no file was modified|image units|visual tokens|evidence pack|_s55|sonnet|fable|claude",
    re.I,
)
REDACT = [
    (re.compile(r"\s*\((?:Basis|Source|Evidence)[^)]*\)", re.I), ""),
    (re.compile(r"(?:Basis|Source):[^.\n]*\.", re.I), ""),
    (re.compile(r"video\.txt|the metadata|metadata", re.I), "the available material"),
]

def scrub(text):
    out = []
    for i, ln in enumerate(text.splitlines()):
        if i == 0 and ln.startswith("#"):
            out.append("# Answers"); continue
        if re.match(r"^#{1,3}\s*Ledger", ln, re.I):
            break
        if BLOCK.search(ln):
            continue
        for rx, rep in REDACT:
            ln = rx.sub(rep, ln)
        out.append(ln)
    return "\n".join(out).strip() + "\n"

def main():
    mp = f"{HERE}/judge/MAPPING.json"
    mapping = json.load(open(mp)) if os.path.exists(mp) else {}
    residue = {}
    for vid in sys.argv[1:]:
        random.seed(f"r6-{vid}")
        arms = {a: scrub(open(f"{HERE}/data/{vid}/{a}/answers.md").read()) for a in ARMS}
        keys = list(arms); random.shuffle(keys)
        d = f"{HERE}/judge/{vid}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/ground_truth.md", "w").write(open(f"{HERE}/data/{vid}/author/ground_truth.md").read())
        for L, k in zip("WXYZ", keys):
            open(f"{d}/{L}.md", "w").write(arms[k])
        mapping[vid] = dict(zip("WXYZ", keys))
        bad, res = [], []
        for L in "WXYZ":
            for ln in open(f"{d}/{L}.md"):
                if BLOCK.search(ln): bad.append((vid, L, ln.strip()[:90]))
                if re.search(r"\bu\d\d_\d+s|sheet_\d+|z_\d+_|\bam\d\d_", ln): res.append(L)
        if bad:
            print("LEAK", bad); sys.exit(1)
        residue[vid] = sorted(set(res))
        # scrub-loss audit: count numbered answer lines before/after
        for a in ARMS:
            before = len(re.findall(r"(?m)^\s*\**\d+[.)]", open(f"{HERE}/data/{vid}/{a}/answers.md").read()))
            after = len(re.findall(r"(?m)^\s*\**\d+[.)]", arms[a]))
            if after < before: print(f"SCRUB LOSS {vid} {a}: {before}->{after} numbered lines")
    os.makedirs(f"{HERE}/judge", exist_ok=True)
    json.dump(mapping, open(mp, "w"), indent=1)
    rp = f"{HERE}/judge/filename_residue.json"
    prev = json.load(open(rp)) if os.path.exists(rp) else {}
    prev.update(residue); json.dump(prev, open(rp, "w"), indent=1)
    print("packs ok; blocklist clean; residue:", residue)

if __name__ == "__main__":
    main()
