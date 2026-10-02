# Round 5, Part 1c: a smaller model. Registered before any 1c arm runs.

## Why

Part 1b's first results (N1b, metadata only, neutral prompt) show Fable 5.1 abstaining
without being told to ("Nothing below is guessed"). Whether an agent invents video content
may depend on the model more than the prompt. Part 1c repeats Part 1b on Claude Haiku 4.5
(`claude-haiku-4-5-20251001`), the smallest current Claude model, which is what cost
sensitive agent pipelines commonly run.

## Design

Identical to Part 1b (neutral prompt, same 56 questions, same packs): arms N1c and T1c on
all 12 videos, B1c (nybls + shipped skill) on the four silent videos. Judged by Fable 5.1
with the same rubric.

## Predictions

- **P13.** N1c and T1c together are classified fabricated or wrong on at least 25% of their
  items (at least 28 of 112 arm-items).
- **P14.** On the four silent videos, B1c has fewer fabricated plus wrong items than T1c.
- **P15.** B1c scores at least 20 points (of 40) above T1c on the four silent videos.
