# notes.md — p09i_hoFdd0 (arm A: transcript + 30 uniform stills)

Transcript is empty of speech (4 lines: "you", "uh", "[Applause]", "you"), so
every line of program.c comes from reading the editor in the stills. The video
is a silent typing session: Vim, file `cube.c`, an ASCII spinning cube rendered
to the terminal with a z-buffer.

## What the stills determine (and which still)

- [145s]–[311s] calculateX / calculateY / calculateZ written from a Symbolab
  product of Rx(A)·Ry(B)·Rz(C) (formulas shown on screen; code matches them).
- [394s] globals: cubeWidth=10, width=160, height=44, zBuffer/buffer sizes.
- [435s]–[477s] backgroundASCIICode=' ', memset calls, `\x1b[2J`, outer loop.
- [601s] includes string.h and unistd.h, distanceFromCam=60, incrementSpeed=0.6,
  calculateForSurface signature, `calcuateZ` typo corrected to `calculateZ`
  by [643s].
- [684s]–[767s] ooz, xp, yp, idx, z-buffer test, `buffer[idx] = ch`.
- [809s] `\x1b[H`, putchar loop, A += 0.005, B += 0.005, usleep(1000).
- [933s]–[1182s] the six face calls, characters '.', '$', '~', '#', ';', ';'
  ([1182s] shows file saved: "cube.c" 81L, 2192B written).
- [1224s] last still: `xp = (int)(width / 2 - 2 + K1 * ooz * x * 2);` being
  typed in INSERT mode (cursor right after the `- 2`).

## Not determined by the evidence — my choices

1. **K1's value.** `K1` is used from [684s] on and a one-line declaration was
   inserted between `distanceFromCam` and `float x, y, z;` (line numbers shift
   by one between [601s] and [684s]), but no still ever scrolls to that line.
   I wrote `float K1 = 40;`. 40 is a plain choice that gives a sensibly sized
   cube at distanceFromCam=60; the video's actual value is unknown.
2. **The `- 2` in xp.** Visible only in the final still, mid-keystroke. It may
   have been completed differently or reverted after 1224s. Kept as seen.
3. **Sixth face character.** At [1182s] line 68 reads `';'` with the cursor
   sitting on it, same as line 67. The file had just been saved in that state,
   so I kept ';' for both; it is possible the author changed it after the
   save (the still shows the cursor parked there).
4. **First face character.** '#' at [643s]–[809s], changed to '.' by [933s].
   '.' is the later state and is what I used.
5. Whitespace/line breaks reproduce the Vim layout where visible; blank lines
   around the globals are approximated.

## Sanity

`cc program.c -lm` compiles (one warning-free build on clang; `usleep` needs
unistd.h which the video includes). Not run to completion — it is an infinite
loop by design.
