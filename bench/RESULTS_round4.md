# Benchmark round 4: silent video, and persistent against transient

**Date:** 2026-09-07 · **4 public silent screen recordings, 6:10 to 28:17, 20 questions.**
Protocol and predictions were committed before any question existed (`round4/PROTOCOL.md`,
`round4/PREDICTIONS.md`, commit f7b5e19). Tool pinned read only at `fd11789`.

## What is different about this round

Three structural changes, each fixing a failure recorded in an earlier round:

- **The reference owes nothing to the tool.** Ground truth was built from a dense uniform
  ffmpeg grid, one frame every 10 s, by an author agent with no access to nybls. Earlier
  rounds built it from the tool's own study sheets.
- **Author, arms and judge are separate agents.** The author wrote questions and ground
  truth; the arms answered; a judge scored each video with the arms labelled X and Y and
  the mapping withheld. Earlier rounds had the experimenter write and score.
- **Every question is labelled P (persistent) or T (transient) at design time**, so the
  hypothesis that fell out of round 3's failed P4 can be tested directly: the gap between
  arms is on transient answers, not on duration.

On silent video the narration leak that voided four earlier questions cannot occur.

## Result

| video | D | Arm A | Arm B | A on P | B on P | A on T | B on T | A tokens | B tokens | ratio |
|---|---|---|---|---|---|---|---|---|---|---|
| C timelapse | 6:10 | 5/10 | 7/10 | 4/4 | 4/4 | 1/6 | 3/6 | 53,760 | 26,600 | 2.0x |
| Rust session | 12:07 | 8/10 | 10/10 | 4/4 | 4/4 | 4/6 | 6/6 | 53,760 | 5,883 | 9.1x |
| HTML and CSS | 28:17 | 10/10 | 10/10 | 6/6 | 6/6 | 4/4 | 4/4 | 53,760 | 15,692 | 3.4x |
| Snake game | 24:05 | pending | | | | | | 53,760 | | |

Rust Arm B is 10/10 after one reference correction (`round4/GT_ERRATA.md`), verified
against the pixels before the judge's stated conditional was applied.

## Predictions, scored so far

**P1, the transcript contributes nothing. HELD.** All four transcripts are degenerate by
the words per minute test: 2.93, 0.33, 0.08 and 0.07 content words per minute against a
healthy floor of 29.6. All four score a perfect 1.000 on the line ratio test, i.e. the
shipped guard calls every one of them healthy. One wrinkle recorded honestly: the timelapse
carries auto captions of its music track and sits at 2.93, above the "below 1" threshold
the prediction wrote; it is still an order of magnitude under the floor.

**P2, the gap is on transient items and near zero on persistent ones. HELD, on all three
videos judged.** Persistent items: 4 to 4, 4 to 4, 6 to 6. Transient items: 1 to 3, 4 to 6,
4 to 4. Every point of difference between the arms sits on a transient item. This is the
round's main test and it is the sharpest confirmation of a mechanism in the benchmark.

**A refinement the round forced.** The label predicts *where* a gap can be, not whether
there is one. Two Rust items and both HTML items were labelled transient by the author
because they happen once, but they persisted in scrollback or in the editor for 50 to 200
seconds, longer than the control's grid interval, and both arms got all of them. The
control's failures are on items that are on screen for under 2 seconds: the timelapse's
nonsense command (at most 0.5 s), its flooded terminal (at most 0.5 s), its all caps
comment (1.25 s), and the Rust job status line (about 2 s). **What the grid cannot reach
is decided by on screen persistence.** The P/T label is a proxy for it and a leaky one.

**P4, sub three second items defeat both arms at least half the time. HELD.** Of the four
items under 2 s, the control missed all four and the iterative arm missed two. The
iterative arm found the all caps comment with a zoom and the job status line by aiming a
sheet at the flood; it did not find either half second terminal state and reported both as
insufficient evidence.

**P5, cost ratio between 2x and 5x per video. FAILED on the high side.** Rust came in at
9.1x, because the iterative arm answered all five from nine images. The timelapse came in
at 2.0x, the bottom of the band, because the iterative arm spent 24 of its 25 unit budget
hunting sub second states it never found. The band was wrong in both directions.

**P6, the reference is corrected by an arm at least once. HELD.** The Rust reference
recorded the PID of the first of two runs of the same command, four seconds apart; the
question asks for the final job status line, which belongs to the second. A 10 s grid
cannot separate two events four seconds apart. Fifth reference correction across the
benchmark.

## Two production findings

**Tile snapping charged for duplicates.** On the timelapse, three `frames --at` requests
inside a five second window were all snapped to two already served tiles: two identical
files served, three units charged, and the window between them unreachable through
`frames`. `zoom` does not snap, which is how the arm eventually read that region. This is
the third round in which the round 2 contamination fix has cost an arm something, and it is
now costing budget as well as coverage.

**A 360 pixel source.** The HTML video was stored at 360 by 640, a vertical low resolution
format, where the other three are 1152 to 1280 wide. Both arms hedged on every digit for
the same reason and neither could resolve it by spending more. Acquisition should prefer
the highest available resolution when the content is a screen recording, and the ledger
should say when it did not get one.

## What must be said against this round

- Four videos, 20 questions, one genre: programming screen recordings. The silent case is
  real but it is one kind of silent video.
- The judge scored from text only and could not check evidence citations against frames.
  Citation filenames (`u07_` versus `sheet_`) reveal the arm; the judge was told to ignore
  them and there is no way to verify that it did.
- The author agent for the HTML video used `sips` to enlarge grid frames. That is not the
  tool under test, but it is a deviation from "read only" and is recorded.
- The persistence measurement fails on small terminal text and the numbers for four of the
  eleven transient items rest on reader agreement rather than OCR (`round4/PERSISTENCE.md`).
- Partial credit is still judgement, now the judge agent's rather than the author's.
