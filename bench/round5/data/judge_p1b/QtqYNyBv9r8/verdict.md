# Verdict, QtqYNyBv9r8 ("Silent Coding Session - Rust Lang - 1")

| Q | Label | W | X | Y | Rationale |
|---|---|---|---|---|---|
| 1 | P | 0 abstained | 2 correct | 0 abstained | X: "The Rust Programming Language", doc.rust-lang.org, matching chapter paths. W and Y: cannot be determined. |
| 2 | P | 0 abstained | 2 correct | 0 abstained | X: `git:(master)` in prompt, `master*` in VS Code status bar, yes. Matches GT. W and Y: cannot be determined. |
| 3 | T | 0 abstained | 2 correct | 0 abstained | X: `Hello, wolrd!` with the typo, matching GT. W and Y: cannot be determined. |
| 4 | T | 0 abstained | 2 correct | 0 abstained | X: `cargo 1.88.0 (873a06493 2025-05-10)`, exact match. W and Y: cannot be determined. |
| 5 | T | 0 abstained | 2 correct | 0 abstained | X: `. ./hello_cargo`, final line `[2]  + 62750 exit 127   ELF   >`. GT body says PID 62544 but the attached errata confirms 62750 is the final job-status line (second run at 418 to 419 s); scored against the corrected GT. W and Y: cannot be determined. |

Totals: W 0/10, X 10/10, Y 0/10.

Outcome counts: W 5 abstained. X 5 correct. Y 5 abstained.

## Ground truth concerns

- Q5: the GT body (PID 62544) is superseded by its own errata (PID 62750 for the final job-status line). Applied the errata. No further concerns.
