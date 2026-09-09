# Ground truth, round 4 (silent video, P/T labelled)

Written 2026-09-07 by four author agents from dense 10 s ffmpeg grids, with no access to nybls.
Committed 2026-09-09 after review run 024 found it had never been committed.

---

## 92gQUnMCA08

# Ground truth, "10 Hour Coding Time Lapse (C programming)" (92gQUnMCA08, 6:10)

Evidence base: 37 reference grid frames at 10 s spacing (g_00005s.png to g_00365s.png), all read. Timestamps for T items are the grid frame time; true on-screen window is somewhere inside the 10 s bracket on either side (item not visible in the neighbouring grid frames unless stated).

## Q1, label P
Answer: Visual Studio Code (dark theme, VS Code Dark+ look). Window title reads "<file> - Coding Time lapse - Visual Studio Code" in every frame, so the workspace name is "Coding Time lapse". The Explorer root folder is "Pushing limits" (also the first breadcrumb segment above the editor: "Pushing limits > 1. Newbie coder > ...").
Frames: every frame; e.g. g_00005s.png, g_00075s.png, g_00175s.png, g_00305s.png, g_00355s.png.
Signature: "Pushing limits" (also "Coding Time lapse").
Accept: "VS Code"/"Visual Studio Code"; workspace "Coding Time lapse"; root "Pushing limits". Note the terminal path also shows C:\Users\admin\Coding Time lapse\Pushing limits\... (g_00015s, g_00055s, g_00095s, g_00245s, g_00295s, g_00365s), which corroborates.

## Q2, label P
Answer: 11 numbered subfolders. First: "1. Newbie coder". Last: "11. Advanced ;v". Full list as displayed: 1. Newbie coder, 2. Really !!!, 3. Still beginner, 4. Not that easy !, 5. Almost intermediate, 6. Getting serious -_-, 7. Intermediate '-', 8. Annoyed ''-'', 9. Frustration level x200, 10. Near advanced _-_, 11. Advanced ;v.
Frames: full list visible in g_00005s.png, g_00015s.png, g_00025s.png, g_00035s.png, g_00045s.png, g_00055s.png, g_00075s.png, g_00115s.png, g_00155s.png, g_00175s.png, g_00235s.png, g_00305s.png, g_00355s.png (and partially in most others).
Signature: "11. Advanced" / "Newbie coder".
Accept: count 11; first "1. Newbie coder"; last "11. Advanced" with or without the ";v" emoticon suffix.

## Q3, label T
Answer: The programmer typed "ezzz" at the PowerShell prompt (PS C:\Users\admin\Coding Time lapse\Pushing limits\4. Not that easy !> ezzz). First error line, shown in red: "ezzz : The term 'ezzz' is not recognized as the name of a cmdlet, function, script file, or operable program." Followed by "Check the spelling of the name, or if a path was included, verify that the path is correct and try again.", "At line:1 char:1", "+ ezzz", "+ CategoryInfo : ObjectNotFound: (ezzz:String) [], CommandNotFoundException", "+ FullyQualifiedErrorId : CommandNotFoundException".
Context in same frame: just above, the output of .\Question-12 (8 times table, "Total sum = 440") and a manual PowerShell sum "8 + 16 + 24 + 32 + 40 + 48 + 56 + 64 + 72 + 80" giving 440.
Frames: g_00095s.png only (g_00085s shows Question-8.c editor, g_00105s shows Question-16.c editor).
Timestamp: ~95 s (window inside 85 to 105 s).
Signature: "ezzz" (secondary: "CommandNotFoundException", "Total sum = 440").

