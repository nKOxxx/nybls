# Answers — p09i_hoFdd0 (control arm: transcript + 30 uniform stills)

Note on evidence: the transcript is empty of content (four tokens: "you", "uh", "[Applause]", "you" at [16:49]–[20:44]); the video has no usable speech. Every answer below rests on the 30 stills only. "Seen" = legible on a frame; "Inferred" = my reasoning, not shown.

## 1. Screen/buffer dimensions and the two buffers

**Seen:** `int width = 160, height = 44;` then `float zBuffer[160 * 44];` and `char buffer[160 * 44];` (u09_394s.png lines 7–9, with `buffer[1` still being typed; completed form in u14_601s.png lines 8–10). The buffers are later cleared with `memset(buffer, backgroundASCIICode, width * height)` and `memset(zBuffer, 0, width * height * 4)` (u11_477s.png lines 30–31), where `int backgroundASCIICode = ' ';` (u10_435s.png line 10).

Evidence: u09_394s.png, u10_435s.png, u11_477s.png, u14_601s.png.

## 2. Tunable constants

**Seen:**
- `float cubeWidth = 10;` (u09_394s.png line 6; u14_601s.png line 7)
- `int distanceFromCam = 60;` (u14_601s.png line 12)
- `float incrementSpeed = 0.6;` (u14_601s.png line 14) — this is the `+=` step for both `cubeX` and `cubeY` loops (u15_643s.png lines 49–51)
- `K1`: **insufficient evidence.** `K1` is used in `xp`/`yp` (u16_684s.png lines 42–43) but its declaration never appears in any frame. u14_601s.png shows lines 1–16 with no K1; u16_684s.png shows lines 17–19 (`float x, y, z; float ooz; int xp, yp;`) and u29_1224s.png line 20 (`int idx;`). Between u14 and u15 two lines were inserted above `calculateX` (it moved from line 18 to line 20), so K1 is presumably declared there, but its value is never on screen.

## 3. Resources for the rotation math and multiplication order

**Seen:**
- Wikipedia "Rotation matrix", section "In three dimensions / Basic rotations", with Rx(θ), Ry(θ), Rz(θ) highlighted (u20_850s.png; tab also open in u01/u02/u25).
- Symbolab "Matrix Multiply, Power Calculator" (symbolab.com/solver/matrix-multiply-calculator) used to multiply the matrices symbolically and, later, to work out the face parameterisations with 90°/180° rotations about y (u01_62s.png, u02_103s.png, u21_892s.png, u24_1016s.png, u25_1058s.png).
- A macOS screenshot/markup preview window floating over the editor containing the Symbolab result expressions, which he copies into `calculateX/Y/Z` (u03–u07, u22–u24).
- Google omnibox autocomplete in u00_20s.png shows a Math StackExchange link "Rotation matrix if X Y Z…" as a history suggestion; whether he visited it in this video is not shown (inferred: possibly consulted earlier, not confirmed).

**Order (seen):** In Symbolab he enters a **row vector on the left** followed by the three matrices: `(i j k) · Rx(A) · Ry(B) · Rz(C)` — u02_103s.png shows `(i j k)` × [1 0 0; 0 cosA −sinA; 0 sinA cosA] × [cosB 0 sinB; 0 1 0; −sinB 0 cosB] × [cosC … ] (third matrix being typed). u01_62s.png shows the first two already placed. The resulting expressions (u03_145s.png preview) match the code:
- `calculateX = j*sin(A)*sin(B)*cos(C) − k*cos(A)*sin(B)*cos(C) + j*cos(A)*sin(C) + k*sin(A)*sin(C) + i*cos(B)*cos(C)`
- `calculateY = j*cos(A)*cos(C) + k*sin(A)*cos(C) − j*sin(A)*sin(B)*sin(C) + k*cos(A)*sin(B)*sin(C) − i*cos(B)*sin(C)`
- `calculateZ = k*cos(A)*cos(B) − j*sin(A)*cos(B) + i*sin(B)` (u08_352s.png lines 6–18).

## 4. Characters for the six calculateForSurface calls

**Seen** (u28_1182s.png lines 63–68, file saved "81L, 2192B written"):
1. `calculateForSurface(cubeX, cubeY, -cubeWidth, '.')` — note this was `'#'` in u18–u21 and changed to `'.'` by u22_933s.png.
2. `calculateForSurface(cubeWidth, cubeY, cubeX, '$')`
3. `calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')`
4. `calculateForSurface(-cubeX, cubeY, cubeWidth, '#')`
5. `calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')`
6. `calculateForSurface(cubeX, cubeWidth, cubeY, ';')` — the sixth literal reads as `';'` in u28 at this resolution (cursor sits just after it). It is small on screen and could plausibly be a different single character; I cannot distinguish with certainty without zooming, which this arm forbids. Treat the sixth as "looks like `;`, low confidence".

So: `.`, `$`, `~`, `#`, `;`, and (probably) `;`. Any change after u28 (video continues ~40 s to u29, which shows a different part of the file) is not visible.

