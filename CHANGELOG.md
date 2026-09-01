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
