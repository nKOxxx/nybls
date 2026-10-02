# Answers, "Silent Coding Session - Rust Lang - 1" (Muttley Dev, 12:06)

Arm: no video, no transcript. Evidence available: title, channel, duration only, plus general knowledge.

## 1. Web page title and domain in the browser on the left

**Answer:** insufficient evidence.

**Basis:** metadata only. The title says this is a Rust coding session, so a plausible inference is that the page is the Rust Book (doc.rust-lang.org) or rust-lang.org, but that is an inference from the topic, not knowledge of this video. The actual header-bar title and address-bar domain cannot be determined without seeing the frames.

## 2. Git branch name in the shell prompt, and whether it appears in the VS Code status bar

**Answer:** insufficient evidence.

**Basis:** metadata only. `cargo new` initialises a git repo whose default branch is whatever the user's git config sets (commonly `master` or `main`), so the branch is probably one of those two, but which one, and whether VS Code's status bar shows it, is undetermined.

## 3. Exact string printed by the first program (hello_world/main.rs via rustc, run with ./main)

**Answer:** insufficient evidence.

**Basis:** own knowledge, not this video. The Rust Book's canonical first program prints `Hello, world!`, and a session titled "Rust Lang - 1" with a `hello_world/main.rs` compiled by `rustc` very likely follows that chapter. However the question asks for a character-for-character quote, and the author may have changed the text (different punctuation, capitalisation, or a custom message). Inference: most likely `Hello, world!`; not determinable from the evidence I have.

## 4. Full `cargo --version` output line

**Answer:** insufficient evidence.

**Basis:** metadata only. The output format is `cargo X.Y.Z (hash YYYY-MM-DD)`, but the specific version number, commit hash and date depend on the toolchain installed on the author's machine at recording time, which nothing in video.txt reveals (no upload date is given).

## 5. Command typed in target/release that produced the flood of "command not found" / "parse error" / "bad pattern" lines, and the final job-status line

**Answer:** insufficient evidence.

**Basis:** own knowledge for the mechanism only. That error pattern is what a shell (zsh, given "bad pattern") produces when a binary file is sourced or piped into the shell as a script, e.g. `. ./hello_cargo`, `source hello_cargo`, `sh hello_cargo`, `cat hello_cargo | zsh`, or `./hello_cargo &` combined with something else. The job-status line (job number, PID, exit code) is entirely specific to that run and cannot be known. The exact command is not determinable.

---
Files read: video.txt, questions.md
