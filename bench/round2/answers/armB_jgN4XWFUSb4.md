# Arm B (iterative, PINNED tool) — jgN4XWFUSb4 — RESULT OF RECORD
Re-run 2026-09-02 against the tool pinned at commit 5864159 with nybls_core/ read-only.
Ledger zeroed and all prior frames archived first. Agent declared no tool file modified;
pinned-tree hash verified identical before and after.
COST: 11 images, ~16,329 visual tokens (budget 11/200).
[Void first attempt: 15 images / 22,888 tokens — see VOID_armB_jgN4XWFUSb4.md]

1. PLATE: "W1MNO" — read from the carVertical overlay panel at 45:38 (f_2738000) and
   zoom-confirmed (z_2738000), cross-checked against the physical rear plate at 79:09.
   Explicitly noted the overlay was load-bearing because the bumper plate alone was too
   blurry to call. CORRECT (2).
2. COLOUR/DETAIL: yellow 991 GT3 RS, black GT3 RS script, fixed wing, centre-locks with
   red RS centres, yellow calipers, yellow stitching/belts/cage, GT3 RS headrests.
   Separated seen from heard (PPF wrap, cage wrapped). CORRECT (2).
3. DIAGNOSTIC DEVICE: f_975000 at 16:15 — "1 DME (Digital Engine Electronics)", DTCs 13,
   Fault 8, 12.3V, "Cylinder 4 misfiring detected", cylinder 5, cylinder 6, intake AND
   exhaust camshaft sensor circuit short to ground Bank 2, all Active/static.
   EXACT MATCH to ground truth item 3, including cylinder 4 and the fault counter.
   (Ground truth records the unit as "SME"; both Arm B runs read "DME", which is correct.)
   CORRECT (2).
4. DOCUMENTS: Porsche Approved inspection report (78:39, heading legible, line items NOT
   legible in any frame) and the carVertical history panel (45:38, 46:00). Explicitly
   graded itself partial on "what does it set out" because the report text was never
   legible on screen and that content came from speech. Did not retrieve the ground
   truth's lettered-conditions warranty policy screen. PARTIAL (1).
5. CGI EXPLAINER: four-stroke animation "STROKE 1 INTAKE" (12:04) and a valvetrain
   comparison animation contrasting bucket tappet with finger follower (26:50). Declined
   to claim a third animated segment it had not spent an image on. CORRECT (2).

SCORE: 9 / 10 at 16,329 visual tokens.

TOOL DEFECT REPORTED, NOT FIXED (as instructed): the named-gap rail also applies to
`sheet --range`, but PROTOCOL.md's rails table says it applies only to frames/zoom. A
second sheet call was refused until --looking-for was added, costing a round-trip.
This is a docs/behaviour mismatch worth fixing after the benchmark, not during it.
