# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Independent benchmark of the iterative loop against a one-shot frame dump at
  equal cost — the open gap named in `docs/RESEARCH.md`
- Simplified small-size logo variant for favicon rendering
- Optional MCP server wrapper so non-Claude-Code agents can use the same verbs

## [0.5.0] — 2026-09-02

### Added
- **`nybls contract --purpose "..." --shape teach|rebuild|procedure|brief`** —
  the extraction contract for a stated purpose. Every comparable tool hardcodes
  one ontology; the shape of what you extract should follow from why you are
  extracting it. Teaching a beginner and reconstructing a system want different
  objects out of the same video.
- **`nybls extract-check <id> --file out.json`** — validates an extraction
  against its contract *and* mechanically verifies every citation, reported
  separately. Cross-references must resolve: a prerequisite pointing at nothing,
  or a contradiction naming a claim that is not present, is an error.
- Claims carry two clocks — `at` (video time) and `observed` (publication date)
  — after ATOM (arXiv:2510.22590). The second only matters across a corpus, where
  it separates "two sources disagree" from "one person changed their mind".
- **First test suite** (18 tests) over the two pure-logic modules, including a
  control that a plausible but fabricated claim must fail verification.

### Notes
- Structural validation is dependency-free on purpose. The schemas are simple and
  every added dependency is install friction.

## [0.4.0] — 2026-09-02

### Added
- **`nybls verify <id> --claims claims.json`** — mechanical citation checking.
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

## [0.3.0] — 2026-09-02

### Added
- **`nybls study --adaptive`** — probes the video densely at low resolution for
  free (no vision tokens), scores each probe by how much the picture changed, and
  spends the image budget only on the biggest changes. A uniform backbone is
  merged in so a quiet stretch is never wholly unrepresented. `--region x,y,w,h`
  restricts scoring to part of the frame; `--max-frames` bounds the spend.
  On a 48-minute lesson: 583 probes free, 71 frames looked at, 12 images total —
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

## [0.2.0] — 2026-09-02

### Added
- **`nybls study`** — a comprehension pass over the whole video. Samples on a
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

## [0.1.1] — 2026-09-01

### Fixed
- `sheet` did not check the budget at all, so contact sheets could be generated
  past the ceiling without refusal. It now goes through the same gate as
  `frames` and `zoom`.
- `sheet` rejected `--looking-for`, which `frames` and `zoom` require — an
  inconsistency that made a targeted sheet impossible to justify. It now accepts
  both `--looking-for` and `--force`.

### Changed
- The named-gap rule now distinguishes coverage from targeting: a whole-video
  `sheet` is the coverage round and never needs a named gap, while a `--range`
  sheet is a targeted request and requires one once spending has begun.

## [0.1.0] — 2026-09-01

First release. Alpha: the interfaces may change.

### Added
- **Frame server** with five verbs: `probe`, `sheet`, `frames`, `zoom`, `ledger`
- **The WATCH protocol** as a Claude Code skill — transcript-first, coverage by
  contact sheet, a mandatory confidence evaluator, named-gap requests, and stop
  rules (`docs/PROTOCOL.md`)
- **Cumulative budget ledger** — duration-scaled budget, visual-token estimates
  matching Claude API billing, and per-command spend reporting
- **Protocol rails enforced by the tool**: `--looking-for` required past three
  spent images, refusal past budget without an explicit human `--force`,
  near-duplicate frame warnings, a ten-frame per-call cap, and next-step nudges
  in every command's output
- **Acquisition** via yt-dlp for YouTube and ~1,800 other sites, plus local files
- **Transcription**: platform captions when available, local whisper.cpp otherwise
- **Scene-aware sampling** via PySceneDetect with perceptual-hash deduplication
- **Optional phone-share receiver** — off by default, time-limited window,
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
