# Verdict — oQtzvzKP5Q0 (IMVC 2024, Assaf Hoogi, FAME optimizer)

Scoring: 2 correct/complete, 1 partial (incl. correct value reached only by explicit labelled inference/own knowledge), 0 wrong/abstained, -1 fabricated.

| Q | W | X | Y | Z | Rationale |
|---|---|---|---|---|---|
| 1 | 2 correct | 1 partial | 2 correct | 2 correct | W, Y, Z: lag limitation + passive-indicator vs active-guidance. X: lag only (own knowledge), finance difference "insufficient evidence" (GT partial). |
| 2 | 1 partial | 1 partial | 1 partial | 2 correct | W: spoken session title + Hoogi + Ariel from transcript; co-authors only as unverified own knowledge. X: Hoogi + Ariel from metadata; title recalled wrongly and authors labelled uncertain. Y: honest insufficient evidence for slide title/co-authors, gives spoken title + Hoogi + Ariel. Z: exact slide title, three authors, Ariel University with departments. |
| 3 | 1 partial | 1 partial | 2 correct | 2 correct | W, X: correct 3EMA1 - 3EMA2 + EMA3 but explicitly labelled as standard finance definition from own knowledge, not from the video. Y, Z: read from slide with DEMA/EMA_k context. |
| 4 | 1 partial | 1 partial | 2 correct | 2 correct | W: correct m_FAME/v_FAME form by labelled inference, beta count insufficient. X: insufficient evidence headline, correct construction only as uncertain own knowledge, no beta count. Y, Z: full equations and five betas (Y flags possible beta6 typo as a caveat; still 2). |
| 5 | 1 partial | 1 partial | 2 correct | 2 correct | W: 6 datasets + 15 architectures, optimizer count insufficient (GT partial). X: labelled uncertain recall "~6 / ~14 / ~6" — 14 architectures is wrong, two of three right, all labelled unreliable; partial. Y, Z: 6 / 15 / 6 from slide. |
| 6 | 0 abstained | 0 abstained | 2 correct | 2 correct | W, X: honest insufficient evidence. Y: 0.723/0.708/0.693 with honest resolution caveat. Z: same via zoom. |
| 7 | 1 partial | 0 abstained | 2 correct | 2 correct | W: 83% only. X: insufficient evidence on all parts. Y, Z: 83% + MobileNet (SGD+M) + DenseNet-201 (Adam) with values. |
| 8 | 1 partial | 1 partial | 2 correct | 2 correct | W: both qualitative conclusions correct, no numbers (GT partial). X: qualitative conclusions as vague own-knowledge recall, no numbers; partial. Y, Z: qualitative + MS-COCO 0.265 / 0.504 / 0.529 / 0.495. |

**Totals:** W 8 · X 7 · Y 15 · Z 16

No fabrications. X's wrong title recall and "~14 architectures" are labelled uncertain, so they are not scored as fabricated; they pull the item to partial rather than wrong because the other components of those answers are correct.

## Ground truth concerns
- Q7: GT says the image-classification table has 12 rows (10/12 ≈ 83%). Z, reading a zoom of the same table, counts 13 rows (CIFAR-10 ResNet18 + 12 CIFAR-100 rows including RevViT) and 11 wins ≈ 85%. Y counts 12. The exceptions themselves (MobileNet, DenseNet-201) are agreed by all; the row count is a minor GT verification item.
- Q4: Y suggests the shared beta5 on the slide may be a typo for beta6. GT scores "five as written on the slide"; keep as is, but note the paper may differ.
