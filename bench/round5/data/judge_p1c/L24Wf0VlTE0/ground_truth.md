## L24Wf0VlTE0 — jet engine, 5:01, 2 scene cuts (continuous animation)
1. **No presenter, no live action.** Entirely 3D animation on a plain grey studio
   background. ("presenter", "narrator": 0 hits)
2. **Colour coding**: cold/intake sections rendered teal-blue; the combustor and
   exhaust glow orange/red. ("orange", "blue", "colour": 0 hits)
3. **Watermark** bottom-right of frame throughout.
4. **Semi-transparent cutaway** — the casing is rendered translucent so fan,
   compressor, combustor and turbine stages are visible inside.
5. **On-screen text** labels airflow speeds over the animation.


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
