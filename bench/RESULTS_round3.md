# Benchmark round 3 — a duration sweep, scored against predictions registered in advance

**Date:** 2026-09-04 · **4 videos, 5:01 to 44:32 (an 8.9x spread), 17 valid questions.**
Predictions were committed at `6b38d3b` **before any of the eight arms returned**
(`round3/PREDICTIONS.md`). Ground truth was written 2026-09-02 and moved out of the
repository during the runs. The tool was pinned at HEAD with `nybls_core/` read-only after
round 2's contamination incident; **its hash was identical before and after all eight runs.**

## Result

| Video | D | Arm A | Arm B | A tokens | B tokens | ratio |
|---|---|---|---|---|---|---|
| jet engine | 5:01 | 9/10 (90%) | 9/10 (90%) | 53,760 | 9,248 | 5.8x |
| docker | 11:53 | 5/6 (83%) | 6/6 (100%) | 53,760 | 12,080 | 4.5x |
| stock market | 24:37 | 8/10 (80%) | 8/10 (80%) | 53,760 | 19,163 | 2.8x |
| rome | 44:32 | 7/10 (70%) | 10/10 (100%) | 53,760 | 12,832 | 4.2x |
| **Round 3** | | **29/36 (81%)** | **33/36 (92%)** | **215,040** | **53,323** | **4.03x** |

**All three rounds — 8 videos, 76 valid questions:** Arm A **56/76 (74%)** for 430,080
visual tokens; Arm B **68/76 (89%)** for 119,363. **Arm A spent 3.60x for 83% of Arm B's score.**

## Predictions, scored

**P1 — Arm A's accuracy falls as duration rises. CONFIRMED, cleanly and monotonically:
90%, 83%, 80%, 70% across 5, 12, 25 and 44 minutes.** This is the sweep's headline. The
control's budget is constant while the interval between its samples grows from 10 s to 89 s,
and its accuracy tracks that directly.

**P2 — Arm A near-maximum on the 5-minute video. CONFIRMED (9/10).** Where the answers are
persistent attributes and the grid is dense, uniform sampling is a perfectly good instrument
and there is nothing to beat. It cost 5.8x more to draw with the iterative arm.

**P3 — item-level failure calls. 4 of 5 confirmed, 1 invalidated.** Named in advance and
confirmed: rome Q3 (Hadrian's Wall — Arm A "insufficient evidence", Arm B found it at 24:39),
rome Q4 (the relief — Arm A found a different one, Arm B matched ground truth exactly),
docker Q3 (the port — see below), stock Q2 (partial for Arm A). docker Q2 was invalidated.

**P4 — the gap widens with duration. NOT CONFIRMED.** Gap in percentage points by duration:
**+0, +17, +0, +30.** Not monotonic. The 25-minute video is a flat tie at 8/10 each. Duration
predicts the *control's* accuracy (P1) but does not predict the *gap*, because what the
iterative arm gains depends on whether the specific questions have transient answers, not on
how long the video is. **This was our prediction and it failed; the mechanism in P1 is
narrower than we claimed.**

**P5 — Arm B not immune to short transients. CONFIRMED,** twice: the jet engine's 4.0-second
speed caption defeated both arms, and Arm B missed the DRHP title cards that Arm A found.

## The single clearest result: docker Q3

The question is what port the Dockerfile sets. Arm A's uniform grid sampled the file at
lines 4-11 and again at lines 20-22; **the port lines 13-18 fell in the gap between two
frames.** It answered "insufficient evidence", then deduced 9000 correctly from side
evidence (`docker run 9000:9000`, `localhost:9000`) and labelled the deduction as such.
Arm B requested the frame it needed and **read `ENV PORT=9000` off line 18.**
Same question, same video, 4.5x less cost, and the difference is not reasoning quality —
Arm A reasoned well — it is whether the pixels were ever fetched.

## Two errata, both against us

**Three of twenty questions do not test looking** (`round3/QUESTION_VALIDITY_ERRATA.md`).
The design filter matched written tokens against spoken words: `.dockerignore` is said as
"docker ignore", `node_modules` as "node modules". Both passed a zero-hit check. Docker Q2
and Q4 are invalid and excluded above; the jet engine's Q5 is partially compromised.
Rounds 1-2 used the same filter and must be re-audited. We caught it only because an arm
answered honestly and named the transcript as its source.

**Our ground truth was wrong about the jet engine, and both arms were nearly right**
(`round3/GT_ERRATA.md`). "310-620 mph" is on screen from 200.75 s for 4.00 s, OCR-verified
at 0.25 s resolution — the design note had rejected it as spoken-only. Arm A's grid samples
at 205.68 s, **0.93 s after it disappears**. Arm B spent a frame at 200.0 s specifically to
check, **0.75 s before it appears**. A four-second event, a five-minute video, both arms
looking in the right place, both missing by under a second from opposite sides. Capture
probability 0.399; even odds need 37 frames.

## Two production findings

**The transcript can be worthless, and the benchmark caught it.** The stock-market video's
ASR output is degenerate — Hindi/Urdu mis-transcribed into pseudo-Latin, one line looping
from 01:48 to 24:35, 65 unique lines in 906. Arm B reported that all five of its answers
rest on frames alone. This is direct evidence for the inverse relationship between what the
transcript carries and what looking is worth.

**Round 2's contamination fix has a cost in production.** Tile-snapping now silently
redirects `frames --at` to an already-served timestamp, with no flag to suppress it. Two
arms reported it independently, and on the stock-market video it **cost Arm B question 2**:
it could not sample a nearby instant of a title animation to see past an occluding banknote.
A 3-second snap tolerance is wider than the events we are measuring, which are 2 to 5 seconds.

## What must be said against this round

- Scoring is still by the tool's author, and partial-credit calls are judgement.
- Ground truth is still built from the tool's own study sheets, and was wrong again here.
- One prediction (P4) failed, and one prediction set (P3) rested partly on invalid questions.
- 17 valid questions across 4 videos remains small.
