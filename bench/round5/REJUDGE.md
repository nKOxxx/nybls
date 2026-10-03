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

**Known residue and instrument damage, disclosed.** (i) Evidence filenames inside
answers (`u07_*`, `sheet_*`) remain, as in round 4; `rejudge/filename_residue.json`
lists which letters carry them, and they identify the {A, B} pair in all eight videos.
(ii) Arm B's answers open with spend narration ("Visual spend was limited to...") that
survives the scrub in several packs and is content-identifying in the same way. A judge
willing to infer from such content could identify arms; no pack any longer *labels* one.
(iii) The scrub damaged six answers, listed in `rejudge/scrub_loss_audit.json`
(regenerate with `audit_scrub_loss.py`): the line filter removed lines whose own prose
contained blocklisted words (three contained the word "arm"), and one redaction regex
consumed text to the first period, truncating at abbreviations such as "e.g.". The
damage and its score effect, item by item: oQtzvzKP5Q0 T Q6 lost its entire body
(scored 0, abstained, in both judgings); 7R-CfL21zIY N Q3 and Q7 each dropped 1 to 0,
and those two points ARE scrub artefacts, not de-biasing; bNpx7gpSqbY A Q1 lost its
speaker-name bullet (A's item score unchanged, verified); p09i_hoFdd0 A Q6 lost 42% of
its text (A's total is 14 in both judgings); jtl4KKRIheo T Q8's conclusion survived.
An earlier revision of this file understated this list as four items, claimed every
conclusion sentence survived, and claimed no A or B item was involved; all three
statements were wrong and were corrected by the run 025 re-verification.

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

**Movement.** B is unchanged at 125/128 under correct anonymisation. The raw baseline
movement is N -3, T -3, A -1; two of N's three points are the scrub artefacts above, so
the movement attributable to de-biasing is N -1, T -3, A -1, B 0. The defensible
statement is the narrow one: the first judging's identity leak did not inflate the
tool's score, and correcting it did not close any gap. No prediction outcome changes: P5
(V items, B 95.0% vs T 20.0%) passes, P6 (S items, both 100%) passes, P7 (B = T + 46,
B > A) passes, P8 still fails (no arm fabricated anything; N's wrong count is now 0),
P9 still fails (T 31.2% on silent, above the registered 20%).

**Costs are unchanged** (same answers, same ledgers): B 68 images / 102,940 distinct
visual tokens vs A 240 / 430,080.

Per-video totals and the full audit trail are in `rejudge/` (packs, verdicts, mapping,
tally.json, scrub_loss_audit.json, filename_residue.json).
