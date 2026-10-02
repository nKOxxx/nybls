"""Build blind judge packs for round 5 Part 1: ground truth section + anonymised arms."""
import json, os, random, re, sys

S = sys.argv[1]  # scratch root containing p1/<id>/{N,T}/answers.md
BENCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R1 = ["LP10_YdKEPw"]
R2 = ["g9xUu2StOYg", "5oNHF72wbmI", "jgN4XWFUSb4"]
R3 = ["L24Wf0VlTE0", "DQdB7wFEygo", "oZAiHH9nrhk", "PV3r6BINlsM"]
R4 = ["92gQUnMCA08", "QtqYNyBv9r8", "Wlu4MsBnjuk", "vxP2PTA1GEk"]


def section(path, vid, ids):
    text = open(path).read()
    lines = text.splitlines()
    out, on = [], False
    for ln in lines:
        if ln.startswith("## ") and any(i in ln for i in ids):
            on = vid in ln
        elif ln.startswith("## Scoring"):
            on = False
        if on:
            out.append(ln)
    return "\n".join(out)


def gt(vid):
    if vid in R1:
        return open(f"{BENCH}/ground_truth.md").read()
    if vid in R2:
        return section(f"{BENCH}/gt_round2.md", vid, R2)
    if vid in R3:
        g = section(f"{BENCH}/gt_round3.md", vid, R3)
        return g + "\n\n# Ground truth errata (applies where it names this video)\n\n" + open(f"{BENCH}/round3/GT_ERRATA.md").read()
    g = section(f"{BENCH}/gt_round4.md", vid, R4)
    return g + "\n\n# Ground truth errata (applies where it names this video)\n\n" + open(f"{BENCH}/round4/GT_ERRATA.md").read()


def strip(path):
    t = open(path).read()
    # drop any final line that names which files were read (it reveals the arm)
    t = re.sub(r"(?im)^.*(files? (i )?read|read only|i read).*$", "", t)
    return t.strip() + "\n"


random.seed(20261002)
mapping = {}
for vid in R1 + R2 + R3 + R4:
    arms = {"N": strip(f"{S}/p1/{vid}/N/answers.md"), "T": strip(f"{S}/p1/{vid}/T/answers.md")}
    if vid in R4:
        m4 = open(f"{BENCH}/round4/judge_inputs/MAPPING.txt").read()
        for letter in "XY":
            mm = re.search(rf"{vid}:.*?\b{letter}=arm([AB])", m4)
            arms[mm.group(1)] = open(f"{BENCH}/round4/judge_inputs/{vid}/{letter}.md").read()
    keys = list(arms)
    random.shuffle(keys)
    letters = "WXYZ"[: len(keys)]
    d = f"{S}/judge/{vid}"
    os.makedirs(d, exist_ok=True)
    open(f"{d}/ground_truth.md", "w").write(gt(vid))
    for L, k in zip(letters, keys):
        open(f"{d}/{L}.md", "w").write(arms[k])
    mapping[vid] = dict(zip(letters, keys))
json.dump(mapping, open(f"{S}/judge/MAPPING.json", "w"), indent=1)
print(json.dumps(mapping))
