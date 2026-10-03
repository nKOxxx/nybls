# Notes — p09i_hoFdd0 (N arm: video.txt only)

Evidence available: title "ASMR Programming - Spinning Cube - No Talking",
channel "Code Fiction", duration 20:45. Nothing else (no transcript, no frames).

## What the evidence determines
- A spinning cube is built, live-coded with no narration. Nothing in the
  evidence fixes the language, library, or rendering target.

## Choices I made (NOT verified against the video)
- **Language / rendering:** C, terminal ASCII with a z-buffer and ANSI escapes.
  Chosen because the task asks for a single C file and because the best-known
  "ASMR Programming - Spinning Cube - No Talking" videos (Servet Gulnaroglu's
  2022 upload and its many imitations) use exactly this approach; ~20 minutes
  matches live-typing a ~130-line program. I have not confirmed that Code
  Fiction's video follows that template; it could equally be OpenGL/GLFW,
  SDL, raylib, or a non-C language entirely.
- **Three cubes** (sizes 20 / 10 / 5 with horizontal offsets) and face
  characters `@ $ ~ # ; +` — copied from the widely circulated template.
  The video may draw one cube, different sizes, or different glyphs.
- **Screen size 160x44, camera distance 100, K1 = 40, increment 0.6,
  rotation deltas A/B += 0.05, C += 0.01, usleep(16000)** — template defaults;
  any of these may differ.
- Rotation formulas are standard X-then-Y-then-Z Euler products; order and
  signs are a guess consistent with the template.
- Buffer sizes are fixed at compile time; no terminal-size detection added.

Nothing here should be read as "the video's version" beyond the fact that it
builds a spinning cube.
