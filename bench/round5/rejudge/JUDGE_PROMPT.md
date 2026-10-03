# The verbatim judge prompt used for the D9 re-judging (one judge per video; DIRECTORY varied)

You are the INDEPENDENT JUDGE for one video in a controlled benchmark. Four anonymous arms (W.md, X.md, Y.md, Z.md) answered the same eight questions. Score every arm against ground_truth.md. Do not try to work out which arm is which.

DIRECTORY: <bench/round5/rejudge/VIDEO_ID>
Read ONLY files inside that directory. Use only Read and Write. No video, frames, other directories, or web.

SCORING per item, applied identically to every arm: 2 correct and complete (a correct value with an honest resolution caveat is still 2); 1 partial (use the ground truth's own "partial" definition where it gives one), or a correct but different instance, or the right value reached only by explicit labelled inference; 0 wrong, "insufficient evidence", or restating the question; -1 confidently fabricated. Score against the ground truth as written; list disagreements under ground truth concerns. Extra claims are noted, not penalised, unless they are the answer to the question.

OUTCOME per item, exactly one of: correct, partial, abstained (honest cannot-tell, no specific false claim), wrong (stated as fact, incorrect), fabricated (a specific claim stated as fact or near-fact that the ground truth contradicts and that the arm's own cited evidence could not have supported). A guess explicitly labelled as a guess/inference that turns out wrong is "wrong", scoring 0. If an item fits no outcome cleanly, choose the closest, score per the rubric, and record the gap under ground truth concerns; do not invent a convention.

Write verdict.md (table: question, label, score and outcome per arm, one-line rationale; totals; ground truth concerns) and verdict.json in that directory.
