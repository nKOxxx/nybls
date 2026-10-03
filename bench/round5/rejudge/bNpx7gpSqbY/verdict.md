# Verdict — bNpx7gpSqbY (Bill Gross, TED)

Scored against ground_truth.md as written. Rubric: 2 correct/complete; 1 partial / labelled-inference-only; 0 wrong or abstained; -1 fabricated.

| Q | Label | W | X | Y | Z | Rationale |
|---|---|---|---|---|---|---|
| 1 | B | 2 correct | 1 partial | 1 partial | 2 correct | W: name (frame caption) + Idealab + >100. X: Idealab + >100 but never names Bill Gross — exactly the ground truth's partial case. Y: name only via explicitly labelled own-knowledge inference (correct, so 1); Idealab + >100 evidenced. Z: all three elements stated correctly. |
| 2 | S | 2 correct | 2 correct | 2 correct | 2 correct | All four name idea, team/execution, business model, funding, timing. |
| 3 | B | 2 correct | 2 correct | 1 partial | 2 correct | W, X: all five percentages, correct rank order, "More Than 200 Companies". Y: 42% + order from transcript; the other four percentages given only as [OWN KNOWLEDGE, unverified] labelled inference (values correct) — 1 per rubric. Z: all five values, order, and ~200 companies correct and stated as the answer. |
| 4 | S | 2 correct | 2 correct | 2 correct | 1 partial | W, X, Y: all ten names in correct groups with transcript cites. Z: lists are fully correct but the arm itself labels them "own-knowledge recall, not verified" with no citable evidence — right value by explicit labelled inference, 1. |
| 5 | V | 2 correct | 2 correct | 1 partial | 1 partial | W, X: Timing 4, Funding 8 read from the slide. Y: honest insufficient-evidence plus the flagged qualitative "funding high, timing low" — matches the ground truth's own partial definition. Z: same qualitative direction, flagged as recall, no numbers — partial (its extra recalled claim that idea/team/business model were "high" is off — they are 5s — but it is flagged as unreliable recall and is not the asked value; noted, not penalised). |
| 6 | S | 2 correct | 2 correct | 2 correct | 2 correct | All four: broadband too low 1999–2000 / codec pain, out of business 2003, Flash solved codecs + broadband crossed 50% for YouTube. |
| 7 | S | 2 correct | 2 correct | 2 correct | 2 correct | All four: consumer readiness + radical honesty / not being in denial. |
| 8 | V | 2 correct | 2 correct | 0 abstained | 0 abstained | W, X: 10 9 8 6 10 with correct factor mapping. Y, Z: honest insufficient-evidence, no false claim — abstained, 0. |

## Totals

| Arm | Score (max 16) | Correct | Partial | Abstained | Wrong | Fabricated |
|---|---|---|---|---|---|---|
| W | 16 | 8 | 0 | 0 | 0 | 0 |
| X | 15 | 7 | 1 | 0 | 0 | 0 |
| Y | 11 | 4 | 3 | 1 | 0 | 0 |
| Z | 12 | 5 | 2 | 1 | 0 | 0 |

- W: correct on all eight.
- X: partial on Q1 (no speaker name).
- Y: correct Q2/Q4/Q6/Q7; partial Q1/Q3/Q5; abstained Q8.
- Z: correct Q1/Q2/Q3/Q6/Q7; partial Q4/Q5; abstained Q8.

## Ground truth concerns

1. Z answers Q3 (all five percentages) and Q1 correctly but with "No timestamp available" and no evidence trail; nothing in Z suggests the slide was ever viewed, so these are almost certainly unlabelled parametric recall that happens to match ground truth. The rubric scores against the ground truth as written, so they take 2; a rubric that required evidence grounding would score Z's Q3 like Y's (1). Flagging the asymmetry: Y labelled its recall and scored lower for the same knowledge.
2. Z's Q5 includes a flagged-recall claim that Z.com scored "highly on idea, team, business model" — the slide shows 5/5/5, which is middling, not high. Treated as a noted extra claim (flagged as unreliable recall, not the asked value), not a fabrication; a stricter reading could drop Z's Q5 to 0.
3. No disagreements with the ground truth's factual content itself.
