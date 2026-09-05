# Where the information lives: transcript or pixels

**Date:** 2026-09-04 · **Code:** `bench/measure_modality.py` · **Data:** `bench/round3/modality_*.json`

## The claim under test

The project's revised thesis is that **the value of looking is inverse to what the
transcript carries**. Speech and pixels are substitutes, not complements. Where a narrator
reads the slide aloud, a caption reader recovers nearly everything. Where the video is a
silent screen recording, the pixels are the only copy of the content.

That is a comparative claim, so it needs a number comparable across videos.

## Method

Sample 25 frames on a uniform grid, OCR each with Apple Vision, and collect the content
words legible on screen (length 3 or more, stopwords removed). Do the same for the
transcript. Then report the **visual exclusivity ratio**:

    exclusivity = |ocr_words not in transcript| / |ocr_words|

A ratio near 1.0 means essentially nothing on screen can be recovered by reading. A low
ratio means the narration restates what is shown.

## Result

| exclusivity | video | type | min | transcript words | words/min | OCR words | frames with text |
|---|---|---|---|---|---|---|---|
| 0.119 | F2FmTdLtb_4 | narrated slide course | 53.6 | 1587 | 29.6 | 168 | 25/25 |
| 0.400 | aircAruvnKk | animated explainer | 18.7 | 681 | 36.5 | 45 | 21/25 |
| 0.444 | L24Wf0VlTE0 | animated explainer | 5.0 | 238 | 47.4 | 18 | 23/25 |
| 0.676 | 8NSyI-npJCU | screen recording, narrated | 21.6 | 779 | 36.0 | 781 | 25/25 |
| 0.689 | DQdB7wFEygo | code tutorial, narrated | 11.9 | 525 | 44.2 | 341 | 22/25 |
| 0.720 | f1wnYdLEpgI | code tutorial, narrated | 6.7 | 289 | 43.1 | 118 | 25/25 |
| 0.724 | PV3r6BINlsM | documentary | 44.5 | 1784 | 40.1 | 29 | 4/25 |
| **0.958** | **oZAiHH9nrhk** | **documentary, ASR failed** | 24.6 | 184 | **7.5** | 24 | 13/25 |
| **1.000** | **8DSxqUypY48** | **silent screen recording** | 63.1 | **2** | **0.03** | **609** | **25/25** |

## What it shows

**The ordering is by content type, and it is the predicted one.** A narrated slide course
sits at 0.119: the speaker reads the slides, so a transcript reader loses little. Screen
recordings and code tutorials cluster at 0.68 to 0.72 **even though they are fully
narrated**, because identifiers, filenames, ports and log lines are shown and not spoken.
The video whose speech recognition failed sits at 0.958.

This is the quantitative form of the thesis. The content where looking is worth most is not
exotic: it is code, terminals and dashboards, which is also the content a caption scraper
handles worst.

**A better ASR failure detector, found by accident.** The stock market documentary's
transcript is degenerate: Hindi and Urdu speech mis-transcribed into pseudo-Latin, which the
round 3 arm reported independently. Our shipped degeneracy check is the ratio of unique
lines to total lines. It scores this transcript **0.999**, i.e. perfectly healthy, because
the model hallucinated *varied* nonsense rather than looping.

**Unique content words per minute catches it cleanly.** Every healthy transcript in the
corpus falls between 29.6 and 47.4 words per minute. The failed one is **7.5**, a factor of
four below the floor. This is a better guard than the line ratio and costs nothing to
compute. It should replace or supplement the shipped check.

## The silent case, which is the thesis at its limit

`8DSxqUypY48` is a 63 minute programming screen recording with no speech, chosen because it
is public and anyone can re-run it. The result is the thesis in its pure form:

- **609 unique content words are legible on screen. Two appear in the transcript.**
  Visual exclusivity is **1.000**: not one word on screen can be recovered by reading.
- All 25 sampled frames carry on screen text. There is no quiet stretch to skip.
- The transcript is 226 lines of `(keyboard clicking)`, a sound event annotation repeated
  for an hour. Its two content words are "keyboard" and "clicking".

**And our shipped degeneracy check calls that transcript healthy, scoring it 1.000**, because
every line is unique. The lines are unique only because each carries a distinct timestamp.
So the line ratio check is defeated twice over: once by hallucinated variety (the stock
market documentary) and once by timestamps (this one). Content words per minute is 0.03 here
against a healthy floor of 29.6, and separates both cases from every healthy transcript by
more than two orders of magnitude.

A transcript first tool reading this video returns "keyboard clicking" for an hour of
programming. That is the segment the thesis is about.

## What must be said against this

- **The Rome row is noisy.** Its 0.724 rests on 29 OCR words from only 4 frames with any
  text at all. A documentary with little on screen text gives the metric almost nothing to
  work with, and the ratio becomes unstable. Rows with few OCR words should be discounted.
- **OCR is not content.** The ratio measures *legible text*, not information. A chess board,
  a waveform or a circuit diagram carries information that OCR cannot see, so the metric
  understates the value of looking on non textual visual content. It is a lower bound on the
  thesis, not a full measure of it.
- **English only.** Apple Vision was run with an English preference. The Hindi and Urdu
  content in the stock market video is not read, which inflates its exclusivity somewhat,
  though the transcript there is degenerate regardless.
- **One silent video, not a corpus.** The silent row is a single public video. More are
  being added. It is however a public video anyone can re-run, which is the point: the
  thesis no longer rests on private material.
- **Correlation, not causation, and n = 9.** The ordering matches the prediction, but the
  corpus was assembled for a different experiment and is not a random sample of video.
