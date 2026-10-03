"""Round 5 Part 2 RE-JUDGING pack builder (deviation D9).

The first judging's packs leaked arm identity: N/T/A self-identified in their H1 title
lines and arm B kept a residual "## Ledger" section (run 025, Whitfield C1, chair
confirmed). This builder strips harder and then mechanically verifies the result against
a blocklist. Evidence filenames inside answers (u07_*, sheet_*) are left and recorded:
they are the round-4-style residue, disclosed, not a label.

Sources: bench/round5/data/p2/<vid>/{N,T,A,B}/answers.md (the committed first-judging
record). Output: bench/round5/rejudge/<vid>/{ground_truth.md, W..Z.md} + MAPPING.json.
"""
import json, os, random, re, sys

BENCH = os.path.dirname(os.path.abspath(__file__))
VIDS = "bNpx7gpSqbY oQtzvzKP5Q0 7R-CfL21zIY dwwhwVaI6vg txspjbMw6ks p09i_hoFdd0 WDAmjfQAkvk jtl4KKRIheo".split()

# A line matching any of these is an arm label or spend reporting, never an answer.
BLOCK = re.compile(
    r"nybls|ledger|oneshot|watch protocol|\barm\b|no-video|transcript-only|"
    r"uniform grid|uniform stills|30 stills|evidence available|"
    r"frames? examined|files? (i )?read|i examined|modif(y|ied) no|did not modify|"
    r"no file was modified|image units|visual tokens|evidence pack",
    re.I,
)

# Inside surviving lines, evidence-type self-naming is redacted to a neutral token so an
# answer survives but stops naming its arm's evidence class. Recorded, not silent.
REDACT = [
    (re.compile(r"\s*\((?:Basis|Source|Evidence)[^)]*\)", re.I), ""),
    (re.compile(r"(?:Basis|Source):[^.\n]*\.", re.I), ""),
    (re.compile(r"video\.txt|the metadata|metadata", re.I), "the available material"),
]


def scrub(text: str) -> str:
    lines = text.splitlines()
    out = []
    for i, ln in enumerate(lines):
        if i == 0 and ln.startswith("#"):
            out.append("# Answers")
            continue
        if re.match(r"^#{1,3}\s*Ledger", ln, re.I):
            break  # ledger section runs to EOF
        if BLOCK.search(ln):
            continue
        for rx, rep in REDACT:
            ln = rx.sub(rep, ln)
        out.append(ln)
    return "\n".join(out).strip() + "\n"


def main():
    outroot = os.path.join(BENCH, "rejudge")
    mapping, residue = {}, {}
    for vid in VIDS:
        random.seed(f"p2v2-{vid}")
        arms = {}
        for a in "NTAB":
            arms[a] = scrub(open(f"{BENCH}/data/p2/{vid}/{a}/answers.md").read())
        keys = list(arms)
        random.shuffle(keys)
        d = f"{outroot}/{vid}"
        os.makedirs(d, exist_ok=True)
        gt = open(f"{BENCH}/data/p2/{vid}/author/ground_truth.md").read()
        open(f"{d}/ground_truth.md", "w").write(gt)
        for L, k in zip("WXYZ", keys):
            open(f"{d}/{L}.md", "w").write(arms[k])
        mapping[vid] = dict(zip("WXYZ", keys))
        # verification: blocklist must not match any pack line; filename residue recorded
        bad, res = [], []
        for L in "WXYZ":
            for ln in open(f"{d}/{L}.md"):
                if BLOCK.search(ln):
                    bad.append((vid, L, ln.strip()[:90]))
                if re.search(r"\bu\d\d_\d+s|sheet_\d+|z_\d+_", ln):
                    res.append(L)
        if bad:
            print("LEAK", bad)
            sys.exit(1)
        residue[vid] = sorted(set(res))
    json.dump(mapping, open(f"{outroot}/MAPPING.json", "w"), indent=1)
    json.dump(residue, open(f"{outroot}/filename_residue.json", "w"), indent=1)
    print("packs ok; blocklist clean; filename residue per video:", residue)


if __name__ == "__main__":
    main()
