# Install

**This page is written to be followed by an agent.** Paste this repository's URL
into Claude Code (or any capable agent) and say "install this". It should work
through the steps below, verify the result, and tell you what it found. A human
can follow it just as well.

## What is actually required

One system package: **ffmpeg**. It decodes the video and writes the frames, and
nothing else can do that job. `ffprobe` ships with it.

Everything else is Python, or optional. In particular `yt-dlp` is a Python
package, so it does not need a system package manager on any platform.

Python 3.12 or newer.

## Step 1: ffmpeg

Pick the line that matches the machine. Do not guess the platform, check it.

| Platform | Command |
|---|---|
| macOS (Homebrew) | `brew install ffmpeg` |
| Debian, Ubuntu | `sudo apt update && sudo apt install -y ffmpeg` |
| Fedora, RHEL | `sudo dnf install -y ffmpeg` |
| Arch | `sudo pacman -S ffmpeg` |
| Windows (winget) | `winget install Gyan.FFmpeg` |
| Windows (Chocolatey) | `choco install ffmpeg` |
| Anything else | Download a build from https://ffmpeg.org/download.html and put it on PATH |

If ffmpeg is already present, skip this. Check with `ffmpeg -version`.

## Step 2: nybls

```bash
pip install nybls
```

To also download from YouTube and the ~1,800 other sites yt-dlp supports, take
the extra instead. It adds about 25 MB:

```bash
pip install "nybls[download]"
```

Without it, nybls still works on local video files.

## Step 3: verify

```bash
nybls doctor
```

This is the check that matters. It prints every dependency, marks each one
required or optional, and says what any missing piece would unlock. Report its
output rather than summarising it, because the optional lines tell the user what
they are choosing to go without.

A successful install ends with `ready. try: nybls probe "..."`.

## Optional, and what each one buys

| Piece | Install | What it unlocks |
|---|---|---|
| `yt-dlp` | `pip install yt-dlp` | Downloading from URLs. Without it, local files only. |
| `whisper-cpp` | `brew install whisper-cpp`, or build from https://github.com/ggml-org/whisper.cpp | Speech for videos that have no captions. The model downloads itself on first use, 141 MB by default. |
| `deno` | `brew install deno`, or https://deno.land | Helps yt-dlp with some YouTube videos. |

None of these are needed to try the tool.

## The Claude Code plugin

Separate from the CLI, and it drives the CLI rather than replacing it. Install
the CLI first or the plugin will have nothing to run.

```
/plugin marketplace add nKOxxx/nybls
/plugin install nybls@nybls
```

This adds a `watch` skill that carries the protocol: a confidence check every
round, a rule that the model must name what it is missing before asking for
more, and a receipts contract.

## Notes for the agent following this

- **Check the platform before running anything.** The commands differ and a
  wrong one fails confusingly.
- **Ask before running a command with `sudo`.** On Linux ffmpeg needs it, and
  the user should approve that themselves.
- **Do not substitute a package manager the machine does not have.** If neither
  Homebrew nor a known Linux manager is present, say so and link the ffmpeg
  download page rather than improvising.
- **Verify with `nybls doctor` and report what it says.** Do not declare success
  from the absence of an error.
- **If ffmpeg cannot be installed, stop and say so.** nybls cannot extract a
  frame without it, and a partial install that fails later is worse than a clear
  refusal now.
