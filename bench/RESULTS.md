# Benchmark — iterative vs one-shot

Three rounds, **eight videos, forty questions, sixteen isolated arms.**

## Method

Questions and ground truth are written **before** any arm runs. Both arms are
separate subagents with clean contexts; neither is the judge, neither sees the
other's evidence or the ground truth.

- **One-shot (control)** — transcript + 30 frames at uniform intervals, all at
  once. This is what the field does today.
- **Iterative (nybls)** — the CLI and the WATCH protocol: free transcript, a
  coverage pass, a confidence check each round, then only what it names a gap for.

Scoring: 2 correct and complete · 1 partial · 0 wrong or "insufficient evidence"
· −1 confidently fabricated.

## Results

| Round | Video | Length | Cuts | One-shot | Iterative |
|---|---|---|---|---|---|
| 3 | Jet engine animation | 5 min | 2 | 9/10 · 30 img | **10/10 · 13 img** |
| 3 | Docker tutorial | 12 min | 293 | 8/10 · 30 | **10/10 · 11** |
| 1 | PS3 teardown | 20 min | 22 | 5/10 · 30+8 | **10/10 · 9** |
| 3 | Stock documentary | 25 min | 201 | **10/10** · 30 | **10/10 · 15** |
| 2 | Motorsport doc | 27 min | 1,700 | 7/10 · 35 | **10/10 · 26** |
| 3 | History of Rome | 44 min | 395 | 9/10 · 30 | **10/10 · 17** |
| 2 | McLaren rebuild | 48 min | 814 | 8/10 · 30 | **10/10 · ~30** |
| 2 | GT3RS rebuild | 81 min | 726 | 9/10 · 35 | **10/10 · 16** |
| | **Total** | | | **65/80** | **80/80** |

Round 3 has the cleanest cost figures: control 120 images, iterative 56 — the
iterative arm scored higher on **47%** of the images.

## Where the difference actually is

Not comprehension. The controls were careful, often exceeded the judge's own
reference, and repeatedly said "insufficient evidence" rather than guess. The
gap sits in **one failure, replicated seven times**: a brief, one-time on-screen
element falling between two uniform samples.

| Video | Missed | Sampled at | Missed by |
|---|---|---|---|
| PS3 teardown | "Cleaning Process" title card | 08:21 / 09:01 | 20 s |
| Motorsport | race-results graphic | 02:16 / 03:11 | 26 s |
| McLaren | iMessage screenshot | 40:55 / 42:31 | 19 s |
| GT3RS | warranty policy document | 71:22 / 74:03 | 65 s |
| Jet engine | "310–620 mph" overlay | 03:15 / 03:25 | 7 s |
| Rome | Hadrian's Wall | 24:29 / 25:58 | 8 s |
| Docker | Dockerfile lines 13–20 | never sampled | — |

The Docker case is the starkest: asked for the port number and the
`.dockerignore` contents, the control reported honestly that those lines never
appear in its thirty frames — they genuinely didn't — and inferred the port from
a container mapping. The iterative arm read `ENV PORT=9000` on line 17 directly.

A fixed grid also spends samples on nothing: one of the Rome control's thirty
frames was a **fade to black**, 1/30th of its budget returning zero information.

## Effect of duration — the useful finding

**The accuracy gap narrows as videos get shorter; the cost advantage does not.**

At 5 minutes a 30-frame grid samples every 10 seconds and catches almost
everything: the control scored 9/10, and the iterative arm won by one point while
spending 13 images against 30. At 25 minutes on visually repetitive talking-head
content the arms **tied at 10/10**, iterative at half the spend.

So below roughly ten minutes the honest claim is not "more correct" — it is
"same answer, less than half the cost". Above it, correctness diverges too.

## What must be said against the result

- **Two of the judge's predictions were wrong.** Round 1 predicted fast-cut
  material would widen the gap: directionally right (widest gap on the 1,700-cut
  video) but overstated, since controls scored 7–9 on round 2 against 5 in round
  1. Round 3 predicted the gap would *close* at 5 minutes: it narrowed and did
  not close.
- **"One-shot" was never purely one-shot.** Given file access, controls generated
  their own zoom crops — 5, 8 and 30 extra reads beyond the supplied 30. That is
  iterative behaviour leaking into the control, and it flatters the control.
- **The judge's ground truth was exceeded at least seven times** — a second title
  card, a vacuuming step, whole podium ceremonies, video-game footage, extra
  diagnostic devices, branding on five objects where the reference had one. A
  reference built by sampling loses to a method that looks harder, which is
  exactly what is under test.
- **The "verified absent from transcript" check was weaker than stated.** It used
  exact string matching, so a term written `node_modules` but *spoken* "node
  modules" passed as visual-only when it was not. Questions about branding,
  layout and graphics are unaffected; questions about written identifiers are.
- **Arms were not identical across rounds.** Round 2 and 3 iterative arms had
  `study --adaptive`; round 1's did not. Rounds should not be pooled naively.
- **One judge, one scoring pass, no blind grading.**

## Bugs the benchmark found

- **Scene drift (fixed, v0.6.0).** Sheet tiles render at 255.035 s, not 255, so a
  request for the labelled second returned a different moment — on fast-cut
  material, a different shot. Measured: **21 of 24 one-second offsets landed in a
  visibly different shot.** Sheets now record real timestamps and `frames` snaps.
- **Silent ASR failure (fixed, v0.7.0).** A video with no captions fell back to
  the English-only default model over Hindi audio. Whisper did not fail — it
  looped, emitting **65 distinct lines across 907**, one line repeated for 23 of
  25 minutes, reported as a healthy transcript. Both iterative arms diagnosed it
  independently. Now detected and labelled UNRELIABLE, with the model named.
- **A ledger reading zero** — an artifact of the sandboxed environment the
  benchmark arms run in, not a product fault; verified by reproducing outside it.
