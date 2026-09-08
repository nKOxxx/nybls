# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Known issues (found by benchmark arms, reported not fixed during the run)
- Contact-sheet tile timestamps resolve differently from `frames`/`zoom` seek, so a zoom
  box derived from a tile can land on a different shot. `snap_to_tile` (added in 0.7.1)
  mitigates this for `frames`; `zoom` is still open.

### Planned
- Independent benchmark of the iterative loop against a one-shot frame dump at
  equal cost, the open gap named in `docs/RESEARCH.md`
- Simplified small-size logo variant for favicon rendering
- Optional MCP server wrapper so non-Claude-Code agents can use the same verbs

## [0.9.4] - 2026-09-08

### Fixed
- **The plugin's own description still handed out the broken install command.**
  It is what the Claude Code Discover tab shows before anyone installs, so it was
  the first thing a stranger read, and it said `pip install nybls`, which PEP 668
  refuses on Homebrew Python and most current Linux.
- **The test meant to protect that description was enforcing the bug.** It
  asserted `"pip install nybls" in text`, so a correct description would have
  failed it. It now requires `pipx install nybls` and rejects the bare form.
  This is the third place the same wrong command survived a fix, after 0.9.2
  corrected the docs and 0.9.3 corrected the skill.

## [0.9.3] - 2026-09-08

### Fixed
- **The skill handed users the install command that does not work.** Its preflight
  fires exactly when the CLI is missing, so the one thing it has to get right is
  the install line, and it still said `pip install nybls`, which PEP 668 refuses
  on Homebrew Python and most current Linux. 0.9.2 fixed this everywhere except
  the one place an agent actually reads.

### Added
- `speakers` documented in `docs/PROTOCOL.md` and in the skill. It shipped in
  0.9.0 documented in the README alone, so an agent following the skill had no
  idea the command existed, including its limits: shots are not people until a
  human names them, and attribution stops during a screen share.
- `extract-check` and `reject` documented for the first time.
- A test asserting every command the CLI exposes appears in at least one document
  a reader or an agent will see, and another asserting the skill's install block
  uses pipx. Both gaps were invisible to every existing check.

## [0.9.2] - 2026-09-08

### Fixed
- **The install instructions did not work.** `pip install nybls` is refused under
  PEP 668 on Homebrew's Python and on most current Linux distributions, so the
  documented first step failed on a normal modern Mac. Both the README and
  INSTALL.md now lead with `pipx`, which exists for precisely this case, and
  explain why rather than just asserting it. A venv is given as the fallback, and
  the agent instructions explicitly forbid reaching for
  `--break-system-packages` on someone else's machine.
  This survived seven releases because nobody had ever installed nybls the way a
  user would; on the author's own machine it existed only inside the development
  virtualenv and was not on PATH at all. Found by installing it properly for the
  first time. A test now pins both documents.

## [0.9.1] - 2026-09-08

### Fixed
- **Caption text kept its HTML entities.** VTT carries them, and YouTube's auto
  captions use `&gt;&gt;` as a speaker marker, so on a real 67-minute video 288
  of 1,666 segments read as `&gt;&gt;` rather than `>>`. That is noise in every
  quote pulled from a transcript and in everything the verifier matches against.
  Found by running the tool on a video nobody had chosen for it.

### Added
- **`INSTALL.md`, written to be followed by an agent.** Someone can paste the
  repository URL into Claude Code and say "install this". It detects the
  platform rather than assuming Homebrew, covers apt, dnf, pacman, winget and
  Chocolatey, verifies with `nybls doctor`, and instructs the agent to ask
  before running sudo and to stop and say so rather than improvise if ffmpeg
  cannot be installed.
- **A `download` extra**: `pip install "nybls[download]"` pulls in yt-dlp for URL
  downloads, about 25 MB. It stays an extra rather than a dependency because
  local files work without it and the base install is advertised at about 50 MB.