## Q4, label T
Answer: The number "21" is repeated (the terminal shows rows of "21 21 21 21 ..." with occasional "1" and "2" fragments where the wrapped text splits). The visible loop condition is `while(EOF != NULL)` in 10. Near advanced / Question-1.c ("// Program to read three integers from a file."), and the file is opened with `ptr = fopen("files.txt", "r");`. Inside the loop: `fscanf(ptr, "%d", &read);` and `printf("%d ", read);`. Explorer shows files.txt next to Question-1.c.
Frames: g_00295s.png only (g_00285s shows Question-9.c in 9. Frustration level x200, g_00305s shows Question-2.c with tabless.txt).
Timestamp: ~295 s (window inside 285 to 305 s).
Signature: "21 21 21" (secondary: "EOF != NULL", "files.txt").

## Q5, label T
Answer: First all-caps comment line: `// WHAT IS GOING ON 1!?!?!?` (line 14). Directly above it, line 13: `printf("The area of the square is %f !", pow(side, 2));` so the library function is `pow` (from `#include <math.h>`, line 2). Further comments in the same file: line 16 `// WHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT` (long run of H and A), line 18 `// Sometimes computers makes no sense at all !!!!`. Task comment line 4: "// Use the library function to calculate the area of a square with side a."
Frames: g_00115s.png only (g_00105s shows Question-16.c in 4. Not that easy !, g_00125s shows Quesiton-5.c in 5. Almost intermediate).
Timestamp: ~115 s (window inside 105 to 125 s).
Signature: "WHAT IS GOING ON" (secondary: "pow(side, 2)", "makes no sense").
Accept: "pow" / "pow(side, 2)"; comment text with the "1!?!?!?" tail in any punctuation-approximate form.

## Label count
P: Q1, Q2. T: Q3, Q4, Q5.

## Transcript
File: [local path] 914 bytes, 47 lines. Contents are YouTube auto-captions of the background music only: "[Music]" and "[Applause]" tags plus misheard lyric fragments ("a holy crime", "with the monsters everything that brought me alive", "playing with the monsters", "it's all can go", "you got me on the road", "I can hear your heart", "say hi what is this", "foreign", "thank you"). No mention of code, files, editors, commands, errors, folders or numbers. None of Q1 to Q5 is answerable from the transcript; all five require looking at frames.

## Other transient candidates noted (not used)
- g_00015s: Question-5.exe run, "Simple Interest: 10.000" (inputs 10, 10, 10).
- g_00055s: 3. Still beginner Question-4 run, "Enter your income (in lakhs): 3", "Income tax = 5 percent", "Income to be paid: 12500.00".
- g_00235s to g_00265s: string literal "Kshitij" in Question-3.c / Question-7.c / Question-10.c (recurs, ~30 s+, so not brief).
- g_00365s: calloc/realloc output "Element 7: 872415284", "Element 8: 17090", "Element 9: 8072032", "Element 10: 8061120".
- g_00125s, g_00325s, g_00355s: misspelled filenames "Quesiton-5.c", "Quesiton-3.c" in Explorer.

---

## QtqYNyBv9r8

# Ground truth, "Silent Coding Session - Rust Lang - 1" (QtqYNyBv9r8, 12:07)

Evidence base: 73 grid frames (one per 10 s, g_00005s.png to g_00725s.png), all read; transcript.txt read.

## Transcript verdict

[local path] contains 53 timestamped lines and nothing but sound tags: "(keyboard clicking)" at 00:00, 00:30, 01:00, 01:30, 01:33, 01:38, 01:43 and 12:04, and "[typing sounds]" for every other line (02:00 through 11:44). No speech, no words, no on screen text. None of the five questions below is answerable from it; every answer requires looking at frames.

## Session outline (for the grader)

Layout throughout: Google Chrome on the left half showing The Rust Programming Language book at doc.rust-lang.org; the right half alternates between a Terminal window and Visual Studio Code. Chapters visited: ch01-01-installation (5 to 25 s), ch01-02-hello-world (35 to 205 s), ch01-03-hello-cargo (215 to 425 s), ch02-00-guessing-game-tutorial (435 s to end). The book's theme is switched from light to "Coal" at about 315 to 325 s. Projects created: hello_world (rustc), hello_cargo (cargo new), guessing_game (cargo new). rust-analyzer and Rust Syntax extensions are installed around 615 to 665 s.

