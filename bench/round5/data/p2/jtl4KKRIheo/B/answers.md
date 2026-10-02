# Answers — jtl4KKRIheo (iPhone 11 screen replacement)

Mode: answer mode. Round 0 transcript (~1,470 words, clean narration, reliable) carries Q1–Q7 fully. Q8 is a visual question (battery label text), so one sheet + one zoom were spent on it.

## 1. Tools and bits

An iOpener, a set of iFixit opening picks, a suction handle or iSclack, a spudger, tweezers, and these screwdriver bits: a P2 pentalobe bit, a Y000 (Y triple-zero) bit, and a Phillips bit [00:13]–[00:27]. (Transcript renders "P2" as "p tube" at [00:20]; the same screws are called "P2 pentalobe" at [00:50].) The video also warns to have replacement waterproof seals / new adhesive ready, since opening the display compromises the seals [00:27]–[00:37].
Evidence: transcript [00:13]–[00:37].

## 2. Battery before starting

Discharge the battery to below 25% before beginning [00:39]–[00:41]. It matters because a charged lithium-ion battery can catch fire and/or explode if you accidentally damage it during the repair [00:42]–[00:46]. Then power the phone off [00:48].
Evidence: transcript [00:39]–[00:48].

## 3. iOpener times

- Bottom edge at the start: about one minute [00:56]–[01:01].
- Top front of the display when loosening the sensors: about one to two minutes [03:46]–[03:51].
Evidence: transcript [00:56]–[01:01], [03:46]–[03:51]; sheet tile [03:49] shows the display resting on the iOpener.

## 4. Bracket screws and bit

- Battery connector bracket: three screws [02:42]–[02:45].
- Logic board cover bracket: five screws [03:02]–[03:05].
- Bit: Y000 (Y triple-zero) for both [02:42], [03:02].
Evidence: transcript [02:42]–[03:05].

## 5. Suction cup won't grip on a cracked screen

Cover the display with a piece of clear packing tape so the cups can stick [01:01]–[01:10]. The video uses an iSclack (one cup on the front, one on the back near the bottom edge; close the handles to open a small gap only) [01:11]–[01:37]; if you only have an iFixit suction handle, it tells you to follow the opening procedure in the guide at ifixit.com [01:13]–[01:17]. No other workaround (e.g. heat alternatives) is given.
Evidence: transcript [01:01]–[01:37].

## 6. Pick order and the clipped edge

1. Insert the pick into the gap at the bottom edge, slide around the lower-left corner and up the left edge [01:39]–[01:52].
2. Re-insert at the bottom edge and slide up the right side [01:59]–[02:06].
3. Top edge last: it is held by both adhesive and clips [02:06]–[02:08]. What to do differently: gently pull the right side of the display down slightly toward the Lightning port, insert the pick in the top-right corner, and slide it across the top edge while continuing to pull down gently [02:10]–[02:20]. Then open the display by swinging it up from the left side like a book cover; don't lift it off, it is still attached by ribbon cables [02:23]–[02:34]. Don't insert the pick too far at any point [01:53]–[01:58].
Evidence: transcript [01:39]–[02:34].

## 7. Earpiece speaker / front sensor assembly

Four screws hold it to the display: three Phillips and one Y000 [03:28]–[03:34].
Reassembly order onto the new display [04:36]–[05:06]:
1. Press the proximity sensor and flood illuminator into their slots on the display.
2. With tweezers, slide the ambient light sensor back into place, then place its bracket straight onto it.
3. Press the microphone back into place with a finger, and press the flex cable below the microphone onto the display so it is well adhered (a spudger can be used).
4. Flip the speaker assembly over and reinstall the four screws.
Evidence: transcript [03:28]–[03:34], [04:36]–[05:06]; sheet tile [04:41] shows the sensor assembly being seated with tweezers.

## 8. Battery capacity and voltage

3.83 V, 11.91 Wh, 3110 mAh (label also reads APN 616-00644). The transcript never states this; it was read off the battery label.
Evidence: zoom frame `z_179000_0_15_50.png` at [02:59] (box 0.0,0.15,0.5,0.8). "3.83V ⎓ 11.91Wh" is large and unambiguous; "3110mAh" is in the small print near the bottom of the label and is legible but smaller, so confidence on the mAh figure is slightly lower than on V/Wh (it is consistent with 11.91 Wh / 3.83 V ≈ 3110 mAh).

## Evidence strip

- [02:24, 02:59, 03:25, 03:49, 04:41, 05:15] `sheet_000.png` (range 150–330 s): phone closed; opened phone with battery label visible under a fingertip; full open view of the chassis; display resting on an iOpener; sensor assembly handled with tweezers; adhesive liner/new display held up.
- [02:59] `z_179000_0_15_50.png`: battery label — "Rechargeable Li-ion Battery, 3.83V ⎓ 11.91Wh, APN: 616-00644", warning text, "3110mAh", Apple South Asia (Thailand) Limited.

## Ledger

watched 7 min · examined 2 images (~2,717 visual tokens, ≈$0.01 at sonnet-5 input rate) of ~9,945 total frames · budget 2/27 units

## Tool-file statement

I did not modify, create, or delete any file in the nybls repository or installation. Note: `nybls probe jtl4KKRIheo` returned "error: not a file" (probe takes a URL/path, not a store id); I worked around it by reading the stored transcript directly and using `ledger`/`sheet`/`zoom` with the id. Nothing under bench/ or oneshot/ was read.
