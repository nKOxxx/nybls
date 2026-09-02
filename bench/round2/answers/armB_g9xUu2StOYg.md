# Arm B (iterative, PINNED tool) — g9xUu2StOYg — RESULT OF RECORD
Re-run 2026-09-02 against the tool pinned at commit 5864159 with nybls_core/ read-only.
Ledger zeroed and all prior frames archived first. Agent declared no tool file modified.
COST: 19 images, ~24,887 visual tokens (budget 19/110). Stopped at confidence "partial".
[Void first attempt: 20 images / 26,284 tokens — see VOID_armB_g9xUu2StOYg.md]

1. BRANDING: "THROTTLE TALK" two-line white wordmark, persistent top-left. CORRECT (2).
2. RESULTS GRAPHIC: **"insufficient evidence" — FAILED (0).** Sampled ~60 moments including
   TEN narrow sheets aimed precisely at every point where the narration quotes a result
   (02:40, 04:17, 06:00, 09:21, 10:02, 19:04, 21:31). Saw no results table, classification
   panel or timing tower. Correctly distinguished the only position list it did find — a
   live running order inside borrowed F1-game esports footage at 22:25 — as NOT a results
   graphic. Reported its stop confidence as "partial" and the answer as an unresolved
   negative: "absence not proven, only not observed across ten targeted regions."
3. INTERVIEW PRESENTATION: two-panel vertical split screen; left interviewer in over-ear
   headset with boom mic, right Mahaveer against a chequered-flag virtual background in an
   AF Corse polo; burned-in caption straddling both panels, speaker name bold red then the
   line in bold white with drop shadow. EXACT MATCH to ground truth item 3. CORRECT (2).
4. PODIUM BRANDING: Monza podium at 25:08 — sparco, magigas, Magneti Marelli, Checkstar,
   ACI SPORT TV, AUTOSPRINT, on a Monza-outline chequerboard backdrop; plus the Brno
   prize-giving at 05:56. Did NOT find the ground truth's JK Tyre / JK Racing India Series
   podium. PARTIAL (1).
5. FOOTAGE TYPES: broadcast across many circuits and eras, onboard/helmet-cam, pit-lane
   and garage b-roll, paddock reaction, podium and celebration, team group photo, esports
   sim capture, split-screen remote interview, modern GT. CORRECT (2).

SCORE: 7 / 10 at 24,887 visual tokens.

THIRD INDEPENDENT FAILURE ON Q2. Arm A, the void Arm B and this pinned Arm B all missed
the results graphic. The graphic is real and was verified independently: OCR-confirmed on
screen for 2.0 seconds (bench/round2/persist_g9xUu2StOYg_162.json).

TOOL DEFECTS REPORTED, NOT FIXED — the same two the McLaren pinned arm reported
independently: (a) the named-gap rail also applies to `sheet`, contradicting PROTOCOL.md's
rails table; (b) sheet tile timestamps and frames/zoom seek resolve differently, so a zoom
box derived from a tile can land on a different shot. (b) is exactly the defect the void
run's arm silently patched mid-experiment.
