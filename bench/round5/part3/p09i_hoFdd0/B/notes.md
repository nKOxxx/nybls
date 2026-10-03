# notes — p09i_hoFdd0 "ASMR Programming - Spinning Cube - No Talking"

Mode: answer mode for a specific deliverable (reconstruct final cube.c). No speech:
captions are 4 filler tokens ("you", "uh", "[Applause]"), so the transcript carried
nothing and the whole budget went to frames. Round 0 gave only the description's
chapter list (00:00 creating cube.c ... 19:39 Completed), used to place requests.

## What the evidence determines

Every line of program.c was read off a full-resolution frame of the vim buffer,
except as listed under "chosen, not seen". Key frames:
- [10:05] lines 1-43: includes, A/B/C, cubeWidth=10, width=160/height=44, zBuffer,
  buffer, backgroundASCIICode=' ', distanceFromCam=60, incrementSpeed=0.6,
  calculateX/Y/Z formulas, start of calculateForSurface.
- [11:10] line 13 `float K1 = 40;`, lines 17-19 `float x, y, z; float ooz; int xp, yp;`.
- [11:35]/[11:50] calculateForSurface body: z + distanceFromCam, ooz = 1/z,
  xp = (int)(width/2 + K1*ooz*x*2), yp = (int)(height/2 + K1*ooz*y), idx, bounds and
  z-buffer test.
- [13:25] main: \x1b[2J, memsets, loops, \x1b[H, putchar(k % width ? buffer[k] : 10),
  A += 0.005, B += 0.005.
- [19:30] lines 44-80 of the final layout: five surface calls ('.', '$', '~', '#', ';'),
  usleep(1000), status line "cube.c" 80L, 2133B/2140B written.
- [19:45] line 68 added: `calculateForSurface(cubeX, cubeWidth, cubeY, '?');` — 81 lines.

## Chosen, not seen (plain choices)

1. Sixth surface character. At [19:45] the cursor sat on the literal; the zoom showed
   something like '-' under the cursor, ambiguous. The runs at [20:15] and [20:43] render
   that face with '+' characters, so '+' is used. The alternative '-' never appears in
   any output frame.
2. `int idx;` placement. idx is used unqualified in calculateForSurface and the final
   layout has one more line above line 44 than the [11:20] layout, so a one-line global
   was added somewhere in lines 1-20. I put `int idx;` after `int xp, yp;`. Only the
   position is a guess; the name/type follow from usage.
3. Lines 1-20 after [11:10] were never on screen again. I assume no later edit to the
   globals. Cross-check: vim reported the 80-line version as 2140 B; my file minus line
   68 is 2131 B (9 bytes off, consistent with whitespace differences such as
   `1/z` vs `1 / z` or trailing spaces, not a missing statement).
4. Whitespace/indentation normalised to 2 spaces as seen; exact column alignment of the
   wrapped `return` lines is approximate.
5. Compiled clean with `cc -Wall program.c -lm`. Not run to completion (infinite loop).

## Evidence strip

- [00:11-03:07] sheet 0-7 min: empty cube.c; Wikipedia rotation-matrix pages; symbolab matrix product; calculateX typed.
- [07:35-13:25] sheet 7-14 min: calculateX/Y/Z; main loop skeleton; globals; calculateForSurface; print loop; A/B increments.
- [09:25-19:17] sheet 14-20.7 min: main with one surface; Wikipedia/symbolab lookups for other faces; code with 5 faces.
- [19:34] frame: zoomed vim, six surface call lines (line 68 still a duplicate of 67).
- [19:55] frame: ./a.out output, faces in . $ ~ # ; + chars.
- [20:15] frame: output, '+' face visible.
- [20:43] frame: output, '+' edge visible.
- [09:25] frame: lines 1-43 (calculateX/Y/Z, globals, calculateForSurface signature).
- [12:15] frame: lines 44-68 (idx/zBuffer block, main).
- [13:25] frame: lines 44-75 (print loop, A/B += 0.005).
- [19:03] frame: lines 44-80, five surfaces, usleep(1000), "80L, 2140B written".
- [19:17] frame: symbolab Ry(90) page (no code).
- [19:30] frame: lines 44-80 final-minus-one, "80L, 2133B written".
- [11:35] frame: lines 27-63, calculateForSurface body through idx.
- [11:50] frame: lines 27-65, bounds check being typed.
- [19:45] frame: lines 44-81 with line 68 added (literal under cursor).
- [19:34] zoom: six argument lists, sixth literal still ';' (pre-edit).
- [11:20] frame: lines 17-59, x/y/z/ooz/xp/yp globals, body.
- [14:20] frame: symbolab Ry(theta) (no code).
- [15:00] frame: symbolab Ry(90) result (-z y x) (no code).
- [19:45] zoom: line 68 literal, ambiguous under cursor.
- [10:40] frame: lines 20-57, xp being typed.
- [10:55] frame: lines 20-58, yp being typed.
- [13:50] frame: first-run output ('#' face), gcc cube.c retyped.
- [10:05] frame: lines 1-43, globals incl. distanceFromCam = 60.
- [10:20] frame: lines 12-54, float ooz added.
- [10:32] frame: lines 1-43, int xp, yp added.
- [19:50] frame: second-run output.
- [11:05] frame: line 13 'fl' with completion popup (K1 being typed).
- [11:10] frame: line 13 float K1 = 40.

## Ledger

watched 21 min · examined 51 images (~81,857 visual tokens, ≈$0.16 at sonnet-5 input rate) of ~31,119 total frames · budget 51/83 units
