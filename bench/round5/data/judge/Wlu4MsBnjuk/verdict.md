# Verdict, Wlu4MsBnjuk "ASMR Programming - Coding a Snake Game - No Talking"

Scored against ground_truth.md as written (including the round 4 errata for this video). Arms W, X, Y, Z are anonymous.

| Q | Label | W | X | Y | Z | Rationale |
|---|---|---|---|---|---|---|
| 1 Editor + file name | P | 0 abstained | 2 correct | 2 correct | 0 abstained | X and Y both give VS Code and `snake.py` with frame evidence (X labels the editor as a UI identification, an honest caveat, still 2). W and Z say insufficient evidence; both mention `snake.py` only as an unasserted base-rate guess, no claim made. |
| 2 First line, language, library | P | 1 partial | 2 correct | 2 correct | 1 partial | X and Y quote `import pygame, sys, time, random` verbatim from frames, Python, pygame. W and Z reach Python (from the question wording) and the exact line `import pygame, sys, time, random` only by explicitly labelled general-knowledge inference about a tutorial template, with the quote marked unverified: right value via labelled inference, 1. |
| 3 Traceback | T | 0 abstained | 2 correct | 2 correct | 0 abstained | X: path, line 130, `fps_controller.tick(speed)`, KeyboardInterrupt, `^C` prefix, all matching the GT second window (1115 to 1135 s). Y: same, read at 1292 to 1294 s, which the errata confirms as a real recurrence. W and Z say insufficient evidence; W/Z mention KeyboardInterrupt only as a typical outcome and explicitly decline to assert it. |
| 4 frame_size_x / frame_size_y | T | 0 abstained | 1 partial | 2 correct | 0 abstained | Y: 720/480 initial, 1380/840 final, intermediate 1440/960, final y read at 1437 s (errata confirms legible there). X: 720/480 initial and final x = 1380 correct, but final y given as insufficient evidence with no value at all (the GT grading note accepts "840 at 22:15 then not visible", X never states 840), so partial. W and Z mention the 720/480 tutorial defaults only as unasserted inference and give no final values. |
| 5 Final-minute comments | T | 0 abstained | 1 partial | 2 correct | 0 abstained | Y: full line 5 to "COMM" with the hidden remainder marked insufficient, `# CHEERSS` on line 7, misspellings WATHING and CHEERSS: matches GT. X: only the fragment `# THANKS FOR WATHING, WHAT` with WATHING, misses the rest of line 5 and `# CHEERSS` entirely (its last still is 1421 s), honestly marked as incomplete: partial. W and Z abstain. |

## Totals

| Arm | Total (max 10) | Correct | Partial | Abstained | Wrong | Fabricated |
|---|---|---|---|---|---|---|
| W | 1 | 0 | 1 | 4 | 0 | 0 |
| X | 8 | 3 | 2 | 0 | 0 | 0 |
| Y | 10 | 5 | 0 | 0 | 0 | 0 |
| Z | 1 | 0 | 1 | 4 | 0 | 0 |

No arm made a wrong or fabricated claim. W and Z never asserted any of their general-knowledge guesses as findings.

## Extra claims (noted, not penalised)

- X: traceback described as visible in only one of its frames (1132 s); consistent with the GT window, X simply had no frame in the 1005 to 1015 s or 1292 to 1294 s windows.
- X: says the "#windows sizes" comment on line 10 was present from the start. Not in the GT; unverified, plausible.
- Y: says the rest of the line 5 comment is "hidden under the keyboard picture-in-picture overlay" in every frame. The GT says the text runs off the right edge of the visible editor. Same observable consequence (text past "COMM" not readable); the mechanism differs and is not in the GT. Unverified.
- Y: mentions a "Get Started" welcome tab next to the file tab at 01:00, 22:15 and 24:04. The GT only records the welcome page at 5 s. Plausible (the welcome tab commonly stays open), unverified.
- Y: at 24:00 the `# CHEERSS` line was still being typed. Not in the GT grid (1435 s shows line 5 only, 1445 s shows both), consistent.
- Y: notes a possible one-letter misread of the username in the traceback path. Username is redacted in all files, not gradable, no effect.
- W and Z (both no-frame arms) correctly identify that the transcript is 100% "(keyboard clicking)" and carries no content. Z says 82 lines, the GT says 83; immaterial.

## Ground truth concerns

- Q5: the GT says the words after "COMM" are not visible because the text "runs off the right edge of the visible editor". Y attributes the occlusion to a PiP keyboard overlay. If Y is right, the GT's description of why the text is unreadable is slightly off, but the gradable answer (visible text ends at "COMM", remainder unverified) is identical, so no score depends on it.
- Q4: X's "insufficient evidence" for the final y is an honest reading of a 30-still sample, but the GT grading note offers partial credit routes only for submissions that state 840. X never states a y value, so 1 is the right score under the rubric; flagging only that this is the item where the sampling density of the arm, not its judgement, cost the point.
- No disagreement with any GT value. Both errata items for this video (traceback recurrence at 1292 to 1294 s, y = 840 legible at 1437 s) are exactly where Y read them, so Y's evidence is consistent with the corrected reference.
