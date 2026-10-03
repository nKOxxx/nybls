# Round 5 addendum: cost-matched control and Part 3. Registered before either runs.

Written 2026-10-03, after the D9 re-judging closed and before any addendum arm, judge or
execution ran. Closes the two experiments the paper has named as not yet run since v2:
the cost-matched control (Limitations; chair 024 conflict 7) and the Part 3 "use it"
task (D8).

## Arm AM: the cost-matched control

Per Part 2 video, arm AM receives the transcript plus a uniform grid of exactly as many
full-resolution frames as arm B was served on that video, per the committed ledgers:
bNpx 4, oQtz 10, 7R 4, dwwh 3, txsp 17, p09i 20, WDAm 8, jtl 2; 68 in total.
[AMENDED 2026-10-03, before any AM arm ran: the first registration asserted "66 distinct
timestamps, two duplicate re-serves", a claim the ledgers cannot support since they
record no per-image timestamps; the match is on served counts, and the first list also
had bNpx7gpSqbY at 2 where the ledger says 4.] Frames are rendered at the same 1568 width as the one-shot
pack, so AM's token total slightly EXCEEDS B's (full-res frames cost more per image than
B's mostly-sheet mix): the mismatch favours the control and is reported. Same prompt and
constraints as arm A. One judge per 4 videos scores AM alone against the author ground
truth, same rubric and outcome classes; single-arm judging cannot be blind and is not
claimed to be.

- **P16.** AM scores below B's 125/128 (the selection method matters at equal image count).
- **P17.** AM scores below A's 115/128 (fewer frames hurt a grid even with the transcript;
  if AM lands between A and B, uniform-at-B's-count beats uniform-at-30 and the paper
  must say the dump was oversized, not undersized).
- **P18.** AM's loss relative to B is concentrated on V items: AM drops at least 4 points
  on V items relative to B's 38/40.

## Part 3: reproduce the program ("use it")

The two coding videos: 7R-CfL21zIY (narrated Python tutorial; final program is the
choose-your-own-adventure game) and p09i_hoFdd0 (silent C spinning-cube). All four arms
(N, T, A, B) per video, same evidence rules as Part 2, fresh agents: "write the program
this video builds, as close to the video's own final version as your evidence allows,"
output a single source file. Execution and grading are mechanical, by committed script
where possible, against a rubric fixed here, derived only from the author ground truths
and the videos' committed persistence data:

- Python (10 points): runs under scripted stdin without crashing (2); uses int(input())
  for age (1); branches on age >= 18 (2); lake/swim scenario with the GT's outcome
  structure (2); at least two distinct endings (1); game loop or linear flow matching the
  GT description (2).
- C cube (10 points): compiles with cc (2); buffer dims 160x44 (1); cubeWidth 10 (1);
  distanceFromCam 60 (1); K1 40 (1); incrementSpeed 0.6 (1); the six face characters
  (1); 1/z z-buffer compare and x*2 aspect projection (1); A/B += 0.005 with usleep and
  the two escape sequences (1).

- **P19.** Grading order on both videos: B >= A >= T >= N.
- **P20.** On the silent C video, T scores at most 3/10 (genre knowledge gets a cube, not
  THIS cube); B scores at least 8/10.
- **P21.** On the narrated Python video, T is within 2 points of B (the speech carries
  the program's logic; the screen holds only exact constants).

## Non-Claude judge (robustness, runs only if a non-Anthropic key is available)

If a usable OpenAI key exists in the local api-treasure-chest, one GPT-class judge
re-scores the two Part 3 gradings' discretionary items and two Part 2 videos
(bNpx7gpSqbY, p09i_hoFdd0) against the same ground truths; agreement is reported as a
robustness line, not a score of record. If no key: reported as not run, blocked on
credentials.

- **P22.** On the two re-scored videos, the non-Claude judge's per-arm totals differ from
  the Claude judge's by at most 2 points per arm.