## 5. Which character wins a cell

**Seen** (u17_726s.png lines 41–52; u18_767s.png lines 46–53):
```
ooz = 1/z;
xp = ...; yp = ...;
idx = xp + yp * width;
if (idx >= 0 && idx < width * height) {
  if (ooz > zBuffer[idx]) {
    zBuffer[idx] = ooz;
    buffer[idx] = ch;
  }
}
```
Per cell, `zBuffer[idx]` stores the **reciprocal depth `ooz = 1/z`** (a float) of whatever currently occupies that cell; a new sample overwrites both the depth and the character only if its `ooz` is **strictly greater** (i.e. the point is closer to the camera, since `z` includes `+ distanceFromCam`). `zBuffer` is reset to 0 each frame (`memset(zBuffer, 0, width*height*4)`) and `buffer` to spaces, so the first sample at a cell always wins against the background.

Evidence: u11_477s.png, u17_726s.png, u18_767s.png.

## 6. Projection to a character cell

**Seen** (u16_684s.png lines 40–43; u18_767s.png lines 41–44):
```
ooz = 1/z;
xp = (int)(width/2 + K1 * ooz * x * 2);
yp = (int)(height/2 + K1 * ooz * y);
```
At u29_1224s.png line 43 he is mid-edit, changing xp to `(int)(width / 2 - 2 + K1 * ooz * x * 2)` (cursor after the `- 2`); whether that edit was kept is not visible.

**Why x is scaled by 2 — inferred, not shown:** there is no narration and no on-screen comment. The standard reason, which I infer, is that terminal character cells are roughly twice as tall as they are wide, so doubling the horizontal projection keeps the cube from looking squashed. The `width/2`, `height/2` terms centre the projection.

## 7. What spins, how fast, delay, and terminal reset

**Seen** (u19_809s.png lines 71–73; u22_933s.png lines 72–74; u28_1182s.png lines 76–78):
- `A += 0.005;` and `B += 0.005;` each iteration of `while (1)`. `C` is declared (`float A, B, C;`) but never incremented in any frame.
- `usleep(1000);` (1 ms) between frames (u19 shows it being typed as `usleep(10|)`; final `usleep(1000)` from u22 on). `#include <unistd.h>` present (u14 line 4).
- Terminal reset: `printf("\x1b[2J");` once before the loop (clear screen), then each frame `printf("\x1b[H");` (cursor home) before writing the buffer with `for (int k = 0; k < width * height; k++) putchar(k % width ? buffer[k] : 10);` — i.e. a newline (ASCII 10) at every row boundary, so each frame overwrites the previous one in place.

Evidence: u08_352s.png (line 21 `\x1b[2J`), u18_767s.png, u19_809s.png, u22_933s.png, u28_1182s.png.

## 8. Editor and development setup

**Seen:**
- Terminal Vim/Neovim: modal statusline (`INSERT`, `NORMAL`, `INSERT COMPL GENERIC`), `-- INSERT --`, `cube.c[+]`, `~` filler lines, a "buffers" tab bar top-right, write messages like `"cube.c" 81L, 2192B written` (u03 onward). Statusline shows `SNIP` and `c | utf…` segments (u19, u14), indicating a statusline plugin.
- Language tooling: clangd LSP — statusline `clangd: file is queued` (u05, u07, u08), completion popups tagged `[LS]`, `[A]`, `[S]`, with signatures like `sin(double) -> double`, `calculateForSurface() -> int` (u06, u07, u12, u13, u16), and inline clang diagnostics (`-Wimplicit-function-declaration` for memset before `<string.h>` was added, u10). Inferred: an LSP completion client (looks like coc.nvim or nvim-cmp style, cannot tell which).
- Window layout: from u19 onward a top bar shows two panes/tabs named `vim` and `./a.out` / `a.out` and `.spinning_cube` (u19, u22, u23, u24, u29). Inferred: a tmux or terminal-emulator tab bar, with the program compiled to the default `a.out` and run as `./a.out` in the second pane. The actual compile command (e.g. `cc cube.c`/`gcc cube.c -lm`) is never on screen — insufficient evidence for the exact command; `a.out` naming is what is seen.
- Host OS inferred as macOS: Chrome with macOS-style tabs, a macOS screenshot/Preview markup toolbar ("Done", crop, markup icons) used to float the formulas over the editor (u01–u07, u21–u25). A mechanical keyboard with the author's hands is overlaid bottom-right in every frame.
- Browser: Chrome with Wikipedia and Symbolab tabs, DevTools open (u02, u21, u24, u25).

---

Frames examined: all 30 of the 30 stills in `~/.nybls/store/p09i_hoFdd0/oneshot/` (u00_20s.png through u29_1224s.png), plus `index.json` and `transcript.txt`. No image was cropped, zoomed, scaled or regenerated; no ffmpeg/nybls/yt-dlp/sips was run; the video file, `bench/`, and other store directories were not opened.

I modified no other file; the only file written is this `answers.md`.
