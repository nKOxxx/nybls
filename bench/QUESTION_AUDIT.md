# Question audit, all rounds

**Run 2026-09-04** after round 3 exposed the flaw. Every round used the same design rule:
"any term appearing in the narration was rejected, so the questions test looking, not
reading." That rule was enforced with token exact substring matching. Narration is speech.
Re-run with normalisation (lowercase, non alphanumerics collapsed to spaces, plus obvious
spoken variants), the filter leaks in every round.

## Terms the ground truth treats as visual only, but which are spoken

| Video | term | spoken as | hits |
|---|---|---|---|
| LP10_YdKEPw | "Lens Cleaning" title card | "lens cleaning" | 1 |
| g9xUu2StOYg | results graphic "14TH" | "14th" | 1 |
| g9xUu2StOYg | "JK Tyre" podium backdrop | "jk racing" | 1 |
| g9xUu2StOYg | chequered flag backdrop | "checkered" | 2 |
| 5oNHF72wbmI | the key fobs | "key fob", "fob", "fobs" | **32** |
| 5oNHF72wbmI | the diagnostic tablet | "tablet" | 7 |
| jgN4XWFUSb4 | camshaft sensor faults | "camshaft", "cam shaft sensor" | 2 |
| jgN4XWFUSb4 | the carVertical report | "car vertical" | 3 |

Two of these were already disclosed honestly in the ground truth at design time
("edgasket: 1 hit, near visual only"; "warranty is spoken 35 times but the document's
wording is visual only"). The rest were not.

## Verdict, question by question

**Void. The narration states the answer.**
- `5oNHF72wbmI` Q3 (what is shown relating to the keys). "fob" is spoken 32 times and the
  three piece arrival, the spare and the programming are all narrated. Not a looking test.
- `5oNHF72wbmI` Q4 (what tool reads the electronics, how does it appear). "tablet" spoken
  7 times, the borrowed McLaren tool and DiagCode are narrated at length.
- `DQdB7wFEygo` Q2 and Q4 (round 3, already recorded).

**Compromised, retained, flagged.** The narration names part of the answer but not the
visual detail the question asks for: `LP10_YdKEPw` Q2 (second title card), `g9xUu2StOYg`
Q2, Q3 and Q4, `jgN4XWFUSb4` Q3 and Q5, `L24Wf0VlTE0` Q5.

## Effect on the headline

Both arms scored 2 on each voided question, so removing them costs each arm the same
4 points and the comparison is unchanged in direction.

| | Arm A | Arm B |
|---|---|---|
| As previously reported | 56/76 (74%) | 68/76 (89%) |
| **Strict, voided questions removed** | **52/72 (72%)** | **64/72 (89%)** |
| Visual tokens | 430,080 | 119,363 |
| Cost ratio | **3.60x** | |

The cost ratio is unaffected because token spend does not depend on which questions are
scored. The paper must quote the strict figures.

## The finding

The obvious way to build a "did it actually look" benchmark is to grep the transcript for
the answer and throw the question out if it hits. That check silently fails across the
speech to writing boundary, and it fails hardest on precisely the content where looking
matters most: filenames, identifiers, code, registration plates, on screen numbers. A
written `node_modules` is a spoken "node modules"; a written `.dockerignore` is a spoken
"docker ignore"; `W1 MNO` is spoken as nothing at all, which is why that one survived.

Any future filter must normalise punctuation and spacing, test multi word variants, and be
run by someone other than the person who wrote the question. Ours was not, three times.
