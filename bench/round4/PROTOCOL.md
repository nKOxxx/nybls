# Round 4 protocol: silent video, and the persistent versus transient split

**Written 2026-09-07, before ingest finished and before any question existed.**

## Why this round

Rounds 1 to 3 never ran on silent video, which is now the paper's central case. And round 3's
failed prediction P4 (that the gap between arms widens with duration) produced a sharper
hypothesis: the gap depends on whether a question's answer is *transient* or *persistent*,
not on how long the video is. Round 4 tests both.

## Videos

Four public silent screen recordings, chosen for duration spread and content variety.
None was seen by anyone in this experiment before selection.

| id | content | duration |
|---|---|---|
| 92gQUnMCA08 | C programming timelapse | 6:10 |
| QtqYNyBv9r8 | Rust coding session | 12:07 |
| Wlu4MsBnjuk | Snake game build | 24:06 |
| vxP2PTA1GEk | HTML and CSS session | 28:17 |

The timelapse is a deliberately hostile case: compressing hours into six minutes makes
essentially every on screen state transient.

## Roles, and what changed since round 3

Three failures of earlier rounds were structural, and this round is designed around them.

**Ground truth was built from the tool's own study sheets.** That biases the reference toward
the iterative arm. Here the reference is built from a dense uniform ffmpeg grid, one frame
every 10 seconds, by an **author agent that has no access to nybls at all**. The reference
owes nothing to the tool it judges.

**Questions were written and scored by the same person.** Here the author agent writes the
questions and ground truth; the arms answer; a **separate judge agent** scores. The judge
sees the two arms as X and Y with the mapping withheld, and never sees the tool.

**The narration filter leaked in every round.** On silent video there is no narration to
leak. The author agent must still confirm the transcript is degenerate (content words per
minute below 1) and record it.

**The tool was modified mid run in round 2.** Pinned read only at `fd11789` before ingest
began; tree hash recorded before, and checked after every arm finishes.

## Question design

Five questions per video. Each is labelled at design time, by the author agent, as:

- **P (persistent)**: the answer is visible for most of the video, or recurs throughout.
  Examples: editor theme, project name in the title bar, a file always open in a tab.
- **T (transient)**: the answer is visible once, for a short stretch. Examples: a specific
  compiler error, a terminal command and its output, a line of code before it was changed.

Roughly balanced, at least two of each per video. For every T item the author records the
approximate timestamp so on screen persistence can be measured afterwards with
`bench/measure_event_persistence.py`, at 0.25 s resolution, and capture probability computed
rather than assumed.

## Arms

- **Arm A, one shot.** Transcript plus 30 frames on a uniform grid, handed over at once.
  May not run ffmpeg, nybls or anything that renders a new image. May not modify any file.
- **Arm B, iterative.** The pinned nybls CLI and the WATCH protocol. May not modify any file.
  Ledger zeroed and all prior frames archived before it starts.

Both arms are told the video is silent only if the transcript tells them; the setup prompt
does not say so.

## Scoring

2 correct and complete, 1 partial or a correct but different instance, 0 wrong or
"insufficient evidence", minus 1 confidently fabricated. The judge scores each item and also
records, per item, whether each arm's evidence citation actually points at a frame that
contains the answer. Per item scores are reported split by P and T.