### Changed
- **The README never said a bare URL is a complete instruction.** A user pasted
  one, got a full digest, and afterwards said he had not known he was supposed to
  ask a question or that he could. Study mode was already the default for a URL
  with no question attached, but that was documented as an implementation detail
  under "two modes" rather than as the thing most people want. There is now a
  section saying it plainly, and it leads into `contract`, which is the answer to
  the question underneath: how to make a watched video leave something behind
  rather than being read once and lost.
- The README overstated the requirements. It said `brew install ffmpeg yt-dlp`,
  which is macOS only and put yt-dlp behind a system package manager it does not
  need: yt-dlp is a Python package and nybls invokes it as a binary from PATH,
  so pip supplies it on every platform. **ffmpeg is the only genuine system
  dependency**, because nothing else decodes a video.
- Plugin and marketplace descriptions now state the prerequisites. `plugin.json`
  has no field for declaring them, so the description is the only place a user
  sees them before installing rather than as an error afterwards.

## [0.9.0] - 2026-09-08

### Added
- **`nybls speakers <id>`, who is on screen across a recorded call.** A call
  recorded in speaker view cuts to whoever is talking, so a shot change is a turn
  boundary and speaker segmentation becomes a change-detection problem, which
  this tool already solves for free. Measured on a 45-minute sales call: 600
  probes every 3 s extracted in 13 s at no vision cost, two shots covering 88% of
  the call, switching about every 9 s. The command prints the split and writes one
  labelled thumbnail per shot so a person can say which one is them. It reports
  honestly when there is no turn signal to read, which is what a screen share or a
  static camera looks like.
  Known limits, stated in the README: measured properly on one call, gallery view
  untested, attribution stops during a screen share, and screen time is a proxy
  for talk time rather than a measurement of it.

### Fixed
- **The ASR guard passed two real failure modes.** It only looked for repetition,
  so it scored a perfect 1.000 and reported "healthy" on both a transcript of
  fluent hallucinated nonsense that never repeats, and a 63-minute silent screen
  recording captioned as hundreds of unique lines of keyboard noise. Round 4 hit
  the same hole on all four of its silent videos.
  Two rate checks now cover both, because the failures point in opposite
  directions: too few words per minute catches silence, and enough words with
  almost no vocabulary catches invention. Measured across 24 videos of at least
  30 seconds, this catches 6 of 6 known failures with no false positives on the
  18 healthy transcripts, including a console teardown with long silent stretches
  and a stream billed as coding without commentary, which are the sparsest real
  speech in the corpus.
  An earlier attempt using a single threshold was discarded during testing: it
  flagged a 48-minute chess lesson, because distinct vocabulary saturates on a
  long video about one narrow subject, and no threshold survived a gap that thin.

### Changed
- README rewritten. It now lists what the tool actually does, documents call
  review, and reports the benchmark honestly at four rounds, 12 videos and 112
  audited questions: 83/112 for the uniform control against 101/112, with the
  control spending 3.41x the visual tokens for 82% of the score. Round 4 was
  judged blind by a separate agent with the arms labelled X and Y, and its ground
  truth was built by an author with no access to the tool.
- Em and en dashes removed from all prose and all command output.
- Three test fixtures rebuilt. They had been written by repeating one sentence
  template, which gives them the vocabulary profile of a hallucination, and the
  new guard correctly flagged them. The guard was right and the fixtures were not.

## [0.8.0] - 2026-09-04

