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
| Q3 typo in program output | `wolrd` | about 90 s, in scrollback | three readers agree; OCR 3 of 241, unusable | about 1.0 |
| Q4 cargo version line | `cargo 1.88.0` | at least 50 s, in scrollback | both arms read it at 229 s and 278 s; OCR 0 of 121, unusable | about 1.0 |
| Q5 sourced binary, exit 127 | `exit 127` | about 2 s | OCR 6 of 121, run 1.5 s from 418.5 s; 2560 px check shows it at 418 to 419 s only | 0.062 |

The two long lived items were labelled T by the author and are transient in the sense
that they happen once, but they persist in scrollback for longer than the control's 24 s
grid interval. Both arms got both. **What the grid cannot reach is decided by persistence,
not by the P/T label.** The label predicts the gap only where T items are genuinely brief.

## vxP2PTA1GEk, HTML and CSS session (1697 s)

| item | signature | visible | basis | p(capture) at N=30 |
|---|---|---|---|---|
| Q4 DevTools edited rule | `200px` | at least 113 s | Arm A read it at 1159, 1216 and 1272 s; OCR 0 of 261 (DevTools text, small), unusable | about 1.0 |
| Q5 second media query | `1080px` | about 160 s per the author | pending OCR | about 1.0 |
