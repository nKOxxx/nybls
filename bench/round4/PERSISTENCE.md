# Round 4 transient item persistence, measured

Measured with `bench/measure_event_persistence.py` at 0.25 to 0.5 s resolution, from the
author agent's approximate timestamp and signature string, after the arms ran and before
scoring. A value of 0.25 s means the signature matched in exactly one sample: the true
visibility is at most 0.5 s at this resolution, and could be shorter.

## A limit of the measurement, found on the Rust video

The method takes the longest contiguous run of samples whose OCR contains the signature.
That assumes OCR reads the text reliably whenever it is on screen. **For small terminal
text at 1280 px it does not.** The Rust item "Hello, wolrd!" sat in terminal scrollback for
roughly ninety seconds by three independent readers (the author agent's dense grid, and
both arms), yet OCR matched it in only 3 of 241 samples across a two minute window, giving
a "longest run" of 1.0 s. That figure is wrong and is not used.

Consequence: this measurement is trustworthy for large, high contrast on screen text
(title cards, captions, editor code at normal size) and undercounts for small terminal
output. Where OCR matches are sparse but readers agree the text persisted, the readers'
range is reported instead and marked as such. `n_matching` versus `n_samples` is now
reported alongside the run length so the reader can see when the tool is flaking.

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
| Q3 typo in program output | `wolrd` | about 90 s, in scrollback | three readers agree (grid, both arms); OCR matched 3 of 241 samples, unusable | about 1.0 |
| Q4 cargo version line | `cargo 1.88.0` | pending | | |
| Q5 sourced binary, exit 127 | `exit 127` | pending | | |