### Changed
- **Install footprint 293 MB → 63 MB** (clean venv, measured; ~50 MB net of the venv's
  own pip). The agreed ceiling is 150 MB and 0.7.x was nearly double it, not because
  of nybls (the wheel is 36 KB) but because two transitive imports we used one
  function from each pulled opencv (120 MB) and scipy (99 MB). Both are gone:
  - Scene detection now uses ffmpeg's own scene-change filter instead of
    `scenedetect`. Verified on real footage: identical cuts on a 5-minute video,
    same first cuts and same end on a 44-minute one (349 vs 395 scenes at threshold
    0.3). Scene cuts only seed contact-sheet placement; adaptive sampling is the
    real signal, so ~88% agreement is sufficient.
  - The perceptual hash behind `[NEAR-DUPLICATE]` is now ~20 lines of numpy DCT
    instead of `imagehash`. **Bit-exact** against the reference on 217 real frames,
    so every stored `_phashes.json` remains valid.
  - Runtime dependencies are now `numpy` and `pillow` only. `imagehash` moved to a
    `bench` extra for `bench/measure_signals.py`, which compares against it as the
    reference implementation.
  - A test asserts the core package never imports cv2/scipy/scenedetect/imagehash,
    and that the declared dependencies stay exactly those two, so the budget cannot
    be blown silently by a future import.

- `requires-python` is now `>=3.12`. It said 3.10, which was never tested; 3.12 and
  3.14 are what the clean-install checks actually ran on, and the test suite uses
  `tomllib` (3.11+).
- Claude Code plugin manifests were still at 0.7.1. Synced, and a test now asserts
  they match `pyproject.toml`.
- GitHub Actions: the pure-Python suite runs on Ubuntu and macOS, 3.12 and 3.13, and
  the job fails if a clean install exceeds 150 MB.

### Removed
- Build artifacts (`dist/`) had been committed by mistake; untracked and ignored.
- The root `nybls` wrapper script (pointed at a dev `.venv`; `pip install` provides
  the real entry point).
- The chess-curriculum use case is dropped (it was only ever an illustrative
  example). The word "chess" still appears where it names a real benchmark
  video, those are measurement records and were left alone.

## [0.7.2] - 2026-09-04

### Changed
- **The `/watch` skill now handles silent video.** It told the agent to read the
  transcript first and to spend "almost nothing" on static scenes, and said
  nothing about what to do when there is no usable transcript at all. The budget
  rule is now stated as the governing principle: spend in inverse proportion to
  what the transcript carries, so a silent screen recording gets the *most*.
  Also warns that small dense text (metrics, log lines) is legible on a contact
  sheet as structure but not as text, and must be read with `zoom`.
- `docs/PROTOCOL.md` gains a **Grounding** section documenting `verify` and every
  verdict, which had been undocumented since it shipped. The Rails table now says
  the named-gap rail covers `sheet --range` too, matching the code (closes the
  docs/behaviour mismatch reported in 0.7.1).
- `README.md` states the inverse-value rule and drops a stale "v0.3" label.

### Added
- **`nybls doctor` detects a stale installed skill.** The installed
  `~/.claude/skills/watch/SKILL.md` is a copy of the repo's, and had silently
  fallen behind it, the agent ran an outdated protocol for days while every
  other surface reported healthy. `doctor` now compares the two and prints the
  refresh command (username scrubbed, since doctor output ends up in bug reports).

### Fixed
- **The verifier called true claims about silent videos "unsupported".** It could
  not distinguish "the transcript contradicts this" from "there is no transcript
  to check against", both scored 0% coverage. A claim read directly off the
  frames of a real reel (a medallion pipeline with self-recovery) came back
  `unsupported`, which pressures an honest agent into deleting a correct finding.
  New `no-speech` verdict says the method does not apply and the claim needs a
  frame citation. Unjudgeable claims leave the clean-percentage denominator
  rather than counting as failures. Verified not to weaken real verification:
  on an 819-segment transcript a fabricated claim still returns `unsupported`.
- **`probe` gave backwards advice on silent videos.** It closed with "Read the
  transcript first" even when the transcript had just been flagged UNRELIABLE,
  pointing the agent at content that does not exist. A silent screen recording
  is the case where frames are the *only* carrier of information, not a
  low-value case. Caught when four build-in-public reels, whose captions are
  one-line headlines and whose videos contain the full system architecture , 
  were written off as "the substance is in the captions" on the strength of an
  empty transcript. `probe` now inverts its guidance when the guard fires.
