<p align="center">
  <img src="brand/nybls_1024.png" alt="nybls" width="120">
</p>

<h1 align="center">nybls</h1>

<p align="center">
  <b>Your AI reads the subtitles. This one actually looks — and shows you what it looked at.</b>
</p>

---

```console
$ nybls probe "https://www.youtube.com/watch?v=f1wnYdLEpgI"

id: f1wnYdLEpgI
title: Learn Git Rebase in 6 minutes // explained with live animations!
duration: 6.7 min · 1280x720 · 10 scenes
transcript: captions:video.en.vtt → ~/.nybls/store/f1wnYdLEpgI/transcript.txt
budget: 27 image units
cost so far: 0 images. Read the transcript first; then request sheets.

$ nybls study f1wnYdLEpgI --adaptive

probing every 5s at low resolution (no vision cost)...
probed 80 frames free → kept the 33 biggest changes (median change score 1.83)
study pass: 33 tiles every 5s → 6 sheets (6 of 27 budget units)
  sheet_000.png  [00:12–01:12]
  sheet_001.png  [01:22–02:17]
  ...
spend: 6 images / 27 budget

$ nybls ledger f1wnYdLEpgI

watched 7 min · examined 6 images (~6,240 visual tokens, ≈$0.01)
of ~10,059 total frames
```

*Verbatim output, not a mockup.* It checked 80 frames for free to decide which 33
mattered, then packed them into **6 images**. Pulling frames is nearly free;
*looking* at them is what costs money, so it only looks at what changed.

On a 48-minute lesson the same command probes 583 frames and looks at 12.

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

[Protocol](docs/PROTOCOL.md) · [Research & evidence](docs/RESEARCH.md) · [Security](docs/SECURITY.md) · [Benchmark](bench/RESULTS.md) · [Changelog](CHANGELOG.md)

MIT.
