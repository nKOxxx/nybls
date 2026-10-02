# Answers — QtqYNyBv9r8 ("Silent Coding Session - Rust Lang - 1")

Note: the video has no speech (probe marked the whisper transcript UNRELIABLE; it is only "(keyboard clicking)" / "[typing sounds]"), so every answer below comes from frames.

1. The page header bar reads **"The Rust Programming Language"** (the mdBook title centered in the header, visible throughout, e.g. [01:19], [04:35], [08:20]). The address bar domain is **doc.rust-lang.org** (paths seen: `/book/ch01-02-hello-world.html` [01:19], `/book/ch01-03-hello-cargo.html` [04:35], `/book/ch02-00-guessing-game-tutorial.html` [08:20]). The Chrome tab title at [00:39] is "Hello, World! - The Rust P…".

2. The shell prompt inside the cargo project shows **`git:(master)`** — e.g. `hello_cargo git:(master) ✗` [04:35], `target git:(master) ✗` [06:38], `release git:(master) ✗` [06:58]. **Yes**, the same branch name appears in the VS Code status bar: at [08:20] the bottom-left of VS Code (guessing_game project) shows **`master*`** (the asterisk marking uncommitted changes), next to "Launchpad", "⊗ 0 ⚠ 0", "Live Share", "Git Graph".

3. `./main` prints **`Hello, wolrd!`** — with the typo "wolrd" (not "world"). Confirmed by zoom at [04:35] on the terminal scrollback: line `→ hello_world ./main` followed by `Hello, wolrd!`.

4. `cargo --version` prints **`cargo 1.88.0 (873a06493 2025-05-10)`** [04:35].

5. In `target/release` the user typed **`. ./hello_cargo`** (a dot, a space, then `./hello_cargo` — i.e. `source`-ing the ELF binary into the shell), at prompt `release git:(master) ✗` [06:58]. The shell immediately printed `[2] 62750`, then the flood of `parse error near ')'`, `permission denied`, `command not found`, `bad pattern` lines. The final job-status line at the bottom of that output is:
   **`[2]  + 62750 exit 127   ELF   >`**
   (job number 2, PID 62750, exit code 127), followed by a fresh `release git:(master) ✗` prompt [06:58].

## Evidence strip

- [00:39–03:14] sheet_000 (6 tiles): browser left on the Rust book, terminal/VS Code right; layout orientation only.
- [04:35–07:56] sheet_001 (6 tiles): hello_cargo chapter, terminal scrollback with cargo commands, later guessing_game chapter.
- [08:20–11:45] sheet_002 (6 tiles): guessing_game in VS Code with status bar; Chrome extension/sidebar panes.
- [01:19] full frame: Chrome tab "Hello, World! - The Rust P…", address `doc.rust-lang.org/book/ch01-02-hello-world.html`, header "The Rust Programming Language"; terminal `projects → mkdir hello_world`, `cd`, `touch main.rs`, `code main.rs`.
- [04:35] full frame: terminal scrollback with `./main` output, `cargo --version` → `cargo 1.88.0 (873a06493 2025-05-10)`, `cargo new hello_cargo`, `hello_cargo git:(master) ✗ cargo build`.
- [06:38] full frame: `cargo run/check/build --release`, `cd target`, `ls` → `CACHEDIR.TAG debug release`, typing `cd rel`.
- [08:20] full frame: VS Code guessing_game, status bar bottom-left `master*`; address `doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html`.
- [00:39] zoom top-left: Chrome title bar "Hello, World! - The Rust Programming Language - Google Chrome", address bar `doc.rust-lang.org/book/ch01-02-hello-world.html`.
- [04:35] zoom terminal top: `→ hello_world ./main` / `Hello, wolrd!` … `cargo --version` / `cargo 1.88.0 (873a06493 2025-05-10)`.
- [08:20] zoom VS Code status bar: `master*`, Launchpad, 0 errors 0 warnings, Live Share, Git Graph.
- [06:58] full frame: `release git:(master) ✗ . ./hello_cargo`, `[2] 62750`, flood of parse error / permission denied / command not found / bad pattern lines, ending `[2]  + 62750 exit 127   ELF   >`.
- [07:30] full frame (NEAR-DUPLICATE flagged): `release` → `ls` → `build deps examples hello_cargo hello_cargo.d incremental`, `cd ..` back to `target`, `cd: string not in pwd: ..`.
- [07:52] full frame (not opened; snapped to sheet tile already seen).
- [06:58] zoom top line: `release git:(master) ✗ . ./hello_cargo` / `[2] 62750`.
- [06:58] zoom bottom line: `[2]  + 62750 exit 127   ELF   >` / `release git:(master) ✗`.
- [04:35] zoom tight: `→ hello_world ./main` / `Hello, wolrd!`.

## Ledger

watched 12 min · examined 16 images (~18,356 visual tokens, ≈$0.04 at sonnet-5 input rate) of ~18,154 total frames · budget 16/49 units
