# Research, evidence, and attribution

This document exists so that every design decision in nybls can be traced to
something other than opinion, and so that the work it stands on is credited.

Research conducted August–September 2026 across three rounds — a tooling survey,
a survey of the video-understanding literature, and an adversarial round whose
explicit job was to disprove the conclusions of the first two. Sources were
fetched and quoted rather than recalled. Where something could not be verified,
it is labelled UNVERIFIED here rather than smoothed over.

---

## 1. The problem, stated precisely

Claude, GPT, and every other frontier chat model in general use accept **images,
not video**. The Claude API accepts up to 600 images per request, each billed as
roughly `ceil(w/28) x ceil(h/28)` visual tokens. There is no video input.

So "an AI watched this video" always decomposes into: *what was extracted, and
what was shown to the model?* Nearly every product answers that question with
"the subtitles."

## 2. What the field actually does

Verified by reading the source, not the marketing:

| Category | Finding |
|---|---|
| Agent frameworks | The canonical YouTube loaders in the major Python agent frameworks are transcript scrapers built on caption APIs |
| Self-hosted chat apps | The YouTube ingestion paths in the leading self-hosted assistants are caption fetchers; their error handling enumerates caption-API failure modes and nothing else |
| Consumer summarizers | Transcript-only; several state it plainly in their own FAQs |
| Google NotebookLM | Its documentation states that a YouTube source imports "only the text transcript of the video" |
| Cloud vision APIs | Real visual understanding, but batch index-then-query: the agent consumes precomputed JSON and never chooses a frame |
| Native-video LLM APIs | Sample at a fixed rate (commonly 1 fps) and burn the whole video into tokens in a single pass; the sampling rate is not developer-controllable |
| Frame-based OSS tools | Exist and some are popular, but are **one-shot**: extract N frames by a fixed rule, hand them over, done |

The practical consequence: a video with no speech returns nothing useful from
most of the field, and no tool in either camp can tell you *which* frames its
answer rests on.

**An honest note on novelty.** The one-shot "extract frames and transcript for an
agent" category is not empty — it contains a tool with over sixteen thousand
GitHub stars. nybls is not the first tool to hand frames to a model. What the
adversarial round could not find was a tool combining an *agent-driven* frame
request loop with *cumulative budget accounting* and an evidence contract. One
project implements a close approximation of the loop and has effectively no
adoption; several implement iteration without budgets, or budgets without letting
the model drive.

## 3. Why the model chooses, and the tool does not

This is the load-bearing decision, and it is empirical rather than aesthetic.

- **VideoAgent** (arXiv:2403.10517, Stanford, ECCV 2024) — initialize with ~5
  uniformly sampled frames, answer, then self-assess confidence on a three-level
  scale, then request frames targeted at the gaps. Reported result: **8.4 frames
  on average matched or beat 180 uniformly sampled frames** on a standard
  long-video benchmark, with accuracy saturating after about three rounds.
  → nybls: the whole loop shape, and the 3-round stop.

- **Adaptive video-agent ablations** (arXiv:2410.20252) — of the components in an
  adaptive video agent, the "can I answer yet?" evaluator had the largest single
  effect on accuracy; removing it hurt more than removing the smart sampler.
  → nybls: the evaluator is mandatory in the protocol and nudged by every command.

- **Confidence-guided interval search** (arXiv:2507.02946) — model confidence
  across temporal intervals correlates strongly with answer correctness, which is
  what makes confidence-gated exploration sound rather than superstitious.
  → nybls: confidence is the primary stop condition.

- **A.I.R.** (arXiv:2510.04428) — adaptive, iterative, reasoning-based frame
  selection with an explicit duration-scaled budget, floor and ceiling, and early
  stop. Beat uniform-32 sampling using fewer frames.
  → nybls: `clamp(8, ceil(minutes * 4), 200)` and the cumulative ledger.

- **Adaptive Keyframe Sampling** (arXiv:2502.21271, CVPR 2025) and **K-frames**
  (arXiv:2510.13891) — adaptive and scene-driven selection beat uniform sampling
  at equal frame count.
  → nybls: scene-medoid sheet timestamps rather than fixed intervals.

