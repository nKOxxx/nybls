# Round 4 predictions, registered before any question was written

**2026-09-07.** Committed before ingest finished, before the author agent ran, and before
either arm saw anything. Question level predictions cannot be made yet because the
questions do not exist; the predictions below are about the structure and must hold
whatever questions the author agent writes.

## Closed form, at N = 30

| video | D (s) | grid interval | dead zone each end | p(capture) 3 s event | p(capture) 10 s event | N for even odds, 3 s |
|---|---|---|---|---|---|---|
| C timelapse | 370 | 12.3 s | 6.2 s | 0.243 | 0.811 | 62 |
| Rust session | 727 | 24.2 s | 12.1 s | 0.124 | 0.413 | 122 |
| Snake game | 1446 | 48.2 s | 24.1 s | 0.062 | 0.207 | 241 |
| HTML and CSS | 1697 | 56.6 s | 28.3 s | 0.053 | 0.177 | 283 |

## Predictions

**P1. The transcript contributes nothing.** Every video's transcript will be degenerate by
the words per minute test (below 1 content word per minute against a healthy floor of
29.6), and the line ratio test will call at least one of them healthy. Arm A's entire score
will rest on its 30 frames.

**P2. The gap is on transient items, not persistent ones.** Pooling all four videos, the
difference between arms on P labelled items will be within 1 point of zero per video on
average, and the difference on T labelled items will be at least 2 points per video on
average in Arm B's favour. This is the refined mechanism from round 3's failed P4, and it is
the round's main test. If the gap on P items is as large as on T items, the mechanism is
wrong again.

**P3. Arm A's transient accuracy tracks capture probability.** Ordering of Arm A's score on
T items, best to worst per question: timelapse is NOT necessarily best despite the highest
p(capture), because timelapse content persists for far less than 3 s. Excluding the
timelapse, Arm A's T item accuracy will fall in the order Rust, Snake, HTML.

**P4. Sub three second items defeat both arms.** Any T item the persistence measurement puts
under 3 s on screen will be missed by both arms at least half the time.

**P5. Cost ratio stays in the band.** Arm A spends 53,760 visual tokens per video. Arm B
will spend between 11,000 and 27,000, giving a per video ratio between 2x and 5x, as in every
prior round.

**P6. The reference will be corrected by an arm at least once.** It has been in every round.
The dense grid reference is better than the study sheet reference but it is still a sample.

## What falsifies the mechanism

P2 is the one that matters. If the gap concentrates on P items, or is flat across P and T,
then "transient answers are what the iterative arm buys" is wrong, and the paper's account
of *why* the iterative arm wins has to be rewritten again.
