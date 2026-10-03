# Verdict — 7R-CfL21zIY (Python Tutorial for Beginners part 1)

| Q | Label | W | X | Y | Z | Rationale |
|---|-------|---|---|---|---|-----------|
| 1 | S | 2 correct | 2 correct | 1 partial | 2 correct | W/X/Z name Repl.it, free browser-based, browser+internet (phone/iPad). Y gives the right value but only as labelled OWN KNOWLEDGE inference, unverified against the video. |
| 2 | S | 2 correct | 2 correct | 1 partial | 2 correct | W/X/Z list str/int/float/bool with the quotes definition of string. Y lists all four and the quotes rule but only as labelled own knowledge, unverified. |
| 3 | S | 2 correct | 2 correct | 0 abstained | 2 correct | W/X/Z give full rules (letters/underscore/numbers, no leading digit, underscore for space convention). Y's answer is a garbled fragment ("g. `user_age`") stating no actual rules — effectively no answer, no false claim. |
| 4 | B | 1 partial | 1 partial | 0 abstained | 2 correct | Full credit needs Love2D and Pyxel (screen-only). W and X give only the spoken subset (Pygame, Tkinter, Java Swing) and honestly flag incompleteness — exactly the GT partial definition. Y abstains. Z gives the complete lists with descriptions. |
| 5 | V | 2 correct | 0 abstained | 0 abstained | 2 correct | W and Z cite the exact banner "Python 3.8.2 (default, Feb 26 2020)". X abstains with an explicitly labelled 3.7/3.8-era guess (not stated as answer). Y abstains. |
| 6 | V | 2 correct | 1 partial | 1 partial | 2 correct | W and Z read line 3 `age = int(input(...))` and `if age >= 18:` from frames. X and Y reach the right pattern (int cast, `if age >= 18`) only via explicitly labelled inference/own knowledge while declaring the exact on-screen value insufficient. |
| 7 | V | 2 correct | 1 partial | 0 abstained | 2 correct | W and Z give Tim Ruscica / @TimRuscica from frames. X reaches "Tim Ruscica" only by labelled own-knowledge inference (scores 1 for that), but its labelled username guess "techwithtim" is wrong per GT (@TimRuscica) — labelled guess, so partial overall, not fabricated. Y abstains. |
| 8 | S | 2 correct | 2 correct | 0 abstained | 2 correct | W/X/Z: bit by a fish, lost 5 health, then house vs river choice. Y declares insufficient evidence on a transcript-answerable item. |

## Totals

| Arm | Total (max 16) | correct | partial | abstained | wrong | fabricated |
|-----|----------------|---------|---------|-----------|-------|------------|
| W | 15 | 7 | 1 | 0 | 0 | 0 |
| X | 11 | 4 | 3 | 1 | 0 | 0 |
| Y | 3 | 0 | 3 | 5 | 0 | 0 |
| Z | 16 | 8 | 0 | 0 | 0 | 0 |

## Ground truth concerns

- Q7 / arm X is a mixed case the rubric does not cleanly cover: the full name "Tim Ruscica" is correct but reached only by labelled own-knowledge inference (rubric: 1), while the accompanying labelled username guess ("techwithtim") contradicts the GT (@TimRuscica). Since the question accepts full name OR username and the guess was explicitly labelled unverified, I scored 1/partial rather than 0/wrong; a stricter reading (penalising the wrong username) would give 0/wrong.
- Y's Q3 answer appears textually truncated/garbled (begins mid-sentence). I scored what is on the page (no rules actually stated → 0, abstained) rather than guessing intended content.
- No disagreements with the ground truth answers themselves.
