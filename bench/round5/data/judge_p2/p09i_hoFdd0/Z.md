# Answers — p09i_hoFdd0 ("ASMR Programming - Spinning Cube - No Talking", 20:45)

Round 0: transcript is 4 tokens of noise ("you", "uh", "[Applause]") — no speech. Every answer below rests on frames; nothing comes from the transcript.

## 1. Screen dimensions and the two buffers

`int width = 160, height = 44;` and the two buffers declared at that size are
`float zBuffer[160 * 44];` and `char buffer[160 * 44];` (cube.c lines 8–10). Background fill is `int backgroundASCIICode = ' ';` (line 11).

Evidence: f_670000_1568.png [11:10] lines 8–11; same lines visible in f_660000_1568.png [11:00].

## 2. Main tunable constants

- Cube half-width: `float cubeWidth = 10;` (line 7)
- Distance from camera: `int distanceFromCam = 60;` (line 12)
- Projection constant: `float K1 = 40;` (line 13 — added at [11:10] right after the editor flagged K1 undefined at [11:00])
- Sampling step over each face: `float incrementSpeed = 0.6;` (line 15), used as `cubeX += incrementSpeed` / `cubeY += incrementSpeed` in the two nested for-loops.

Evidence: f_670000_1568.png [11:10] lines 7–15; f_660000_1568.png [11:00] (K1 still underlined/undefined at lines 41–42). Caveat: I did not re-read lines 1–15 at the very end of the video; the final main loop at [19:30]/[19:45] still references these same names, and the compiled output looks consistent with a ~10-unit cube, but a late edit to a value cannot be excluded.

## 3. Rotation math resources and multiplication order

He does not derive it. He opens the Wikipedia "Rotation matrix" article ("In three dimensions → Basic rotations", showing Rx, Ry, Rz) and Google-searches "symbolab matrix", then uses Symbolab's Matrix Multiply calculator to multiply the matrices symbolically, screenshotting the Wikipedia matrices in a floating macOS screenshot/markup window while typing them in. Symbolab's expanded result is then transcribed into `calculateX/Y/Z`.

Order: a row vector times the three matrices, left to right **(i j k) · Rx(A) · Ry(B) · Rz(C)**, i.e. X-rotation by A first, then Y by B, then Z by C. The resulting code uses exactly those angle names (`float A, B, C;`, line 5) in `calculateX/Y/Z` (lines 21–33).

Evidence: sheet_000.png tiles [00:26],[00:31] (Wikipedia rotation matrix page), [00:36] (Google "symbolab matrix"), [03:07] (Symbolab result expression); f_64349_1568.png [01:04] (entering `(i j k)` × Rx(A) × second matrix starting `cos(B)`); f_120000_1568.png [02:00] (full product `(i j k)·Rx(A)·Ry(B)·Rz(C)` typed in Symbolab); f_670000_1568.png [11:10] lines 21–33 for the transcribed formulas. He later returns to Symbolab/Wikipedia at [14:11]–[15:32] and [18:37]–[19:17] to work out the face orientations (e.g. `(x y z)·Ry(90°) = (−z y x)`), see sheets 003/005.

## 4. Characters for the six calculateForSurface calls

Final main loop (lines 63–68 at [19:45]):

```
calculateForSurface(cubeX, cubeY, -cubeWidth, '.');
calculateForSurface(cubeWidth, cubeY, cubeX, '$');
calculateForSurface(-cubeWidth, cubeY, -cubeX, '~');
calculateForSurface(-cubeX, cubeY, cubeWidth, '#');
calculateForSurface(cubeX, -cubeWidth, -cubeY, ';');
calculateForSurface(cubeX, cubeWidth, cubeY, '+');
```

So the six characters are `.`, `$`, `~`, `#`, `;`, `+`. At [19:30] only the first five existed; the sixth (`'+'`) was added just before [19:45], and the `+` face is visible in the running output at [20:00] and [20:30].

Evidence: f_1185000_1568.png [19:45] lines 63–68; f_1170000_1568.png [19:30] (five calls); f_1200000_1568.png [20:00] and f_1230000_1568.png [20:30] (output containing `.`, `$`, `~`, `#`, `;`, `+`).

## 5. Which character wins a cell

A per-cell z-buffer of inverse depth. In `calculateForSurface`: `ooz = 1/z;` (z already has `distanceFromCam` added), `idx = xp + yp * width;`, then

```
if (idx >= 0 && idx < width * height) {
  if (ooz > zBuffer[idx]) {
    zBuffer[idx] = ooz;
    buffer[idx] = ch;
  }
}
```

So what is stored per cell is the float `ooz` (1/z) in `zBuffer[idx]` and the char in `buffer[idx]`; a new sample wins only if its 1/z is larger (it is closer to the camera). Each frame starts with `memset(zBuffer, 0, width * height * 4)` so any positive 1/z beats the empty cell, and `memset(buffer, backgroundASCIICode, width * height)`.

Evidence: f_1170000_1568.png [19:30] lines 46–53 and 58–59; f_700000_1568.png [11:40] (writing the `if (idx >= 0 && id…` line).

## 6. Projection to a terminal cell

```
xp = (int)(width/2 + K1 * ooz * x * 2);
yp = (int)(height/2 + K1 * ooz * y);
```

(lines 42–43 at [11:10]; still identical at [19:30], where `yp = (int)(height / 2 + K1 * ooz * y);` is line 44). Perspective: multiply by `K1 * ooz` (K1/z), offset to screen centre. The x axis carries an extra `* 2` because terminal character cells are roughly twice as tall as they are wide, so horizontal coordinates must be stretched ~2x to keep the cube's aspect square on screen. No on-screen comment states this reason; it is the standard justification and the only one consistent with the code (inference, not something he says or writes).

