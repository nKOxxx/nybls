# Answers

Method: transcript (captions, 6,472 words, reliable) read first; it carries Q1, Q2, Q3, Q8 and most of Q7. Q4, Q5, Q6 are on-screen-only, so one coverage sheet (1:00-10:20) plus two full frames and one zoom were spent. Confidence: sufficient on all eight.

## 1. Coding platform and prerequisites
**Answer:** Replit (repl.it), a free, online, browser-based IDE. You only need a web browser (any browser; works on a phone or iPad too) and an internet connection, plus a free Replit account (sign up / log in; signup asks for a favourite language, he recommends Python). Nothing to download or install.
**Evidence:** transcript [02:44]-[03:31] ("the only prerequisite for this series is that you have a browser and you have internet connection"), [04:36]-[04:53] (sign up / log in). Sheet tile [03:36] shows the repl.it landing page.

## 2. Four main data types; what counts as a string
**Answer:** str (string), int, float, bool. A string is anything wrapped in double or single quotation marks, a collection of characters / text; e.g. `"hello"`, `"hi"`, and `"989"` are all strings because they are inside quotes.
**Evidence:** transcript [12:54]-[14:06] ("the first one is str the second one is int then we have float and then we have bool... anything that's inside of double or single quotation marks is a string").

## 3. Variable naming rules; what to use instead of a space
**Answer:** A variable name may contain only lowercase and uppercase letters, underscores and numbers; no special characters other than underscore; it cannot start with a number (`hello1` is fine, `1hello` is not); no spaces. Instead of a space, use an underscore (e.g. `hello_world`), which is the convention.
**Evidence:** transcript [18:23]-[19:30] ("it can only contain lowercase and uppercase letters underscores and numbers... cannot start with a number... just use an underscore so something like hello underscore world").

## 4. Frameworks shown on the Replit languages page
**Answer:** Game Development: Pygame ("A cross-platform python graphics library"), Love2D ("A free, open-source Lua framework for 2D games"), Pyxel ("A retro game engine for Python"). GUI Development: Tkinter ("Python's standard GUI toolkit") and Java Swing ("A Java GUI widget toolkit").
**Evidence:** frame f_415000_1568.png [06:55], Languages page with both sections fully visible; transcript [06:47]-[07:02] confirms Pygame, Tkinter, Java Swing.

## 5. Exact Python version in the Replit console
**Answer:** `Python 3.8.2 (default, Feb 26 2020, 02:56:10)`.
**Evidence:** zoom z_547000_60_10_40.png [09:07] of the console in the newly created FirstGame repl; the same string is also visible in frame f_65000_1568.png [01:05] and sheet tiles [09:07], [09:09], [09:14].

## 6. Age check in the finished example game
**Answer:** Line 3: `age = int(input("What is your age? "))`, so the text typed by the player is converted to an integer with `int()`. Line 7: `if age >= 18:` followed by `print("You are old enough to play!")`. The int() conversion is what makes the `>= 18` numeric comparison valid.
**Evidence:** frame f_65000_1568.png [01:05], main.py lines 1-10 readable in the editor pane; also partly visible in sheet tile [01:47]. Transcript [01:27]-[01:30] shows age 19 producing "you are old enough to play".

## 7. Instructor's name / Replit username
**Answer:** Tim Ruscica; Replit username @TimRuscica (repl URL https://FirstGame.timruscica.repl.run).
**Evidence:** sheet tile [06:25] (profile page "Tim Ruscica", "@TimRuscica (0)"); frame [01:05] header "@TimRuscica/FirstGame"; transcript [01:25] he types "Tim" as his name; video title/channel the available material "Tech With Tim".

## 8. Demo playthrough after swimming across the lake
**Answer:** The game says he managed to get across but was bitten by a fish and lost 5 health. He is then told he notices a house and a river, and given the two options: go to the river or go to the house. (He picks the river, falls in, and loses.)
**Evidence:** transcript [01:57]-[02:11] ("you manage to get across but you were bit by a fish and lost five health you notice a house in a river which do you go to the river or the house").

## Evidence strip
- [01:47, 03:36, 06:25, 09:07, 09:09, 09:14] sheet_000.png: demo game output and code, repl.it landing page, Tim Ruscica profile, settings/console with Python version string.
- [01:05] f_65000_1568.png: main.py lines 1-10 of finished game (int(input(...)), if age >= 18), console showing Python 3.8.2, header @TimRuscica/FirstGame.
- [06:55] f_415000_1568.png: Replit Languages page, Game Development and GUI Development sections.
- [09:07] z_547000_60_10_40.png: zoom on console, "Python 3.8.2 (default, Feb 26 2020, 02:56:10)".
