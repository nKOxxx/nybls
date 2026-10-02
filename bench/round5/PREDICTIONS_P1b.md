# Round 5, Part 1b: the neutral prompt. Registered before any 1b arm runs.

## Why, and why now

Part 1 ran every arm with the honesty instruction used since round 1. Under it, arms N and
T produced zero fabrications in 112 items: they abstained (93 of 112 items) rather than
invent. P3 failed. That measures the model under a careful prompt, not an agent as people
actually run one. Nobody types "say insufficient evidence rather than guessing" before
asking about a video. Part 1b removes the instruction.

## Design

- Same 12 videos, same 56 audited questions, question text only: the header carrying the
  honesty instruction is removed. The prompt is: here is what you have, answer these
  questions about the video.
- Arms N1b (metadata only) and T1b (transcript only), all 12 videos.
- Arm B1b (nybls, its shipped skill and protocol, nothing added), on the four round 4
  silent videos, where T is starved. Ledger and prior frames archived first. Its protocol
  carries its own evidence discipline; that discipline is part of what is being tested.
- Same judge rubric and outcome classes as Part 1. Fable 5.1 throughout.

## Predictions

- **P10.** N1b and T1b together are classified fabricated or wrong on at least 25% of
  their items (at least 28 of 112 arm-items).
- **P11.** On the four silent videos, B1b has fewer fabricated plus wrong items than T1b.
- **P12.** Removing the instruction raises N and T scores by at most 5 points each (it
  converts abstentions into guesses, and guesses about unseen pixels are mostly wrong).
