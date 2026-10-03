# Verdict — jtl4KKRIheo (iFixit, iPhone 11 screen replacement)

Scored against ground_truth.md as written. Scale: 2 correct/complete, 1 partial (per GT's own partial definitions), 0 wrong/insufficient/restated, -1 confidently fabricated.

| Q | Label | W | X | Y | Z | Rationale |
|---|---|---|---|---|---|---|
| 1 Tools and bits | S | 1 partial | 2 correct | 2 correct | 2 correct | W: leads "insufficient evidence", then gives a substantially correct list as labelled UNVERIFIED own knowledge (extra standoff bit) — right values only by explicit labelled inference. X/Y/Z: full list with P2/Y000/Phillips from transcript (Z also cites on-screen caption). |
| 2 Battery before starting | S | 1 partial | 2 correct | 2 correct | 2 correct | W: correct 25% threshold + fire/explosion reason, but only as labelled own knowledge, not from the video. X/Y/Z: exact answer with transcript cites (Z corroborates with the 24% frame). |
| 3 iOpener times | S | 0 abstained | 2 correct | 2 correct | 2 correct | W declines both durations (generic "1–2 min per edge" is not the two asked values). Others: ~1 min bottom edge, 1–2 min top front, both cited. |
| 4 Bracket screws and bit | S | 0 abstained | 2 correct | 2 correct | 2 correct | W refuses to state counts (bit Y000 alone does not meet GT's partial, which requires counts). Others: 3 + 5, Y000 for both. |
| 5 Cracked screen workarounds | B | 1 partial | 1 partial | 1 partial | 2 correct | GT: packing tape alone = partial; full credit needs ≥2 on-screen-only workarounds. W: packing tape + tape-handle but as labelled UNVERIFIED own knowledge → partial. X and Y: transcript-only packing tape → partial. Z: packing tape plus sticky-tape and superglue read off the on-screen guide page → full credit. |
| 6 Pick route and clipped edge | S | 1 partial | 2 correct | 2 correct | 2 correct | W: labelled own knowledge gets book-style opening from the left and top clips, but misses the right-side pass and the pull-toward-Lightning step (matches GT partial: clips without pull step). Others: complete sequence incl. pull-down-toward-Lightning-port and top-right insertion. |
| 7 Sensor assembly screws + reinstall order | S | 0 abstained | 2 correct | 2 correct | 2 correct | W refuses count and order. Others: 4 screws (3 Phillips, 1 Y000) and the full 5-step reinstall sequence matching GT. |
| 8 Battery capacity and voltage | V | 1 partial | 1 partial | 2 correct | 2 correct | GT allows "insufficient evidence" from a transcript-only arm. W and X both say not in the available material and give 3110 mAh / 3.83 V only as labelled own knowledge → partial. Y: read from a zoomed battery-label frame (3110 mAh, 3.83 V, 11.91 Wh, APN) with an honest resolution caveat on the mAh → correct. Z: read from frames, all values incl. APN → correct. |

## Totals

| Arm | Total (max 16) | correct | partial | abstained | wrong | fabricated |
|---|---|---|---|---|---|---|
| W | 5 | 0 | 5 | 3 | 0 | 0 |
| X | 14 | 6 | 2 | 0 | 0 | 0 |
| Y | 15 | 7 | 1 | 0 | 0 | 0 |
| Z | 16 | 8 | 0 | 0 | 0 | 0 |

## Ground truth concerns

1. **Rubric vs GT on Q8 abstention.** The global rubric scores "insufficient evidence" as 0, but GT Q8's partial definition says insufficient evidence "is acceptable" from a transcript-only arm. I followed the GT's own partial definition (per the rubric's parenthetical) and scored W and X at 1 on Q8; under a strict reading they would be 0, lowering W to 4 and X to 13.
2. **Labelled own-knowledge answers.** W repeatedly supplies correct values only as UNVERIFIED own knowledge after declaring insufficient evidence. I treated these as "right value reached only by explicit labelled inference" (score 1, outcome partial) when the content matched GT, and abstained/0 when W declined to state the asked values. The rubric does not explicitly address external-knowledge answers; a stricter convention (all = abstained/0) would put W at 0.
3. **Q5 full-credit bar.** Z names two of the three on-screen-only workarounds (sticky tape, superglue) but not the duct-tape handle or safety glasses; GT's "at least two" threshold is met, so full credit — flagging in case the intent was all on-screen content.
