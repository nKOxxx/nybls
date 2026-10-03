# notes for program.py (7R-CfL21zIY, arm A: transcript + 30 uniform stills)

## What the video builds
This is video 1 of a 3-part beginner series (Tim Ruscica, Replit, Python 3.8.2). The
"final version" at the end of THIS video is the 16-line main.py visible in the last
still at [24:39] (u29_1479s.png), and program.py reproduces it verbatim, including the
leftover triple-quoted data-type notes block the presenter parks at the bottom
([15:20]–[16:19], stills u19–u29).

Evidence per line:
- line 1 `print("Welcome to my first game!")` — stills u15 [12:57] onward, transcript [12:19]–[12:40].
- line 2 `name = input("What is your name? ")` — u25 [21:17], u26 [22:08]; trailing space discussed [20:57].
- line 3 `age = input("What is your age? ")` — u27 [22:58], transcript [22:35]–[22:47]. Plain `input`,
  NOT `int(input(...))`; the `int(...)` wrapper only appears in the series-final demo (u01/u02)
  and is not written in this video.
- line 5 `print("Hello", name, "you are", age, "years old.")` — u29 [24:39], transcript [23:36]–[24:10].
- comment block — u19 [16:17] onward, text unchanged through u29.

## Choices the evidence does not fully determine
1. **Period after "years old."** The code in u29 reads `"years old."` with a period, but the
   console in the same still shows `Hello tim you are 19 years old` (no period), and the
   transcript says only "years old". I kept the period because the source pane is the
   program and the console line may be from the run before the period was typed; low
   confidence either way.
2. **Blank-line count.** u29 shows line 4 blank, print on line 5, lines 6–10 blank, `'''` on
   line 11, closing `'''` on line 16. program.py matches that line numbering. Earlier
   stills show varying blank-line counts (12–19 lines), so only the final still governs.
3. **Spacing inside the comment block** (e.g. two or three spaces after `string`, `int`,
   `float`) is read off the still at 1568px and may be off by one space; semantically
   irrelevant since it is inside a string literal that is never used.

## What this video does NOT build (deliberately excluded)
The opening demo [00:58]–[02:34] and stills u01/u02 show the SERIES-final game
(`age = int(input(...))`, `health = 10`, `if age >= 18:`, `wants_to_play = ...`,
left/right, lake across/around, fish -5 health, river/house, lose). Only lines 1–10 of
that file are partially visible and the branch logic is never shown as code; it is
built in videos 2 and 3 per the transcript [24:44]–[24:58]. Reproducing it would be
guessing, so it is left out.

## Things the presenter wrote and then deleted (not in final)
`print("Hello World!")`, `x = 5` / `print(x)`, `x = True`, `hello = 9`, `yes = "hello"`,
`hello = yes`, `hello = hello + 9`, `hello1`, `1hello` (error), `hello_world`,
`print(name)` — all scratch demos ([11:41]–[20:06]), removed by u24 [21:17].
