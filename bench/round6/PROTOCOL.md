# Round 6: scaling the grounding benchmark from 8 to 32 videos

**Written 2026-10-06, before any round 6 author, arm or judge ran, and before the author
read any transcript or frame of any round 6 video.** The ten nominated videos had been
probed (download and caption fetch only) when this was written; nothing in them had been
viewed. Round 5 (`../round5/`) is the method of record; this file states only what round 6
changes or adds. Deviations are appended as they occur.

## Why

Round 5 Part 2 settled direction (nybls beats a transcript-only agent, a 30-frame grid and a
cost-matched grid, on 8 videos, 7 to 8 of 8 per video) but not size: the cluster bootstrap
95% interval on the B minus AM gap at 8 videos is +12.5 to +21.1 points of percentage, on
B minus A it is +3.1 to +12.5. And B at 97.7% is saturated: the set measures the baselines,
not the tool. Round 6 quadruples the video count, adds long-form, non-English, sports and
handheld footage where frame selection should be harder, and reports results per stratum.

## Videos: two strata, reported separately

**Stratum N (nominated), 10 videos.** Supplied by the project owner on 2026-10-06 before
any round 6 work, listed in `NOMINATED.md` with their metadata. The owner states they were
picked at random from their own viewing; there is no documented procedure a reader could
rerun, which is the only reason they form a separate stratum. The paper says so and never
pools them with stratum S without also showing the strata apart (prediction P27 tests
whether the two strata agree). Seven exceed round 5's 30-minute cap (four exceed an hour), one is
360p; the cap is lifted for round 6 (see Selection), the resolution floor applies only to
stratum S. One (GaQE-voqIfc) is a fan reupload channel and may be removed from YouTube;
if it is unavailable when an arm needs it, it is dropped and the drop recorded.

**Stratum S (sampled), 22 videos.** Eleven genres, two videos each, chosen by the committed
`sample_videos.py` with no human choice at any step:

| # | genre | query | fallback query |
|---|---|---|---|
| 1 | whiteboard math | `linear algebra lecture whiteboard` | `calculus lecture blackboard` |
| 2 | news bulletin, lower thirds | `evening news bulletin full` | `news hour full episode` |
| 3 | French talk | `conférence TEDx français` | `cours magistral français` |
| 4 | Arabic talk | `محاضرة كاملة` | `تيدكس بالعربي` |
| 5 | sports highlights | `full match highlights` | `extended highlights football` |
| 6 | handheld walking vlog | `walking tour vlog handheld` | `city walk vlog talking` |
| 7 | dense slide keynote | `keynote slides conference talk` | `conference talk slides full` |
| 8 | no-text daily vlog | `day in my life vlog` | `weekly vlog` |
| 9 | guitar lesson | `guitar lesson tabs on screen` | `how to play guitar lesson` |
| 10 | woodworking DIY | `woodworking project build` | `diy build step by step` |
| 11 | science demonstration | `science experiment demonstration explained` | `physics demo lecture` |

**Selection rule (stratum S).** For each query, `yt-dlp ytsearch15:<query>` in the order
YouTube returns; keep the first two results that pass every filter: duration 300 to 3600 s;
height at least 480; a caption track (manual or automatic) in the video's own language; not
live; not already in `~/.nybls/store` or any earlier round; title not matching
`compilation|best of|#shorts|top 10|reaction` (case-insensitive). If a query yields fewer
than two, the fallback query is run under the same rule for the remainder. The raw search
dumps (`candidates.jsonl`), the per-candidate pass/fail with the failing filter, and the
final list (`SELECTED.md`) are committed. A video that passes the filters but fails
`nybls probe` (download or caption fetch fails) is replaced by the next survivor of the same
query and the replacement is recorded in `SELECTED.md`. No other exclusion is permitted.

**Non-English caption handling.** Transcripts are used in the video's language, untranslated.
Arms and authors read them as they are. If probe reports no captions, `probe --model turbo`
is used (recorded).

## Arms

Round 5 had five arms. Round 6 keeps three and adds one:

- **T** transcript only (unchanged prompt from round 5 Part 2).
- **B** nybls plus its shipped WATCH skill, Fable 5.1 (unchanged prompt).
- **B2** identical to B, run on Claude Sonnet 5.5. Tests the "model is the ceiling" claim,
  which in round 5 rested on Haiku 4.5 versus Fable 5.1 on four silent videos.
- **AM** transcript plus a uniform grid of exactly as many 1568-wide frames as B was served
  on that video, Fable 5.1 (unchanged from the round 5 addendum). Runs after B.

Dropped, with reason: **N** (title only; 22% and zero fabrications on 64 items, nothing
left to learn at this cost), **A** (30 uniform frames; AM is the sharper control and A lost
to it on the argument that matters).

Every arm runs on Fable 5.1 except B2. Each video's B and B2 run from separate store
ledgers: B2 uses a copy of the store entry under media id `<id>_s55` so no two agents share
a ledger (round 5 deviation D5).

## Authors

One author agent per video, isolated from nybls, prompt unchanged from round 5 Part 2
(`PROMPTS.md`), with one change for long videos: the reference grid interval is
`max(10, ceil(duration_s / 120))` seconds, so no author sees more than about 120 frames.
Eight questions per video, S/V/B labels after writing, mechanical transcript re-check
by `check_labels.py` here, which is round 5's checker with one change: normalisation keeps
every Unicode word character, because round 5's ASCII-only normalisation would delete all
Arabic and accented text and make the re-check vacuous on genres 3 and 4. Relabel-safe as
before.

