# Answers

## Preliminary note on the evidence

The transcript (`transcript.txt`) contains four lines only:

```
[16:49] you
[19:34] uh
[20:28] [Applause]
[20:44] you
```

There is no speech content at all. The video is ~21 minutes long and evidently has no (or near-no) narration; it is a screen-recorded coding session whose content is carried entirely by the frames. Nothing in the transcript identifies the video, the code, the editor, or any numeric value. Every question below is a *visual* question (code on screen), and the transcript cannot answer any of them.

**General-knowledge caveat.** The question set (ASCII cube, `calculateForSurface`, K1, zBuffer, three rotation angles, six faces with different characters) matches the well-known "3D ASCII cube in the terminal in C" video by Servet Gulnaroglu. I cannot confirm from the transcript that this is that video, and even if it is, the values typed on screen during the video can differ from the final repository version. So for each question I give: (a) the transcript-based answer, which is "insufficient evidence", and (b) a clearly labelled *unverified general-knowledge candidate* recalled from memory of that `cube.c`, which should be treated as a hypothesis, not as an answer grounded in this video.

---

### 1. Screen/buffer dimensions and the two buffers

**Answer (from evidence): insufficient evidence.** The transcript contains no code or numbers.

*Unverified general-knowledge candidate (Gulnaroglu `cube.c`, from memory):* `int width = 160; int height = 44;` with `float zBuffer[160 * 44];` and `char buffer[160 * 44];`. Also a `backgroundASCIICode = ' '`. In the video he may have started with other dimensions (e.g. 80x22) before changing them; not determinable here.

### 2. Tunable constants (half-width, camera distance, K1, sampling step)

**Answer (from evidence): insufficient evidence.**

*Unverified general-knowledge candidate:* `cubeWidth = 20` (half-width, faces loop from `-cubeWidth` to `cubeWidth`), `distanceFromCam = 100`, `K1 = 40`, `incrementSpeed = 0.6` (the step for `cubeX`/`cubeY` in the face loops). I recall a tweak between video and repo (K1 and the increment were adjusted), so these may not match what appears on screen.

### 3. Source of the rotation formulas and multiplication order

**Answer (from evidence): insufficient evidence.** No speech to indicate what resource he consults.

*Unverified general-knowledge candidate:* He looks up the 3D rotation matrices (Wikipedia "Rotation matrix" and/or a symbolic tool such as Wolfram Alpha / a matrix calculator) and expands the product Rz(C) * Ry(B) * Rx(A) * [i, j, k] by letting the tool multiply the matrices, then transcribes the expanded expressions into `calculateX/Y/Z`. I am not certain of the exact tool shown on screen or the order (which matrix is applied first); the expanded `calculateX` in the repo is `j*sin(A)*sin(B)*cos(C) - k*cos(A)*sin(B)*cos(C) + j*cos(A)*sin(C) + k*sin(A)*sin(C) + i*cos(B)*cos(C)`, which is consistent with rotating about x by A, then y by B, then z by C.

### 4. The six face characters

**Answer (from evidence): insufficient evidence.**

*Unverified general-knowledge candidate (repo order):* `'@'`, `'$'`, `'~'`, `'#'`, `';'`, `'+'` for the calls `calculateForSurface(cubeX, cubeY, -cubeWidth, '@')`, `(cubeWidth, cubeY, cubeX, '$')`, `(-cubeWidth, cubeY, -cubeX, '~')`, `(-cubeX, cubeY, cubeWidth, '#')`, `(cubeX, -cubeWidth, -cubeY, ';')`, `(cubeX, cubeWidth, cubeY, '+')`. The video may use a different set/order from the final repository.

### 5. Depth test per screen cell

**Answer (from evidence): insufficient evidence.**

*Unverified general-knowledge candidate:* A z-buffer storing the reciprocal depth `ooz = 1 / z` per cell (`float zBuffer[]`), initialized to 0 each frame. For each sampled point: `if (ooz > zBuffer[idx]) { zBuffer[idx] = ooz; buffer[idx] = ch; }` — larger 1/z means closer to the camera, so the nearer face overwrites the cell's character.

### 6. Projection expressions and the axis scaling

**Answer (from evidence): insufficient evidence.**

*Unverified general-knowledge candidate:* `xp = (int)(width / 2 + horizontalOffset + K1 * ooz * x * 2); yp = (int)(height / 2 + K1 * ooz * y);` with `z = calculateZ(...) + distanceFromCam`. The x term is multiplied by 2 because terminal character cells are roughly twice as tall as they are wide, so without the factor the cube appears horizontally squashed.

### 7. Spin speed, frame delay, terminal clearing

**Answer (from evidence): insufficient evidence.**

*Unverified general-knowledge candidate:* Per frame `A += 0.05; B += 0.05; C += 0.01;` (the exact increments vary between versions), `usleep(8000 * 2)` (or `usleep(8000)`) between frames, and the terminal is cleared with ANSI escapes: `printf("\x1b[2J")` once at start and `printf("\x1b[H")` (cursor home) each frame before the buffer is printed with `putchar`.

### 8. Editor and development setup

**Answer (from evidence): insufficient evidence.** The transcript shows nothing about the environment.

*Unverified general-knowledge candidate:* A macOS terminal with a Vim/Neovim-style setup (I recall a terminal-based editor with a status line rather than a GUI IDE), creating `cube.c` from the shell and compiling/running with `gcc cube.c -o cube && ./cube` (or `cc cube.c -lm`). I have low confidence in the editor specifics for this particular video.

---

## Summary of what is and is not grounded

- **Transcript says:** nothing usable (four filler tokens and an applause tag).
- **Inferred:** the video is likely a silent screen-recorded coding session of a C ASCII cube; the candidate values above come from my memory of a specific public `cube.c` and are not verified against this video. Score every question as "insufficient evidence" from the permitted evidence; the candidates are offered only as labelled hypotheses.
