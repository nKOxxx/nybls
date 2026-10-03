# Part 3: reproduce the program ("use it"). Exploratory, registered in PREDICTIONS_ADDENDUM.md

Run 2026-10-04 on Fable 5.1 after the usage reset (the first launch on 2026-10-03 died on
credits with no output; nothing from it survives). Artefacts, notes and the mechanical
grades are in `part3/` (`GRADES.txt` is `grade_part3.py part3`, re-runnable; compiled
binaries are not tracked).

## Silent C spinning cube (p09i_hoFdd0), rubric of 10

| arm | grade | compiles | what it missed |
|---|---|---|---|
| N | 7 | yes | distanceFromCam, the face characters, the timing/escape idiom |
| T | 2 | yes | wrote an explicit placeholder ("nothing in this file is determined by the video"), compiling but empty of content: an honest abstention, scored as such |
| A | 9 | yes | one face character: it merged two faces into `;`, five distinct characters where the video has six |
| B | **10** | yes | nothing |

B spent 51 images (81,857 visual tokens) to reach 10/10 here, against 20 images for the
same video's question answering: reproducing a whole program needs every constant and
the loop structure, and the protocol kept buying frames until it had them. A reached
9/10 from its fixed 30 frames, because this video's code is on screen almost
continuously and a uniform grid cannot miss much of it; the one point it dropped is a
face character the grid never caught legibly. **N's 7/10 from the title alone** is
the clearest instance in the whole benchmark of what a transcript or a bare URL buys an
agent on a famous pattern: the "spinning ASCII cube in C" is a known program, and the
model reconstructed most of it from memory. It is a cube, not this cube.

## Narrated Python tutorial (7R-CfL21zIY), rubric of 10: **the registered rubric was wrong**

All four arms scored 2/10 under the registered rubric, which is not a result about the
arms. The rubric graded against the choose-your-own-adventure game the ground truth
describes, because the author's ground truth describes that game; the video *demos* that
game in its first two minutes as the goal of the series and then *builds* a three-line
program (ask name, ask age, print both). T, A and B each wrote that three-line program,
and wrote the same three-line program (`name = input(...)`, `age = input(...)`, a print). N wrote a
number guessing game from the title alone. The arms answered the question asked; the
rubric asked about the wrong program.

What is defensible to report: under a post hoc reading of "the program the video
builds", T, A and B are correct and indistinguishable, and N is wrong. This post hoc
reading is NOT a score of record; it is recorded here as the observation, and the
registered 2/10 row stands as the registered result, so that the rubric error is visible
rather than repaired in the data.

## Predictions

- **P19** (B >= A >= T >= N on both): cube, B = 10 >= A = 9 > T = 2 but N = 7 > T, so the
  T >= N clause **fails**; Python, all tied under the registered rubric, trivially
  holds, uninformatively. **Fail**, and the failure is the same finding as Part 2's
  genre-inference partials: on a famous pattern, prior knowledge beats an empty
  transcript.
- **P20** (silent C: T <= 3, B >= 8): 2 and 10. **Pass.**

- **P21** (Python: T within 2 of B): 2 and 2 under the registered rubric. **Pass**, but
  only because the rubric failed; under the post hoc reading T and B are identical, which
  is what the prediction meant. Reported as a pass with that caveat.

**Correction (2026-10-04, addendum re-review, Chen).** The first revision of this file
said the transcript arm wrote "a generic cube" and scored A 10/10. Both were wrong: T
wrote a placeholder, and the grader's six-character check tested only three characters,
so A's merged face went unnoticed. Grader fixed to require all six distinct literals,
GRADES.txt regenerated; A is 9/10. No prediction outcome changes.

## Deviation D10

The Part 3 rubric for 7R-CfL21zIY targeted the demoed final game rather than the program
the first episode builds. Found at grading, after the arms ran. Not corrected in the
scores of record; disclosed here and in PROTOCOL.md.

## Non-Claude judge (P22): not run, blocked on credentials

No non-Anthropic API key exists in the environment, the keychain, or the local
api-treasure-chest (which holds feed configuration, not credentials). Per the
registration, P22 is recorded as not run. The same-family-judge limitation stands in the
paper's Limitations as written.
