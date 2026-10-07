# Round 6 results: 31 videos, 248 questions, Sonnet 5.5 as the agent, Fable on a bridge subset

Protocol `PROTOCOL.md` and predictions `PREDICTIONS.md` registered at `315d909` (2026-10-06),
before any selection, author, arm or judge ran. Deviations D1 to D12 in `PROTOCOL.md`; the
model re-plan is D8. Everything here reproduces from `judge/*/verdict.json`, `judge/MAPPING.json`,
`data/*/labels.json` and `VIDEOS.json` by `python3 tally.py` (writes `tally.json`).

Arms: **T** transcript only · **B** nybls plus its shipped WATCH skill · **AM** transcript plus a
uniform grid of exactly as many 1568-wide frames as B spent on that video · **BF** nybls on
Fable 5.1, eight videos chosen by rule. T, B, AM and the judges ran on Claude Sonnet 5.5
(D8). Scoring 2/1/0/-1 and outcome classes unchanged from round 5. One blind judge per video,
arms anonymised W/X/Y(/Z).

## The result in one line

On 31 videos and 248 natural questions, nybls on Sonnet 5.5 scores **90.5%** against a
transcript-only agent's **60.7%** and a cost-matched uniform grid's **69.6%**, while spending
215 images in total (0 to 28 per video). The gain is where it was in round 5: on the 71
screen-only items the transcript arm scores 7%, the uniform grid 28%, nybls 81%. The set is no
longer saturated: nybls scores below 90% on 11 of the 31 videos, and the Fable bridge arm,
96.9% on its 8 videos against Sonnet's 93.8% on the same 8, says the remaining gap is mostly
the model, not the tool. No arm fabricated anything in 248 items; the video-less arm
abstained on 64.

## Pooled (31 videos, 248 items, 496 points)

| arm | model | points | % | correct | partial | abstained | wrong | fabricated | images | visual tokens |
|---|---|---|---|---|---|---|---|---|---|---|
| T | Sonnet 5.5 | 301 | 60.7 | 123 | 55 | 64 | 6 | 0 | 0 | 0 |
| AM | Sonnet 5.5 | 345 | 69.6 | 147 | 53 | 45 | 3 | 0 | 215 | 385,280 |
| **B** | Sonnet 5.5 | **449** | **90.5** | 207 | 35 | 5 | 1 | 0 | 215 | 275,379 |
| BF (8 videos, 64 items, 128 pts) | Fable 5.1 | 124 | 96.9 | 61 | 2 | 1 | 0 | 0 | 94 | 121,087 |

Cluster bootstrap by video, 95%: B minus T +23.8 to +36.1 points of percentage; B minus AM
+15.3 to +27.2. At 8 videos (round 5) the same intervals were 29 and 9 points wide; at 31 they
are 12 and 12.

## By where the answer lives

| label | items | T | AM | B | BF (subset) |
|---|---|---|---|---|---|
| S spoken | 124 | 243/248 (98%) | 244/248 (98%) | 245/248 (99%) | 72/72 |
| B both | 53 | 48/106 (45%) | 61/106 (58%) | 89/106 (84%) | 23/24 |
| V screen only | 71 | 10/142 (7%) | 40/142 (28%) | 115/142 (81%) | 29/32 |

Labels are the authors' S/V/B after the mechanical transcript re-check (3 of 248 relabelled).

## By stratum

| stratum | videos | T | AM | B | BF |
|---|---|---|---|---|---|
| N owner-supplied | 10 | 60.0 | 66.2 | 93.1 | 97.9 (3 videos) |
| S sampled by rule | 21 | 61.0 | 71.1 | 89.3 | 96.2 (5 videos) |

The B minus T gap is 33 points in N and 28 in S; P27 (sampled gap within 10 points of the
nominated gap) passes. Hand supply did not flatter the tool.

## By genre (stratum S, points of 32; genre 6 has one video, of 16)

| # | genre (query) | T | AM | B |
|---|---|---|---|---|
| 1 | whiteboard math | 27 | 30 | 31 |
| 2 | news bulletin | 17 | 20 | 29 |
| 3 | French talk | 23 | 27 | 31 |
| 4 | Arabic talk | 14 | 20 | 25 |
| 5 | sports highlights | 14 | 17 | 28 |
| 6 | handheld walking vlog (1 video) | 11 | 12 | 14 |
| 7 | dense slide keynote (actually talks about keynotes, D3) | 24 | 24 | 30 |
| 8 | no-text daily vlog | 9 | 12 | 23 |
| 9 | guitar lesson | 23 | 25 | 31 |
| 10 | woodworking DIY | 23 | 25 | 27 |
| 11 | science demonstration | 20 | 27 | 31 |

B beats T in all 11 genres and AM in all 11 (P31). The largest gains over the transcript are
news (+12), sports (+14) and the daily vlogs (+14), the genres whose content is on screen.

## Per video (points of 16)

