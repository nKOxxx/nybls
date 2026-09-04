# Errata — three round-3 questions are invalid, and how the design let them through

Found 2026-09-04 while scoring, by auditing our own transcripts rather than trusting the
design note. This invalidates questions, not arms; both arms are affected equally.

## The design rule, and how it failed

Round 3's ground truth states: "Candidates appearing in narration were rejected at design
time." That check was run with **token-exact substring matching**. Narration is speech.
A file called `node_modules` on screen is *spoken* as "node modules"; `.dockerignore` is
spoken as "Docker ignore". The filter searched for the written form, found zero hits, and
passed the question as visual-only.

Re-run with normalisation (lowercase, non-alphanumerics collapsed to spaces):

| Video | term | written form hits | spoken form hits |
|---|---|---|---|
| DQdB7wFEygo | `.dockerignore` | 0 | **1** ("docker ignore") |
| DQdB7wFEygo | `node_modules` | 0 | **2** ("node modules") |
| DQdB7wFEygo | "layer caching" | — | **2** |
| L24Wf0VlTE0 | "310-620 mph" | 0 | **1** ("310 to 620", "mph") |

## Consequence

- **DQdB7wFEygo Q2** (the "Layer Caching For Dummies" slide) — INVALID. "Layer caching" is
  said aloud twice; the concept is answerable from the transcript.
- **DQdB7wFEygo Q4** (what `.dockerignore` contains) — INVALID. The narration states the
  answer outright: "we're going to add the node modules folder". Arm A answered it correctly
  *from the transcript* and said so honestly.
- **L24Wf0VlTE0 Q5** (on-screen text) — PARTIALLY COMPROMISED. The speed figure is both
  spoken and shown, so the specific number can be read rather than seen. The rest of the
  question (what *kinds* of text appear) remains visual-only and is scored.

Round 3 is therefore scored over **17 valid questions, not 20**. Rounds 1 and 2 used the
same token-exact filter and should be re-audited before the paper quotes them.

## The finding worth keeping

A benchmark that tests "did the model look?" must exclude anything the narration says. The
obvious check — grep the transcript for the answer — silently fails across the
speech/writing boundary, and it fails hardest on exactly the content type where looking
matters most: filenames, identifiers, code, on-screen numbers. Any future question filter
must normalise punctuation and word spacing, and should be run against a phonetic or
loose-match form, not a literal one.

We caught this only because an arm answered a question honestly and named the transcript
as its source. Had it answered from the frames and stayed silent about provenance, the
question would have looked valid and scored.