Evidence: f_670000_1568.png [11:10] lines 40–43; f_1170000_1568.png [19:30] line 44.

## 7. Spin, speed, delay and terminal reset

- Per frame, after the draw loop: `A += 0.005;` and `B += 0.005;` (C is declared but never incremented, so rotation is about X and Y only).
- Delay: `usleep(1000);` (1 ms) at the end of each `while (1)` iteration.
- Terminal: once before the loop, `printf("\x1b[2J");` (clear screen); each frame, `printf("\x1b[H");` (cursor home) then the buffer is emitted with `for (int k = 0; k < width * height; k++) putchar(k % width ? buffer[k] : 10);` — a newline (10) at every row start — so each frame overwrites the previous one in place.

Evidence: f_1185000_1568.png [19:45] lines 56, 71–78; f_1170000_1568.png [19:30] lines 56, 70–77.

## 8. Editor and dev setup

- Editor: **Vim** in a terminal (terminal tab titled "vim"; Vim modes `-- INSERT --`, `NORMAL`, `COMMAND` with `:w` shown; `cube.c[+]` buffer indicator; `~` tilde lines). A powerline-style statusline (airline/lightline-like) plus a top buffer-tab bar ("cube.c+", "buffers").
- Language tooling: a C language server is attached — the statusline shows `clangd: file is queued` and the completion popup lists items tagged `[LS]` (language-server source) and `[A]` (around/buffer), e.g. `putc_unlocked … From <stdio.h>` at [12:50]. Diagnostics appear as `>>` gutter marks and underlines (undefined `K1` at [11:00]). Mode `INSERT COMPL GENERIC` is visible at [11:40]. Which plugin provides this (vim-lsp/coc/ALE etc.) is not identifiable on screen — insufficient evidence beyond "clangd via a Vim LSP/completion plugin".
- Terminal: macOS terminal emulator with two tabs ("vim" and "./a.out" / "../spinning_cube"); shell prompt `➜ spinning_cube` (zsh/oh-my-zsh robbyrussell-style arrow prompt), working directory `spinning_cube`. The file is edited as `cube.c` (empty buffer at [00:08]; the exact `vim cube.c` invocation is not on screen — insufficient evidence for the literal command).
- Build/run: `gcc cube.c` then `./a.out` (tab title "./a.out"; `^C` to stop before recompiling), seen at [20:30] and [19:00].
- Side tools: Chrome with Wikipedia "Rotation matrix" and Symbolab matrix-multiply tabs, DevTools Elements panel open (he deletes ad/popup nodes), macOS screenshot markup overlay for the matrices.

Evidence: f_8000_1568.png [00:08]; f_700000_1568.png [11:40]; sheet_004.png [12:50]; f_1170000_1568.png [19:30]; f_1185000_1568.png [19:45]; f_1140000_1568.png [19:00]; f_1230000_1568.png [20:30]; f_120000_1568.png [02:00].

---

## Evidence strip (every image opened)

- sheet_000.png [00:11, 00:26, 00:31, 00:36, 01:04, 03:07] — empty main(); Wikipedia Rotation matrix; Google "symbolab matrix"; Symbolab entry; Symbolab expanded result
- sheet_001.png [07:35, 08:45, 09:55, 11:05, 12:15, 13:25] — calculateX/Y/Z typed; main loop growing; completion popup; z-buffer code; A/B increments + usleep
- sheet_002.png [09:25, 14:16, 15:32, 17:52, 18:12, 19:17] — top of file; Wikipedia cube permutation figure; Symbolab "(−z y x)"; Google "surface matrix 3d"; Wikipedia again; Symbolab Ry(90°)
- f_1100000_1568.png [18:20] — Symbolab (x y z)·Ry(180) with DevTools open
- f_1140000_1568.png [19:00] — running cube, `^C`, prompt `➜ spinning_cube`
- f_1170000_1568.png [19:30] — cube.c lines 44–80, five calculateForSurface calls, main loop
- f_1200000_1568.png [20:00] — running cube with `.`, `$`, `~`, `#`, `;`, `+`
- f_1230000_1568.png [20:30] — running cube; `gcc cube.c` in shell
- f_1243000_1568.png [20:43] — running cube (end)
- f_64349_1568.png [01:04] — Symbolab: (i j k)·Rx(A)·[cos(B)…]; Wikipedia Rx/Ry/Rz screenshot
- f_660000_1568.png [11:00] — cube.c lines 1–43, K1 undefined, constants
- f_700000_1568.png [11:40] — calculateForSurface body, completion popup `[LS]`, `clangd: file is queued`
- f_1185000_1568.png [19:45] — final main, six calls incl. `'+'`, `:w`
- f_1195000_1568.png [19:55] — running cube
- f_8000_1568.png [00:08] — empty cube.c buffer in Vim, INSERT mode
- f_120000_1568.png [02:00] — Symbolab full product (i j k)·Rx(A)·Ry(B)·Rz(C)
- sheet_003.png [09:25, 14:11, 14:15, 14:40, 15:04, 15:32] — top of file; Wikipedia; Ry screenshot; Symbolab (−z y x)
- sheet_004.png [11:10, 11:30, 11:50, 12:10, 12:30, 12:50] — K1 line added; z-buffer code; putchar completion with clangd
- sheet_005.png [16:27, 17:52, 18:06, 18:37, 19:17, 19:34] — running cube; Google; Symbolab/Wikipedia; main with five calls
- f_670000_1568.png [11:10] — `float K1 = 40;` and all constants, lines 1–43

## Ledger
