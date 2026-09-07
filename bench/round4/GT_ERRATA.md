# Ground truth errata, round 4

Corrections to the author agent's reference, each verified against the pixels before
being applied. The judge scored against the reference as written and listed the
disagreement; the experimenter then checked the video and applied the judge's stated
conditional. No score was changed without a frame.

## QtqYNyBv9r8, Rust session, Q5: the reference recorded the earlier of two runs

The question asks for the command that flooded the terminal and the **final** job status
line. The reference gives PID 62544. Arm B (judge label Y) gave PID 62750 and was scored
1 with the judge's note: "if Y's reading is right, Y's Q5 should be raised to 2."

Checked at 2560 px, one frame per second, OCR:

| t | on screen |
|---|---|
| 414 to 416 s | `[2] 62544` with parse errors |
| 417 s | terminal cleared or scrolled, neither PID legible |
| 418 to 419 s | `[2] 62750` ... `exit 127` |

The binary was sourced twice, about four seconds apart. The reference's dense grid landed
on the first run at 415 s; the final job status line, which is what the question asks for,
belongs to the second. **Arm B is correct. Y's Q5 is raised to 2, Y's total to 10/10.**

This is prediction P6 confirmed, and the fifth reference correction by an arm across the
benchmark. The dense grid reference is better than the study sheet reference it replaced,
and it is still a sample: a 10 s grid cannot distinguish two events four seconds apart.
