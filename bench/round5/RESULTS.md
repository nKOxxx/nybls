# Round 5 results: does giving the model the video improve what it says?

Protocol `PROTOCOL.md` and predictions `PREDICTIONS.md` registered at `b6f46be`; Part 1b at
`e03b73e`; Part 1c at `f2ff358`. All before the arms they govern ran. Deviations D1 to D6 are
in `PROTOCOL.md`. Raw answers, judge inputs, verdicts and arm mappings are in `data/`.

Arms: **N** title/channel/duration only · **T** transcript only (what caption loaders give
an agent) · **A** transcript + 30 uniform frames · **B** nybls + its shipped protocol.
Scoring 2/1/0/-1 as in every round; every item also classified correct / partial /
abstained / wrong / fabricated by a blind judge (Fable 5.1).

## The result in one line

nybls (arm B) does what it is built to do: it ingests the video, pulls the frames the
question needs, reads them, and answers. On natural questions it scores **99%** against a
transcript-only agent's 73% and a 30-frame dump's 94%, at **6.7x fewer images** than the
dump; on silent video, where a transcript-only agent scores 0, nybls scores 90%. The gain
is **coverage**: it converts questions a video-less agent can only abstain on into correct,
frame-cited answers. The failure mode a video-less agent has is not invention, it is
silence — so nybls's value is measured in questions *answered*, not hallucinations avoided.
The ceiling is the model that reads the frames: on Fable it is near-perfect, on Haiku it
drops and picks up a few misreads nybls fetched correctly but the weak model misread.

(What these runs do **not** test: the "summarize, compact, then delete the frames"
lifecycle. Every arm kept its frames and ledger for auditing. That garbage-collecting
digest step is ENVISIONED, not benchmarked here.)

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

## Part 2 (final, all 8 videos): natural questions, blind-judged, Fable 5.1

64 questions written by isolated authors as "what a person who wants to learn from or act
on this video would ask", labels (S spoken / V screen-only / B both) assigned after writing
and checked mechanically. Videos: TED talk, conference lecture, Python tutorial, bread
recipe, silent campfire cooking, silent spinning-cube coding, Apple Watch unboxing, iPhone
screen repair. Earlier revisions of this file reported the 5- and 7-video partials; this
table supersedes them (D7).

| arm | points (of 128) | % | abstained | wrong | fabricated |
|---|---|---|---|---|---|
| N | 31 | 24.2 | 30 | 3 | 0 |
| T | 82 | 64.1 | 8 | 2 | 0 |
| A | 116 | 90.6 | 1 | 1 | 0 |
| B | **125** | **97.7** | 0 | 0 | 0 |

By where the answer lives:

| label | items | N | T | A | B |
|---|---|---|---|---|---|
| S (spoken) | 28 | 12/56 | **56/56** | 56/56 | **56/56** |
| B (both) | 15 | 7/30 | 14/30 | 28/30 | **29/30** |
| V (screen only) | 21 | 12/42 | 12/42 | 32/42 | **40/42** |

Cost: arm A examined 240 images (430,080 visual tokens); arm B examined **68 images
(102,940 visual tokens)**, 4.2x fewer, while scoring 9 points higher. Per-video B spend
ranged from 2 images (repair video, speech-heavy) to 20 (silent cube) — the protocol's
"spend in inverse proportion to what the transcript carries" is visible in the ledgers.

## Part 2 predictions

| id | prediction | result |
|---|---|---|
| P5 | on V items, B >= T + 40 points of percentage | **pass**: 95.2% vs 28.6% |
| P6 | on S items, B within 10 points of T | **pass**: both 100% |
| P7 | B >= T + 20 points and B >= A | **pass**: +43; 125 vs 116 |
| P8 | N has the most fabrications | **fail**: no arm fabricated anything |
| P9 | T <= 20% on the two silent videos | **fail**: 40.6% |

P9's failure is itself a finding, in two parts. First, the "silent" cooking video is not
informationally silent: its caption track carries burned-in ingredient lines, and T read
them (every point T scored there was an S item). The visual exclusivity ratio of the
*transcript file*, not the absence of speech, is what predicts T's score. Second, on the
truly empty-transcript cube video T still scored 6/16 by labelled genre inference: a
"spinning ASCII cube in C" is a known pattern and the model part-reconstructed it from
prior knowledge. Judges scored those 1 (labelled inference), not 2.

## Deviations affecting this file

D7 (three authors re-run after network and usage-limit failures; no content effect). **D8:
Part 3 (the exploratory "reproduce the program" task) was not run, to conserve the owner's
usage budget after this round consumed a large share of it; it was registered as
exploratory and no prediction depends on it.
