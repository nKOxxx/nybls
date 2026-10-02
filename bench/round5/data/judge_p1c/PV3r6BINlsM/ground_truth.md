## PV3r6BINlsM — history of Rome, 44:32, 395 cuts
1. **Map**: yes — the Mediterranean basin and Europe from satellite-style relief,
   overlaid with a dense white network of Roman roads. ("map": 0 hits)
2. **Illustrated/generated recreations**, not archival photography — uniform
   lighting, painterly detail and impossible camera positions across scenes.
3. **Frontier fortification**: a long stone wall running over green hills with
   regular crenellations, Hadrian's-Wall-like. ("hadrian's wall": 0 hits)
4. **Carved relief**: a polychrome (painted) stone relief of togate figures,
   standards and horses. ("relief": 0 hits)
5. **Street scenes**: paved streets between colonnaded buildings and arches, with
   citizens in togas and tunics and horse-drawn carts.


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
