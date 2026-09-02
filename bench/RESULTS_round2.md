# Benchmark round 2 — three videos, and two of our own claims falsified

**Date:** 2026-09-02 · **n = 3 videos, 15 questions** (round 1: 1 video, 5 questions).
Questions and ground truth were committed **before** either arm ran
(`bench/gt_round2.md`, `bench/q_*.md`); ground truth was moved out of the repository
during the runs so neither arm could reach it.

## Method

Both arms were subagents with clean contexts. Neither was the judge, neither saw the
other's evidence, neither saw the ground truth. Each candidate answer was checked for
transcript hits at design time and any term appearing in the narration was rejected, so
the questions test looking rather than reading.

- **Arm A — one-shot (control).** Transcript plus 30 frames on a uniform grid, handed over
  at once. Round 1's control leaked iterative behaviour by making its own zoom crops; this
  round the arm was explicitly forbidden to run ffmpeg, nybls, or anything that renders a
  new image. All three arms complied.
- **Arm B — iterative (nybls).** The CLI and the WATCH protocol. Ledgers were **reset to
  zero** and the sheets used to build ground truth were **archived out of the workspace**
  before each run, so the reported cost is real spend, not a cached discount.

Scoring: 2 correct and complete · 1 partial · 0 wrong or "insufficient evidence"
· −1 confidently fabricated. A correct-but-different instance of the thing asked for
scores 1.

## Result

| Video | Arm A score | Arm A tokens | Arm B score | Arm B tokens |
|---|---|---|---|---|
| g9xUu2StOYg — motorsport doc, 27:24, 62 cuts/min | 6 / 10 | 53,760 | 7 / 10 | 26,284 |
| 5oNHF72wbmI — McLaren rebuild, 48:06, 17 cuts/min | 8 / 10 | 53,760 | 9 / 10 | 27,171 |
| jgN4XWFUSb4 — GT3 RS rebuild, 80:48, 9 cuts/min | 8 / 10 | 53,760 | 9 / 10 | 22,888 |
| **Round 2 total** | **22 / 30** | **161,280** | **25 / 30** | **76,343** |

**Combined with round 1** (4 videos, 20 questions): Arm A **27/40** for 215,040 visual
tokens; Arm B **35/40** for 89,284. Arm A spent **2.41x** the visual tokens for 77% of
Arm B's score.

## What this round overturned

**1. Round 1's margin did not replicate.** Round 1's control scored 5/10; round 2's
averaged 7.3/10. The 2x gap was the outlier, not the finding. Given file access and no
zoom, a careful one-shot agent reads persistent visual attributes — branding, colour,
recurring devices, footage types — about as well as the iterative arm does. The honest
headline is a **narrow, consistent advantage at roughly half the cost**, not a rout.

**2. The iterative protocol failed a question too — the same one.** Arm B spent 20 images
and 54 sampled moments on the motorsport video, specifically targeting the five narration
windows where finishing positions are read aloud, and still reported "insufficient
evidence" for the results graphic. **Both arms missed it.** We measured why: the graphic
is on screen for **2.0 seconds** in a 1,642-second video (`bench/round2/persist_*.json`).
A uniform 30-frame grid captures it with probability 0.037; even odds would need 410
frames. Answer-mode iteration does not fix this either — only the dense adaptive study
pass that built the ground truth found it. **Coverage mode matters more than iteration.**

**3. Ground truth built by sampling is unreliable, again.** Round 1 recorded this as a
weakness; round 2 reproduced it three ways. Arm B read the Porsche diagnostic unit as
"DME (Digital Engine Electronics)" where our ground truth recorded "SME" — arm B is right
and the reference was wrong. On the McLaren, arm B found a real full-screen Facebook post
screenshot our reference had not recorded, while neither arm retrieved the iMessage thread
the reference does record. A reference assembled by sampling can be both incomplete and
wrong, and it can be corrected by the systems it is meant to judge. This is a structural
problem for video-QA benchmark construction, not a local mistake.

## What must be said against this result

- **n = 4 videos, 20 questions.** Still small. Three of round 2's videos are the same
  genre (vehicle/motorsport long-form), so genre is confounded with round.
- **The judge is not independent of the tool.** Ground truth was built from nybls adaptive
  study sheets. That biases toward Arm B on anything only a dense pass surfaces — and the
  results-graphic failure shows the bias is real, because the reference contains an item
  neither answer-mode arm could reach.
- **Scoring was done by the same author who built the tool.** There is no blind human
  scorer. Partial-credit calls (correct-but-different instances) are judgement, and a
  different judge could move two or three points in either direction.
- **The fast-cut prediction was half right.** Round 1 predicted faster cutting would widen
  the gap. The fastest-cut video (62 cuts/min) did produce the widest relative gap and the
  lowest absolute scores for both arms — but it did so by defeating *both* arms, which is
  not what the prediction said.

## Verdict

The iterative protocol answers slightly more correctly for roughly 40% of the cost, and it
degrades honestly. It does not solve transient on-screen events, which are defeated by
sampling density rather than by search strategy. The clean result of this round is not the
score table; it is the demonstration that specific failures were predicted in advance from
arithmetic alone (see `bench/uniform_coverage.py`), and that a benchmark reference built by
sampling cannot be trusted to judge a sampler.
