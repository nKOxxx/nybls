# Round 3 predictions — registered BEFORE any arm result was seen

**Written 2026-09-04, after the eight arms were launched and before any of them
returned.** Committed immediately so the timestamp is checkable against the answer
files. Round 3 is a duration sweep; its purpose is to test whether the capture-probability
model from rounds 1-2 predicts failures as duration varies, rather than merely describing
four videos after the fact.

## The model

A uniform grid of N frames over duration D samples at `t_i = D(i+0.5)/N`. Therefore:
- dead zones of `D/2N` at each end (**always 1/N = 3.33% of the video at N=30**, regardless
  of length — the *fraction* is constant, the *seconds* are not)
- an event visible for `v` seconds is captured with probability `min(1, vN/D)`
- even odds require `N >= D/2v`

## Computed, at N=30 and a nominal 4-second event

| Video | D (s) | grid interval | dead zone each end | p(capture) 4s event | N for even odds |
|---|---|---|---|---|---|
| jet engine | 301.0 | 10.0 s | 5.0 s | **0.399** | 38 |
| docker | 712.7 | 23.8 s | 11.9 s | **0.168** | 90 |
| stock market | 1477.5 | 49.2 s | 24.6 s | **0.081** | 185 |
| rome | 2672.2 | 89.1 s | 44.5 s | **0.045** | 335 |

An 8.9x spread in duration produces an **8.9x spread in the probability of catching the
same event** with the same 30-frame budget. This is the sweep's whole point.

## Predictions

**P1 — Arm A's score should fall as duration rises**, because the questions' answers are a
mix of persistent and transient content and only the transient half is duration-sensitive.
Ordering predicted: jet engine > docker ≈ stock market > rome.

**P2 — Arm A should score near-maximum on the jet engine video (5:01).** Its ground-truth
items are almost entirely *persistent* properties — no presenter, colour coding throughout,
a watermark present throughout, a translucent cutaway sustained across the animation. A
uniform grid is a perfectly good instrument for persistent attributes, and at 10-second
spacing it is a dense one. **If uniform sampling is going to win anywhere, it is here.**

**P3 — Arm A should fail specifically on the transient, once-shown items**, and these are
predicted item-by-item:
- docker Q2 (the "Layer Caching For Dummies" slide) and Q3 (`ENV PORT=9000`, a single line
  visible only while that file is on screen) — 23.8 s between samples
- stock market Q2 (the "DRHP" / "BOOK BUILDING PROCESS" title cards) — 49.2 s between samples
- rome Q3 (the frontier wall) and Q4 (the carved polychrome relief) — 89.1 s between samples

**P4 — The gap between arms should widen with duration**, for the same reason: Arm B's
budget is duration-scaled (`clamp(8, ceil(4*minutes), 200)`) and its sampling is
change-driven, so it does not degrade linearly with D the way a fixed grid does.

**P5 — Arm B will not be immune to the shortest transient items.** Rounds 1-2 showed a
2.0-second graphic defeating three arms including two iterative ones. Any round-3 item
below roughly 3 seconds on screen is predicted to defeat both arms.

## What would falsify the model

- Arm A failing the *persistent* items on the long videos, or succeeding on the transient
  items on the long ones — either would mean duration is not the operative variable.
- Arm A scoring worse on the jet engine (5 min) than on Rome (44 min).
- No relationship between an item's on-screen persistence and which arm retrieves it.

Persistence for any contested item will be measured with `bench/measure_event_persistence.py`
after scoring, not estimated.
