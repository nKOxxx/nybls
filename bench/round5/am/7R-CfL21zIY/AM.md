# Answers — 7R-CfL21zIY (fixed evidence pack: transcript.txt + 4 uniform stills)

Legend: SEEN = read directly from a frame or transcript line; INFERRED = my interpretation on top of that.

## 1. Coding platform and what you need to follow along

**Answer:** Repl.it (repl.it), a free, browser-based online IDE. The only prerequisites he states are a web browser (any browser) and an internet connection; nothing to download or install. He adds that it works on a phone or iPad. You also need a Repl.it account (sign up or log in; sign-up asks for a favourite language, he recommends choosing Python).

**Evidence (SEEN):**
- Transcript [02:45]–[03:01] "platform called rep lit ... online browser-based coding environment ... without having to download or install any software"; [03:14]–[03:31] "free browser-based coding environment ... only prerequisite ... is that you have a browser and you have internet connection ... you can actually do all of ... on your phone ... on an iPad"; [04:39]–[04:50] sign up / log in, pick Python as favourite language.
- Frame `am00_188s.png` (188 s = [03:08]): repl.it homepage, logo "repl.it", tagline "Use our free, collaborative, in-browser IDE to code in 50+ languages — without spending a second on setup."

## 2. Four main data types, and what counts as a string

**Answer:** The four types are **string (str), int, float, bool**. A string is anything wrapped in double or single quotation marks — a collection of characters / text — so even `"89"` counts as a string because it is quoted.

**Evidence (SEEN):**
- Transcript [12:54]–[13:31] "four main types ... the first one is screen [string] the second one is int then we have float and then we have bool"; [13:32]–[13:57] string "represented by STR ... is anything wrapped inside of double quotation marks or single quotation marks ... 989 [sic] is an example of a string ... strings are just a collection of characters they're just text".
- Frame `am02_940s.png` ([15:40]) shows the on-screen comment block: `string "hello", 'hi', "89"` / `int 8, 7, -9, 100000` / `float 6.0, 7.5, -9.8, -100.0` / `bool True, False`. (The transcript's "989" is an ASR mishearing; the frame shows `"89"`.)

## 3. Variable naming rules; what to use instead of a space

**Answer:** A variable name may contain only lowercase and uppercase letters, underscores, and numbers; no special characters other than underscore; it cannot start with a number (though a number may appear inside or at the end, e.g. `hello1`). Spaces are not allowed; use an **underscore** instead (e.g. `hello_world`), which is the convention for separating words.

**Evidence (SEEN):** Transcript [18:34]–[18:51] "can only contain lowercase and uppercase letters underscores and numbers ... cannot contain any special characters other than an underscore and it cannot start with a number"; [18:56]–[19:03] `1hello` gives a red squiggly, not allowed; [19:17]–[19:30] "there's no spaces allowed in variable names just use an underscore so something like hello underscore world this is the convention". No frame in the pack shows this code section (frames are at 188/564/940/1316 s; the naming section is ~1114–1170 s).

## 4. Frameworks page: game dev and GUI options

**Answer:** From the transcript only: under game development he names **Pygame** ("one of my personal favorites"); under GUI development he names **Tkinter** (a Python module) and **Java Swing**. Whether the page listed additional frameworks beyond those three: **insufficient evidence** — none of the four stills captures the frameworks page (it appears around [06:47]–[07:07], ~407–427 s, between frames am00 at 188 s and am01 at 564 s), so I cannot confirm the full list as shown on screen.

**Evidence (SEEN):** Transcript [06:47]–[07:05] "some game development frameworks one of my personal favorites which is PI game here and then there's GUI development so to kinter that's a Python module Java swing". INFERRED: "PI game" = Pygame, "to kinter" = Tkinter (ASR renderings).

## 5. Exact Python version in the Replit console

**Answer:** **Python 3.8.2** (default, Feb 26 2020, 02:56:1…).

**Evidence (SEEN):** Frame `am01_564s.png` ([09:24]): console on the right reads `Python 3.8.2 (default, Feb 26 2020, 02:56:1` then wraps to `0)`. The last digits of the build time are partly overlapped by the console's search icon; "3.8.2" itself is clearly legible. The transcript never states the version.

## 6. Finished demo game: age condition and how age input is read

**Answer:** **Insufficient evidence** for the exact condition. The demo at [01:23]–[01:31] only shows the behaviour: he enters age 19 and the program prints "you are old enough to play"; the source of the finished game is never shown or read aloud in this video, so I cannot state the exact comparison (e.g. `>= 18` vs `> 18`) or the threshold. On how age input is read: in this video's own code he writes `age = input("What is your age? ")` ([22:35]–[22:46]), which stores a string; he does not convert it to a number here and explicitly defers conditions to the next video ([24:46]–[24:51] "in the next video ... talk a bit about conditions"). INFERRED, not seen: for a numeric comparison to work the input would need an `int(...)` conversion — but the video does not show or say this, so it is not an evidenced answer.

**Evidence (SEEN):** Transcript [01:23]–[01:31]; [22:35]–[22:58]; [24:46]–[24:51]. Frame `am03_1316s.png` ([21:56]) shows only `name = input("What is your name? ")` — no age line yet, no condition.

## 7. Instructor's full name / Replit username

**Answer:** Replit username **@TimRuscica**; he refers to himself as **Tim**. The surname as spelled on screen is "Ruscica"; the full name "Tim Ruscica" is INFERRED from the handle plus his saying "I'm gonna put Tim" — the video does not state the surname aloud.

**Evidence (SEEN):** Frames `am01_564s.png`, `am02_940s.png`, `am03_1316s.png` all show the repl header `@TimRuscica/FirstGame` and the console URL `https://FirstGame.timruscica.repl.run`. Transcript [01:25] "what is your name I'm gonna put Tim".

## 8. After choosing to swim across the lake

**Answer:** The game says he managed to get across but was bitten by a fish and lost 5 health. He then notices a house and a river, and the two options offered are **go to the river** or **go to the house**. (He picks the river, falls in, and loses.)

**Evidence (SEEN):** Transcript [01:51]–[02:11] "reach a lake you swim across or go around ... let's go across ... you manage to get across but you were bit by a fish and lost five health you notice a house in a river which do you go to the river or the house so let's decide to go to the river ... you fell in the river and you lost". INFERRED: "a house in a river" is ASR for "a house and a river", consistent with the two options given. No frame covers the demo (it ends before 188 s).

---
Frames examined: 4 of 4 (`am00_188s.png`, `am01_564s.png`, `am02_940s.png`, `am03_1316s.png`), each opened as-is; no crops, zooms, or new images were produced, and no extraction tools were run.
Files: only `answers.md` was created in this directory; no other file was modified.
