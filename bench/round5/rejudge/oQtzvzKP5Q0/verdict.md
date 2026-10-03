# Verdict — oQtzvzKP5Q0 (IMVC 2024, Assaf Hoogi, FAME optimizer)

Scored against ground_truth.md as written. Arms judged anonymously.

| Q | Label | W | X | Y | Z | Rationale (one line per question) |
|---|---|---|---|---|---|---|
| 1 | S | 1 partial | 2 correct | 2 correct | 2 correct | W names only the lag (labelled own knowledge) and abstains on the finance contrast; X, Y, Z give both the inherent lag and the passive-indicator vs active-guidance distinction with correct citations. |
| 2 | V | 1 partial | 2 correct | 1 partial | 1 partial | X gives the exact slide title, all three authors and Ariel University with affiliations; W gives Hoogi + Ariel from evidence plus an uncertain, differently-worded title from memory; Y gives speaker + Ariel + the spoken session title only; Z gives the spoken title (not the slide title) and reaches the co-authors only by labelled unverified own knowledge. |
| 3 | V | 1 partial | 2 correct | 2 correct | 1 partial | X and Y read TEMA = 3EMA1 − 3EMA2 + EMA3 off the slide; W and Z state the same (correct) formula but only via explicitly labelled own-knowledge/inference, never confirmed from the video. |
| 4 | V | 0 abstained | 2 correct | 2 correct | 1 partial | X and Y transcribe all moment equations and the five betas from the slide (Y's typo caveat is honest and does not change the answer); W abstains; Z infers the correct m_FAME/v_FAME form but has no beta count. |
| 5 | B | 0 abstained | 2 correct | 2 correct | 1 partial | X and Y give 6 datasets / 15 architectures / 6 optimizers from the slide; Z has 6 + 15 from transcript but abstains on the optimizer count (ground truth's own partial definition); W declines to rely on its ~6/~14/~6 recollection — abstention, and 14 architectures would have been wrong anyway. |
| 6 | V | 0 abstained | 2 correct | 2 correct | 0 abstained | X and Y report 0.723 / 0.708 / 0.693 exactly (Y's resolution caveat is honest and still a 2); W abstains; Z's section is empty — no answer given, treated as abstention. |
| 7 | B | 0 abstained | 2 correct | 2 correct | 1 partial | X and Y give 83% plus both exceptions (MobileNet → SGD+M 0.644; DenseNet-201 → Adam 0.742) with the right values; Z gives 83% only; W abstains. X's "13 rows, 11 wins ≈ 85%" row count differs from the ground truth's 12/10 — noted below, not penalised, since the exceptions and winners asked for are correct. |
| 8 | B | 1 partial | 2 correct | 2 correct | 1 partial | X and Y give both qualitative conclusions and all four MS-COCO mAP numbers (0.265 / 0.504 / 0.529 / 0.495); W and Z give the correct qualitative conclusions (both moments better; QEMA not better) without numbers — the ground truth's partial case (W's via labelled uncertain recall, Z's from transcript). |

## Totals

| Arm | Total (max 16) | correct | partial | abstained | wrong | fabricated |
|---|---|---|---|---|---|---|
| W | 4 | 0 | 4 | 4 | 0 | 0 |
| X | 16 | 8 | 0 | 0 | 0 | 0 |
| Y | 15 | 7 | 1 | 0 | 0 | 0 |
| Z | 8 | 3 | 4 | 1 | 0 | 0 |

## Ground truth concerns

1. **Q7 row count:** X reports the image-classification table as 13 rows with 11 FAME wins (≈85%), listing SEResNet-18 among the FAME-won rows; the ground truth says 12 rows and 10/12 ≈ 83% (and Y independently reports 12 rows). The exceptions and winning optimizers agree across all sources, so this did not affect scoring, but the exact row count of the table is worth a recheck.
2. **Q6 for Z:** Z's answer file contains the "## 6" heading with no body at all — not even an explicit "insufficient evidence". I scored it as abstained (0) rather than wrong, since no claim was made; the rubric does not define an "empty section" case.
3. **Q4 beta count:** Y flags that β5 appearing in both third-order lines may be a slide typo for a β6. The ground truth already states β5 is shared as written on the slide, so Y's five-beta answer with caveat scores 2; no conflict, just noting the caveat exists.