- **Query-adaptive frame selection** (arXiv:2502.19680) — selection driven by the
  question beats uniform sampling at an equal downstream frame count.
  → nybls: budget ceilings are permission, not instruction.
  **[CORRECTED 2026-09-02.** This entry previously claimed the paper showed video-QA
  performance peaking around 32 well-chosen frames. Verification against the paper
  found the opposite: it treats 32 frames as too few and samples 128 before selection.
  No saturation finding exists in it. The nearest real support for a saturation-shaped
  claim is A.I.R. (arXiv:2510.04428, Table 4) and VideoAgent's observation that more
  frames do not always help.**]

- **Necessary sampling density** (arXiv:2503.12496) — some questions are
  answerable at one frame per minute, others need ~1 fps in a narrow window;
  uniform high-rate sampling wastes the context budget.
  → nybls: coarse coverage first, dense only inside a named interval.

- **IG-VLM** (arXiv:2403.18406) — an image grid can substitute for a frame
  sequence; ablations over 4 to 20 tiles found **six tiles in a near-square
  layout optimal**, with larger grids performing worse.
  → nybls: 3x2 contact sheets, six tiles, raster order.

- **MMNeedle** (arXiv:2406.11230) — multimodal needle-in-a-haystack testing shows
  accuracy collapsing as image count grows and models performing poorly at
  localizing content inside stitched sub-image grids.
  → nybls: sheets are for *where to look*; detail is always read from a
  full-resolution frame or a zoom, never from a tile.

- **T\*** (arXiv:2504.02259) building on **V\*** (arXiv:2312.14135) — reframing
  temporal search to include spatial localization and adaptive zoom gained 2.6 to
  5.9 accuracy points **under an identical frame budget**.
  → nybls: `zoom` is a first-class verb, not an afterthought.

- **SlowFast-LLaVA** (arXiv:2407.15841) — a few high-detail frames plus many
  low-detail ones covers time and detail within a fixed token budget.
  → nybls: cheap sheets plus expensive targeted frames, rather than one uniform rate.

- **Video understanding with LLMs: a survey** (arXiv:2312.17432) — situates the
  "LLM-based video agent" as a recognized architecture class.

## 4. What nybls is built on

nybls orchestrates existing tools. It vendors none of them, and claims none of
their work.

