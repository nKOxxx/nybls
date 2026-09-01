# Benchmark 001 — iterative vs one-shot

**Date:** 2026-09-01 · **Video:** `LP10_YdKEPw`, a 20:03 PS3 Super Slim teardown,
never seen by the judge or either arm before this run · **n = 1 video, 5 questions.**

## Method

Questions and ground truth were written **before** either arm ran. Both arms were
separate subagents with clean contexts; neither was the judge, neither saw the
other's evidence or the ground truth. Every answer was verified absent from the
transcript first ("glove", "Instagram", "GCR", "subscribe", "cleaning process",
"IPA", "ultrasonic", "soap" — all zero hits), so the questions test looking, not
reading.

- **Arm A — one-shot (control).** Transcript + 30 frames sampled at uniform
  intervals, handed over at once. No ability to request more. This is what the
  field does today.
- **Arm B — iterative (nybls).** The `nybls` CLI and the WATCH protocol: free
  transcript, a coverage sheet, a confidence check each round, then only what it
  named a gap for.

Scoring: 2 correct and complete · 1 partial · 0 wrong or "insufficient evidence"
· −1 confidently fabricated.

## Result

| Q | Arm A (one-shot) | Arm B (iterative) |
|---|---|---|
| 1 Channel + handle | logo yes, handle **not reachable** — honestly declined · **1** | both, and flagged what was inferred vs seen · **2** |
| 2 Title card(s) | found one of two; read only its top line · **1** | both cards, both timings · **2** |
| 3 Gloves | correct, **plus** a detail the judge missed (one hand only) · **2** | correct incl. "not throughout" · **2** |
| 4 Cleaning methods | 3 of 5; **missed the immersion bath** · **1** | 4 of 5, incl. two the judge missed · **2** |
| 5 Final 30s | **outside its evidence window** — honestly declined · **0** | reassembly → subscribe card → thanks card · **2** |
| **Total** | **5 / 10** | **10 / 10** |

**Cost:** Arm A 53,760 visual tokens across 30 frames (plus 8 zoom crops it made
on its own, uncounted). Arm B 12,941 across 9 images. **Arm A spent 4.2× the
visual tokens for half the score.**

## Why Arm A lost, precisely

Not through bad reasoning — its analysis was careful and it degraded honestly.
It lost on the structural failure mode of uniform sampling:

- **The 08:41 title card fell exactly between two samples** (08:21 and 09:01), so
  the immersion-bath segment and the card announcing it were both invisible.
- **The video ends at 20:03; its last frame was 19:42.** The end cards carrying
  the social handle were outside its evidence window entirely. Nothing about its
  method could have recovered them.

A fixed grid cannot adapt to where the information is. That is the whole claim,
and this is what it looks like in practice.

## What must be said against the result

- **n = 1.** A signal, not a finding. One video, one domain, one question set.
- **The judge's ground truth was wrong and an arm corrected it.** Arm B reported
  a second title card and a vacuuming step the judge's 18-sample reference had
  missed; both were independently verified before scoring. A benchmark whose
  reference is built by sampling can be beaten by a method that looks harder —
  a real weakness in this benchmark's construction.
- **Both arms exceeded the reference.** Arm A caught that only one hand was
  gloved, which the judge had also missed. Neither arm was sloppy.
- **Arm A's honesty is worth more than its score.** It said "insufficient
  evidence" twice rather than inventing a handle or an ending, and lost 3 points
  doing so. A one-shot pipeline driven by an honest agent fails safely; the risk
  it carries is silence, not fabrication.
- **Arm A was not purely one-shot.** Given file access it spontaneously made 8
  zoom crops — iterative behaviour leaking into the control. If anything this
  flatters the control arm.
- **A teardown is close to a best case for uniform sampling**: slow, static bench
  work at one frame per 40 seconds. Faster-cut material should widen the gap;
  that is a prediction, and it is untested.

## Verdict

On this video, the iterative protocol answered every question correctly for a
quarter of the visual-token cost, while the one-shot control answered half — and
failed specifically where a fixed sampling grid structurally cannot reach.
That is one honest data point, not a proof.

**Next:** repeat on fast-cut and dialogue-heavy material before this is quoted as
anything more than a first result.