- `nybls --version` errored instead of printing a version. The subcommand was
  marked required, so argparse rejected the bare flag, the first thing anyone
  types after installing. Now reads the installed package metadata, so it cannot
  drift from `pyproject.toml`. Covered by a test.
- The `cli.py` docstring still advertised "five commands". There are fifteen.


## [0.7.1] - 2026-09-02

### Fixed
- Degenerate-transcript detection missed the *short* half of the same failure.
  The v0.7.0 check required 20+ segments before examining anything, so a silent
  video producing a single hallucinated line passed as healthy. Four real
  Instagram reels, all silent screen recordings, yielded exactly one line each
  ("Thank you.", "We'll see you next time.", "We'll be right back.", and a
  Spanish request to subscribe) and all four were reported as valid transcripts.
  Stock filler and near-empty transcripts are now flagged with the likely cause.

### Added
- **`nybls corpus <name> --add <ids>`**, group videos from one source into a
  timeline. Each entry carries its publication date and author, so the corpus can
  distinguish *evolution* (one author, different dates) from *disagreement*
  (different authors), the distinction the build-in-public case turns on.
  Videos without a publication date are excluded from evolution detection and
  said to be excluded, rather than silently treated as oldest.
- **Benchmark round 2**, 3 videos, 15 questions, pre-registered, with a tightened control
  arm that could not zoom. `bench/RESULTS_round2.md`. Round 1's 2x margin did not
  replicate; combined result across 4 videos is 35/40 vs 27/40 at 3.26x less cost.
- **`bench/uniform_coverage.py`**, closed-form dead zones and capture probability for a
  uniform grid, plus what it predicts about specific benchmark questions.
- **`bench/measure_event_persistence.py`**, measures how long an on-screen event actually
  persists, so capture probability rests on measurement rather than estimate.
- **`bench/measure_signals.py`**, scores candidate change-detection signals against an
  independent OCR-derived reference.
- **`paper/`**, draft arXiv paper with a fully verified bibliography.

### Changed
- **The change-detection design rule from 0.3.0 is WITHDRAWN.** "Use the hash to detect
  duplicates, never to detect change" was stated from a single observation on a single
  video. Measured against an independent OCR reference across seven videos, perceptual
  hashing and pixel difference are comparable (mean AUC 0.734 vs 0.762; pixel difference
  better on 2 of 4 videos with a usable reference). Pixel difference is retained for a
  narrower, real reason: on static-camera content the hash's distribution compresses into
  the duplicate-detection band. See `bench/RESULTS_signals.md` and `docs/RESEARCH.md` §8.
- The uncited grounding statistic in 0.4.0 was traced to EG-VQA (arXiv:2606.24797) and
  found to combine two different metric columns. Restated at a matched threshold.
- One reference in `docs/RESEARCH.md` (arXiv:2502.19680) did not support the claim made
  of it and has been corrected.

## [0.7.0] - 2026-09-02

### Fixed
- **Silent ASR failure.** Whisper does not fail on audio it cannot handle, it
  loops, emitting the same line indefinitely and reporting success. A real
  25-minute video with no captions fell back to the English-only default model
  over Hindi audio and produced 65 distinct lines across 907, one repeated for 23
  minutes, presented as a healthy transcript. Degenerate output is now detected
  and the transcript labelled UNRELIABLE, naming the model and pointing at
  `--model turbo` when the English-only default is the likely cause.

### Added
- `probe --model tiny|base|small|turbo` to choose the speech model up front.

### Changed
- Benchmark extended to **eight videos, forty questions, sixteen arms**
  (`bench/RESULTS.md`): iterative 80/80, one-shot 65/80, with round 3's iterative
  arms scoring higher on 47% of the images. The gap narrows on short and visually
  repetitive video while the cost advantage persists, one video tied on accuracy
  at half the spend. Two of the judge's own predictions are recorded as wrong.

