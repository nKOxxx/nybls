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
| Rust session | 12:07 | 8/10 | 10/10 | 4/4 | 4/4 | 4/6 | 6/6 | 58,800 | 5,883 | 10.0x |
| HTML and CSS | 28:17 | 10/10 | 10/10 | 6/6 | 6/6 | 4/4 | 4/4 | 168,000 | 15,692 | 10.7x |
| Snake game | 24:05 | 8/10 | 10/10 | 4/4 | 4/4 | 4/6 | 6/6 | 53,760 | 21,514 | 2.5x |
| **Round 4** | | **31/40 (78%)** | **37/40 (93%)** | **18/18** | **18/18** | **13/22** | **19/22** | **334,320** | **69,689** | **4.80x** |

Correction from review run 024: Arm A's cost was originally written as a constant 53,760 per video. Recomputed from the one shot frames on disk with the ledger's estimator, the Rust control is 58,800 (frames 1568 by 980) and the HTML control 168,000 (frames 1568 by 2788, a vertical 360 by 640 source upscaled). The round and overall totals below use the recomputed figures; under the API's longest edge limit the HTML row would be at most 143,520 on the tier the arms ran on.

Rust Arm B is 10/10 after one reference correction (`round4/GT_ERRATA.md`), verified
against the pixels before the judge's stated conditional was applied.

**All four rounds, 12 videos, 112 audited questions:** Arm A **83/112 (74%)** for
764,400 distinct visual tokens served (645,120 before the review run 024 recomputation); Arm B **101/112 (90%)** for 189,052. **Arm A was served 4.0x the
distinct visual tokens for 82% of Arm B's score.** 112 is a point total over 56 audited questions.

## Predictions, scored

**P1, the transcript contributes nothing. Substantive claim HELD; registered threshold FAILED on one video.** All four transcripts are degenerate by
the words per minute test: 2.93, 0.33, 0.08 and 0.07 content words per minute against a
healthy floor of 29.6. Correction from review run 024: the shipped line ratio guard, which strips timestamps, flagged the three whisper transcripts (their manifests read UNRELIABLE); it never ran on the timelapse, whose transcript came through the caption path the guard does not check. The 1.000 figures in the first version of this file came from the bench script counting timestamped lines. One wrinkle recorded honestly: the timelapse
carries auto captions of its music track and sits at 2.93, above the "below 1" threshold
the prediction wrote; it is still an order of magnitude under the floor.

**P2, the gap is on transient items and near zero on persistent ones. Qualitative clause HELD on all four videos; registered quantitative clause (transient gap of at least 2 points per video on average) FAILED at a mean of 1.5.** Persistent items: 4 to 4, 4 to 4, 6 to 6, 4 to 4, a perfect tie at 18 to 18.
Transient items: 1 to 3, 4 to 6, 4 to 4, 4 to 6, for 13 to 19 (gaps +2, +2, 0, +2, mean 1.5). **Every one of the six
points separating the arms sits on a transient item.** This is the
round's main test and it is the sharpest confirmation of a mechanism in the benchmark.

**A refinement the round forced.** The label predicts *where* a gap can be, not whether
there is one. Two Rust items and both HTML items were labelled transient by the author
because they happen once, but they persisted: measured at 2560 px, 33 s and 20 s in
scrollback for the Rust items (the 20 s item just under the 24.2 s grid interval, caught at
p = 0.83), and 113 to 160 s by both arms' readings for the HTML items, which OCR cannot
measure on that 360 px source. Both arms got all four. The
control's failures are on items that are on screen for under 2 seconds: the timelapse's
nonsense command (at most 0.5 s), its flooded terminal (at most 0.5 s), its all caps
comment (1.25 s), and the Rust job status line (about 2 s). **What the grid cannot reach
is decided by on screen persistence.** The P/T label is a proxy for it and a leaky one.

**P3, the control's transient accuracy falls in the order Rust, Snake, HTML (excluding the timelapse). FAILED.** Observed 4/6, 4/6, 4/4: the longest video scored best on transient items. This prediction was registered and omitted from the first version of this file; review run 024 found the omission.

**P4, sub three second items defeat both arms at least half the time. HELD.** Of the four
items under 2 s, the control missed all four and the iterative arm missed two. On the
Snake video the control's two partial answers were both content typed after its last
sample at 1421.4 s (D = 1445.49 s; an earlier version of this file said 1421.9 s), inside the closing dead zone of 24.1 s that Section 4 of the paper
derives in closed form. Correction from review run 024: of the six points separating the arms, five sit on items under two seconds or typed after the last sample; the sixth, Snake Q4, is the final frame_size_y, a long lived value on screen until 1335 s and again at 1437 s that was not legible at any of the control's sample instants. That is a third failure class the capture model does not cover. The
iterative arm found the all caps comment with a zoom and the job status line by aiming a
sheet at the flood; it did not find either half second terminal state and reported both as
insufficient evidence.

**P5, cost ratio between 2x and 5x per video. FAILED on the high side.** Rust came in at
10.0x (58,800 against 5,883 once the control's frames were costed from disk; 9.1x at the
constant 53,760 this file first used), because the iterative arm answered all five from
nine images. The timelapse came in
at 2.0x, the bottom of the band, because the iterative arm spent 24 of its 25 unit budget
hunting sub second states it never found. The band was wrong in both directions.

**P6, the reference is corrected by an arm at least once. HELD, three times.** The Rust
reference recorded the PID of the first of two runs of the same command, four seconds
apart; the question asks for the final job status line, which belongs to the second. The
Snake reference missed a recurrence of the traceback and a late reappearance of the final
height; both were on screen where the arm said. Fifth, sixth and seventh reference
corrections across the benchmark. A dense grid read once is still a sample.

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
