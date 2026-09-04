# Arm B (iterative, pinned 0.8.0) — DQdB7wFEygo (Docker, 11:53)
COST: 8 images, ~12,080 visual tokens (budget 8/48). No tool file modified.
1 VS Code dark theme; flagged the icon theme as inferred, named theme as insufficient (2)
2 quoted "What makes Docker so good?" - a different slide [QUESTION INVALID]
3 **READ `ENV PORT=9000` at line 18 and `EXPOSE 9000` at line 20 directly** (2)
4 .dockerignore = single line `node_modules`, lines 2-4 empty [QUESTION INVALID]
5 explorer contents, plus the honest caveat that the compose filename was never legible (2)
SCORE 6/6 on the three valid questions, at 12,080 tokens.

THE CLEANEST SINGLE RESULT IN THE BENCHMARK: Q3. The uniform grid's samples straddled the
Dockerfile's port lines (lines 4-11, then 20-22) so Arm A could only deduce 9000 from
side evidence. Arm B requested the frame it needed and read the line. Same question, same
video, 4.5x less cost.

TOOL NOTE (reported, not fixed): `frames --at 63,560` was silently snapped to sheet-tile
timestamps. This is the round-2 contamination fix now shipped - and it has a cost: `--at`
is not honoured precisely once a sheet covers the region, with no flag to suppress it.
