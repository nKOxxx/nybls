# Answers: "10 Hour Coding Time Lapse (C programming)" (92gQUnMCA08)

Note on method: the video has no speech (captions are song lyrics / [Music] tags only), so every answer below comes from frames. Status per question is marked; the budget was exhausted at 25/25 units.

## 1. Editor, window title, root folder

- Editor: **Visual Studio Code** (VS Code logo top-left, Activity Bar, "Visual Studio Code" in every title bar) [00:15], [01:52], [04:21].
- Window title bar: **"<open file> - Coding Time lapse - Visual Studio Code"**, i.e. the workspace name is **"Coding Time lapse"** (e.g. "Question-2.c - Coding Time lapse - Visual Studio Code" [01:52]; with no file open just "Coding Time lapse - Visual Studio Code" [04:52]).
- Root folder at the top of the Explorer tree: **"Pushing limits"** (shown directly under a sibling `.vscode` entry; the breadcrumb also starts "Pushing limits > ...") [00:15 zoom], [01:52].

Status: sufficient.

## 2. Numbered subfolders

**11** numbered subfolders inside "Pushing limits" [01:52], [02:07], [04:52]:

1. Newbie coder
2. Really !!!
3. Still beginner
4. Not that easy !
5. Almost intermediate
6. Getting serious -_-
7. Intermediate '-'
8. Annoyed ''-''
9. Frustration level x200
10. Near advanced _-_
11. Advanced ;v

- First: **"1. Newbie coder"**
- Last: **"11. Advanced ;v"**

Status: sufficient.

## 3. Nonsense terminal command and shell error

**Not found - partial / unanswered.** The integrated PowerShell terminal was only visible in two of the frames I examined ([04:21] in folder "8. Annoyed", [04:59] in folder "10. Near advanced"), and in both cases the only command in the visible history is the VS Code Code Runner `cd "..." ; if ($?) { gcc Question-N.c -o Question-N } ; if ($?) { .\Question-N }` line followed by the program's own output; no nonsense command and no shell error appear there. The budget ran out before I could sweep the remaining terminal-open moments. I will not guess the typed text or the error line.

## 4. Program that floods the terminal with a repeated number

File: `10. Near advanced _-_/Question-1.c`, "// Program to read three integers from a file." [04:57]-[05:01].

- `fopen` filename: **`"files.txt"`** (`ptr = fopen("files.txt", "r");`) [04:57], [04:59], [05:00].
- Loop condition visible in the source at the time the terminal is on screen: **`while(ch != EOF)`** [04:59], with the body `ch = fgetc(ptr); fscanf(ptr, "%d", &read); printf("%d ", read);`. Shortly after, the programmer is rewriting it to `while(1)` with an `if(ch == ...)` / `ch++` body [05:01].
- Repeated number: **partial.** The terminal frame I caught [04:59] shows the run's output as `429 21 21`, so the number being repeated is **21** (the last value successfully read, re-printed when `fscanf` fails). I did not capture a frame where the terminal is actually full of the repeated value, so "21" is inferred from the visible output line rather than seen as a flood; the loop condition and filename above are read directly.

Status: partial (filename and loop condition confirmed; repeated number inferred from one output line, flood itself not captured).

## 5. All-caps comment in "5. Almost intermediate/Question-2.c"

- Library function in the printf directly above: **`pow`** (`printf("The area of the square is %d !", pow(side, side));`, with `#include <math.h>`) [01:52], [01:54].
- First all-caps comment line, as it reads on screen [01:54]:
  **`// WHAT IS GOING ON 1!?!?!?`**
  The character right after "ON " renders as a `1` at full resolution (a plausible missed-shift for `!`); if it is in fact `!`, the line is `// WHAT IS GOING ON !!?!?!?`. I had no budget left to zoom and settle the glyph.

Status: sufficient for the function name; comment text read at full-frame resolution with the one-glyph caveat above.

---

## Evidence strip

- [00:15]-[02:49] sheet_000: six tiles; VS Code throughout, "Pushing limits" tree with folders 1-11, files in folders 1, 4, 5, 7.
- [03:20]-[05:53] sheet_001: six tiles; folders 7, 8, 10, 11; terminal visible at 04:21; empty VS Code window at 04:52.
- [00:15] zoom on sidebar: `.vscode`, "Pushing limits", "1. Newbie coder", Question-1.c / .exe.
- [01:52] Question-2.c (folder 5): `#include <math.h>`, printf with `pow(side, side)`, comment on line 14 just started (`// `).
- [01:54] Question-2.c (folder 5): line 14 `// WHAT IS GOING ON 1!?!?!?`, pow() tooltip.
- [01:55] Question-3.c (folder 5): empty skeleton, "Prgoram using functions to find average of three numbers".
- [01:59] Question-3.c: `int average(...) //OMGMGG`, `// Yes, I'm an idiot I know that...`.
- [02:00] Question-3.c: same file, `float average(...)`.
- [02:07] Question-6.c (folder 5): skeleton; full folder-5 file list.
- [04:15] Question-7.c (folder 8): "Program to encrypt a string...".
- [04:21] Question-9.c (folder 8) with PowerShell terminal: Code Runner cd/gcc command, "Number of occurences of letter 'i': 2". No nonsense command.
- [04:22] Question-10.c (folder 8): skeleton.
- [04:36] Quesiton-5.c (folder 9): "// What is a complex number !?!?!?!/".
- [04:52] Empty VS Code window, title "Coding Time lapse - Visual Studio Code", creating Question-1.c in folder 10.
- [04:57] Question-1.c (folder 10): `fopen("files.txt","r")`, `while(ch != EOF)`, fscanf/printf body.
- [04:59] Question-1.c (folder 10) with terminal: Code Runner command, output `429 21 21`; loop `while(ch != EOF)` with `ch = fgetc(ptr)` inside.
- [05:00] Question-1.c (folder 10): same code, no terminal.
- [05:01] Question-1.c (folder 10): loop being rewritten to `while(1)` with `if(ch -- )`, `ch++`.
- [05:05] Question-2.c (folder 10): `fopen("tabless.txt","w")`, multiplication table.
- [05:17] Quesiton-3.c (folder 10): letters.txt -> doubles.txt, `while(1)` with `if(ch == EOF) break;`.
- [05:35] Question-4.c (folder 10): gets/fflush/fprintf to ptr.
- [05:41] Question-4.c (folder 10): `fopen("info.txt","w")`.
- [05:46] Question-5.c (folder 10): `fopen("square.txt", ...)`.
- [05:53] Question-4.c (folder 11): "// Program to dynamically create an array of".

## Ledger
