# Verdict — dwwhwVaI6vg (Jamie Oliver, basic bread + pesto twister)

| Q | Label | W | X | Y | Z | Rationale |
|---|---|---|---|---|---|---|
| 1 | S | 2 correct | 0 abstained | 2 correct | 2 correct | W/Y/Z give all four quantities (650 ml tepid, 1 sachet dried yeast, 1 kg strong flour, pinch of salt) plus optional sugar/honey; X says insufficient evidence with only labelled UNVERIFIED background. |
| 2 | S | 2 correct | 0 abstained | 2 correct | 2 correct | W/Y/Z: sugar/honey wakes the yeast, bubbles after a couple of minutes = CO2. X abstains. |
| 3 | S | 2 correct | 0 abstained | 2 correct | 2 correct | W/Y/Z: first prove 1–1.5 h under damp cloth until doubled; second prove 0.5–1 h, at least twice as big, draught-free. X abstains. |
| 4 | S | 2 correct | 0 abstained | 2 correct | 2 correct | W/Y/Z: 180 °C for about 35 minutes. X abstains. None repeat the 220 °C packet-recipe trap. |
| 5 | B | 2 correct | 0 abstained | 2 correct | 1 partial | W and Y confirm GREEN pesto from a frame, plus olives, cheddar, and the mozzarella remark. Z (transcript-only) gives pesto+olives+cheddar+mozzarella but honestly cannot settle the colour — exactly the ground truth's partial definition. X abstains. |
| 6 | B | 2 correct | 0 abstained | 2 correct | 1 partial | W and Y: half×3 = 8 pieces, round dark pan/skillet, swirl up, gaps prove together. Y labels 8 as arithmetic inference, but the GT says 8 is derivable from the transcript alone, so it is fully supported — correct. Z gives 8 pieces but only "a little pan" with no shape/colour (visual-only detail missing) — partial. X abstains. |
| 7 | V | 2 correct | 1 partial | 1 partial | 1 partial | W names Jamie Oliver AND "Keep Cooking and Carry On" from the opening tin title card — complete. X has the chef from title/channel metadata but marks the series insufficient — GT's partial case. Y has the chef from the end card but marks the series UNVERIFIED/insufficient — partial. Z reaches both chef and series only by explicit labelled inference ("inferred, not established") — right values via labelled inference = 1, partial. |
| 8 | S | 2 correct | 0 abstained | 2 correct | 2 correct | W/Y/Z: dusted tray, one knead, tap and stretch into an oval "rustic slipper", flour on top so it breaks and puffs up. X abstains. |

## Totals

| Arm | Total (max 16) | Correct | Partial | Abstained | Wrong | Fabricated |
|---|---|---|---|---|---|---|
| W | 16 | 8 | 0 | 0 | 0 | 0 |
| X | 1 | 0 | 1 | 7 | 0 | 0 |
| Y | 15 | 7 | 1 | 0 | 0 | 0 |
| Z | 13 | 5 | 3 | 0 | 0 | 0 |

## Ground truth concerns

1. Rubric tension on Q6 for Y: the rubric scores "right value reached only by explicit labelled inference" as 1, but the ground truth itself states "The number 8 is derivable from the transcript alone". Since the arm's cited evidence (the transcript's "in half, then in half, then in half again") fully supports the value, I scored Y's 8-pieces answer as correct rather than demoting the honest "inferred arithmetic" label. Same reasoning does not rescue Z on Q7, where the chef/series are genuinely not in the transcript and the inference rests on outside knowledge.
2. X's Q7 is scored partial (chef correct from title/channel metadata, series missing), matching the GT's explicit partial case "Jamie Oliver without the series name"; its labelled UNVERIFIED series guess was explicitly "not offered as the answer", so it earns neither credit nor a fabrication penalty.
3. No disagreements with the ground truth's factual content; no fabrications found in any arm.