## Q1, P

Answer: Header title "The Rust Programming Language"; domain doc.rust-lang.org (paths /book/ch01-01-installation.html, /book/ch01-02-hello-world.html, /book/ch01-03-hello-cargo.html, /book/ch02-00-guessing-game-tutorial.html).
Frames: every frame, g_00005s.png through g_00725s.png. The header text is visible in all 73 frames; the address bar in all 73.
Signature (for persistence measurement): "Rust Programming Language" (also "doc.rust-lang.org").

## Q2, P

Answer: master. The zsh prompt reads e.g. "hello_cargo git:(master) ✗", "target git:(master) ✗", "release git:(master) ✗", "guessing_game git:(master) ✗". Yes, the VS Code status bar also shows "master" (with an asterisk, "master*", when the tree is dirty, e.g. at 255 s and 485 s onward).
Frames: terminal prompt with git:(master) from g_00235s.png through g_00465s.png (terminal frames) and g_00715s.png, g_00725s.png; VS Code status bar "master" in g_00255s.png and g_00485s.png through g_00705s.png. Recurs from 235 s to the end (about 490 s of the 727 s video).
Signature: "git:(master)".

## Q3, T

Answer: Hello, wolrd!  (the word "world" is misspelled "wolrd"; the source line is println!("Hello, wolrd!"); and the program output matches).
Frames: source visible in g_00175s.png and g_00185s.png (VS Code main.rs line 2); terminal output "Hello, wolrd!" visible in g_00205s.png, g_00215s.png, g_00225s.png, g_00235s.png and again in the scrollback of g_00265s.png.
Approx timestamp: 175 s (source), 205 s (output). On screen roughly 175 to 265 s.
Signature: "wolrd".

## Q4, T

Answer: cargo 1.88.0 (873a06493 2025-05-10)
Frames: g_00225s.png (the command and output at the top of the terminal), g_00235s.png, g_00265s.png (scrollback).
Approx timestamp: 225 s. On screen roughly 220 to 265 s.
Signature: "cargo 1.88.0".

## Q5, T

Answer: The command typed was ". ./hello_cargo" (a dot, a space, then ./hello_cargo, i.e. the shell sourced the compiled ELF binary instead of executing it). The final job-status line reads "[2]  + 62544 exit 127    ELF    >" (job 2, PID 62544, exit 127). The first line of the output was "[2] 62544", and the garbage includes "./hello_cargo:9: parse error near `)'", "./hello_cargo:1: permission denied:", "./hello_cargo:1: command not found: ^D", "bad pattern:" lines.
Frames: g_00415s.png only (the terminal is cleared by g_00425s.png, which shows just the prompt "release git:(master) ✗").
Approx timestamp: 415 s. On screen roughly 410 to 420 s.
Signature: "exit 127".

## Label count

P: Q1, Q2. T: Q3, Q4, Q5.

## Other verifiable on screen facts not used (spares)

- 315 to 325 s: mdBook theme menu (Auto, Light, Rust, Coal, Navy, Ayu); "Coal" is selected at 325 s (signature "Coal").
- 655 s: VS Code dialog "Do you trust the publisher 'Dusty Pomerleau'?" for the Rust Syntax extension (signature "Dusty Pomerleau").
- 695 s: rust-analyzer hover on Result showing "29 implementations".
- 515 s onward: guessing_game main.rs line println!("Guessing Game!<3"); its output "Guessing Game!<3" is in the terminal at 715 s.
- 165 s: GitHub Copilot extension page, version 1.338.0, "This extension is disabled globally by the user."
- Compile lines show the path /home/[redacted]/ytb/rustlang-book/projects/... (275, 305, 395, 715 s).

---

## Wlu4MsBnjuk

# Ground truth, Wlu4MsBnjuk "ASMR Programming - Coding a Snake Game - No Talking" (24:05)

