# Round 4 transient item persistence, measured

Measured with `bench/measure_event_persistence.py` at 0.25 to 1.0 s resolution, from the
author agent's approximate timestamp and signature string, after the arms ran and before
scoring. A value of 0.25 s means the signature matched in exactly one sample: the true
visibility is at most 0.5 s at this resolution, and could be shorter.

## A limit of the measurement, found on the Rust video

The method takes the longest contiguous run of samples whose OCR contains the signature.
That assumes OCR reads the text reliably whenever it is on screen. **For small terminal
text at the tool's 960 px working resolution it does not.** Two Rust items make the point:

- "Hello, wolrd!" sat in terminal scrollback for roughly ninety seconds by three
  independent readers (the author's dense grid, and both arms), yet OCR matched it in 3 of
  241 samples across a two minute window, giving a "longest run" of 1.0 s.
- "cargo 1.88.0" was read verbatim by both arms, from at least two grid frames fifty
  seconds apart, yet OCR matched it in **0 of 121 samples**.

Both figures are wrong and neither is used. Consequence: this measurement is trustworthy
for large, high contrast on screen text (title cards, captions, editor code at normal
size) and fails for small terminal output. Where OCR matches are sparse but readers agree
the text persisted, the readers' range is reported instead and marked as such.
`n_matching` versus `n_samples` is reported alongside the run length so the reader can see
when the tool is flaking. Raising the working resolution to 2560 px does read this text
(see `GT_ERRATA.md`), at four times the cost per sample; the tool should do that by default
when the signature is not found.

## 92gQUnMCA08, C timelapse (370 s)

| item | signature | visible | from | p(capture) at N=30 | N for even odds |
|---|---|---|---|---|---|
| Q3 nonsense terminal command and error | `ezzz` | at most 0.5 s | 95.0 s | 0.020 | 738 |
| Q4 terminal flooded with a number | `21 21 21` | at most 0.5 s | 295.0 s | 0.020 | 738 |
| Q5 all caps frustrated comment | `WHAT IS GOING ON` | 1.25 s | 113.0 s | 0.102 | 147 |

A timelapse compresses hours into minutes, so every state is transient by construction.
The dense 10 s reference grid caught each of these in exactly one frame, which is itself
luck: at 1.25 s visibility a 10 s grid catches an item with probability 0.125.

## QtqYNyBv9r8, Rust session (727 s)

| item | signature | visible | basis | p(capture) at N=30 |
|---|---|---|---|---|
| Q3 typo in program output | `wolrd` | at least 33 s, in scrollback | re-measured at 2560 px: 55 of 121 matches, longest run 33.0 s from 203.0 s (`remeasure_2560/persist_QtqYNyBv9r8_220.json`); the 960 px pass had 3 of 241 | 1.0 |
| Q4 cargo version line | `cargo 1.88.0` | at least 20 s, in scrollback | re-measured at 2560 px: 32 of 81 matches, longest run 20.0 s from 266.0 s (`remeasure_2560/persist_QtqYNyBv9r8_255.json`); the 960 px pass had 0 of 121 | 0.83 |
| Q5 sourced binary, exit 127 | `exit 127` | about 2 s | OCR 6 of 121, run 1.5 s from 418.5 s; 2560 px check shows it at 418 to 419 s only | 0.062 |

The two long lived items were labelled T by the author and are transient in the sense
that they happen once, but they persist in scrollback: 33 s for the typo, above the
control's 24.2 s grid interval, and 20 s for the cargo line, just under it (capture
probability 0.83). Both arms got both. **What the grid cannot reach is decided by persistence,
not by the P/T label.** The label predicts the gap only where T items are genuinely brief.

## vxP2PTA1GEk, HTML and CSS session (1697 s)

This video is stored at **360 by 640**, a vertical low resolution source, where the other
three are 1152 to 1280 wide. OCR cannot read code at that size at all, and both arms
reported digit level uncertainty on every numeric answer for the same reason. Persistence
here rests entirely on reader agreement.

| item | signature | visible | basis | p(capture) at N=30 |
|---|---|---|---|---|
| Q4 DevTools edited rule | `200px` | at least 113 s per readers; UNMEASURABLE by OCR | 0 of 261 at 960 px and 0 of 121 at 2560 px (`remeasure_2560/persist_vxP2PTA1GEk_1215.json`): the source is 360 by 640 and upscaling creates no pixels; rests on Arm A's three frames at 1159, 1216, 1272 s | about 1.0, unmeasured |
| Q5 second media query | `1080px` | about 160 s per readers; UNMEASURABLE by OCR | 0 of 171 at 960 px and 0 of 86 at 2560 px (`remeasure_2560/persist_vxP2PTA1GEk_1615.json`); rests on both arms' frames from 1555 s to the end | about 1.0, unmeasured |

## Wlu4MsBnjuk, Snake game (1445.49 s)

OCR works here: the editor and terminal text is large enough at 1280 px, and match counts
are dense, so these figures are used as measured.

| item | signature | visible | from | n_matching | p(capture) at N=30 | N for even odds |
|---|---|---|---|---|---|---|
| Q3 KeyboardInterrupt traceback | `KeyboardInterrupt` | 10.5 s (recurs; 21 matches in an 80 s window) | 1008.0 s | 21 of 161 | 0.218 | 68 |
| Q4 final frame_size_x | `1380` | 27.0 s | 1419.0 s | 40 of 121 | 0.560 | 26 |
| Q5 closing comment | `WATHING` | 25.5 s, to the end of the video | 1420.0 s | 51 of 61 | 0.529 | 28 |
| Q4 final frame_size_y (the item that separated the arms) | `840` | intermittent: 8 of 141 matches over 140 s at 2560 px, longest run 3.0 s from 1333.0 s (`remeasure_2560/persist_Wlu4MsBnjuk_1400.json`) | | 8 of 141 | 0.062 for the longest run; not a single interval event | 241 |

The control's grid interval on this video is 48.2 s, so each of these is caught by at most
one uniform frame, and at 0.22 to 0.56 probability. The last two also sit inside the
control's closing dead zone of 24.1 s for part of their run: the final uniform sample is
at 1421.4 s (D = 1445.49 s), so anything typed after that is structurally unreachable, which is exactly
what the control reported for the end of the closing comment and the final height.


## Re-measurement at 2560 px, 2026-09-09 (review run 024, required item 12)

Raising the OCR working width from 960 to 2560 px reads terminal text: `wolrd` 55 of 121
matches, `cargo 1.88.0` 32 of 81, where the 960 px pass found 3 of 241 and 0 of 121. The
two HTML items remain unmeasurable at any resolution because the stored source is 360 by
640; those rows rest on reader agreement and are marked so. The Snake `840` value, which
separated the arms and had never been measured, matches 8 of 141 samples over 140 s with
no run longer than 3 s: a long lived value that OCR, and evidently the control's three
nearby samples, could read only intermittently. That is a third failure class, neither a
brief event nor a dead zone, and the paper now says so.
