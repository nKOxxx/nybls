# Change-detection signals — testing our own design rule, and failing it

**Date:** 2026-09-02 · **Code:** `bench/measure_signals.py` · **Data:** `bench/round2/signals_*.json`

## The claim under test

nybls v0.3.0 replaced perceptual hashing with mean absolute pixel difference as the
change-detection signal behind adaptive sampling, and the changelog stated the rule
flatly: *"Use the hash to detect duplicates, never to detect change."* That rule came
from **one observation on one chess lesson** — board states ten seconds apart differing
by 2-4 bits of a 64-bit hash. This is the measurement that should have come first.

## Method

Probe each video every 10 s. From each probe compute, against the previous probe:

- **phash** — Hamming distance between 64-bit perceptual hashes
- **pixdiff** — mean absolute difference of 192px grayscale pixels

Neither is ground truth. The reference is **independent of both**: the set of words Apple
Vision OCR reads on screen, compared between consecutive probes by Jaccard distance. On
text-bearing content the on-screen text changing is the information changing, and OCR
knows nothing about either candidate. A pair is a content change when OCR Jaccard > 0.5.
Discriminability is reported as AUC via Mann-Whitney U.

## Result

| Video | cuts/min | pairs | changes | phash AUC | pixdiff AUC |
|---|---|---|---|---|---|
| 8NSyI-npJCU (screen recording) | 6.89 | 129 | 107 | 0.834 | 0.820 |
| F2FmTdLtb_4 (slide course) | 1.19 | 321 | 151 | 0.823 | **0.877** |
| aircAruvnKk (animated lesson) | 1.29 | 111 | 69 | 0.757 | 0.745 |
| g9xUu2StOYg (fast-cut doc) | 62.11 | 163 | 101 | 0.523 | **0.606** |
| **mean (4 usable)** | | | | **0.734** | **0.762** |

Excluded for a degenerate reference (fewer than 20 positives or 20 negatives):
LP10_YdKEPw, OngJKc-FAS0, f1wnYdLEpgI.

## Conclusion: the rule was overstated, and is withdrawn

**Pixel difference is better on 2 of 4 videos, by a mean of 2.75 AUC points.** At n = 4
that is not a real effect. The strong form of the claim — that a perceptual hash is
*blind* to content change — **is not supported**. Both signals are mediocre-to-decent
change detectors and neither dominates.

Two things survive:

1. **The distribution-compression observation is real and separate from discriminability.**
   On the static-camera chess lesson, phash has median 4 and p90 8 out of a possible 64 —
   meaning 90% of consecutive ten-second pairs fall at or below the Hamming threshold of 8
   that the same code uses to declare two frames *duplicates*. A threshold-based change
   detector has nowhere to put its threshold. Pixel difference on the same video spans
   median 2.81 to max 33.46. This is a genuine property of the signal on static content.

2. **We could not test the claim on the content it was about.** A chess move changes the
   board, not the on-screen text, so the OCR reference is degenerate exactly where the
   original observation was made (5 positives in 290 pairs). The honest position is that
   the static-camera case remains **untested**, and needs a non-textual reference signal —
   annotated move times, or human labelling — to settle.

## What this cost us to learn

A design rule was written into the code, the changelog and the README from a single
observation, and it survived three months because it sounded mechanical and had a number
attached. The number was real; the generalisation was not. Any claim of this shape in this
project now requires a reference signal that is independent of the thing being measured.