## [0.6.0] - 2026-09-02

### Fixed
- **Scene drift on targeted frame requests.** A sheet tile labelled "04:15" is
  rendered at 255.035 s, so a request for second 255 returned a different moment , 
  and on fast-cut material, a different shot. Measured across three videos, 21 of
  24 one-second offsets landed in a visibly different shot. Sheets now record the
  exact timestamps they rendered and `frames` snaps to the nearest within three
  seconds, reporting when it does. No new command and no new flag: `frames`
  simply became accurate. Degrades safely, with no sheet yet rendered there is
  nothing to snap to and behaviour is unchanged.

### Changed
- Benchmark extended to **four videos across two domains** (`bench/RESULTS.md`):
  iterative 40/40, one-shot 29/40, with the difference concentrated in brief
  on-screen graphics falling between uniform samples, replicated four times.
  The round-1 prediction that fast-cut material would widen the gap is recorded
  as only half right: directionally correct, but overstated.

### Maturity
- The **watching core** (probe, study, sheet, frames, zoom, ledger, verify) is now
  beta-quality: 24 tests, benchmarked on four videos, interface stable.
- The **extraction layer** (contract, extract-check) remains alpha, single-video
  only; the corpus half is not built.

## [0.5.0] - 2026-09-02

### Added
- **`nybls contract --purpose "..." --shape teach|rebuild|procedure|brief`** , 
  the extraction contract for a stated purpose. Every comparable tool hardcodes
  one ontology; the shape of what you extract should follow from why you are
  extracting it. Teaching a beginner and reconstructing a system want different
  objects out of the same video.
- **`nybls extract-check <id> --file out.json`**, validates an extraction
  against its contract *and* mechanically verifies every citation, reported
  separately. Cross-references must resolve: a prerequisite pointing at nothing,
  or a contradiction naming a claim that is not present, is an error.
- Claims carry two clocks. `at` (video time) and `observed` (publication date)
 , after ATOM (arXiv:2510.22590). The second only matters across a corpus, where
  it separates "two sources disagree" from "one person changed their mind".
- **First test suite** (18 tests) over the two pure-logic modules, including a
  control that a plausible but fabricated claim must fail verification.

### Notes
- Structural validation is dependency-free on purpose. The schemas are simple and
  every added dependency is install friction.

## [0.4.0] - 2026-09-02

### Added
- **`nybls verify <id> --claims claims.json`**, mechanical citation checking.
  Every claim names a timestamp; the verifier pulls the transcript window around
  it and reports the fraction of the claim's content words actually present, as
  `verified` / `weak` / `unsupported`, listing what it could not find.
  A citation is never trusted because a model asserted it.

  Rationale: on a 2026 grounded-video-QA benchmark, frontier models scored 8.5%
  and 1.5% on evidence grounding while scoring 45% and 41% on answer accuracy.
  Every large quality gain in that literature came from adding a separate
  checking step, not from better prompting.

  Validated against a hand-made extraction of a 48-minute lesson: 14 of 15 claims
  verified, and a deliberately wrong control claim was caught at 22%.

### Fixed
- The verifier's first version produced a false negative on a correct claim,
  because ASR and a written claim disagree on word form ("ask"/"asking",
  "save"/"saves") and on numerals ("90%" vs "90 percent"). Added light suffix
  stripping and numeral normalisation; the control claim still fails at 22%,
  so the check did not simply get looser.

## [0.3.0] - 2026-09-02

### Added
- **`nybls study --adaptive`**, probes the video densely at low resolution for
  free (no vision tokens), scores each probe by how much the picture changed, and
  spends the image budget only on the biggest changes. A uniform backbone is
  merged in so a quiet stretch is never wholly unrepresented. `--region x,y,w,h`
  restricts scoring to part of the frame; `--max-frames` bounds the spend.
  On a 48-minute lesson: 583 probes free, 71 frames looked at, 12 images total , 
  5-second temporal resolution for less than a uniform 30-second pass costs.