| video | stratum | genre | min | T | AM | B | BF |
|---|---|---|---|---|---|---|---|
| J7DzL2_Na80 | S | 1 | 39 | 16 | 16 | 16 | 16 |
| OH-5LJFiYHA (Korean, D7) | S | 1 | 31 | 11 | 14 | 15 | |
| 5bVQqrzjCI8 | S | 2 | 17 | 9 | 9 | 16 | |
| 2TvP0aXC4Ss | S | 2 | 21 | 8 | 11 | 13 | |
| vRaghhAFsFo | S | 3 | 19 | 12 | 13 | 16 | 16 |
| J8PEymuDf6A | S | 3 | 11 | 11 | 14 | 15 | |
| qVIzSMux720 | S | 4 | 36 | 13 | 13 | 16 | |
| qSIX7qvPmlo (Arabic, D7) | S | 4 | 55 | 1 | 7 | 9 | |
| Xxq8hZc6mws | S | 5 | 20 | 7 | 10 | 12 | 14 |
| 0oJG3EkcR2o | S | 5 | 23 | 7 | 7 | 16 | |
| AvCFhznItLU | S | 6 | 11 | 11 | 12 | 14 | |
| n0VSqz69k3Q | S | 7 | 7 | 11 | 12 | 15 | |
| y08TrAsHZzI | S | 7 | 9 | 13 | 12 | 15 | 16 |
| WjUeusWRXp4 | S | 8 | 15 | 9 | 10 | 11 | |
| -uJAz0fmPOY (music only, all V) | S | 8 | 12 | 0 | 2 | 12 | |
| pQC3JsbgaTw | S | 9 | 5 | 11 | 11 | 15 | |
| Yb4ajV0C1BE | S | 9 | 12 | 12 | 14 | 16 | |
| l_mOoZNuuDg | S | 10 | 10 | 13 | 13 | 14 | 15 |
| Ze1s_FB8CeI | S | 10 | 6 | 10 | 12 | 13 | |
| t8pcKyc3XbM | S | 11 | 41 | 10 | 12 | 15 | |
| fDEFGpMoPkk | S | 11 | 16 | 10 | 15 | 16 | |
| WSYAW4U7ZYc | N | | 104 | 10 | 10 | 15 | 15 |
| pQ6G9TQfGIA (360p) | N | | 27 | 8 | 7 | 16 | |
| 7GIULwETan4 (karting) | N | | 20 | 9 | 11 | 13 | |
| d95J8yzvjbQ | N | | 84 | 11 | 11 | 13 | |
| k1njvbBmfsw | N | | 109 | 7 | 8 | 16 | 16 |
| x_YwyhAcHRE | N | | 39 | 11 | 13 | 16 | |
| GaQE-voqIfc | N | | 72 | 11 | 12 | 15 | |
| LCEmiRjPEtQ | N | | 39 | 5 | 8 | 14 | |
| bmRJjcsFOoE (Starcraft) | N | | 28 | 9 | 11 | 16 | 16 |
| Px3HfB2UkyU | N | | 55 | 15 | 15 | 15 | |

B never scores below T on any video and ties T on three (J7DzL2_Na80, Px3HfB2UkyU and, in
effect, l_mOoZNuuDg at 14 vs 13). AM beats B on no video.

## The Fable bridge (8 videos chosen by rule, 64 items)

| arm | points of 128 | % |
|---|---|---|
| T | 87 | 68.0 |
| AM | 93 | 72.7 |
| B (Sonnet) | 120 | 93.8 |
| BF (Fable) | 124 | 96.9 |

Sonnet B scores 96.8% of Fable BF's points on the same questions (P26 pass, threshold 85%),
with zero fabrications in 248 items. Fable spent 94 images where Sonnet spent 48 on the same
8 videos; the extra spend bought 4 points, all on the sports highlights video (Xxq8hZc6mws,
12 vs 14). This is the bridge to round 5's Fable figures, not a pooled comparison.

## Where the tool loses

The 11 videos where B is under 90% (P25): two Arabic lectures, the music-only vlog, the two
news bulletins, both sports videos, the two documentary-length nominated videos, the
handheld vlog, the Karpathy talk, the woodworking build and the TikTok-style daily vlog. The
worst is the second Arabic lecture (9/16): the author's questions there are about on-screen
Arabic text that Sonnet read poorly, and the one "wrong" item B produced in the whole round is
there (Q6, shared by all three arms, a ground-truth dispute recorded by the judge). The
music-only vlog (-uJAz0fmPOY) is the clearest demonstration of the modality argument: T 0,
AM 2, B 12 of 16.

## Spend

B examined 215 images across 31 videos (275,379 visual tokens by the ledger), a median of 5
per video; AM received the same 215 frames at full resolution (385,280 tokens, 40% more);
BF examined 94 images on its 8 videos (121,087 tokens). Sonnet as the agent spends far less
than Fable did in round 5 (D10) and still beats the matched grid by 21 points of percentage.

## Predictions (registered 2026-10-06; P26 as amended under D8)

| id | prediction | result |
|---|---|---|
| P23 | B >= T + 20 pp pooled | **pass** (+29.8) |
| P24 | B >= AM + 8 pp pooled | **pass** (+21.0) |
| P25 | B < 90% on at least 2 videos | **pass** (11 of 31) |
| P26 | Sonnet B >= 85% of Fable BF points on the subset, B fabrications <= 2 | **pass** (96.8%, 0) |
| P27 | sampled B minus T gap within 10 pp of the nominated gap | **pass** (28 vs 33) |
| P28 | non-English: T >= 90% on S items, B >= 75% on V items | **pass** |
| P29 | B minus AM gap grows with duration (Spearman > 0) | **pass** |
| P30 | T zero fabrications, B at most 1 | **pass** (0, 0) |
| P31 | B beats T in all 11 genres and AM in at least 9 | **pass** (11, 11) |

Nine of nine. In round 5, nine of 22 failed, mostly predictions about fabrication that the
models never produced; round 6 did not repeat those predictions.

## What round 6 does not show

The agent model changed (Sonnet 5.5 here, Fable 5.1 in round 5), so round 5 and round 6
numbers are not pooled; the 8-video BF subset is the only cross-model comparison. The judge
is Sonnet 5.5 (round 5: Fable), a departure listed in Limitations. Authors were mixed (8 Fable,
23 Sonnet; recorded per video). Stratum S holds no silent-video genre (D2): the registered
caption filter excluded them, so the silent-video result still rests on round 5. The
compact-and-delete lifecycle remains ENVISIONED. No non-Claude judge ran.
