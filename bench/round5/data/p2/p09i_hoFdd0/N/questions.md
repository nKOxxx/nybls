Answer all eight. State your answer and the evidence (timestamps and/or frame filenames). If your evidence does not determine an answer, say "insufficient evidence" rather than guessing. A confident wrong answer scores worse than an honest gap.

1. I want to reproduce this in my own terminal. What screen/buffer dimensions does the programmer set for the ASCII display, and what are the two buffers he declares at that size?

2. What values does he give the main tunable constants of the renderer — the cube's half-width, the distance from the camera, the projection constant K1, and the sampling step used when looping over each face?

3. He doesn't derive the 3D rotation math by hand. What resources/tools does he use to get the rotation formulas, and in what order are the three rotation matrices multiplied with the point?

4. The finished cube draws each of its six faces with a different ASCII character. Which characters does he use for the six calculateForSurface calls?

5. How does the code decide which character "wins" a screen cell when two faces project to the same spot — what exactly is stored and compared per cell?

6. How does he project a rotated 3D point to a terminal character cell — what are the exact expressions for xp and yp, and why is one axis scaled differently from the other?

7. What makes the animation actually spin and how fast: which angle variables are incremented each frame, by how much, and what delay is inserted between frames? Also, how is the terminal cleared/reset so frames overwrite each other?

8. What editor and development setup is he coding in (editor, any language tooling visible, how the program is created and run from the terminal)?
