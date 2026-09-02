# Benchmark — iterative vs one-shot

Two rounds, **four videos**, twenty questions, eight isolated arms.

## Method

Questions and ground truth are written **before** any arm runs. Both arms are
separate subagents with clean contexts; neither is the judge, neither sees the
other's evidence or the ground truth. Every candidate answer is checked against
the transcript first, and any term that appears in the narration is rejected as a
question — otherwise the benchmark tests reading, not watching.

- **One-shot (control)** — transcript + 30 frames at uniform intervals, handed
  over at once. This is what the field does today.
- **Iterative (nybls)** — the CLI and the WATCH protocol: free transcript, a
  coverage pass, a confidence check each round, then only what it names a gap for.

Scoring: 2 correct and complete · 1 partial · 0 wrong or "insufficient evidence"
· −1 confidently fabricated.

## Results

| Round | Video | Scene cuts | One-shot | Iterative |
|---|---|---|---|---|
| 1 | PS3 teardown (20 min) | 22 | 5/10 · 30 frames + 8 crops | **10/10 · 9 images** |
| 2 | Motorsport doc (27 min) | 1,700 | 7/10 · 35 reads | **10/10 · 26 images** |
| 2 | McLaren rebuild (48 min) | 814 | 8/10 · 30 reads | **10/10 · ~30 images** |
| 2 | GT3RS rebuild (81 min) | 726 | 9/10 · 35 reads | **10/10 · 16 images** |
| | **Total** | | **29/40** | **40/40** |

## Where the difference actually is

Not general comprehension. The controls were strong, careful, and repeatedly
honest — twice declining to guess rather than fabricate. The gap sits almost
entirely in **one failure, replicated four times**: a brief, one-time on-screen
graphic falling between two uniform samples.

| Video | The thing missed | Sampled at | Missed by |
|---|---|---|---|
| PS3 teardown | "Cleaning Process" title card, 08:41 | 08:21 / 09:01 | 20 s |
| Motorsport | race-results graphic, 02:42 | 02:16 / 03:11 | 26 s |
| McLaren | iMessage screenshot, 42:12 | 40:55 / 42:31 | 19 s |
| GT3RS | warranty document, 72:27 | 71:22 / 74:03 | 65 s |

A fixed grid cannot land on a brief graphic except by luck, and cannot go back
once it learns the graphic exists. Every control missed these; every iterative
arm found them.

The zoom tool earns its place on small text: the GT3RS arm read a number plate
and a vehicle-history card by cropping into two frames, scoring 10/10 on an
81-minute video for **16 images** — under half what the control used.

## What must be said against the result

- **The round-1 prediction was only half right.** Round 1 predicted faster-cut
  material would widen the gap. Directionally it did — the widest gap (3 points)
  was on the 1,700-cut video and the narrowest (1 point) on the 726-cut one — but
  the controls scored **7–9 here against 5 in round 1**, so this material is
  *easier for both arms*, not harder for one. The prediction as written
  overstated the effect.
- **"One-shot" was never purely one-shot.** Given file access, controls generated
  their own zoom crops — 5, 8 and 30 extra reads beyond the supplied 30. That is
  iterative behaviour leaking into the control, and it flatters the control.
- **The judge's ground truth was exceeded six times.** Arms found a second title
  card, a vacuuming step, a whole podium ceremony, video-game footage, two extra
  diagnostic devices and branding on five objects where the reference had one. A
  reference built by sampling loses to a method that looks harder — which is
  exactly what is under test. This is a real weakness in the benchmark's
  construction.
- **Round 2's iterative arm had `study --adaptive`, which round 1's did not.**
  The two rounds are therefore not the same arm and should not be pooled naively.
- **n = 4.** Four videos, two domains, one judge. A signal, not a proof.

## Bugs the benchmark surfaced

- **Scene drift, since fixed.** Two targeted requests landed on adjacent shots.
  Measured across three videos, **21 of 24 one-second offsets landed in a visibly
  different shot** (mean pixel difference 24–53). Sheets now record the exact
  moment each tile was rendered — 255.035 s, not 255 — and `frames` snaps to it,
  verified as an exact match on all three videos.
- **A ledger reading zero.** Both iterative arms reported it independently. It was
  an artifact of the sandboxed environment the benchmark arms run in discarding
  their writes, not a product fault; verified by reproducing the same commands
  outside the sandbox, where the ledger records correctly.

Two arms catching and correctly diagnosing an instrument problem is a better
outcome than either silently reporting a wrong number.
