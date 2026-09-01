# Ground truth — LP10_YdKEPw

Established 2026-09-01 from 18 sampled timestamps across three coverage sheets,
BEFORE either arm was run. Verified absent from the transcript: "glove",
"Instagram", "gameconsolerepairs", "GCR", "subscribe", "cleaning process",
"ultrasonic", "soap", "alcohol" all return zero hits — so every answer below is
obtainable only by looking.

1. **Channel/brand.** Logo reads **GCR** (gamepad-inside-a-gear mark, orange and
   blue). Instagram handle **@gameconsolerepairs** shown on the end cards
   (~19:59–20:02). Logo also appears as a watermark at 00:10 and 19:41.

2. **Title cards.** **TWO**, both in the same yellow-over-white style:
   - "PS3 Super Slim / Cleaning Process" at ~08:41, over parts in a liquid bath.
   - "PS3 Super Slim / Lens Cleaning with 100% IPA" at ~11:03, over the laser
     mechanism. **[CORRECTION — see provenance note below]**

3. **Gloves.** **Purple/blue nitrile**, worn **only during the cleaning phase**
   (~09:59–10:39). Bare hands during disassembly (00:10, 03:42, 06:28) and
   reassembly (16:53, 19:41). The "not throughout" half is the discriminator: it
   requires coverage of the whole video, not a single lucky frame.

4. **Cleaning methods.** Four, not three:
   - Immersion in a foamy/soapy bath in a stainless tray (~08:41). Nothing on
     screen confirms *ultrasonic*; it is a soak.
   - Vacuuming with a bristle-brush nozzle (~09:06). **[CORRECTION]**
   - Board wiped by hand with the purple gloves on (~10:39–10:54).
   - Lens cleaned with 100% IPA from a dropper bottle (~11:03), per the on-screen
     caption. **[CORRECTION]**
   - Compressed-air duster on the fan/shroud (~12:03).

5. **Final ~30 seconds.** A subscribe end card — GCR logo, thumbs-up, red
   SUBSCRIBE button, notification bell, @gameconsolerepairs (~19:59) — followed
   by a **"Thanks For Watching"** card with the GCR logo (~20:01–20:02).

## Scoring

2 = correct and complete · 1 = partially correct, or correct but incomplete
0 = wrong, or "insufficient evidence" · −1 = confidently wrong (fabricated)

Max 10 per arm. Cost is reported alongside; correctness-per-image is the
comparison that matters.


## Provenance note — the judge's reference was incomplete

This ground truth was first built from 18 sampled timestamps and **missed two
real things**: the second title card at 11:03 and the vacuuming step at 09:06.
Arm B reported both. Rather than mark them wrong for exceeding the reference, I
verified each independently (frames at 663s and 546s, examined by the judge after
Arm B reported and before either arm was scored) and both confirmed. The
corrections above are the result.

Two consequences worth stating plainly:
- The corrected version is what **both** arms are scored against, which is the
  only fair basis even though it raises the bar for the arm that reported second.
- A benchmark whose reference is built by sampling can be *beaten* by a method
  that looks harder. That is a real limitation of this benchmark's construction,
  not a flourish — and it is itself weak evidence for the thing being tested.
- "IPA" returns zero transcript hits, so that caption was read off the screen and
  could not have been inferred from the narration.
