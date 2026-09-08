<p align="center">
  <img src="brand/nybls_1024.png" alt="nybls" width="120">
</p>

<h1 align="center">nybls</h1>

<p align="center">
  <b>Your AI reads the subtitles. This one actually looks, and shows you what it looked at.</b>
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
  sheet_000.png  [00:07-01:52]
  sheet_002.png  [10:30-19:32]
  sheet_007.png  [34:12-37:30]
  ...

$ nybls ledger F2FmTdLtb_4

watched 54 min · examined 12 images (~12,480 visual tokens, ≈$0.02)
of ~80,443 total frames
```

**A 54-minute course. 12 images. Two cents.** *Verbatim output, not a mockup.*

It pulled 644 frames for free to work out which 72 were worth looking at, then
packed them into 12 sheets. Pulling frames is nearly free, but looking at them is
what costs money, so it only looks at what changed.

The frames it picked were the right ones. A single sheet from the middle of the
course covers a tradeoffs diagram, the throughput versus latency slide, TCP
against UDP, a TCP header breakdown, the networking infrastructure slide, and
live browser devtools showing a real HTTP request. Six distinct teaching moments,
and not one redundant shot of a talking head.

You do not have to ask it anything to get that. Pasting a URL on its own means
"digest this", and that is [the common case](#you-do-not-need-to-ask-it-anything).

## Why this exists

Almost every tool that claims to watch YouTube is really just reading the
captions. That is not a cheap shot, it is what the code does: the YouTube loaders
in the major agent frameworks are caption scrapers, and Google's own
documentation says a YouTube source in NotebookLM imports "only the text
transcript."

The consequence is that a video with no speech returns nothing at all, a chart
might as well not be there, and a demo that shows rather than tells is invisible.
Worse, you cannot tell a tool that looked from one that guessed, because neither
of them shows you any evidence.

The other half of the field takes the opposite approach and dumps a hundred
evenly spaced frames on the model in the hope that something useful lands. That
is expensive, mostly redundant, and still blind to anything that happened between
two samples.

## Install

**Or let Claude do it.** Paste this repository's URL into Claude Code and say
"install this". [INSTALL.md](INSTALL.md) is written to be followed by an agent:
it detects the platform, installs what is needed, verifies the result with
`nybls doctor`, and is told to stop and say so rather than improvise if
something cannot be installed.

By hand, two lines:

```bash
brew install ffmpeg pipx
```

```bash
pipx install "nybls[download]"
```

**Use pipx, not pip.** Homebrew's Python, and most current Linux distributions,
refuse `pip install` into the system environment under PEP 668, so `pip install
nybls` fails outright on a normal modern Mac. pipx is built for command line
tools: it puts nybls in its own environment and the `nybls` command on your PATH.
If you would rather not add pipx, a virtual environment works too:
`python3 -m venv ~/.venvs/nybls && ~/.venvs/nybls/bin/pip install "nybls[download]"`.

ffmpeg is the only thing that needs a system package manager, because nothing
else can decode a video. On Linux that line is `sudo apt install ffmpeg pipx` or
your distribution's equivalent; [INSTALL.md](INSTALL.md) has the table. The
`[download]` extra pulls in yt-dlp for URLs and adds about 25 MB. Plain
`pipx install nybls` works fine on local files.

That is the whole setup. There are no API keys, no account and no telemetry,
because your agent brings its own model and everything else runs on your machine.
The base install comes to about 50 MB, which is numpy and Pillow and nothing
else. It was 293 MB before 0.8.0, and the difference was two libraries we were
using one function from each.

Videos without captions need speech recognition, which is one more line
(`brew install whisper-cpp`). The model fetches itself the first time you need
it, and the default is 141 MB rather than 1.5 GB.

```bash
nybls doctor
```

tells you what works, and what any missing piece would unlock.

## What it does

| | |
|---|---|
| `probe` | Ingest a URL or a local file, pull captions or transcribe locally, map the scenes. Costs nothing. |
| `sheet` | Six timestamped thumbnails in one image, so the model can see where to look before it spends. |
| `frames` | Full resolution stills at the moments that turned out to matter. |
| `zoom` | Crop into one frame to read small text, a chart axis, a log line. |
| `study` | Cover a whole video properly, for when you want to learn it rather than query it. |
| `speakers` | Work out who is on screen across a recorded call, from free probes. |
| `verify` | Check every cited timestamp against the transcript, mechanically. |
| `contract` | Shape an extraction for a purpose: teach, rebuild, procedure, brief. |
| `corpus` | Put several videos from one source on a timeline and see what changed. |
| `ledger` | What you spent, in images, tokens and cents. |

Everything lands in `~/.nybls/store/<id>/` as ordinary PNGs and text files. There
is no API to integrate against, because your agent simply reads the files.

### With Claude Code

The plugin drives the CLI, it does not replace it, so install the CLI first or
the skill will have nothing to run:

```
brew install ffmpeg pipx
pipx install "nybls[download]"
/plugin marketplace add nKOxxx/nybls
/plugin install nybls@nybls
```

Then restart Claude Code, or run `/reload-plugins`. A newly installed plugin
does not load into a session that is already running, and neither command says
so.

Then just ask it about a video. The plugin ships the protocol itself, including a
mandatory confidence check on every round, a rule that the model has to name what
it is missing before it may ask for more, and a receipts contract. The discipline
travels with the tool instead of depending on how carefully you prompted.

## Reviewing a recorded call

When a call is recorded in speaker view, the picture cuts to whoever is talking,
which means a shot change is a turn boundary. nybls already detects visual change
for free, so it can work out the shape of a conversation without spending
anything on vision.

```console
$ nybls speakers my-client-call.mp4