Evidence base: 145 grid frames (one per 10 s, g_00005s.png .. g_01445s.png), all reviewed. Transcript file reviewed (see bottom).

## Q1, label P (persistent)
Answer: Visual Studio Code, editing a file named `snake.py`.
Evidence: g_00005s.png shows the VS Code welcome page ("Visual Studio Code, Editing evolved", Explorer panel titled SNAKE, file `snake.` being created). From g_00015s.png onward every editor frame shows the tab and breadcrumb `snake.py` (e.g. g_00025s, g_00265s, g_00775s, g_01005s, g_01115s, g_01225s, g_01445s). The `snake.py` text is on screen in essentially every non-game frame, roughly two thirds of the video.
Signature (P, for reference): "snake.py"

## Q2, label P (persistent)
Answer: `import pygame, sys, time, random`. Language is Python (file `.py`, Python status icon, terminal runs `python3 snake.py`); game library is pygame.
Evidence: line 1 visible verbatim in g_00025s, g_00035s, g_00045s, g_00055s, g_00065s, g_00075s, g_00085s, g_00095s (start of video, about 25 s to 95 s) and again in g_01225s, g_01285s, g_01295s, g_01315s, g_01335s, g_01415s, g_01425s, g_01435s, g_01445s (about 20:25 to end). The identifier `pygame` is also present on screen in nearly every code frame in between (pygame.Color, pygame.display, pygame.draw.rect, pygame.K_UP, etc.).
Signature (P, for reference): "import pygame"

## Q3, label T (transient)
Answer: The terminal shows
```
^CTraceback (most recent call last):
  File "/Users/[redacted]/Desktop/snake/snake.py", line 129, in <module>
    fps_controller.tick(speed)
KeyboardInterrupt
```
A second occurrence later names line 130 (same code line, file had grown by one line). Exception type: KeyboardInterrupt. Code line: `fps_controller.tick(speed)`.
Evidence: g_01005s.png and g_01015s.png (line 129); g_01115s.png, g_01125s.png, g_01135s.png (line 130). Not present before 995 s (g_00995s shows the clean run output) and gone by g_01215s (terminal shows fresh run output).
Approx timestamp: 1005 s (16:45) first seen; second window 1115 to 1135 s (18:35 to 18:55).
Signature: "KeyboardInterrupt"

## Q4, label T (transient)
Answer: Initially `frame_size_x = 720` and `frame_size_y= 480` (note the missing space before `=` on the y line as typed). In the last visible edit: `frame_size_x = 1380` and `frame_size_y= 840`. (An intermediate edit to 1440 x 960 is also visible.)
Evidence:
- Initial: g_00045s (x = 720 typed, y line still being typed as `frame_size=y =`), g_00055s through g_00165s show `frame_size_x = 720` / `frame_size_y= 480`; still 720/480 at g_01225s.
- Intermediate: g_01295s shows `frame_size_x = 1440`, `frame_size_y= 960`; g_01305s and g_01325s show the resulting near full-screen game window.
- Final: g_01335s shows `frame_size_x = 1380`, `frame_size_y= 840`; g_01415s, g_01425s, g_01435s, g_01445s show `frame_size_x = 1380` (line 12, later line 14). frame_size_y is scrolled out of view in those last four frames; 840 is the last value seen for it (g_01335s) and no later edit to it is visible in the grid. Grading note: accept 1380 x 840 as final; if a submission says y not visible at the very end but 840 at 22:15, that is also correct.
Approx timestamps: initial 45 to 165 s; final value first at 1335 s (22:15), through 1445 s.
Signature: "1380"

