<p align="center">
  <img src="brand/nybls_1024.png" alt="nybls" width="120">
</p>

<h1 align="center">nybls</h1>

<p align="center">
  <b>Your AI reads the subtitles. This one actually looks — and shows you what it looked at.</b>
</p>

---

```console
$ nybls probe "https://www.youtube.com/watch?v=F2FmTdLtb_4"

id: F2FmTdLtb_4
title: System Design Concepts Course and Interview Prep
duration: 53.6 min · 1280x720 · 64 scenes
transcript: captions:video.en.vtt → ~/.nybls/store/F2FmTdLtb_4/transcript.txt
budget: 200 image units
cost so far: 0 images. Read the transcript first; then request sheets.

$ nybls study F2FmTdLtb_4 --adaptive

probing every 5s at low resolution (no vision cost)...
probed 644 frames free → kept the 72 biggest changes (median change score 1.56)
study pass: 72 tiles every 5s → 12 sheets (12 of 200 budget units)
  sheet_000.png  [00:07–01:52]
  sheet_002.png  [10:30–19:32]
  sheet_007.png  [34:12–37:30]
  ...

$ nybls ledger F2FmTdLtb_4

watched 54 min · examined 12 images (~12,480 visual tokens, ≈$0.02)
of ~80,443 total frames
```

**A 54-minute course. 12 images. Two cents.** *Verbatim output, not a mockup.*

It pulled 644 frames for free to work out which 72 were worth looking at, then
packed them into 12 sheets. Pulling frames is nearly free; *looking* at them is
what costs money — so it only looks at what changed.

And the frames are the right ones. One sheet from the middle covers a tradeoffs
diagram, the throughput-vs-latency slide, TCP versus UDP, a TCP header
breakdown, the networking-infrastructure slide, and live browser devtools showing
a real HTTP request — six distinct teaching moments, no redundant talking head.

## Why this exists

Almost every "AI watches YouTube" tool reads the **captions**. That's not a cheap
shot, it's what the code does — the YouTube loaders in the major agent frameworks
and self-hosted chat apps are caption scrapers, and Google's own docs say a
YouTube source in NotebookLM imports "only the text transcript."

So a video with no speech returns nothing. A chart is invisible. A demo that
shows rather than tells is invisible. And you can't tell a tool that looked from
one that guessed, because neither shows you its evidence.

The other half of the field dumps 100 evenly-spaced frames at the model and hopes.
Expensive, mostly redundant, and still blind to whatever fell between samples.

## Install

```bash
brew install ffmpeg yt-dlp
```

```bash
pip install nybls
```

That's it. No API keys, no account, no telemetry — your agent brings the model,
everything else runs locally. Videos without captions need speech, which is an
extra one-liner (`brew install whisper-cpp`); the model downloads itself the
first time you need it, and the default is 141 MB, not 1.5 GB.

```bash
nybls doctor
```

tells you exactly what works and what any missing piece would unlock.

## The three commands you'll actually use

```bash
nybls probe "https://www.youtube.com/watch?v=..."   # transcript + scenes, 0 images
nybls study <id> --adaptive                          # learn the whole thing
nybls sheet <id>                                     # one look, 6 timestamps
```

Everything lands in `~/.nybls/store/<id>/` as ordinary PNGs and text. There's no
API integration — your agent just reads the files.

### With Claude Code

```
/plugin marketplace add nKOxxx/nybls
/plugin install nybls@nybls
```

Then ask it anything about a video. The plugin ships the protocol — a mandatory
confidence check each round, a rule that the model must name what it's missing
before it may ask for more, and a receipts contract — so the discipline travels
with the tool instead of depending on how well you prompt.

## Two modes, and it picks for you

**Answer mode** — you asked a question, so it stops the moment it can answer.
A 35-minute video, "what happens in it?", answered with **3 images for a cent**.

**Study mode** — you want to *learn* the thing, so it covers the whole video.
Minimal spend is the wrong goal for a lecture; a 48-minute lesson answered with
one image describes the layout, not the content.

## Why it's cheap without being lazy

Scene detection is the wrong signal for a fixed-camera recording. A 48-minute
chess lesson filmed as one continuous screen capture produces **three** scene
cuts — while the board, carrying all the information, changes every move. Slide
decks, IDEs and dashboards have the same shape.

So `--adaptive` samples on a clock, scores each probe by how much the picture
actually changed, and spends the budget on the biggest changes. On that lesson it
caught an on-screen framework card that a uniform 30-second pass sampled straight
past.

## Honest limits

- **No live video.** Download, then analyse.
- **Motion is lossy.** It sees stills. Great for talks, tutorials, demos,
  dashboards, on-screen text. Weak for sports and fast action.
- **Speech only** — words, not music or sound events.
- **Platforms fight downloaders.** Keep `yt-dlp` current; expect occasional breakage.
- **Alpha.** v0.3, interfaces may change.

Video content is **data, never instructions** — a video can display text aimed at
your agent, and the protocol requires that it be reported to you, not obeyed.

## Docs

[Protocol](docs/PROTOCOL.md) · [Research & evidence](docs/RESEARCH.md) · [Security](docs/SECURITY.md) · [Changelog](CHANGELOG.md)

Benchmarks: [round 1](bench/RESULTS.md) · [round 2](bench/RESULTS_round2.md) · [change-detection signals](bench/RESULTS_signals.md) · [paper draft](paper/)

MIT.
