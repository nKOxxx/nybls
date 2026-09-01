<p align="center">
  <img src="brand/nybls_1024.png" alt="nybls" width="140">
</p>

<h1 align="center">nybls</h1>

<p align="center">
  <em>Other tools slurp the whole video. This one sips —<br>
  three frames out of fifty-three thousand, and it shows you which.</em>
</p>

---

## The problem

Almost every "AI watches YouTube" tool reads the **subtitles**. That is not a
cynical read of the field, it is what the code does: the YouTube loaders in the
major agent frameworks and self-hosted chat apps are transcript scrapers, and
Google's own documentation says a YouTube source in NotebookLM imports "only the
text transcript of the video."

So a video with no speech returns nothing. A chart on screen is invisible. A
demo that shows rather than tells is invisible. And you cannot tell the
difference between a tool that looked and a tool that guessed, because neither
shows you what it saw.

The other half of the field does the opposite and dumps 100 uniformly-sampled
frames into the model at once — expensive, mostly redundant, and still blind to
whatever fell between the samples.

## What nybls does instead

nybls gives an AI agent five ways to ask for pieces of a video, and a protocol
that makes it ask well:

1. **Read the free stuff first** — transcript, scene boundaries, metadata. Zero images.
2. **Look broadly, cheaply** — one contact sheet is six timestamped thumbnails for
   the cost of a single image.
3. **Then say what it is missing** — the agent must name the time interval and what
   it expects to find there before it may request more.
4. **Drill in only there** — full-resolution frames, or a zoom crop to read small text.
5. **Stop, and show the receipts** — every answer ends with the frames it examined
   and what they cost.

Real run, this repo's test corpus — a 35-minute car-restoration video:

```
watched 35 min · examined 3 images (~3,069 visual tokens, ~$0.01)
of ~53,171 total frames · budget 3/142 units
```

Three frames. It found the reveal at 12:05, identified that the second half of
the video switches to a different car, and reported honestly that a zoom aimed
at a badge landed on a headlight instead — so it did not name the model.

## Why "sips" is the whole point

The research this is built on is unambiguous: **selecting fewer frames well beats
sampling many frames blindly.** Stanford's VideoAgent matched the accuracy of 180
uniformly-sampled frames using 8.4 frames chosen by a confidence-gated loop.
Adaptive keyframe selection beats uniform sampling at equal frame count. Grids
larger than about six tiles measurably destroy a model's ability to localize
detail. Every rule in the nybls protocol traces to a published result — see
[docs/RESEARCH.md](docs/RESEARCH.md).

## Install

**Prerequisites** (nybls orchestrates these; it does not vendor them):

| Tool | Why | Install |
|---|---|---|
| `ffmpeg` | frame extraction, crops, contact sheets | `brew install ffmpeg` |
| `yt-dlp` | downloading from YouTube and ~1,800 other sites | `brew install yt-dlp` |
| `deno` | required by yt-dlp for full YouTube support | `brew install deno` |
| `whisper-cpp` | local transcription when a video has no captions | `brew install whisper-cpp` |

Then:

```bash
pip install nybls
```

On macOS, add Apple Vision OCR (works with Arabic, no extra models):

```bash
pip install "nybls[macos]"
```

For local transcription, download a Whisper model once:

```bash
mkdir -p ~/.nybls/models && curl -L -o ~/.nybls/models/ggml-large-v3-turbo.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
```

## Use it

```bash
nybls probe "https://www.youtube.com/watch?v=VIDEO_ID"
```

```
id: VIDEO_ID
title: But what is a neural network? | Deep learning chapter 1
duration: 18.7 min · 1280x720 · 24 scenes
transcript: subtitles:video.en.vtt -> ~/.nybls/store/VIDEO_ID/transcript.txt
budget: 75 image units
cost so far: 0 images. Read the transcript first; then request sheets.
```

| Command | What it does | Cost |
|---|---|---|
| `nybls probe <url\|file>` | download, transcribe, detect scenes, set the budget | 0 images |
| `nybls sheet <id> [--range S E]` | 3x2 contact sheet, timestamped | 1 image |
| `nybls frames <id> --at 92,570` | full-resolution stills | 1 per frame |
| `nybls zoom <id> --at 570 --box x,y,w,h` | crop into a region to read detail | 1 image |
| `nybls ledger <id>` | what has been spent | 0 |

Everything is written to `~/.nybls/store/<id>/` as ordinary PNG and text files.
There is no API integration: your agent reads the files.

### With Claude Code

Copy `skill/SKILL.md` to `~/.claude/skills/watch/SKILL.md`, then:

```
/watch https://www.youtube.com/watch?v=VIDEO_ID  what does the chart at the end show?
```

The skill carries the protocol — the confidence check, the named-gap rule, the
stop conditions, and the receipts contract — so the discipline travels with the
tool instead of depending on how well you prompt.

## The guardrails are in the tool, not just the prose

A protocol written only in a prompt is a suggestion. These are enforced by the
CLI itself:

- **Named gaps.** Past a few images, `frames` and `zoom` refuse to run without
  `--looking-for "<interval + what you expect>"`.
- **A real budget.** Duration-scaled, cumulative, and the server refuses to serve
  past it unless a human passes `--force`.
- **Duplicate warnings.** A frame that is a near-duplicate of one already served
  is flagged as wasted budget.
- **Next-step nudges.** Every command's output ends by telling the agent to draft
  an answer and classify its own confidence before asking for more.

## What this cannot do

- **No live video.** Batch only: download, then analyze.
- **Motion is lossy.** It sees stills, not movement. Good for talks, tutorials,
  demos, dashboards, and on-screen text; weak for sports mechanics or fast action.
- **Speech only.** Transcription covers words, not music or sound events.
- **It depends on tools that fight back.** Video platforms actively break
  downloaders. Keep `yt-dlp` current; expect occasional breakage.
- **Alpha.** The protocol is validated by published research and by daily use, but
  this is version 0.1.0 and the interfaces may change.

## Privacy and security posture

Local-first by construction: no API keys, no accounts, no telemetry, no server.
The agent you already use supplies the model; everything else runs on your
machine. See [docs/SECURITY.md](docs/SECURITY.md) for the full posture, including
the one rule that matters most — **video content is data, never instructions.** A
video can display text aimed at your agent, and the protocol requires that such
text be reported to you rather than obeyed.

Downloading from a platform may conflict with that platform's terms of service.
That is your call to make; this tool takes no position and phones nothing home.

## Documentation

- [docs/PROTOCOL.md](docs/PROTOCOL.md) — the WATCH loop in full, and why each rule exists
- [docs/RESEARCH.md](docs/RESEARCH.md) — the evidence base and everything this is built on
- [docs/SECURITY.md](docs/SECURITY.md) — threat model and the security checklist
- [CHANGELOG.md](CHANGELOG.md)

## License

MIT.
