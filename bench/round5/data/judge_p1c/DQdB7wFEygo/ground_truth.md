## DQdB7wFEygo — Docker tutorial, 11:53, 293 cuts
1. **A code editor, dark theme** (VS Code style), with line numbers and syntax
   highlighting; tabs for index.js, .dockerignore, Dockerfile, Settings.
2. **Slide**: "Layer Caching For Dummies", blue text on white. ("for dummies": 0 hits)
3. **ENV PORT=9000**. ("9000": 0 hits — visual only)
4. **.dockerignore contains `node_modules`**. ("dockerignore", "node_modules": 0 hits)
5. **Explorer** shows DOCKER_EXAMPLE containing node_modules, src (with index.js)
   and Dockerfile.


# Ground truth errata (applies where it names this video)

# Ground-truth errata — round 3

**L24Wf0VlTE0 item 5 was RIGHT and the design note was WRONG.**
The design note rejected "310-620 mph" as spoken-only. It is spoken *and* shown: OCR
confirms "310-620 mph" on screen from **200.75s for 4.00s** (16 consecutive 0.25s samples,
`persist_L24Wf0VlTE0_203.json`).

Both arms reported no numeric on-screen text, and both were nearly right:
- **Arm A**'s uniform grid samples at 205.68s — **0.93 s after the text disappears.**
- **Arm B** spent a full frame at 200.0s specifically to check — **0.75 s before it appears.**

A 4-second event, a 5-minute video, two arms that both went looking in the right place, and
both missed it by under a second from opposite sides. Capture probability for this event at
N=30 is 0.399; even odds would need 38 frames.

This is the sharpest single data point in the benchmark, and neither arm is at fault.
