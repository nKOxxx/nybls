"""Mechanical grader for Part 3 (PREDICTIONS_ADDENDUM.md rubric). Usage: grade_part3.py <p3root>.

Execution items run the artefacts; feature items are regex checks on the source. Each
check prints its evidence so a reader can re-score by hand.
"""
import os, re, subprocess, sys

def have(src, pat):
    return re.search(pat, src, re.I | re.S) is not None

def grade_python(d):
    pts, notes = 0, []
    p = f"{d}/program.py"
    if not os.path.exists(p):
        return 0, ["no program.py"]
    src = open(p).read()
    # runs under scripted stdin (2)
    try:
        r = subprocess.run([sys.executable, p], input="25\nswim\nyes\nleft\n1\n" * 20,
                           capture_output=True, text=True, timeout=20)
        ok = r.returncode == 0 and "Traceback" not in r.stderr
    except Exception as e:
        ok, r = False, None
        notes.append(f"run error: {e}")
    pts += 2 if ok else 0; notes.append(f"runs: {ok}")
    checks = [
        (1, r"int\s*\(\s*input", "int(input"),
        (2, r"age\s*>=\s*18", "age >= 18"),
        (2, r"lake|swim", "lake/swim scenario"),
        (1, r"(def\s+\w*end|game over|the end|you (die|lose|win))", ">=2 endings marker"),
        (2, r"(while|def\s+\w+\(.*\):)", "loop or scene functions"),
    ]
    for w, pat, name in checks:
        got = have(src, pat)
        pts += w if got else 0
        notes.append(f"{name}: {got}")
    return pts, notes

def grade_c(d):
    pts, notes = 0, []
    p = f"{d}/program.c"
    if not os.path.exists(p):
        return 0, ["no program.c"]
    src = open(p).read()
    binp = f"{d}/a.out"
    comp = subprocess.run(["cc", p, "-o", binp, "-lm"], capture_output=True, text=True)
    ok = comp.returncode == 0
    pts += 2 if ok else 0; notes.append(f"compiles: {ok}")
    checks = [
        (1, r"160.{0,40}44|44.{0,40}160", "160x44 buffers"),
        (1, r"cubeWidth\s*=\s*10|width\s*=\s*10", "cubeWidth 10"),
        (1, r"distanceFromCam\w*\s*=\s*60", "distanceFromCam 60"),
        (1, r"K1\s*=\s*40", "K1 40"),
        (1, r"0\.6", "incrementSpeed 0.6"),
        (1, None, "six face chars"),
        (1, r"1\s*/\s*z.{0,400}x\s*\*\s*2|ooz|\*\s*2\s*\*.{0,20}ooz", "1/z and x*2 projection"),
        (1, r"\+=\s*0\.005.{0,400}usleep|usleep.{0,400}\+=\s*0\.005|\\x1b\[2J.{0,600}\\x1b\[H", "A/B 0.005, usleep, escapes"),
    ]
    for w, pat, name in checks:
        if pat is None:  # all six distinct face characters must appear as char literals
            got = all(f"'{c}'" in src for c in [".", "$", "~", "#", ";", "+"])
        else:
            got = have(src, pat)
        pts += w if got else 0
        notes.append(f"{name}: {got}")
    return pts, notes

def main():
    root = sys.argv[1]
    for vid, fn in [("7R-CfL21zIY", grade_python), ("p09i_hoFdd0", grade_c)]:
        print(f"== {vid}")
        for arm in "NTAB":
            d = f"{root}/{vid}/{arm}"
            pts, notes = fn(d)
            print(f"  {arm}: {pts}/10  | " + "; ".join(notes))

if __name__ == "__main__":
    main()