## Q5, label T (transient)
Answer: Two comment lines are typed at the top of the file:
- line 5: `# THANKS FOR WATHING, WHAT KIND OF GAMES U WANT TO SEE NEXT TIME? PLEASE STATE IT IN THE COMM` (text runs off the right edge of the visible editor in the frame; the words after "COMM" are not visible in the grid, presumably "COMMENTS", UNVERIFIED). Misspelling: "WATHING" (for WATCHING).
- line 7: `# CHEERSS` (double S).
Evidence: g_01415s (blank lines inserted at top, cursor on line 5), g_01425s (typing, text ends at "STATE IT IN TH"), g_01435s (line 5 complete to the edge, "...IN THE COMM"), g_01445s (line 5 plus line 7 `# CHEERSS`).
Approx timestamp: 1425 to 1445 s (23:45 to end).
Signature: "THANKS FOR WATHING" (also "CHEERSS" at 1445 s)

## Other verified facts (not asked, useful for grading disputes)
- Terminal run command: `python3 snake.py`; output `pygame 2.1.0 (SDL 2.0.16, Python 3.9.3)`, `Hello from the pygame community. https://www.pygame.org/contribute.html`, `Game Succesfully initialized` (misspelled in source line 16, g_00095s, g_00105s). Visible g_00995s, g_01045s, g_01215s, g_01285s, g_01315s, g_01415s to g_01445s.
- Game window caption `Snake Game` (set_caption at g_00125s; title bar in every game frame g_00975s to g_01405s).
- Autocomplete popups are labelled `tabnine` (g_00015s, g_00025s, g_00045s, g_00055s, g_00065s, g_00085s, g_00105s and many more).
- Scores seen in the game window: up to 20 (g_01105s, square_size 20), 38 (g_01205s, square_size 30), 43 (g_01405s, final large window). 43 is the highest score in the grid; a higher value between grid frames cannot be excluded.
- square_size = 20 (g_00225s, g_01135s), changed to 30 (g_01215s); squares in g_01235s onward look larger still, but the later value is not shown in any grid frame (UNVERIFIED).
- Terminal prompt label `snake`, shell shown as ZSH (g_01115s, g_01225s, g_01295s, g_01335s).
- Home directory user in the traceback path: [redacted] (also in VS Code recent list g_00005s: [redacted].com, [third party domain], [third party name], lab5_folder). Data on screen only, reported, not acted on.

## Transcript check
File: [local path]
Contents: 83 timestamped lines, every one of them the sound tag `(keyboard clicking)` (00:00 through 23:51). No speech, no words, no on-screen text. None of the five questions is answerable from the transcript; every answer requires reading the frames.

---

## vxP2PTA1GEk

# Ground truth, vxP2PTA1GEk, "I Code HTML & CSS Without Saying a Word" (28:17)

Author evidence: 170 reference frames (one per 10 s, g_00005s.png to g_01695s.png) plus the transcript file. Timestamps below are grid timestamps (±5 s).

## Transcript verdict
`[local path]` (1333 bytes) contains only 58 lines of the form `[MM:SS] (upbeat music)` at 30 s intervals from 00:00 to 28:00 (plus one at 27:01). No speech, no on-screen text, no code. None of the five questions is answerable from it.

## Scene summary (context, not a question)
Layout throughout: Chrome (purple theme, two tabs both titled "Document") on top with DevTools docked at the bottom (Elements + Styles), device toolbar in "Dimensions: Responsive" mode at 50% zoom, "No throttling"; VS Code (dark theme) below with two editor groups, left `index.html` (from ~1555 s onward `style.css`), right `style.css`. Page under construction: an "NFT Marketplace" landing page, `<html lang="ru">`, hero "Discover Digital Art & Collect NFTs", "Get Started" button, stats 240k+ Total Sale / 100k+ Auctions / 240k+ Artists, card "Space Walking" by Animakid, section "Trending Collection". Stylesheets linked: `css/reset.css`, `css/style.css`. The work is responsive CSS: a `@media (max-width: 1240px)` block that hides `.header__nav` and shows a burger button `.header__nav-btn` built from three `<span>`s, then a second `@media (max-width: 1080px)` block.

