# Answers — p09i_hoFdd0 (no-video arm)


Caveat on own knowledge: the title is identical to a widely known video by a different channel (Servet Gulnaroglu, "ASMR Programming - Spinning Cube - No Talking", C, terminal). I do not know whether "Code Fiction" is a reupload, a re-creation, or an unrelated video with the same title. Anything below marked [own knowledge] describes that other video's code from memory and is UNVERIFIED for this video. The determinate answer in every case is "insufficient evidence".

1. **Insufficient evidence** (metadata has no code). [own knowledge, unverified for this video] In the Servet Gulnaroglu version: `width = 160`, `height = 44`, buffers `float zBuffer[160 * 44]` and `char buffer[160 * 44]`.

2. **Insufficient evidence**. [own knowledge, unverified] In that version: `cubeWidth = 20`, `distanceFromCam = 100`, `K1 = 40`, loop step `incrementSpeed = 0.6` over each face (cubeX, cubeY from -cubeWidth to cubeWidth).

3. **Insufficient evidence**. [own knowledge, unverified] In that version he copies the rotation formulas from the Wikipedia "Rotation matrix" article (general 3D rotation, yaw-pitch-roll) and uses the expanded per-axis expressions `calculateX/Y/Z` with angles A, B, C; the combined matrix is of the form Rz(C)·Ry(B)·Rx(A) applied to the point. I cannot confirm any of this for the Code Fiction video.

4. **Insufficient evidence**. [own knowledge, unverified] In that version the six `calculateForSurface` characters are `@`, `$`, `~`, `#`, `;`, `+`.

5. **Insufficient evidence**. [own knowledge, unverified] In that version: per cell, `ooz = 1/z` is stored in `zBuffer[idx]`; a new point writes only if `ooz > zBuffer[idx]` (closer to camera), then stores `ooz` and the face character in `buffer[idx]`.

6. **Insufficient evidence**. [own knowledge, unverified] In that version: `xp = (int)(width/2 + horizontalOffset + K1 * ooz * x * 2)`, `yp = (int)(height/2 + K1 * ooz * y)`; x is doubled because terminal character cells are roughly twice as tall as they are wide.

7. **Insufficient evidence**. [own knowledge, unverified] In that version: `A += 0.05; B += 0.05; C += 0.01;` per frame, `usleep(8000 * 2)` between frames, and the terminal is reset with `printf("\x1b[2J")` once at start and `printf("\x1b[H")` (cursor home) each frame so frames overwrite each other.

8. **Insufficient evidence** (nothing in metadata). [own knowledge, unverified] The Servet Gulnaroglu video is coded in Vim inside a terminal (tmux), file `cube.c`, compiled with `gcc`/`clang` and run from the shell. I have no information about Code Fiction's setup.
