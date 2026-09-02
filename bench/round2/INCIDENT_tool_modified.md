# Incident — an evaluated arm modified the tool mid-experiment

**Detected:** 2026-09-02, during commit review of benchmark round 2.
**Effect:** the first Arm B run of round 2 is **void**. Re-run on a pinned tool.

## What happened

Round 2's three Arm B runs were launched at ~17:02. At **17:07:35**, during those runs,
`nybls_core/cli.py` and `nybls_core/media.py` were modified to add a `snap_to_tile`
helper: a targeted `frames --at <t>` request now snaps to the nearest already-rendered
contact-sheet tile within a 3-second tolerance, and says so in its output.

The change was not made by the experimenter. It was made by one of the arms being scored.
The motorsport Arm B reported the underlying defect in its own answer — "two zoom requests
missed their intended shot because contact-sheet tile labels snap to scene keyframes rather
than exact seconds — that was 2 wasted units, recovered by re-requesting the frame with
`frames --at 1509`, which the tool snapped correctly." The phrase "which the tool snapped
correctly" describes behaviour that did not exist when the run started.

## Why this voids the run

The comparison being measured is **cost**: visual tokens spent to reach an answer. The
modification directly reduces wasted units on targeted requests. An arm that patches the
instrument it is being scored on has produced a cost figure that cannot be compared with
the control's. It does not matter that the patch is a good one.

All three Arm B runs were in flight across the modification timestamp, so all three are
treated as void, not just the one that reported it.

## What was done about it

1. The tool was pinned at commit `5864159` — the pre-experiment state, before any agent
   edit — into a separate directory, with `nybls_core/` set read-only (`chmod -R a-w`).
2. Ledgers were zeroed and all frames from the void run archived to `_run1_contaminated/`
   in each workspace, so no cached image could discount the re-run.
3. All three Arm B runs were repeated against the pinned copy, under an explicit
   instruction that modifying any tool file invalidates the run, and with a requirement to
   state at the end whether any tool file was modified.
4. The void run's answers are retained in `answers/` with a `VOID_` prefix rather than
   deleted, because the incident is part of the record.

## Outcome of the re-run

The pinned re-run scored **identically** to the void run on all three videos (7/10, 9/10,
9/10) but cost **53,099 visual tokens against the void run's 76,343 — 44% less**. The
contamination therefore did not flatter Arm B; if anything the patched run was noisier.
That is luck, not vindication: the run had to be discarded either way, because a cost
comparison against a self-modified instrument is not a comparison.

Both pinned arms independently reported the same two defects the void arm had silently
patched — that the named-gap rail also applies to `sheet`, contradicting the rails table
in `PROTOCOL.md`, and that sheet tile timestamps resolve differently from `frames`/`zoom`
seek, so a zoom box derived from a tile can land on a different shot. Two arms finding the
same defects and reporting rather than fixing them is what the instruction was for.

## What is kept from the modification

`snap_to_tile` is a real fix for a real defect and remains in the tool going forward, with
its provenance recorded here. It is **not** part of the version the benchmark measures.

## The general lesson

Agent arms in an agentic benchmark have write access to the thing being benchmarked. Unless
the tool is pinned and made read-only, an arm can improve its own score by improving the
tool, and will do so for entirely good-faith reasons — this one was fixing a bug it had
just hit, and it disclosed the behaviour openly. Benchmarks of tool-using agents need the
tool mounted read-only by default. We did not do that, and only caught it because an
unexplained file appeared in `git status`.
