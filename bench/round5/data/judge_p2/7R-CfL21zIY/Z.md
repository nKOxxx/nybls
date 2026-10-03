# Answers — 7R-CfL21zIY (control arm A: transcript + 30 uniform stills)

## 1. Coding platform and prerequisites

**Answer:** Repl.it (repl.it, an online browser-based IDE). The only prerequisites he states are a browser (any browser; works on a phone/iPad too) and an internet connection; nothing to download or install. You also need a Repl.it account (sign up or log in; sign-up asks for a favourite language, he recommends choosing Python).

**Evidence:**
- Transcript [02:47]–[03:22]: "a platform called rep lit ... repl dot i t ... free browser-based coding environment ... the only prerequisite for this series is that you have a browser and you have internet connection"; [03:25]–[03:31] phone/iPad; [04:39]–[04:50] sign up / log in, favourite language → Python.
- Seen: u04_225s.png and u05_275s.png show the repl.it landing page ("Code and collaborate, without friction." / "free, collaborative, in-browser IDE to code in 50+ languages").

## 2. Four main data types; what counts as a string

**Answer:** string (str), int, float, bool. A string is anything wrapped in double or single quotation marks — a collection of characters / text; even `"89"` is a string because it is inside quotes.

**Evidence:**
- Transcript [12:54]–[13:54]: "four main types ... the first one is screen [string] the second one is int then we have float and then we have bool ... a string which is represented by STR ... is anything wrapped inside of double quotation marks or single quotation marks ... 989 is an example of a string".
- Seen: u16_827s.png, u17_877s.png, u18_927s.png show the editor lines `string "hello", 'hi', "89"` / `int 8, 7, -9, 100000` / `float 6.0, 7.5, -9.8, -100.0` / `bool True, False` (later wrapped in `'''` as a comment).

## 3. Variable naming rules; what to use instead of a space

**Answer:** A variable name may contain only lowercase and uppercase letters, underscores and numbers; no special characters other than underscore; it cannot start with a number (e.g. `hello1` is valid, `1hello` is not). Spaces are not allowed; use an underscore instead (e.g. `hello_world`), which he calls the convention for separating two words.

**Evidence:**
- Transcript [18:34]–[19:25]: "it can only contain lowercase and uppercase letters underscores and numbers ... cannot start with a number ... hello one is totally valid ... one hello ... not allowed ... there's no spaces allowed in variable names just use an underscore so something like hello underscore world this is the convention".
- No frame on the grid lands in this interval (u22_1128s.png at 18:48 shows the editor with a blank line 3 and `print()`; u23_1178s.png at 19:38 shows `hello = 9` / `yes =`). The rules themselves come from the transcript only; I did not see the `1hello` red-squiggle example.

## 4. Frameworks page: game development and GUI options

**Answer (partial — insufficient evidence for the complete lists):** From the transcript, the game-development section includes **Pygame** (his "personal favourite"), and the GUI-development section includes **Tkinter** (Python) and **Java Swing**. The transcript says "some game development frameworks", implying more than one, but he names only Pygame. The full lists on that page are not determinable from my evidence.

**Evidence:**
- Transcript [06:47]–[07:05]: "some game development frameworks one of my personal favorites which is PI game here and then there's GUI development so to kinter that's a Python module Java swing".
- The nearest frame, u08_426s.png (07:06), shows the Repl.it **Languages** page with the "Popular" section (Python, Nodejs, C, Java, C++, Ruby, HTML/CSS/JS, Scheme, Go, Rust) and the start of "Practical" (Clojure); the frameworks section is below the visible area and is not shown. No other frame covers that page. So any framework beyond Pygame / Tkinter / Java Swing: insufficient evidence.

## 5. Python version in the Replit console

**Answer:** `Python 3.8.2 (default, Feb 26 2020, 02:56:10)`.

**Evidence (seen):** u10_526s.png (08:46, newly created `@TimRuscica/FirstGame` repl, empty main.py), u11_576s.png, u12_626s.png, u13_676s.png all show that line at the top of the console. The same line also appears in u00_25s.png for the finished-example repl. The transcript never states the version.

## 6. Age check in the finished example game

**Answer:** The age is read with `age = int(input("What is your age? "))` — the `input()` string is wrapped in `int()` so the value is a number. The condition is `if age >= 18:` followed by `print("You are old enough to play!")`.

**Evidence (seen):** u00_25s.png (00:25) shows the finished code: line 3 `age = int(input("What is your age? "))`, line 7 `if age >= 18:`, line 8 `print("You are old enough to play!")`. Also visible in u01_75s.png and u03_175s.png. Transcript [01:27]–[01:30] confirms entering 19 → "you are old enough to play". (Inference: the `int()` wrapper is what makes the `>= 18` comparison work; the video at this point does not explain it.)

## 7. Instructor's full name / Replit username

**Answer:** Tim Ruscica, Replit username **@TimRuscica**.

**Evidence (seen):** u07_376s.png (06:16) shows the profile page with heading "Tim Ruscica", "@TimRuscica (0)", "Tim has no repls yet". The header of every editor frame reads `@TimRuscica/FirstGame` (e.g. u00_25s.png, u10_526s.png), and the run URL is `https://FirstGame.timruscica.repl.run`. Transcript [01:25] has him enter "Tim" as his name; the surname comes only from the frames.

## 8. Demo playthrough: after swimming across the lake

**Answer:** The game prints "You managed to get across, but were bit by a fish and lost 5 health." and then "You notice a house and a river. Which do you go to (river/house)?" — the two options are **river** or **house**. (He then picks river and gets "you fell in the river and you lost".)

**Evidence:**
- Seen: u02_125s.png (02:05) shows the console output: "...swim across or go around (across/around)? across / You managed to get across, but were bit by a fish and lost 5 health. / You notice a house and a river. Which do you go to (river/house)?"
- Transcript [02:00]–[02:11]: "you manage to get across but you were bit by a fish and lost five health you notice a house in a river which do you go to the river or the house ... you fell in the river and you lost".
