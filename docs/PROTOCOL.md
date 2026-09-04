# The WATCH protocol

The CLI is deliberately unintelligent. It extracts frames, it does not decide
which frames matter. The deciding happens in the model, guided by this protocol
and constrained by rails in the tool.

That split is the central design choice, and it is not arbitrary: every attempt
to make the *extractor* smart loses to letting the *model* choose, because the
extractor has to decide before it understands the question. Measured result:
a confidence-gated loop matched the accuracy of 180 uniformly sampled frames
using 8.4 chosen ones (arXiv:2403.10517).

---

## Two modes — pick one before you start

The loop below is **answer mode**: a question exists, and stopping as soon as it
is answered is correct. It is the wrong mode for a dense instructional video.

**Study mode** is for comprehension: "watch this and tell me what's in it",
tutorials, lectures, anything where the goal is to absorb rather than to look
something up.

```bash
nybls study <id> [--every SECONDS]
```

It samples the whole video on a clock and returns every sheet at once. Read all
of them. Do not stop early — there is no question to satisfy, so "sufficient"
does not apply until the video is covered.

Default interval scales with length: 10s up to 5 min, 20s to 20 min, 30s to
60 min, 45s beyond. A 48-minute video costs 17 sheets, about 3 cents.

**Why a clock and not scene detection.** Scene detection is the wrong signal for
static-camera instructional content. A 48-minute chess lesson recorded as one
continuous screen capture yields *three* scene cuts, because the frame
composition never changes — while the board, the thing that carries all the
information, changes every move. Anything shot as a fixed screen recording (a
board, a slide deck, an IDE, a dashboard) has the same shape. Sampling on cuts
sees nothing; sampling on a clock sees everything.

## The loop

### Round 0 — free

```bash
nybls probe <url-or-file>
```

Produces the transcript, the scene list, metadata, and the budget. Costs zero
images. Read all of it before spending anything.

For talk-heavy video this round frequently answers the question outright. It
must never be used to answer a *visual* question — if the user asks what is on
screen, the transcript is evidence about the audio, not the picture.

**Check the transcript is real before trusting it or its absence.** If `probe`
marks it UNRELIABLE, or it is a few words of stock politeness ("Thank you.",
"We'll see you next time."), the video has no speech. That is not a low-value
video. It is the case where frames are the *only* carrier of content, and the
one that most deserves the budget. Four real build-in-public reels had one-line
captions and filler transcripts; their videos held the entire system
architecture, including a restructure no caption mentioned. Never conclude a
silent video is empty, or that "the substance is in the caption", without
looking. Go straight to `sheet` and expect to spend.

### Round 1 — coverage

```bash
nybls sheet <id> [--range START_S END_S]
```

One sheet is six timestamped thumbnails in a 3x2 grid: six moments for the price
of one image. Use `--range` to cover a specific region of a long video; for a
20-minute video, one sheet per five to seven minutes of interest is a sane
budget.

**Six tiles, not more.** IG-VLM ablated 4 to 20 tiles per grid and found six in a
near-square layout optimal, with larger grids performing worse (arXiv:2403.18406).
Needle-in-a-haystack testing shows every current model — Claude included — loses
the ability to localize detail inside dense sub-image grids (arXiv:2406.11230).
Sheets tell you *where to look*. They are not for reading.

### The evaluator — mandatory, every round

Draft the answer. Then classify, explicitly:

| Verdict | Meaning | Action |
|---|---|---|
| `sufficient` | the evidence supports the answer | stop, write the output |
| `partial` | the shape is right, detail is missing | name the gap, request only that |
| `insufficient` | cannot answer | name the gap, request only that |

This step is not decoration. In component ablations of adaptive video agents, the
"can I answer yet?" evaluator was the single highest-impact part of the system —
removing it hurt accuracy more than removing the smart sampler (arXiv:2410.20252).
Interval-level model confidence also correlates with correctness, which is what
makes confidence-gated search work (arXiv:2507.02946).

### Rounds 2–3 — targeted

```bash
nybls frames <id> --at 92,570 --looking-for "09:30, the chart he refers to"
nybls zoom   <id> --at 570 --box 0.3,0.2,0.4,0.4 --looking-for "axis labels"
```

Request frames for a **named** interval and a **named** expectation. Never
re-sample globally; that is what Round 1 was for.