### Fixed
- The adaptive sampler's first implementation used perceptual hashing to detect
  change. That was backwards: a perceptual hash is designed to be *robust* to
  small changes. Measured on the test video, board states ten seconds apart
  differed by 2-4 bits of a 64-bit hash, below any usable threshold, so real
  moves were classified as "no change". Replaced with mean absolute pixel
  difference, which separates the quiet floor (0.03-0.3) from move and
  annotation activity (1.0-1.8) cleanly. **Use the hash to detect duplicates,
  never to detect change.**
- The probe loop capped at 400 samples, silently truncating coverage of anything
  longer than ~33 minutes at a 5-second probe interval.

## [0.2.0] - 2026-09-02

### Added
- **`nybls study`**, a comprehension pass over the whole video. Samples on a
  clock (10s/20s/30s/45s by length, `--every` to override) and emits every sheet
  at once. For dense instructional video, minimal spend was the wrong objective:
  a 48-minute lesson answered with one image describes the format, not the
  content.

### Changed
- The protocol now distinguishes **answer mode** (a question exists; stop when
  answered) from **study mode** (comprehension; cover the whole video). The skill
  defaults to study mode for instructional material when intent is ambiguous.

### Known limitation, now documented
- **Scene detection is the wrong signal for static-camera content.** A 48-minute
  chess lesson recorded as one continuous screen capture produced three scene
  cuts, while the board changed every move. Study mode therefore ignores scenes
  entirely and samples on a clock. Scene-adaptive sheets remain the default for
  edited footage.

## [0.1.1] - 2026-09-01

### Fixed
- `sheet` did not check the budget at all, so contact sheets could be generated
  past the ceiling without refusal. It now goes through the same gate as
  `frames` and `zoom`.
- `sheet` rejected `--looking-for`, which `frames` and `zoom` require, an
  inconsistency that made a targeted sheet impossible to justify. It now accepts
  both `--looking-for` and `--force`.

### Changed
- The named-gap rule now distinguishes coverage from targeting: a whole-video
  `sheet` is the coverage round and never needs a named gap, while a `--range`
  sheet is a targeted request and requires one once spending has begun.

## [0.1.0] - 2026-09-01

First release. Alpha: the interfaces may change.

### Added
- **Frame server** with five verbs: `probe`, `sheet`, `frames`, `zoom`, `ledger`
- **The WATCH protocol** as a Claude Code skill, transcript-first, coverage by
  contact sheet, a mandatory confidence evaluator, named-gap requests, and stop
  rules (`docs/PROTOCOL.md`)
- **Cumulative budget ledger**, duration-scaled budget, visual-token estimates
  matching Claude API billing, and per-command spend reporting
- **Protocol rails enforced by the tool**: `--looking-for` required past three
  spent images, refusal past budget without an explicit human `--force`,
  near-duplicate frame warnings, a ten-frame per-call cap, and next-step nudges
  in every command's output
- **Acquisition** via yt-dlp for YouTube and ~1,800 other sites, plus local files
- **Transcription**: platform captions when available, local whisper.cpp otherwise
- **Scene-aware sampling** via PySceneDetect with perceptual-hash deduplication
- **Optional phone-share receiver**, off by default, time-limited window,
  token-authenticated, private-interface binding, and per-item human approval
  before anything is fetched
- Documentation: protocol reference, research and attribution, security posture
- Claude Code plugin and marketplace manifests

### Known issues
- Whisper emits a hallucinated line on silent audio; the transcript for a
  speechless clip may contain one phantom sentence. Detection is not yet implemented.
- Instagram acquisition depends on session cookies and breaks when the platform
  presents a consent or checkpoint wall; the error message explains the fix but
  clearing it requires a browser.
