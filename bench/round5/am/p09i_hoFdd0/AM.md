# Answers — p09i_hoFdd0 (fixed evidence pack)

Evidence base: transcript.txt is empty of content (four filler tokens: [16:49] "you", [19:34] "uh", [20:28] [Applause], [20:44] "you"), so nothing below rests on speech. Every answer rests on the 20 uniform stills in frames/. "Seen" = legible in a frame; "Inferred" = my reasoning on top of what is seen.

## 1. Screen/buffer dimensions and the two buffers

**Answer (seen):**
- `int width = 160, height = 44;`
- `float zBuffer[160 * 44];`
- `char buffer[160 * 44];`

Also visible alongside: `int backgroundASCIICode = ' ';` (the fill character for `buffer`).

**Evidence:** am07_466s.png lines 7-9 (`int width = 160, height = 44;`, `float zBuffer[160 * 44];`, `char buffer[160 * 44];`); confirmed again in am09_591s.png lines 8-10, with line 11 `int backgroundASCIICode = ' ';`.

## 2. Main tunable constants

**Answer:**
- Cube half-width: `float cubeWidth = 10;` — **seen** (am07_466s.png line 6; am09_591s.png line 7).
- Sampling step over each face: `float incrementSpeed = 0.6;` — **seen** (am09_591s.png line 14; used as `cubeX += incrementSpeed` / `cubeY += incrementSpeed` in am10_653s.png lines 50-52).
- Distance from camera: the variable is being typed as `int distanceFro` (am09_591s.png line 12) and is used as `distanceFromCam` (am10_653s.png line 37: `z = calculateZ(...) + distanceFromCam;`). **Its numeric value is never on screen in any frame — insufficient evidence.**
- K1: used as `K1 * ooz * x * 2` / `K1 * ooz * y` (am10_653s.png lines 41-42, am11_715s.png lines 43-44), but **its declaration/value never appears in any frame — insufficient evidence.**

## 3. Resources for the rotation math and multiplication order

**Answer (seen):**
- Wikipedia, "Rotation matrix" article, section "In three dimensions / Basic rotations", showing Rx(θ), Ry(θ), Rz(θ) — am00_31s.png (URL `en.wikipedia.org/wiki/Rotation_matrix`), and the article top in am17_1089s.png.
- Symbolab "Matrix Multiply, Power Calculator" (`symbolab.com/solver/matrix-multiply-calculator`) — am01_93s.png, am14_902s.png. He also keeps a screenshot of the three Wikipedia matrices in a floating macOS screenshot-markup window (am01, am02) and later a screenshot of Symbolab's expanded result (am02_155s.png, am03_217s.png, am04_280s.png), which he transcribes into `calculateX` / `calculateY` / `calculateZ`.
- Chrome DevTools is open on the Symbolab page (am01, am14) — inferred purpose: hiding ads/panels (the Elements pane is on an `ad_closed_panel` / `mute_panel` div); not confirmable.

**Order of multiplication (seen in am01_93s.png):** the point is a *row vector* `(i j k)` on the left, multiplied by `Rx(A)` first, then `Ry(B)`, then a third matrix whose right side is cut off by the ad panel but whose visible left column entries `cos ... sin C` match `Rz(C)`. So: **(i j k) · Rx(A) · Ry(B) · Rz(C)**. The resulting expanded expressions in am02/am03 (e.g. x = j sinA sinB cosC − k cosA sinB cosC + j cosA sinC + k sinA sinC + i cosB cosC) are consistent with that ordering — inferred confirmation, I did not re-derive by hand. In am14_902s.png / am15_964s.png / am16_1026s.png he additionally runs Symbolab on `(x y z) · Ry(90°)` etc. to get the per-face argument permutations (results `(−z y x)`, `(z y −x)`, `(−x y −z)`), which is how he decides which of `cubeX/cubeY/±cubeWidth` go into each `calculateForSurface` call.

## 4. The six characters for the six calculateForSurface calls

**Answer: partial — insufficient evidence for the full six-call mapping.**

**Seen in code:** the most complete code frame, am16_1026s.png lines 63-66, shows only four calls:
- `calculateForSurface(cubeX, cubeY, -cubeWidth, '.');`
- `calculateForSurface(cubeWidth, cubeY, cubeX, '$');`
- `calculateForSurface(-cubeWidth, cubeY, -cubeX, '~');`
- `calculateForSurface(-cubeX, cubeY, cubeX, '~');` (cursor is on this line, being edited; the `'~'` here is likely a not-yet-changed duplicate — inferred)
Earlier (am08-am12) there is a single call with `'#'`.