probed 600 frames every 3s over 30 min, free (no vision cost)
6 distinct shots · picture changes every 9s

  shot 0   48.5%   14.6 min  ###################
  shot 1   37.8%   11.3 min  ###############
  shot 2    5.7%    1.7 min  ##
```

You tell it once which shot is you and who the others are, and from that point
every line of the transcript has a speaker attached. That is enough to answer the
questions people actually want answered about their own calls: how much of it did
you talk, did you ask something and then fill the silence yourself four seconds
later, and which buying signal went past unremarked.

Naming solves identity and the video solves segmentation, so both halves are
needed. If the camera was off there is nothing to attach a name to.

## You do not need to ask it anything

Paste a URL and stop there. That is a complete instruction, and it is the common
case.

```
https://www.youtube.com/watch?v=...
```

With no question attached, nybls reads it as "digest this" and runs **study
mode**: it covers the whole video, end to end, and hands back what the video
actually contains. Spending as little as possible is the wrong goal here. A
48-minute lesson answered from a single image describes the layout instead of
the content, so study mode deliberately does not stop early.

Ask a question instead and it switches to **answer mode**, which stops the moment
it can answer. A 35-minute video, asked only what happens in it, came back for
three images and about a cent.

You never choose between them. The presence or absence of a question decides it.

### Turning a video into something that lasts

A digest you read once and lose is not much better than watching it yourself. If
you want the video to leave something behind, a set of notes, a decision record,
a procedure your agent can follow later, ask for a **contract**:

```bash
nybls contract --purpose "teach me the technique in this video" --shape teach
```

Four shapes, each a different job. `teach` pulls out concepts, prerequisites,
worked examples and the errors people make. `rebuild` pulls out decisions and
the reasoning behind them, so you can build your own version of what you
watched. `procedure` pulls out ordered steps with checkpoints. `brief` pulls out
claims and what backs each one.

Every field carries a timestamp, and `nybls verify` checks those citations
against the transcript mechanically. So what you keep is grounded in the video
rather than in the model's memory of it, which is the difference between notes
you can trust and notes you have to re-check.

## Why it is cheap without being lazy

Scene detection turns out to be the wrong signal for a fixed camera. A 48-minute
chess lesson filmed as one continuous screen capture produces three scene cuts,
while the board, which carries all of the information, changes every move. Slide
decks, IDEs and dashboards all have that same shape.

So `--adaptive` samples on a clock instead, scores each probe by how much the
picture actually changed, and spends the budget where the changes are biggest. On
that lesson it caught an on-screen framework card that a uniform pass every 30
seconds sampled straight past.

The deeper pattern is that the value of looking runs inverse to whatever the
transcript already carries. A podcast barely needs frames at all. A silent screen
recording, whether that is a build-in-public demo, a dashboard or a tutorial set
to music, has no transcript worth reading, and the frames are the only place its
content exists. Four short reels with one-line captions turned out to hold an
entire data pipeline architecture, complete with table names and retry logic
firing, along with a product restructure that no caption mentioned anywhere.

## Does it actually work

Four rounds, 12 videos, 112 audited questions. A control arm that gets a uniform
grid of frames scores 83 of 112, or 74 percent, for 645,120 visual tokens. nybls
scores 101 of 112, or 90 percent, for 189,052. The control spends 3.41 times the
tokens to get 82 percent of the score.

Round 4 was run properly, which matters more than the numbers. The questions and
the ground truth were written by an agent with no access to nybls, working from a
dense uniform grid. The arms answered separately. A third agent scored them with
the arms labelled X and Y and the mapping withheld, so the scoring was blind.
Earlier rounds had the experimenter write the questions and mark the results,
which is exactly the weakness you would expect it to be.

The mechanism held up too. Every question was labelled at design time as
persistent or transient, and on silent screen recordings the two arms tied 18 to
18 on persistent items. Every single point that separated them came from
transient ones, and the control's failures were all on things that were on screen
for under two seconds. That is the argument for adaptive sampling, tested
directly rather than asserted.

Four earlier questions were voided when an audit found the narration stated the
answer, and that audit is published alongside the results.

## Honest limits

- **No live video.** Download first, then analyse.
- **Motion is lossy,** because it works from stills. That suits talks, tutorials,
  demos, dashboards and anything with text on screen, and it does badly on sports
  and fast action.
- **Speech only,** meaning words rather than music or sound events.
- **Call review is new and thinly tested.** The shot clustering has been measured
  properly on one call. Speaker view works; gallery view has not been tested; and
  during a screen share nobody's face is on screen, so attribution stops exactly
  where a demo begins. Screen time is also a proxy for talk time rather than a
  measurement of it.
- **Platforms fight downloaders,** so keep `yt-dlp` current and expect the
  occasional breakage.
- **Still early.** Interfaces may change before 1.0. See `CHANGELOG.md`.

Video content is treated as **data and never as instructions**. A video can put
text on screen aimed squarely at your agent, and the protocol requires that it be
reported to you rather than obeyed.

## Docs

[Install](INSTALL.md) · [Protocol](docs/PROTOCOL.md) · [Research and evidence](docs/RESEARCH.md) · [Security](docs/SECURITY.md) · [Changelog](CHANGELOG.md)

Benchmarks: [round 1](bench/RESULTS.md) · [round 2](bench/RESULTS_round2.md) · [round 3](bench/RESULTS_round3.md) · [round 4, blind judged](bench/RESULTS_round4.md) · [question audit](bench/QUESTION_AUDIT.md) · [where information lives](bench/RESULTS_modality.md) · [change detection signals](bench/RESULTS_signals.md)

MIT.