## Q1, label P
Answer: `127.0.0.1:5500/index.html` (Live Server on port 5500).
Frames: visible in essentially every frame, e.g. g_00005s.png, g_00485s.png, g_01105s.png, g_01615s.png (address bar, top of frame).
Signature (for OCR): `5500/index.html`

## Q2, label P
Answer: `ru` (`<html lang="ru">`).
Frames: line 1 of index.html in the left VS Code pane in all frames from ~g_00095s.png to g_01545s.png (e.g. g_01105s.png, g_01205s.png, g_01415s.png); also in the DevTools Elements tree (`<html lang="ru">`) in e.g. g_00005s.png, g_01315s.png, g_01535s.png.
Signature: `lang="ru"`

## Q3, label P
Answer: `1240px` (`@media (max-width: 1240px) { .header__nav { display: none; } ... }`).
Frames: right VS Code pane from g_00005s.png (empty block at line 933) through g_00485s.png (filled), g_01355s.png, g_01415s.png, g_01535s.png, g_01695s.png; also DevTools Styles shows "@media (max-width: 1240px)" in g_01125s.png to g_01315s.png and the VS Code breadcrumb "@media (max-width: 1240px)" in g_01345s.png to g_01475s.png.
Signature: `1240px`

## Q4, label T
Answer: `width: 200px` and `background-color: blue` (keyword, with a blue swatch). The DevTools rule reads `.header__nav-btn span { width: 200px; height: 4px; background-color: blue; }` under "@media (max-width: 1240px)", source link "style.css?_...:933"; from ~1145 s a fourth line `position: relative;` is added. The editor file at the same moment says `width: 100%; height: 4px; background-color: #37..FF` (hex, not readable at grid resolution), so the answer must come from the DevTools panel, not the editor.
Approximate timestamp: 1125 s to 1325 s (first full rule at g_01125s.png; typing of the rule with autocomplete popups at g_01105s.png "height" and g_01115s.png "background-clip"; rule gone by g_01335s.png).
Frames: g_01125s.png, g_01135s.png, g_01155s.png, g_01205s.png, g_01275s.png, g_01305s.png, g_01325s.png.
Signature: `200px`  (secondary: `blue`)

## Q5, label T
Answer: `1080px`; first selector inside it is `.about__inner` (`@media (max-width: 1080px) { .about__inner { padding: 40px 0; gap: 15px; } ... }`; the padding/gap digits are approximate at grid resolution, the selector and breakpoint are clear). At the very end (g_01695s.png) a second selector `.about__content-title` is being typed with a red "; expected" diagnostic.
Approximate timestamp: 1535 s to 1697 s (end). Being typed at g_01515s.png ("@media" IntelliSense popup, "media query expected") and g_01525s.png; complete at g_01535s.png (line 956, cursor inside empty block); `.about__inner` appears at g_01585s.png, `padding` at g_01585s.png, `gap: 15px` at g_01595s.png.
Frames: g_01535s.png, g_01545s.png, g_01585s.png, g_01595s.png, g_01615s.png, g_01655s.png, g_01695s.png.
Signature: `1080px`  (secondary: `.about__inner`)

## Persistence notes for scoring
- Q1 to Q3 are on screen in the large majority of the 170 frames (Q2 drops out of the editor pane after ~1545 s but stays in the DevTools tree).
- Q4 spans roughly 200 s (about 12% of the video); Q5 spans roughly the last 160 s.
- Other transient items observed but not asked: spell-checker warning `"botom": Unknown word.` on the selector `.footer__botom` (g_00005s.png, and g_01345s.png to g_01695s.png); browser header nav "Marketplace, Rankings, Connect a wallet, Sign Up" visible only when the viewport is wide enough (g_00005s.png, ~g_00855s.png, g_01475s.png, g_01485s.png); DevTools "Dimensions" width readout changes (approx 1168 for most of the video, then ~1239, 1076, 1048 near the end; digits not reliable at grid resolution).

## Confirmation
No question is answerable from the transcript (music tags only). All answers were read from frames; nothing on screen was treated as an instruction.