**Seen in the running output:** am18_1151s.png shows `.`, `~`, `$`, `#` and a `;` column at the left edge; am19_1213s.png shows `;`, `~`, `+`, `.`. Across the two final output frames the distinct characters are `.` `$` `~` `#` `+` `;` — six characters, which is consistent with six faces (inferred). Which face/call gets which character beyond the first three above is **not determinable** from the frames.

## 5. How a cell is won when two faces overlap

**Answer (seen, am11_715s.png lines 41-48 and am12_777s.png lines 44-51):**
```
ooz = 1/z;                                   // reciprocal of depth
idx = xp + yp * width;
if (idx >= 0 && idx < width * height) {
  if (ooz > zBuffer[idx]) {
    zBuffer[idx] = ooz;
    buffer[idx]  = ch;
  }
}
```
Per cell, `zBuffer[idx]` stores the largest `1/z` seen so far this frame (floats, reset to 0 by `memset(zBuffer, 0, width*height*4)` each frame — am08_529s.png line 31), and `buffer[idx]` stores the character of that winner. A new sample overwrites only if its `ooz` is strictly greater, i.e. if it is closer to the camera (larger 1/z = smaller z). Inferred: the reciprocal is used so that the zero-initialised buffer means "infinitely far", and `z` is already offset by `distanceFromCam` (am10 line 37) so it stays positive.

## 6. Projection to a character cell

**Answer (seen, am11_715s.png lines 43-44; am12_777s.png line 44):**
- `xp = (int)(width/2 + K1 * ooz * x * 2);`
- `yp = (int)(height/2 + K1 * ooz * y);`
with `ooz = 1/z` and `z = calculateZ(...) + distanceFromCam` (am10_653s.png lines 37-39). `width/2`, `height/2` centre the cube on the 160x44 grid.

**Why x is scaled by 2 (inferred, not stated in evidence):** there is no audio and no on-screen comment. The standard reason is that terminal character cells are roughly twice as tall as they are wide, so doubling the horizontal projection keeps the cube from looking squashed. I did not see him state this.

## 7. What spins it, how fast, delay, and terminal reset

**Answer (seen, am15_964s.png lines 72-74 and am16_1026s.png lines 74-76):**
- `A += 0.005;`
- `B += 0.005;`
- `usleep(1000);` (1 ms; `<unistd.h>` is included — am09_591s.png line 4)
- `C` is declared (`float A, B, C;`) but no increment of `C` is visible in any frame.

**Terminal reset (seen):**
- Once before the loop: `printf("\x1b[2J");` — clear screen (am06_404s.png line 20; am16 line 56).
- Every frame: `memset(buffer, backgroundASCIICode, width * height);` and `memset(zBuffer, 0, width * height * 4);` (am08_529s.png lines 30-31), then after rasterising, `printf("\x1b[H");` — cursor home (am12_777s.png line 66; am16 line 69), then `for (int k = 0; k < width * height; k++) putchar(k % width ? buffer[k] : 10);` (am16 lines 70-72), which prints the buffer with a newline (ASCII 10) every `width` characters, overwriting the previous frame in place.

## 8. Editor and development setup

**Seen:**
- Editor: Vim/Neovim in a terminal — mode indicator `INSERT` / `NORMAL`, `-- INSERT --`, `"cube.c" 23L, 575B written` (am06), `"cube.c" 77L, 1951B written` (am15), file tab `cube.c+`, a `buffers` label top-right (am02 onward). A completion popup labelled `[LS]` (am08_529s.png line 30) and a status `INSERT COMPL GENERIC`.
- Language tooling: **clangd** LSP — status line `clangd: file is queued` (am03_217s.png, am11_715s.png); hover signature `cos(double) -> double` (am04_280s.png); `putchar(int) -> int` signature help (am12_777s.png); warning gutter marks.
- Run: the program is run as `./a.out` — a terminal tab bar shows two tabs, `vim` and `./a.out` (am13_840s.png, am15_964s.png, am16, am18, am19). The compile command itself is **never visible** (insufficient evidence); `a.out` as the output name is consistent with a bare `cc cube.c -lm` / `gcc`/`clang` invocation (inferred).
- Browser: Google Chrome with DevTools (Elements panel) open on Symbolab (am01, am14).
- OS: macOS — inferred from the Chrome window chrome, the floating screenshot-markup toolbar (macOS Screenshot/Preview markup with "Done" button), and `usleep`/`unistd.h` working as-is; not confirmed by any explicit label.
- Not determinable: which Vim distribution/plugins (the status line and tabline look like a themed plugin setup — e.g. lightline/airline-style), whether the tabs are a terminal app or tmux, the terminal emulator name.

---

Frames examined: all 20 (am00_31s.png through am19_1213s.png), each opened once at native size, no crops or zooms produced. Transcript read once.

I modified no other file; the only file written is this answers.md.
