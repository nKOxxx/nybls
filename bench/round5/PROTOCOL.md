# Round 5 protocol: does access to the video improve what the model says?

**Written 2026-10-02, before any round 5 arm, author or judge ran, and before any round 5
video was selected.** Committed together with `PREDICTIONS.md`; the commit timestamp is the
registration time.

## Why this round

Rounds 1 to 4 compared nybls against another way of showing a model frames (30 uniform
stills plus the transcript). That isolates *how* to look. It never measured the question a
user of the tool actually has: **compared with what an agent does today, does giving it the
video make its answers more correct and less invented?** What agents do today, per
`docs/RESEARCH.md` section 2, is one of two things: answer from the model's own knowledge,
or read the captions. Neither arm has ever been run.

## Arms

| arm | name | evidence |
|---|---|---|
| N | nothing | the video title, channel and duration only. Stands in for an agent that is handed a URL it cannot open. |
| T | transcript | the transcript file only. Stands in for every caption loader in section 2 of RESEARCH.md. |
| A | one shot | transcript plus 30 uniform frames (unchanged from rounds 1 to 4) |
| B | nybls | the CLI and the WATCH protocol (unchanged from rounds 1 to 4) |

All arms receive the same honesty instruction used since round 1 ("insufficient evidence"
rather than a guess; a confident wrong answer scores worse). This is conservative: it
suppresses fabrication in the weak arms, so any fabrication gap measured here is a lower
bound on what an unprompted agent does.

All roles run as Claude Code subagents on Fable 5.1, the model rounds 1 to 4 used, default
sampling. No role can message another. Arms N and T get their inputs copied into an
isolated scratch directory and are told to read nothing else; they run no tools beyond
reading those files and writing their answer.

Tool under test: nybls 0.10.0 as installed by pipx, `nybls_core` source sha256
`3669416d4906b0cd3eb39bcd5d9b61595e1ca21a818741325d29e053ba108313`, rechecked after every
B arm finishes.

## Part 1: the existing 56 audited questions, two new arms

The 12 videos and 56 audited questions of rounds 1 to 4 (`bench/SCORES.md`), with arms N
and T added. **Stated bias:** these questions were selected to be answerable by looking and
not from narration, so T is disadvantaged by construction. Part 1 therefore measures *how
an agent behaves when the answer is not in the captions* (does it abstain or invent), not
how often captions suffice. Part 2 measures the second.

Judging: one fresh judge per video sees every available arm's answers, anonymised as
W/X/Y/Z with the mapping withheld and arm headers stripped. Round 1 (`LP10_YdKEPw`) has no
retained A or B answer files, so its judge sees N and T only. A and B are rejudged blind in
rounds 2 to 4; the original scores stay the result of record for the A versus B comparison
and the rejudge is reported as an inter judge consistency check.

## Part 2: natural questions on new videos

**Selection.** Eight new public videos, one per category below, chosen by rule: the first
`yt-dlp ytsearch10:<query>` result with duration between 6 and 30 minutes that is not
already in the store, not a livestream, and has an English audio track. Selected before any
of its content is viewed. The query list is fixed here:

| # | category | query |
|---|---|---|
| 1 | interview / podcast, speech carries content | `startup founder interview podcast` |
| 2 | slide lecture | `university lecture slides machine learning` |
| 3 | narrated coding tutorial | `python project tutorial for beginners` |
| 4 | narrated cooking | `how to make bread recipe` |
| 5 | silent cooking | `cooking no talking asmr` |
| 6 | silent screen recording | `silent coding session no talking` |
| 7 | product review / unboxing | `unboxing and review` |
| 8 | narrated repair / DIY | `how to replace step by step repair` |

**Questions.** One author agent per video, isolated from nybls, sees a dense reference
grid (one frame every 10 s, built with ffmpeg directly) and the transcript. It writes
**eight questions that a person who wants to learn from or act on this video would
actually ask**, with no rule for or against visual content. Only after writing them does it
label each **S** (answer is in the speech), **V** (answer is only on screen) or **B**
(needs both), with grid frames and transcript lines cited. A mechanical check then searches
the normalised transcript for each V answer's key terms (the QUESTION_AUDIT normalisation);
a hit relabels the item to B or S, recorded.

**Arms and judging.** All four arms answer; one judge per video scores all four blind.

