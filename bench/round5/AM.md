# Arm AM: the cost-matched control (registered in PREDICTIONS_ADDENDUM.md)

Run 2026-10-04 on Fable 5.1. Per Part 2 video, AM received the transcript plus a uniform
grid of exactly as many full-resolution (1568 wide) frames as arm B was served on that
video (4, 10, 4, 3, 17, 20, 8, 2; 68 in total), under arm A's prompt and constraints.
Frames, index and transcript per video were built by the addendum script and are
reproducible from the ledgers' per-video counts; the answers, single-arm judge verdicts
(two batch judges, four videos each, same rubric and outcome classes; single-arm judging
is not blind and is not claimed to be) and `tally_am.py` are in `am/`.

**Token match.** AM's 68 full-resolution frames cost 121,856 distinct visual tokens
against B's 102,940 for the same 68 images (B's mix is mostly 1448x544 contact sheets).
The control therefore had 18% MORE visual tokens than the tool, as the registration
predicted and as reported: the mismatch favours the control.

## Result

| arm | images | visual tokens | points (of 128) | % | S (56) | B-label (32) | V (40) | silent (32) |
|---|---|---|---|---|---|---|---|---|
| A (30 uniform) | 240 | 430,080 | 115 | 89.8 | 56 | 28 | 31 | 25 |
| **AM (uniform at B's count)** | **68** | **121,856** | **104** | **81.2** | 56 | 17 | 31 | 27 |
| B (protocol) | 68 | 102,940 | **125** | **97.7** | 56 | 31 | 38 | 30 |

AM outcomes: 44 correct, 16 partial, 4 abstained, 0 wrong, 0 fabricated.

## What it settles

Rounds 1 to 5 compared the protocol against a 30 frame grid that spent more than it did,
so "cheaper and better" could not be separated from "30 large frames is too many". At
the same image count and a higher token count, the uniform grid loses **21 points** to
the protocol, and loses them where the registration said it would: on the spoken items
the three arms are identical (56/56), on the screen-only items AM reads 31/40 to B's
38/40, and on the items needing both AM falls to 17/32 against B's 31/32. Fewer uniform
frames also hurt the grid against itself: AM (68 frames) scores 11 points below A (240
frames). The protocol's advantage is selection, not spend.

The one place the uniform grid at B's count did not lose is the spoken items, which is
the modality argument again: where the transcript carries the answer, no frame policy
matters.

## Predictions

- **P16** (AM < B 125): 104. **Pass.**
- **P17** (AM < A 115): 104. **Pass.**
- **P18** (AM at least 4 V points below B's 38): 31. **Pass.**