| Component | Role in nybls | License |
|---|---|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | acquisition from YouTube and ~1,800 other sites; caption retrieval; metadata | Unlicense |
| [FFmpeg](https://ffmpeg.org) | frame extraction, crops, scaling, audio conversion | LGPL-2.1+/GPL-2+ |
| [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | shot-boundary detection (`AdaptiveDetector`) driving scene-medoid sampling | BSD-3-Clause |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | local transcription with Metal acceleration | MIT |
| [OpenAI Whisper](https://github.com/openai/whisper) models | the ASR weights themselves (`large-v3-turbo`) | MIT |
| [ImageHash](https://github.com/JohannesBuchner/imagehash) | perceptual hashing for near-duplicate frame detection | BSD-2-Clause |
| [Pillow](https://python-pillow.org) | contact-sheet composition and timestamp overlays | MIT-CMU |
| [ocrmac](https://github.com/straussmaximilian/ocrmac) | optional Apple Vision OCR, including Arabic | MIT |

All are invoked as libraries or subprocesses; nybls itself is MIT.

Two engineering notes that cost real debugging time and are recorded so others
do not repeat them: Homebrew's FFmpeg may ship without `libfreetype`, so
`drawtext` is unavailable and timestamp overlays must be composited in Pillow;
and a system Python older than 3.10 silently resolves an older PySceneDetect
whose API differs.

## 5. What is actually new here

Not the algorithm — that is VideoAgent's, and it is two years old. What did not
exist, as far as an adversarial search could determine:

1. **A cumulative, model-facing budget ledger.** Existing budgets are static caps
   chosen at extraction time. Here the budget persists across a session, the model
   sees its own spend, and the tool refuses to exceed it without human override.
2. **Mechanically enforced protocol discipline.** Named-gap requirements, refusal
   past budget, duplicate warnings, and next-step nudges embedded in tool output —
   so the discipline survives an agent that was not carefully prompted.
3. **An evidence contract.** Every answer must ship the frames it rests on. This
   is what makes the difference between looking and guessing legible to a user.
4. **The packaging.** The protocol travels as a skill, so it applies to a generic
   agent rather than requiring a specific one.

## 6. Falsifiability — what would invalidate this

Stated up front, because a claim that cannot fail is not a claim:

- If a frontier model ships **native video input at competitive cost**, the frame
  server becomes a legacy path and only the budget/evidence discipline survives.
- If measurement on a real benchmark shows the iterative loop **failing to beat a
  one-shot 30-frame dump** at equal or lower cost, the core premise is wrong.
  Round 1 (`bench/RESULTS.md`, 2026-09-01, n=1): iterative 10/10 vs one-shot 5/10 at
  4.2x fewer visual tokens. Round 2 (`bench/RESULTS_round2.md`, 2026-09-02, n=3 with
  a tightened control that could not zoom): **the margin did not replicate** — 25/30
  vs 22/30. Combined across 4 videos and 20 questions: 35/40 vs 27/40 at 3.26x the
  cost (215,040 visual tokens against 66,040). The advantage is narrow and consistent, not a rout, and it narrowed as the
  control was tightened. **Both arms failed the same question** — a 2.0-second
  on-screen graphic — which iteration does not fix and only dense coverage reaches.
- If the mechanical rails prove trivially bypassable by ordinary agent behavior,
  the "works for unprompted agents" claim fails.

## 7. Method and honesty notes

- Research was performed by parallel agents with an explicit adversarial round
  tasked with falsifying the conclusions. It succeeded: it overturned a
  "nobody has built this" claim by locating a sixteen-thousand-star one-shot tool
  the earlier rounds had missed through poor search phrasing. The positioning in
  this document reflects the corrected picture.
- One distribution claim repeated in earlier drafts — a standalone
  `npx skills add` protocol — **did not survive verification** and was removed.
  Skills are distributed as plugins through marketplaces.
- Star counts, release dates, and registry availability were verified directly
  against the relevant APIs rather than recalled.
- Trademark status for the name has **not** been verified in any jurisdiction:
  UNVERIFIED.
- Maturity: the frame server and protocol are IMPLEMENTED and used daily. Formal
  benchmarking is ENVISIONED, not done.


---

## 8. Corrections log

Claims that were stated in this repository and did not survive verification. Recorded
rather than silently edited, because the point of the document is traceability.

**2026-09-02 — "use the hash to detect duplicates, never to detect change" (WITHDRAWN).**
Stated in CHANGELOG 0.3.0 and in the `adaptive_timestamps` docstring on the strength of
one observation on one chess lesson. Measured properly against an independent OCR
reference across seven videos (`bench/RESULTS_signals.md`): mean AUC 0.734 for perceptual
hashing against 0.762 for pixel difference, with pixel difference better on only 2 of 4
videos where the reference was usable. **At n=4 this is not a real effect.** What survives
is narrower: on static-camera content the perceptual hash's distribution compresses into
the same band used for duplicate detection (median 4, p90 8 of a possible 64), leaving a
threshold detector nowhere to sit. The static-camera case itself remains **untested**,
because a chess move changes the board and not the on-screen text, so the OCR reference is
degenerate exactly where the original claim was made.

**2026-09-02 — the EG-VQA grounding statistic (RESTATED).** CHANGELOG 0.4.0 stated that
"frontier models scored 8.5% and 1.5% on evidence grounding while scoring 45% and 41% on
answer accuracy," with no citation. The source is EG-VQA (arXiv:2606.24797). The four
numbers are all real but were **assembled from two different metric columns**: 8.49 is
GPT-4o's EG-F1 at (0.3, 0.5) and 1.48 is Gemini-2.5-Flash's at (0.3, 0.75). At a matched
threshold the pair is 8.49 / 12.64, which makes Gemini *better* at grounding, not six
times worse. The accuracy figures are Relaxed Accuracy; Strict is 28.47 / 24.87. Correct
statement: on EG-VQA, GPT-4o and Gemini-2.5-Flash reach 45.1% and 41.2% relaxed answer
accuracy but 8.5% and 12.6% EG-F1 at (0.3, 0.5), falling to 1.2% and 1.5% at (0.3, 0.75).

**2026-09-02 — arXiv:2502.19680 miscited (CORRECTED above in section 3).**
