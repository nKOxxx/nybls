# Round 5 Part 2 re-judging (deviation D9)

**Why.** Review run 025 (chair ruling, 2026-10-03) found the Part 2 "blind judged" claim
false: the first judging's packs leaked arm identity. N, T and A self-identified in their
H1 title lines ("control arm A: transcript + 30 uniform stills", "transcript-only arm",
"no-video arm") and arm B kept a residual "## Ledger" section in all eight videos. The
chair offered two remedies; this is the stronger one: re-judge all eight videos with
corrected anonymisation and report the movement.

**Method.** `build_judge_packs_p2_v2.py` rebuilt the packs from the committed first-judging
answers (`data/p2/<vid>/<arm>/answers.md`): first heading replaced with "# Answers",
ledger sections removed, arm-label and spend-reporting lines removed by blocklist, and
evidence-type self-naming inside surviving lines redacted to a neutral token (the
"(Basis: ...)" clauses, "metadata", "video.txt"). After building, every pack was
mechanically verified against the blocklist: zero matches. New per-video anonymisation
seeds; `rejudge/MAPPING.json` withheld from judges. Eight fresh judge agents (Fable 5.1),
one per video, same rubric as the first judging plus an explicit no-new-conventions
instruction; none saw any earlier verdict.

**Known residue, disclosed.** (i) Evidence filenames inside answers (`u07_*`, `sheet_*`)
remain, as in round 4; `rejudge/filename_residue.json` lists which letters carry them.
(ii) The scrub damaged four baseline answers whose own prose contained blocklisted words
(three contained the word "arm", e.g. "which this arm cannot see"; one a basis clause):
`rejudge/scrub_loss_audit.json` lists all items where more than 40% of an answer's text
was removed. In each of the four the conclusion sentence survived, and each item is an
N or T abstention or labelled inference; none involves arm A or B.

**Result of record (replaces the first judging; first judging retained in `data/judge_p2/`).**

| arm | first judging | re-judged (of 128) | % | abstained | wrong | fabricated |
|---|---|---|---|---|---|---|
| N | 31 | 28 | 21.9 | 41 | 0 | 0 |
| T | 82 | 79 | 61.7 | 13 | 0 | 0 |
| A | 116 | 115 | 89.8 | 1 | 1 | 0 |
| B | 125 | **125** | **97.7** | 0 | 0 | 0 |

By label, with the registered relabel applied (dwwhwVaI6vg Q7, V to B, per run 025 Morrow
M3): S (28 items): N 13/56, T 56/56, A 56/56, B 56/56. V (20 items): N 6/40, T 8/40,
A 31/40, B **38/40**. B-label (16 items): N 9/32, T 15/32, A 28/32, B 31/32. Silent
videos: N 3/32, T 10/32, A 25/32, B 30/32.

**Movement.** B is unchanged at 125/128 under correct anonymisation; the three baselines
each moved down slightly (N -3, T -3, A -1). The direction of the first judging's leak
bias, if any, favoured the baselines, not the tool. No prediction outcome changes: P5
(V items, B 95.0% vs T 20.0%) passes, P6 (S items, both 100%) passes, P7 (B = T + 46,
B > A) passes, P8 still fails (no arm fabricated anything; N's wrong count is now 0),
P9 still fails (T 31.2% on silent, above the registered 20%).

**Costs are unchanged** (same answers, same ledgers): B 68 images / 102,940 distinct
visual tokens vs A 240 / 430,080.

Per-video totals and the full audit trail are in `rejudge/` (packs, verdicts, mapping,
tally.json, scrub_loss_audit.json, filename_residue.json).
