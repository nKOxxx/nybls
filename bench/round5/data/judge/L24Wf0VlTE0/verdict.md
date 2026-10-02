# Verdict — L24Wf0VlTE0 (jet engine, 5:01)

Arms present in directory: W, X. Ground truth gives no P/T labels.

| Q | Label | W | X | Rationale |
|---|---|---|---|---|
| 1 Presenter vs animated | – | 1 correct-by-inference (outcome: partial) | 1 correct-by-inference (outcome: partial) | Both say entirely animated, explicitly labelled as inference from channel knowledge (X adds transcript cues). Correct value, reached only by labelled inference → 1. |
| 2 Hot vs cold colouring | – | 0 abstained | 0 abstained | W: insufficient evidence, no guess. X: headline answer "insufficient evidence"; adds an explicitly unconfirmed convention (hot red-orange, cool blue) that happens to match GT (teal-blue intake, orange/red combustor/exhaust), but declines to assert it for this video. Scored as abstention. |
| 3 Watermark | – | 0 abstained | 0 abstained | Both: insufficient evidence on visible branding/position. GT: watermark bottom-right throughout. |
| 4 Technique for internals | – | 0 abstained | 0 abstained | Both: insufficient evidence. X lists cutaway / transparent casing as channel conventions, explicitly "not determinable here". GT: semi-transparent cutaway. |
| 5 On-screen text | – | 0 abstained | 1 partial | W: insufficient evidence. X: infers (labelled) that on-screen text exists (section titles) and flags "310 to 620 mph" as a candidate on-screen number but cannot confirm. GT: on-screen text labels airflow speeds (310-620 mph on screen 200.75s–204.75s). Existence correct, content only partially/unconfirmed → 1. |

## Totals
- W: 1 / 10
- X: 2 / 10

## Extra claims (noted, not penalised)
- W Q1, X Q1: channel is Animagraffs / Jacob (Jake) O'Neal. Not in GT; not contradicted.
- X Q5: claims transcript contains isolated headings ("The Core", "The Compressor", etc.) suggesting chapter-title captions. GT does not mention section titles; unverifiable here.
- X Q1: transcript quote [01:28] "The design shown here is an annular combustor". Not in GT.

## Ground truth concerns
- GT item 2 and 4 have "0 hits" annotations for keywords, i.e. the colour/presenter facts were established from frames not transcript; fine, but GT does not state whether section-title captions appear on screen, so X's Q5 "section titles" inference cannot be confirmed or refuted — scored as partial on the existence of on-screen text alone.
- Judgment call on X Q2: the rubric's "right value reached only by explicit labelled inference = 1" could apply (X names red-orange hot / blue cool as a convention), but X's declared answer is "insufficient evidence" and it explicitly refuses to assert it for this video. Scored 0 abstained; an alternative reading gives 1. Same reasoning applied to X Q4 (cutaway/transparent casing named but disclaimed) → 0 abstained.
- GT errata confirms "310-620 mph" is on screen for 4.00 s; X's Q5 flags exactly this number as a candidate without confirming — consistent with GT, counted toward the partial.
