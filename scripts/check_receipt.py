#!/usr/bin/env python3
"""Recompute the benchmark headline from the stored results files.

What this proves: the per-video rows in rounds 2, 3 and 4 add up to the totals the
files print, the headline in RESULTS_round4.md equals those totals plus a round 1
remainder, the percentages and the ratio follow from the counts, and the README
quotes the same numbers. A README that drifts from the results file fails here.

What it does not prove: the judge scores themselves. Those came from language-model
judges and cannot be replayed from this repository. And round 1's contribution is
not in a table of its own, so it is derived as headline minus rounds 2 to 4 and
printed as "implied", not verified.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

BENCH = Path(__file__).resolve().parent.parent / "bench"
README = Path(__file__).resolve().parent.parent / "README.md"


def num(s: str) -> int:
    return int(s.replace(",", ""))


def rows(path: Path, pat: str) -> list[re.Match]:
    return [m for line in path.read_text().splitlines() if (m := re.search(pat, line))]


def check() -> list[str]:
    errs: list[str] = []
    out: list[str] = []

    def eq(label, got, want):
        ok = got == want
        out.append(f"{'ok  ' if ok else 'FAIL'} {label}: {got} vs {want}")
        if not ok:
            errs.append(label)

    # round 2: rows "| name | A / 10 | A tokens | B / 10 | B tokens | ... |"
    r2 = (BENCH / "RESULTS_round2.md").read_text()
    body = [ln for ln in r2.splitlines() if re.match(r"\| \w{11} ", ln)]
    cells = [re.findall(r"\d[\d,]*", ln.split("|", 2)[2]) for ln in body]  # drop the id column
    eq("round 2 videos found", len(body), 3)
    a2 = sum(int(c[0]) for c in cells)
    tot2 = re.search(r"\*\*Round 2 total\*\* \| \*\*(\d+) / 30\*\* \| \*\*([\d,]+)\*\* \| \*\*(\d+) / 30\*\* \| \*\*([\d,]+)\*\*", r2)
    eq("round 2 arm A points (rows)", a2, int(tot2.group(1)))
    eq("round 2 arm A tokens (rows)", sum(num(c[2]) for c in cells), num(tot2.group(2)))
    eq("round 2 arm B points (rows)", sum(int(c[3]) for c in cells), int(tot2.group(3)))
    eq("round 2 arm B tokens (rows)", sum(num(c[5]) for c in cells), num(tot2.group(4)))
    r2_a_pts, r2_a_tok, r2_b_pts, r2_b_tok = int(tot2.group(1)), num(tot2.group(2)), int(tot2.group(3)), num(tot2.group(4))

    # round 3
    r3 = (BENCH / "RESULTS_round3.md").read_text()
    t3 = re.search(r"\*\*Round 3\*\* \| \| \*\*(\d+)/36 \(\d+%\)\*\* \| \*\*(\d+)/36 \(\d+%\)\*\* \| \*\*([\d,]+)\*\* \| \*\*([\d,]+)\*\*", r3)
    rows3 = re.findall(r"^\| (?:jet engine|docker|stock market|rome) \| [\d:]+ \| (\d+)/(\d+) \(\d+%\) \| (\d+)/\d+ \(\d+%\) \| ([\d,]+) \| ([\d,]+) \|", r3, re.M)
    eq("round 3 videos found", len(rows3), 4)
    eq("round 3 arm A points (rows)", sum(int(r[0]) for r in rows3), int(t3.group(1)))
    eq("round 3 arm B points (rows)", sum(int(r[2]) for r in rows3), int(t3.group(2)))
    eq("round 3 arm A tokens (rows)", sum(num(r[3]) for r in rows3), num(t3.group(3)))
    eq("round 3 arm B tokens (rows)", sum(num(r[4]) for r in rows3), num(t3.group(4)))

    # round 4
    r4 = (BENCH / "RESULTS_round4.md").read_text()
    rows4 = re.findall(r"^\| (?:C timelapse|Rust session|HTML and CSS|Snake game) \| [\d:]+ \| (\d+)/10 \| (\d+)/10 \|.*?\| ([\d,]+) \| ([\d,]+) \| [\d.]+x \|", r4, re.M)
    t4 = re.search(r"\*\*Round 4\*\* \| \| \*\*(\d+)/40 \(\d+%\)\*\* \| \*\*(\d+)/40 \(\d+%\)\*\*.*?\*\*([\d,]+)\*\* \| \*\*([\d,]+)\*\*", r4)
    eq("round 4 videos found", len(rows4), 4)
    eq("round 4 arm A points (rows)", sum(int(r[0]) for r in rows4), int(t4.group(1)))
    eq("round 4 arm B points (rows)", sum(int(r[1]) for r in rows4), int(t4.group(2)))
    eq("round 4 arm A tokens (rows)", sum(num(r[2]) for r in rows4), num(t4.group(3)))
    eq("round 4 arm B tokens (rows)", sum(num(r[3]) for r in rows4), num(t4.group(4)))

    # headline
    h = re.search(r"Arm A \*\*(\d+)/112 \((\d+)%\)\*\* for\s+([\d,]+) distinct visual tokens.*?Arm B \*\*(\d+)/112 \((\d+)%\)\*\* for ([\d,]+)\.", r4, re.S)
    a_pts, a_pct, a_tok, b_pts, b_pct, b_tok = int(h[1]), int(h[2]), num(h[3]), int(h[4]), int(h[5]), num(h[6])
    eq("headline arm A percent", round(100 * a_pts / 112), a_pct)
    eq("headline arm B percent", round(100 * b_pts / 112), b_pct)
    ratio = a_tok / b_tok
    eq("headline token ratio rounds to 4.0x", round(ratio, 1), 4.0)
    eq("control gets this share of the score", round(100 * a_pts / b_pts), 82)
    out.append(f"info round 1, implied (headline minus rounds 2 to 4, NOT verified): "
               f"A {a_pts - r2_a_pts - int(t3.group(1)) - int(t4.group(1))}/6 pts, "
               f"B {b_pts - r2_b_pts - int(t3.group(2)) - int(t4.group(2))}/6 pts, "
               f"tokens A {a_tok - r2_a_tok - num(t3.group(3)) - num(t4.group(3)):,} "
               f"B {b_tok - r2_b_tok - num(t3.group(4)) - num(t4.group(4)):,}")

    # README quotes the same numbers
    rd = README.read_text().replace("\n", " ")
    for label, needle in [("README arm A points", f"scores {a_pts} of 112"),
                          ("README arm A tokens", f"{a_tok:,} visual tokens"),
                          ("README arm B points", f"nybls scores {b_pts} of 112"),
                          ("README arm B tokens", f"{b_tok:,}"),
                          ("README ratio", f"{ratio:.1f} times the tokens"),
                          ("README hero ratio", f"<h3>{ratio:.1f}x</h3>"),
                          ("README hero scores", f"<h3>{b_pct}% vs {a_pct}%</h3>")]:
        eq(label, needle in rd, True)
    print("\n".join(out))
    return errs


if __name__ == "__main__":
    bad = check()
    print("\nRECEIPT " + ("FAILED: " + ", ".join(bad) if bad else "OK"))
    sys.exit(1 if bad else 0)
