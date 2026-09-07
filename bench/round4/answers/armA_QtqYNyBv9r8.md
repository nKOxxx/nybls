# Arm A (one shot, 30 uniform frames), QtqYNyBv9r8, Rust session 12:07
Run 2026-09-07. Clean context, blind to ground truth, no image generation permitted.
Frames examined: 30 of 30. Declared no file modified. COST: 53,760 visual tokens.
Verbatim answers follow; scoring is by the independent judge, not the experimenter.

1. Header title: "The Rust Programming Language"; address bar domain: doc.rust-lang.org.
   Seen in every frame, e.g. u00_12s (URL doc.rust-lang.org/book/ch01-01-installation.html)
   and u29_714s (doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html).

2. Branch name: master, shown in the prompt as "git:(master)" (u11_278s, u12_302s,
   u16_399s, u17_423s, u19_472s, u29_714s). Yes, the same branch appears in the VS Code
   status bar, rendered as "master*" at bottom left (u10_254s, u20_496s through u28_689s).
   The asterisk (uncommitted changes) is an inference from VS Code's convention; the word
   "master" is what I read.

3. Seen: "Hello, wolrd!" (world misspelled as "wolrd"). Evidence: u08_205s, terminal line
   "hello_world ./main" followed by "Hello, wolrd!"; the same output remains in scrollback
   at the top of u09_229s and u11_278s. Caveat: the terminal text is small at this
   resolution and I could not zoom, but the transposition reads consistently in all three.

4. Seen: "cargo 1.88.0 (873a06493 2025-05-10)". Evidence: u09_229s and u11_278s, line
   directly under "hello_world cargo --version". Same small text caveat applies to the
   hash digits.

5. insufficient evidence. The flood happened between the sampled frames: u16_399s shows
   "cd relea" being typed inside target, and u17_423s already shows a cleared terminal with
   only the "release git:(master) x" prompt; u18_447s shows the subsequent "ls" in release
   (build, deps, examples, hello_cargo, hello_cargo.d, incremental). No frame captures the
   command, the error lines, or the job status line, and the transcript contains only
   typing sounds.
