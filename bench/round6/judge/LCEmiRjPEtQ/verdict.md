# Verdict LCEmiRjPEtQ

| Q | W | X | Y | Rationale |
|---|---|---|---|---|
| 1 | 2 correct | 2 correct | 2 correct | All three map code/weights/prompts. |
| 2 | 2 correct | 2 correct | 2 correct | All give verification speed-up and leash. |
| 3 | 1 partial | 0 abstained | 0 abstained | W read the limit as 10/min (truth 50) but has token bucket, user_id, thread-safe, cleanup, tuple; X, Y say insufficient. |
| 4 | 2 correct | 2 correct | 0 abstained | W, X give 22 and 27.0k; Y says never spoken. |
| 5 | 1 partial | 1 partial | 1 partial | All give hard parts and hours vs week; none give the slide checklist (partial per ground truth). |
| 6 | 2 correct | 1 partial | 0 abstained | W has all three dates; X has 1940s and 2012 only; Y gives no dates. |
| 7 | 2 correct | 0 abstained | 0 abstained | W full diagram mapping; X and Y say insufficient (Y's labelled recollection not asserted). |
| 8 | 2 correct | 0 abstained | 0 abstained | W full red X and green check lists incl. AGI 2027; X, Y say insufficient. |

Totals: W 14, X 8, Y 5 (max 16)

## Ground truth concerns
- Q3: W's misread limit (10 vs 50) fits no clean outcome; scored 1 partial (token bucket and all other elements right, limit wrong), not fabricated since it cited a legible frame.
- Q5: ground truth makes the slide checklist required for a 2, so all arms capped at partial though the spoken content is fully correct.
- Q8: AGI 2027 is slide-only, so transcript-only arms cannot reach it.
