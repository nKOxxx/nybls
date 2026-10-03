# Verdict — p09i_hoFdd0 (arm: AM)

| Q | Label | Score | Outcome | Rationale |
|---|---|---|---|---|
| 1 | V | 2 | correct | width 160, height 44, `float zBuffer[160*44]`, `char buffer[160*44]`, plus backgroundASCIICode. |
| 2 | V | 1 | partial | cubeWidth = 10 and incrementSpeed = 0.6 correct; distanceFromCam and K1 values honestly abstained. Two of four correct, nothing wrong. |
| 3 | V | 2 | correct | Wikipedia "Rotation matrix", Symbolab matrix-multiply calculator, and order (i j k)·Rx(A)·Ry(B)·Rz(C); also the later per-face permutation runs. |
| 4 | V | 1 | partial | Full set of six characters (. $ ~ # + ;) recovered from the rendered output but presented as inferred, with only three face/char pairs confirmed in code; AM itself labels the answer partial. |
| 5 | V | 2 | correct | ooz = 1/z, idx bounds check, `ooz > zBuffer[idx]` closer-wins, both memsets, correct reasoning on the reciprocal. |
| 6 | V | 2 | correct | Both projection formulas exact, including the ×2 on x; aspect-ratio reason given with an honest "not stated on screen" caveat (the video has no narration, so GT's reason is likewise inferred). |
| 7 | V | 2 | correct | A += 0.005, B += 0.005, usleep(1000), C unused, \x1b[2J before loop, \x1b[H per frame, putchar newline-at-row-boundary. |
| 8 | V | 2 | correct | Vim with clangd LSP ([LS] popups, "clangd: file is queued"), run as ./a.out in a second terminal tab, Chrome + Symbolab. Misses the `touch cube.c` / `spinning_cube` opening (no frame at 5 s in its pack) — minor omission, not a GT partial condition. |

**Total: 14 / 16**

## Ground truth concerns
- Q2: GT's partial definition is "three of the four values correct". AM gives two correct and abstains honestly on the other two. This fits neither "partial" (as defined) nor 0 ("wrong / insufficient evidence" for the whole item). Scored 1/partial as the closest fit; a stricter reading of the GT definition would give 0.
- Q4: GT says the set of six characters suffices for full credit regardless of pairing. AM does list exactly that set from the render frames but explicitly declines to assert it ("consistent with six faces (inferred)", "partial — insufficient evidence"). Scored as right-value-by-labelled-inference = 1.
- Q3: AM reports the face-permutation Symbolab runs as using Ry(90°); GT cites cos(-90) and cos(180). Different instances of the same activity; not scored.
- Q8: GT key terms include `touch cube.c` and `spinning_cube`, but its partial definition only concerns vim/clangd/a.out. AM's omission of the folder name was therefore not penalised.