## Part 3 (exploratory, not part of any prediction): use it

For the two coding videos (3 and 6), each arm is additionally asked to reproduce the
program the video builds. The output is executed in a scratch directory and the run is
recorded (runs or not; behaviour against the video's final state). Exploratory because
"behaviour against the final state" needs a rubric written per program after the video is
selected, which is weaker than the registered parts.

## Scoring

Unchanged: 2 correct and complete, 1 partial or labelled inference, 0 wrong or
"insufficient evidence", minus 1 confidently fabricated. In addition the judge classifies
every item into one outcome: **correct**, **partial**, **abstained** (honest gap),
**wrong** (stated as fact, incorrect but not invented from nothing) or **fabricated**
(stated as fact, specific, and with no support in any evidence the arm was given). The
fabrication rate is the headline hallucination measure.

## What is reported regardless of outcome

Every prediction's pass or fail, every voided item with its reason, every protocol
deviation, and the per item table. If T matches B on Part 2, the paper says so.

## Deviations, recorded as they occur

- **D1 (2026-10-02, before any judging).** Rounds 1 to 3 retained only experimenter
  summaries of the A and B answers, with scores embedded, not the raw answers. A blind
  rejudge of A and B is therefore possible only for round 4 (`round4/judge_inputs`). For
  rounds 1 to 3 the judge sees N and T only; A and B scores of record are used. P4 is
  evaluated on round 4 alone (40 points per arm; tolerance scaled to 3 points).
- **D2.** Part 2 selection, category 5 (silent cooking): the "English audio track" clause
  cannot apply to a silent category and was not applied. Selection list in
  `round5/SELECTED.md`.
- **D3.** The concurrency limit (20 subagents) delayed three Part 1 arms; they ran the same
  prompt later. No content effect.
- **D4.** Blinding is nominal for N and T. Their answers name their own evidence ("from the
  transcript", "the metadata gives no...") and some headed themselves with the arm name.
  Self-labels were stripped; the content still reveals the arm. A and B remain as blind as
  in round 4. The judge rubric is mechanical (ground truth as written), which limits but
  does not remove the risk.
- **D5 (Part 1b/1c).** The Haiku nybls arm for `92gQUnMCA08` was launched while the Fable
  nybls arm for the same video was still running, so both wrote to one ledger and frame
  directory. Both runs were stopped before writing answers, their state moved to
  `_void_r5_d5/` in the store, and the Fable arm rerun from a clean ledger. From then on, nybls
  arms on the same video run strictly one after another, with state archived between them.
- **D6 (observed, not a deviation).** The stored transcript for `oZAiHH9nrhk` (stock
  documentary) is a Whisper repetition loop after [00:17]. All arms in rounds 3 and 5 saw
  the same file. This is the failure `fix/transcript-loop-share-gate` detects.
- **D7 (Part 2, in progress).** Three author agents (7R-CfL21zIY, txspjbMw6ks, p09i_hoFdd0)
  failed twice: once on a network outage, once on the session usage limit. Part 2 results
  are reported first on the five completed videos, marked partial; the remaining three run
  after the limit resets, under the same registered protocol, and the combined table
  replaces the partial one.
- **D8.** Part 3 skipped for budget on 2026-10-02; run on 2026-10-04 under the registered
  addendum (PART3.md). Registered exploratory.
- **D9 (2026-10-03).** The Part 2 "blind judged" claim was false: the first judging's
  packs leaked every arm's identity (run 025, Whitfield C1, chair-confirmed). All eight
  videos were re-judged with corrected, mechanically verified anonymisation; see
  REJUDGE.md. The re-judged scores are the scores of record; the first judging is
  retained in data/judge_p2/ as the superseded record. D4's claim that "A and B remain
  as blind as in round 4" was wrong for Part 2 and is withdrawn in favour of this entry.
- **D10 (2026-10-04).** The registered Part 3 rubric for 7R-CfL21zIY graded against the
  choose-your-own-adventure game the video demos, not the three-line program episode 1
  builds. All arms but N wrote the latter, correctly. Rubric error, found at grading;
  registered scores stand, observation disclosed in PART3.md.
- **D11 (2026-10-04).** The addendum arms (AM, Part 3) first launched 2026-10-03 and all
  died on an account credit limit with no output; relaunched after reset on Fable 5.1.
  No content effect.