Prefer a zoom over more frames when the answer is inside one frame. Adding
spatial zoom to a temporal search gained 2.6 to 5.9 accuracy points under an
identical frame budget (arXiv:2504.02259, building on arXiv:2312.14135).

### Stop

Stop at the first of:

- confidence is `sufficient`
- three rounds after probe — accuracy saturates there (arXiv:2403.10517)
- the budget is exhausted

If you stop at `partial`, **say so in the output.** A confident answer built on
insufficient evidence is the failure mode this whole design exists to prevent.

---

## Budget

```
budget = clamp(8, ceil(duration_minutes * 4), 200)   # image units
```

One sheet, one full frame, and one zoom each cost one unit. The ledger also
tracks estimated visual tokens, computed the way the Claude API bills them
(ceil(w/28) * ceil(h/28) per image).

Duration-scaled budgets with a floor and ceiling follow the pattern in
arXiv:2510.04428. The ceiling matters more than the floor: past roughly 32
well-chosen frames, video QA accuracy plateaus (arXiv:2502.19680), so a large
budget is permission to look carefully, not an instruction to look often.

Sampling density is genuinely task-dependent — some questions are answerable at
one frame per minute, others need one frame per second in a narrow window
(arXiv:2503.12496). Coarse first, dense only where the question points.

---

## Rails: what the tool enforces

Prose can be ignored. These cannot:

| Rail | Behavior |
|---|---|
| Named gaps | past 3 spent images, `frames`, `zoom` and `sheet --range` refuse without `--looking-for` (a whole-video `sheet` is the coverage round and is exempt) |
| Budget stop | requests beyond the budget are refused; only a human may `--force` |
| Duplicate detection | a near-duplicate of an already-served frame is flagged as waste |
| Per-call cap | at most 10 frames per invocation |
| Next-step nudges | every command's output restates the next protocol step |

The rails exist because the protocol must work for an agent that was not
carefully prompted. Discipline that depends on the operator does not survive
distribution.

---

## Grounding: what the verifier can and cannot judge

`nybls verify <id> --claims claims.json` checks each claim against the transcript in a
window around its timestamp (45 s before, 120 s after). Citations are generated
by the tool, never written by the model; the verifier is the check that the
model's *claims* match what was actually said.

| Verdict | Meaning |
|---|---|
| `verified` | ≥55% of the claim's content words appear near the timestamp |
| `weak` | 30–55% — quote more precisely, or the timestamp is off |
| `unsupported` | <30% — the transcript does not say this here; treat as a fabrication until shown otherwise |
| `out-of-range` | the timestamp is past the end of speech |
| `no-speech` | the video has no usable transcript; speech can neither confirm nor deny this claim |

`no-speech` is not a failure of the claim. It says this method does not apply,
and the claim needs a **frame citation** instead. Claims that speech cannot
judge leave the clean-percentage denominator rather than counting as failures:
a corpus of silent screen recordings would otherwise verify as 0% clean while
being entirely correct on screen. Never delete a finding you can see because the
transcript did not corroborate it; cite the frame and its timestamp.

The distinction exists because it was missed once. A true claim, read off the
frames of a silent reel, came back `unsupported` at 0% — indistinguishable from a
fabrication — and the honest response to that verdict would have been to delete
a correct finding.

---

## Output contract

Every answer ends with three blocks:

1. **Answer** — grounded in what was seen and heard, with inline `[mm:ss]` citations.
2. **Evidence strip** — every image examined, and what it showed.
3. **Ledger** — verbatim output of `nybls ledger <id>`.

The evidence strip is what separates a claim from an assertion. It is also the
product's most visible difference: a transcript-only tool cannot produce one.

---

## Worked example

A 35-minute video, question: what happens in it?

| Round | Action | Spend | Outcome |
|---|---|---|---|
| 0 | probe, read transcript | 0 | narrative clear; the visual payoff is not |
| 1 | one whole-video sheet | 1 | six moments; the second half is a *different car* |
| — | evaluator | — | `partial` — the titular reveal is not in these six |
| 2 | sheet of the final 5.5 minutes | 1 | not there either; the reveal is earlier |
| 3 | zoom on a badge | 1 | landed on a headlight — reported honestly, model not named |

Final: 3 images, ~3,069 visual tokens, about one cent, against 53,171 frames.
The reveal was located at 12:05 by combining a Round 1 thumbnail with a free
transcript read — not by spending more images.
