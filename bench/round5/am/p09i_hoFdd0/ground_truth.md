# Ground truth — p09i_hoFdd0 (ASMR-style "spinning ASCII cube in C" screen-capture video, ~20:40)

**Transcript contents overall:** effectively empty / unreliable. The whole transcript is four auto-caption fragments: "[16:49] you", "[19:34] uh", "[20:28] [Applause]", "[20:44] you". There is no spoken explanation; every substantive fact in this video is on screen only (vim editing a file `cube.c`, a terminal running `./a.out`, browser tabs with Wikipedia "Rotation matrix" and Symbolab's matrix-multiply calculator, and a handwriting/notes overlay with derived formulas). All eight answers are therefore label V.

## Q1
**Label: V**
**Answer:** width = 160, height = 44. He declares `float zBuffer[160 * 44];` and `char buffer[160 * 44];` (a depth buffer and a character/output buffer of the same size). Also `int backgroundASCIICode = ' ';` for empty cells.
**Evidence:** g_00425s.png lines 6–10 (`float cubeWidth = 10; int width = 160, height = 44; float zBuffer[160 * 44]; char buffer[160 * 44];`), also visible in g_00605s.png and g_01205s.png.
**Key terms:** "160", "44", "zBuffer", "buffer", "char buffer[160 * 44]"
**Partial:** gives 160×44 but misses one of the two buffers, or names the buffers without the dimensions.

## Q2
**Label: V**
**Answer:** `cubeWidth = 10` (half-width; faces sampled from -cubeWidth to +cubeWidth), `distanceFromCam = 60`, `K1 = 40`, `incrementSpeed = 0.6` (the cubeX/cubeY sampling step).
**Evidence:** g_01205s.png lines 7–15 show all four: `float cubeWidth = 10;`, `int distanceFromCam = 60;`, `float K1 = 40;`, `float incrementSpeed = 0.6;`. distanceFromCam and incrementSpeed also on g_00605s.png; incrementSpeed used in the for-loops in g_00485s.png.
**Key terms:** "cubeWidth = 10", "distanceFromCam = 60", "K1 = 40", "incrementSpeed = 0.6"
**Partial:** three of the four values correct; or correct values but confuses which constant is which.

## Q3
**Label: V**
**Answer:** He opens the Wikipedia article "Rotation matrix" (tab visible) and copies the three basic rotation matrices Rx(θ), Ry(θ), Rz(θ), then uses Symbolab's matrix-multiply calculator (symbolab.com/solver/matrix-multiply-calculator) to multiply the row vector (i j k) by the matrices in the order Rx(A) · Ry(B) · Rz(C) (x-rotation first, with angle A, then y with B, then z with C). The resulting symbolic expressions are pasted into a notes/annotation overlay and transcribed by hand into `calculateX`, `calculateY`, `calculateZ` in cube.c. He also re-uses Symbolab later with specific angles (e.g. -90°, 180°) to work out the per-face coordinate swaps.
**Evidence:** g_00045s.png (Wikipedia "Rotation matrix" tab + Symbolab with (i j k) entered; notes overlay listing Rx, Ry, Rz matrices); g_00105s.png ((i j k) times the three matrices, A then B then C); g_00155s.png (derived jsin(A)sin(B)cos(C)−kcos(A)sin(B)cos(C)... expressions in overlay while typing calculateX); g_00875s.png, g_01115s.png, g_01165s.png (Symbolab with cos(-90), cos(180) to derive face orientations, results like (z y −x), (−x y −z)).
**Key terms:** "Rotation matrix" (Wikipedia), "Symbolab", "matrix-multiply-calculator", "(i j k)", "Rx(A) Ry(B) Rz(C)"
**Partial:** names Symbolab or Wikipedia but not the multiplication order; or gives the order without the tools.

## Q4
**Label: V**
**Answer:** Six faces, six characters:
- `calculateForSurface(cubeX, cubeY, -cubeWidth, '.')` — '.'
- `calculateForSurface(cubeWidth, cubeY, cubeX, '$')` — '$'
- `calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')` — '~'
- `calculateForSurface(-cubeX, cubeY, cubeWidth, '#')` — '#'
- `calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')` — ';'
- `calculateForSurface(cubeX, cubeWidth, cubeY, '+')` — '+'
(The very first version used '#' for the single test face, g_00545s/g_00785s, before the six-face version.)
**Evidence:** g_01185s.png lines 63–68 (all six calls); g_01145s.png (first five plus one being typed); renders confirm the characters: g_01195s.png and g_01215s.png show '.', '~', '$', '#', ';', '+' regions; g_01235s.png shows '#', '$', '+'.
**Key terms:** "'.'", "'$'", "'~'", "'#'", "';'", "'+'", "calculateForSurface"
**Partial:** at least four of the six characters correct; full credit needs all six (order/face pairing not required, just the set of six characters).

## Q5
**Label: V**
**Answer:** A z-buffer with reciprocal depth. For each sampled surface point: `ooz = 1 / z;` compute `idx = xp + yp * width;` then `if (idx >= 0 && idx < width * height) { if (ooz > zBuffer[idx]) { zBuffer[idx] = ooz; buffer[idx] = ch; } }` — i.e. it stores 1/z per cell and the face character only replaces the cell when its 1/z is larger (point is closer to the camera). zBuffer is reset to 0 each frame via `memset(zBuffer, 0, width * height * 4);` and buffer to the background character via `memset(buffer, backgroundASCIICode, width * height);`.
**Evidence:** g_00755s.png lines 46–51 (the exact if-logic), g_00695s.png (ooz = 1/z, idx = xp + yp * width), g_00455s.png lines 30–31 (both memsets).
**Key terms:** "ooz", "1/z", "zBuffer[idx]", "ooz > zBuffer[idx]", "buffer[idx] = ch", "memset"
**Partial:** describes "z-buffer, closer wins" without the 1/z reciprocal comparison or without the bounds check/reset.

## Q6
**Label: V**
**Answer:** `xp = (int)(width / 2 + K1 * ooz * x * 2);` and `yp = (int)(height / 2 + K1 * ooz * y);` — perspective projection by multiplying by K1 and 1/z (ooz), centered at width/2, height/2. The x term carries an extra factor of 2 because terminal characters are roughly twice as tall as they are wide, so x must be stretched horizontally to make the cube look square. (Near the end, ~g_01225s, he edits the xp centering to `width / 2 - 2 * cubeWidth + ...` to shift the cube.)
**Evidence:** g_00695s.png lines 43–44 (both formulas with the * 2 on x only), g_00665s.png (typing them), g_01225s.png (offset edit in progress).
**Key terms:** "xp = (int)(width / 2 + K1 * ooz * x * 2)", "yp = (int)(height / 2 + K1 * ooz * y)", "* 2", "aspect"
**Partial:** correct formulas without the aspect-ratio reason, or the reason with an imprecise formula.

## Q7
**Label: V**
**Answer:** After drawing each frame: `A += 0.005; B += 0.005;` (rotation angles about x and y; C stays unused at 0) and `usleep(1000);` between frames. Terminal handling: `printf("\x1b[2J");` once before the loop (clear screen) and `printf("\x1b[H");` at the top of each frame (cursor home), then the buffer is printed with `putchar(k % width ? buffer[k] : 10);` (newline, ASCII 10, at each row boundary).
**Evidence:** g_00785s.png (A += 0.005, \x1b[2J, \x1b[H, putchar line), g_00905s.png / g_00965s.png lines 72–74 (A += 0.005; B += 0.005; usleep(1000)).
**Key terms:** "A += 0.005", "B += 0.005", "usleep(1000)", "\x1b[2J", "\x1b[H", "putchar(k % width ? buffer[k] : 10)"
**Partial:** gets the 0.005 increments or the escape codes but not both; mentions usleep without the 1000 value.

## Q8
**Label: V**
**Answer:** He codes in vim (mode line shows NORMAL/INSERT/COMMAND, ":w", "cube.c[+]", a "buffers" indicator top right), with the clangd language server providing completions/diagnostics (status line shows "clangd: file is queued"; LSP completion popups marked [LS]; an "undeclared identifier ... did you mean 'cubeX'?" clang diagnostic appears). The file is created in a terminal in a folder named `spinning_cube` with `touch cube.c`, and the program is run as `./a.out` in a second terminal pane (title ".../a.out"); the fancy backlit mechanical keyboard is shown on camera throughout (ASMR-style, no narration).
**Evidence:** g_00005s.png (`spinning_cube` prompt, `touch cube.c`), g_00425s.png ("clangd: file is queued", INSERT mode), g_00545s.png ([LS] completion popup), g_01145s.png (clang "undeclared identifier 'obeX'... did you mean 'cubeX'" style diagnostic), g_00815s.png / g_01195s.png (right pane titled ./a.out showing the running cube), g_00965s.png ("cube.c" 77L, 1951B written — vim write message).
**Key terms:** "vim", "clangd", "touch cube.c", "spinning_cube", "./a.out", "a.out"
**Partial:** identifies vim and running via ./a.out but misses clangd/LSP, or vice versa.