## Judging

One blind judge per video, Fable 5.1, prompt unchanged from `../round5/rejudge/JUDGE_PROMPT.md`,
four anonymised arms W/X/Y/Z (T, B, B2, AM) built by `build_judge_packs.py` here (round 5's
D9 builder with `sonnet`, `fable`, `claude` and `_s55` added to the blocklist, since B2
differs from B only by model), and the scrub-loss audit run before judging as in D9.
Blinding is nominal for T, as in round 5 D4. Scoring and outcome classes unchanged.

## Reporting

Per stratum and pooled: points per arm, outcomes, label table (S/B/V), per-video table,
per-genre table for stratum S, image and visual-token spend per arm, and a cluster bootstrap
95% interval (by video) for every arm gap, the same script as the planning estimate
(`power.py`). Every prediction's pass or fail. If nybls loses on a video or a genre, the
paper says so.

## What round 6 does not test

The compact-and-delete lifecycle (ENVISIONED). The Part 3 "use it" task (round 5 only).
A non-Claude judge (still blocked on credentials, as round 5 P22).

## Deviations, recorded as they occur

- **D1 (2026-10-06, before any selection).** The first run of `sample_videos.py` crashed on
  the first query: yt-dlp prints the literal `NA` where a video has no caption dictionary,
  which the script parsed as JSON. Fixed to treat `NA` as empty; no filter or rule changed.
  No candidate had been selected.
- **D2 (2026-10-06, at selection).** Genre 6 (handheld walking vlog) yielded one survivor
  from 30 candidates (primary and fallback). 16 failed duration (walking tours run 1 to 12
  hours), 13 failed the caption filter: most walking tours have no speech and YouTube tags
  no audio language, so the "caption track in the video's own language" rule cannot be met.
  Three of those 13 did carry English captions with the language untagged; the script treats
  an untagged language as a fail, which is the registered rule read strictly, and it was not
  loosened after the fact because that would be selection with the results in view. Round 6
  therefore has 31 videos (10 + 21) and 248 items; predictions stated as counts of 32 apply
  to 31. A consequence worth stating: the stratum S filter excludes silent video, so every
  silent-video result in the paper still rests on round 5.
- **D3 (2026-10-06, at selection, disclosure).** The rule picked some off-target videos and
  they stay: genre 1 second pick is a Korean-language lecture (ko captions, used untranslated);
  genre 7 picked two talks about giving keynotes rather than slide-dense keynotes; genre 10
  first pick has a finance-styled title ("I Paid My Credit Cards Off With These") returned for
  a woodworking query. Genre labels in the per-genre table describe the query, not the content.
- **D4 (2026-10-06, at probe, tool finding).** nybls as shipped fetches only English caption
  tracks (`SUB_LANGS = "en"` in ingest.py) and falls back to the English-only whisper `base`
  model. On the four non-English videos (OH-5LJFiYHA ko, vRaghhAFsFo fr, qVIzSMux720 and
  qSIX7qvPmlo ar) probe therefore produced looping transcripts it itself flagged UNRELIABLE,
  although yt-dlp reports caption tracks in those languages. Per the registered rule the
  four were re-probed with `--model turbo` (multilingual); the unreliable store entries were
  archived under `_void_r6_base_<id>`, not deleted. This is reported in the paper as a
  limitation of the tool, not of the benchmark: an agent using nybls on non-English video
  today gets no usable transcript unless it passes `--model turbo` itself. Arm T uses the
  same store transcript as arm B, so the arms stay comparable.
- **D5 (2026-10-06, at probe).** Eight English videos for which yt-dlp reported English
  captions were transcribed by whisper `base` instead (probe's caption fetch is best-effort
  and YouTube rate-limited it): 0oJG3EkcR2o, n0VSqz69k3Q, y08TrAsHZzI, WjUeusWRXp4,
  l_mOoZNuuDg, x_YwyhAcHRE, GaQE-voqIfc, LCEmiRjPEtQ. This is the tool's normal fallback and
  the transcripts are kept; the source is recorded per video in `VIDEOS.json` once probing
  closes.
- **D6 (2026-10-06, at probe).** DVx22QXGTT4 (genre 8, rank 1) failed download twice with
  HTTP 403, an hour apart. Per the registered rule it is replaced by the next survivor of the
  same query: -uJAz0fmPOY (genre 8, primary query, rank 3, 729 s, 1080p, en), the first
  quota-filled candidate that passes every filter when re-evaluated. Recorded in SELECTED.md.
- **D7 (2026-10-06, at probe).** OH-5LJFiYHA (genre 1, Korean lecture) stays UNRELIABLE
  under `--model turbo` as well: probe's flag fired on one line repeated 28 times in a row.
  Inspection of the file shows 688 lines of real Korean speech otherwise, so the flag marks a
  looping stretch, not an empty transcript. The video and the flagged transcript are kept as
  the tool produced them; arm T receives the same file. Reported per video. The same flag
  fired on qSIX7qvPmlo (one line repeated 121 times, a looping stretch inside an otherwise
  real Arabic transcript); kept on the same basis.
