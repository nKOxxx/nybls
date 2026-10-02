# Round 5 results: does giving the model the video improve what it says?

Protocol `PROTOCOL.md` and predictions `PREDICTIONS.md` registered at `b6f46be`; Part 1b at
`e03b73e`; Part 1c at `f2ff358`. All before the arms they govern ran. Deviations D1 to D6 are
in `PROTOCOL.md`. Raw answers, judge inputs, verdicts and arm mappings are in `data/`.

Arms: **N** title/channel/duration only · **T** transcript only (what caption loaders give
an agent) · **A** transcript + 30 uniform frames · **B** nybls + its shipped protocol.
Scoring 2/1/0/-1 as in every round; every item also classified correct / partial /
abstained / wrong / fabricated by a blind judge (Fable 5.1).

## Part 1: the 56 audited questions, with the instruction "say insufficient evidence rather than guess"

| arm | points (of 112) | % | fabricated | wrong |
|---|---|---|---|---|
| N | 3 | 2.7 | 0 | 0 |
| T | 17 | 15.2 | 0 | 0 |
| A (of record) | 83 | 74.1 | – | – |
| B (of record) | 101 | 90.2 | – | – |

Round 4 blind rejudge (P4): A 31/40 and B 37/40, identical to the scores of record.

These questions were chosen to be answerable by looking (stated bias, PROTOCOL Part 1), so
T's 15% says little about captions in general. What it does say: on questions whose answer
is on screen, a caption-reading agent answers 15% and abstains on 40 of 56; the no-video
agent abstains on 53 of 56. **Neither invented anything.**

## Part 1b: same questions, neutral prompt (no honesty instruction), Fable 5.1

| arm | points | % | fabricated | wrong | abstained |
|---|---|---|---|---|---|
| N | 3/112 | 2.7 | 0 | 0 | 53 |
| T | 18/112 | 16.1 | 0 | 1 | 39 |
| B (silent videos only) | 36/40 | 90.0 | 0 | 0 | 1 |
| T (silent videos only) | 0/40 | 0.0 | 0 | 0 | 20 |

Removing the instruction changed nothing material. Asked about a video it cannot see, with
no instruction to be careful, the model says so ("Nothing below is guessed").

## Part 1c: same, on Claude Haiku 4.5

| arm | points | % | fabricated | wrong | abstained |
|---|---|---|---|---|---|
| N | 1/112 | 0.9 | 0 | 0 | 55 |
| T | 19/112 | 17.0 | 0 | 0 | 40 |
| B (silent videos only) | 11/40 | 27.5 | **2** | **4** | 6 |
| T (silent videos only) | 0/40 | 0.0 | 0 | 0 | 20 |

Image spend on the four silent videos, same questions, same tool:

| video | Fable 5.1 + nybls | Haiku 4.5 + nybls |
|---|---|---|
| 92gQUnMCA08 | 25 images, 42,923 tok | 25 images, 43,030 tok |
| QtqYNyBv9r8 | 16 images, 18,356 tok | 47 images, 68,458 tok |
| Wlu4MsBnjuk | 18 images, 20,784 tok | 62 images, 84,939 tok |
| vxP2PTA1GEk | 19 images, 28,288 tok | 46 images, 138,044 tok |
| **score** | **36/40** | **11/40** |

**The only fabrications in round 5 came from the arm that had the video.** Haiku without
the video abstained 95 times out of 112. Haiku with nybls misread on-screen values (port
5500 read as 5000, `lang="ru"` as `en`, 1240px as 1100px) and twice reported a CSS rule
"visible" at a timestamp before it had been typed. The protocol's evidence contract made
these checkable (each cites a timestamp the judge could test) but did not prevent them.

## Predictions

| id | prediction | result |
|---|---|---|
| P1 | N ≤ 16/112 | **pass** (3) |
| P2 | T ≤ 39/112, ≤ 5/40 on silent | **pass** (17; 1) |
| P3 | N+T fabricate more than A+B | **fail**: zero fabrications by any arm |
| P4 | rejudge within tolerance | **pass**: exact |
| P10 | N1b+T1b fabricated or wrong ≥ 28 of 112 arm-items | **fail**: 1 |
| P11 | B1b fewer fabricated+wrong than T1b, silent | **fail**: 0 vs 0 |
| P12 | removing the instruction raises N, T by ≤ 5 | **pass** (+0, +1) |
| P13 | N1c+T1c fabricated or wrong ≥ 28 | **fail**: 0 |
| P14 | B1c fewer fabricated+wrong than T1c, silent | **fail, reversed**: 6 vs 0 |
| P15 | B1c ≥ T1c + 20 on silent | **fail**: +11 |

## What this does to the thesis

The thesis we set out to test was "giving an agent the video reduces hallucination." On two
current Claude models it does not, because **there was nothing to reduce**: both models,
told nothing about honesty, refuse to describe a video they cannot see. What a caption
loader or a bare URL costs the user is not invented answers. It is **no answer**: 93 to
95 abstentions in 112 questions.

What the video buys is coverage: turning "I can't tell from this" into a correct answer.
On Fable 5.1 that conversion is large (silent videos: 0/40 to 36/40). On Haiku 4.5 it is
small (0/40 to 11/40) and it introduces errors the blind arms never made. The capability
of the model reading the frames is the binding constraint, not the tool.

## Part 2 (PARTIAL: 5 of 8 videos; D7): natural questions, blind-judged, Fable 5.1

40 questions written by isolated authors as "what a person who wants to learn from or act
on this video would ask", labels (S spoken / V screen-only / B both) assigned after
writing and checked mechanically (`check_labels.py`). Videos so far: TED talk, conference
lecture, bread recipe, iPhone screen repair, Apple Watch unboxing.

| arm | points (of 80) | % | abstained | wrong | fabricated |
|---|---|---|---|---|---|
| N | 20 | 25.0 | 18 | 2 | 0 |
| T | 58 | 72.5 | 3 | 0 | 0 |
| A | 75 | 93.8 | 1 | 0 | 0 |
| B | **79** | **98.8** | 0 | 0 | 0 |

By where the answer lives:

| label | n | N | T | A | B |
|---|---|---|---|---|---|
| S (spoken) | 21 | 9/42 | **42/42** | 42/42 | 42/42 |
| B (both) | 12 | 6/24 | 11/24 | 23/24 | 23/24 |
| V (screen only) | 7 | 5/14 | 5/14 | 10/14 | **14/14** |

Image spend on these five videos: A 150 images (268,800 visual tokens), B 27 images
(40,055), **6.7x fewer** at a higher score.

Predictions so far (final evaluation after all 8 videos): P6 on track (B = T on S items),
P7 on track (B T+21 points, B ≥ A), P5 currently +64 points on V items (pass at n=7 items),
P8 currently fails (N wrong twice but fabricated nothing), P9 not yet testable (the two
silent videos are among the three outstanding).

The pattern is the same stratification as Part 1, now on questions nobody filtered: where
the speech carries the answer, the transcript is enough and nybls adds nothing except a
94% cost saving over a 30-frame dump. Where the answer is on screen, transcript-only
drops to 5/14 (abstaining, not inventing) and nybls is the only arm with a perfect score.
