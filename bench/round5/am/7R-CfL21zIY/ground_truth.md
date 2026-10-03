# Ground truth — "Python Tutorial for Beginners (with mini-project)" part 1 (7R-CfL21zIY, ~25 min)

## Q1
**Label: S**
Answer: The platform is Repl.it (repl.it), a free online browser-based IDE / coding environment. The only prerequisites are a browser and an internet connection — nothing to download or install; it even works on a phone or iPad/mobile devices. (He will link it in the description.)
Evidence: transcript [02:47]–[03:33] "we're actually gonna be using a platform called rep lit ... it's spelt repl dot i t that is the website URL ... this is a free browser-based coding environment ... the only prerequisite for this series is that you have a browser and you have internet connection ... you can actually do all of what I'm gonna be showing you on your phone ... on an iPad"; [03:35] "it's just an online browser-based IDE". Frames g_00205s.png (repl.it landing page "Code and collaborate, without friction", "free, collaborative, in-browser IDE to code in 50+ languages") corroborate.
Partial credit: naming Repl.it plus either "free/browser-based" or "just a browser + internet"; missing the phone/iPad point is acceptable.

## Q2
**Label: S**
Answer: The four main data types are string (str), int, float, and bool. A string is anything wrapped inside a matching set of double or single quotation marks — a collection of characters / text (so "989"/"89" in quotes is a string, not a number); an int is any whole number with no decimal point (can be negative); a float is any number with a floating decimal point (even 100.0); a bool is one of two values, True or False, with the capital T/F mattering.
Evidence: transcript [13:26]–[15:13] "the first one is screen [string] the second one is int then we have float and then we have bool ... a string which is represented by STR ... anything wrapped inside of double quotation marks or single quotation marks ... intz are any whole number ... a float is any number that has a floating decimal point ... a boolean is one of two values true or false ... the capital T and the capital F is very important". Frames g_00815s.png / g_00915s.png show on screen: str/int/float/bool and examples string "hello", 'hi', "89"; int 8, 7, -9, 100000; float 6.0, 7.5, -9.8, -100.0; bool True, False.
Partial credit: all four types named but string definition incomplete; listing only 3 of 4 types is wrong, not partial.

## Q3
**Label: S**
Answer: A variable name can only contain lowercase and uppercase letters, underscores, and numbers — no other special characters — and it cannot start with a number (hello1 is valid, 1hello is not; a number in the middle is fine). Spaces are not allowed; use an underscore instead (the convention, e.g. hello_world, separating words with underscores).
Evidence: transcript [18:37]–[19:30] "it can only contain lowercase and uppercase letters underscores and numbers ... cannot contain any special characters other than an underscore and it cannot start with a number ... something like hello one is totally valid ... as soon as I go one hello ... not allowed ... if you want to do a space ... just use an underscore so something like hello underscore world this is the convention". Frames g_01135s.png (hello1 = 9), g_01155s.png (hello_), g_01175s.png corroborate.
Partial credit: letters/numbers/underscore + "can't start with a number" without the underscore-for-space convention.

## Q4
**Label: B**
Answer: On the Languages page, under Game Development Replit lists three frameworks: Pygame ("a cross-platform python graphics library"), Love2D ("a free, open-source Lua framework for 2D games") and Pyxel ("a retro game engine for Python"). Under GUI Development it lists Tkinter ("Python's standard GUI toolkit") and Java Swing ("a Java GUI widget toolkit").
Evidence: frame g_00415s.png shows the full on-screen list (Game Development: Pygame, Love2D, Pyxel; GUI Development: Tkinter, Java Swing). Transcript [06:52]–[07:05] only names some of them: "there is some game development frameworks one of my personal favorites which is PI game [pygame] here and then there's GUI development so to kinter [tkinter] that's a Python module Java swing" — the speech never mentions Love2D or Pyxel, so the complete Game Development list requires the screen.
**Key terms:** "Love2D", "Pyxel", "Pygame", "Tkinter", "Java Swing", "Game Development", "GUI Development"
Partial credit: Pygame + Tkinter + Java Swing only (the spoken subset) is partial; full credit needs Love2D and Pyxel for the game-dev list.

## Q5
**Label: V**
Answer: Python 3.8.2. The console banner in the new repl reads "Python 3.8.2 (default, Feb 26 2020, 02:56:10)".
Evidence: frames g_00495s.png, g_00515s.png, g_00555s.png, g_00595s.png (console right/bottom pane banner). The transcript never states a Python version (no mention of "3.8" anywhere in speech).
**Key terms:** "3.8.2", "Python 3.8.2", "Feb 26 2020"
Partial credit: "Python 3.8" without the patch version counts as essentially correct; "Python 3" alone is insufficient.

## Q6
**Label: V**
Answer: The demo code reads the age with a cast to int — `age = int(input("What is your age? "))` (line 3) — and then gates play with `if age >= 18:` (line 7), printing "You are old enough to play!" when true. So the threshold is 18 (greater than or equal to), and int() conversion is what makes the numeric comparison possible.
Evidence: frames g_00015s.png and g_00165s.png show lines 1–17 of the finished main.py: line 3 `age = int(input("What is your age? "))`, line 5 `health = 10`, line 7 `if age >= 18:`, line 8 `print("You are old enough to play!")`. The transcript never states the number 18, the `>=` condition, or the int() cast — it only says [01:27]–[01:31] "what is your age let's put 19 and says you are old enough to play" and [22:31]-[22:33] "make sure there's certain age before we let them play".
**Key terms:** "18", "age >= 18", "int(", "int(input"
Partial credit: ">= 18" without mentioning the int() conversion; "18" alone with no condition direction is weaker partial. Any other number (e.g. 19, which is only the age typed in) is wrong.

## Q7
**Label: V**
Answer: Tim Ruscica — his Replit profile shows "Tim Ruscica" with username @TimRuscica, and the repl lives at @TimRuscica/FirstGame (URL https://FirstGame.timruscica.repl.run).
Evidence: frames g_00335s.png (profile page "Tim Ruscica", "@TimRuscica (0)", "Tim has no repls yet"), g_00495s.png and later editor frames (@TimRuscica/FirstGame header; FirstGame.timruscica.repl.run URL bar). The transcript only ever gives the first name "Tim" ("what is your name I'm gonna put Tim", [01:25]); the surname/username appears only on screen.
**Key terms:** "Ruscica", "TimRuscica", "@TimRuscica"
Partial credit: "Tim" alone is not enough (it is in the speech); credit requires the surname or the @TimRuscica handle.

## Q8
**Label: S**
Answer: After choosing to swim across ("across"), the game says he managed to get across but was bitten by a fish and lost 5 health; he is then given the choice between a house and a river ("You notice a house and a river. Which do you go to (river/house)?"). (In the demo he then picks the river, falls in, and loses.)
Evidence: transcript [02:00]–[02:11] "I go across says you manage to get across but you were bit by a fish and lost five health you notice a house in a river which do you go to the river or the house so let's decide to go to the river and let's see you fell in the river and you lost". Frame g_00125s.png shows the console text verbatim: "You managed to get across, but were bit by a fish and lost 5 health. / You notice a house and a river. Which do you go to (river/house)?".
Partial credit: "bitten by a fish, lost 5 health" without the house/river follow-up choice, or vice versa.
