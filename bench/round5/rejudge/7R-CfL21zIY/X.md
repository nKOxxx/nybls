# Answers


## 1. Coding platform and prerequisites

**Answer:** Replit (repl.it), a free, online browser-based IDE. You need only a browser and an internet connection (any browser; works on phone/iPad), plus a free Replit account (sign up / log in).

**Evidence (transcript):**
- [02:47]-[02:52] "we're actually gonna be using a platform called rep lit ... this is an online browser-based coding environment"
- [03:05]-[03:09] "spelt repl dot i t that is the website URL"
- [03:12]-[03:20] "a free browser-based coding environment ... the only prerequisite for this series is that you have a browser and you have internet connection"
- [03:23]-[03:30] "it doesn't really matter what that browser is ... you can actually do all of what I'm gonna be showing you on your phone ... on an iPad"
- [04:39]-[04:42] "you need to go to this link and obviously sign up if you don't have an account or log in"

## 2. Four main data types; what counts as a string

**Answer:** string (str), int, float, bool. A string is anything wrapped in double or single quotation marks — a collection of characters / text — so "hi" and "989" in quotes are both strings.

**Evidence (transcript):**
- [13:26]-[13:29] "the first one is screen [str] the second one is int then we have float and then we have bool"
- [13:32]-[13:41] "a string which is represented by STR ... is anything wrapped inside of double quotation marks or single quotation marks"
- [13:45]-[13:57] "hi is an example of a string 989 is an example of a string anything that's inside of double or single quotation marks is a string and strings are just a collection of characters they're just text"

## 3. Variable naming rules; what to use instead of a space

**Answer:** A variable name may contain only lowercase and uppercase letters, underscores, and numbers; no special characters other than underscore; it cannot start with a number (e.g. `hello1` ok, `1hello` not). Spaces are not allowed; use an underscore instead (e.g. `hello_world`), which is the convention for separating words.

**Evidence (transcript):**
- [18:37]-[18:49] "it can only contain lowercase and uppercase letters underscores and numbers so it cannot contain any special characters other than an underscore and it cannot start with a number"
- [18:49]-[19:03] "hello one is totally valid ... as soon as I go one hello ... red squiggly line not allowed"
- [19:16]-[19:28] "there's no spaces allowed in variable names just use an underscore so something like hello underscore world this is the convention"

## 4. Frameworks page: game dev and GUI options

**Answer (partial):** The transcript names only Pygame under game development, and Tkinter (Python) and Java Swing under GUI development. The full list shown on the page is not readable from the transcript — **insufficient evidence** for the complete lists; the question requires the frame.

**Evidence (transcript):**
- [06:52]-[07:02] "there is some game development frameworks one of my personal favorites which is PI game here and then there's GUI development so to kinter that's a Python module Java swing"

## 5. Exact Python version shown in the Replit console

**Answer:** **Insufficient evidence.** The version is never spoken; it would only be visible on screen. (Own knowledge, unverified: Replit Python repls of that era, ~2019, typically ran Python 3.7.x or 3.8.x — but this is a guess, not an answer.)

**Evidence:** No transcript mention of a Python version anywhere (full transcript searched).

## 6. How the finished game decides the player is old enough

**Answer:** **Insufficient evidence for the exact condition.** The demo only shows the behavior: enter age 19 → "you are old enough to play". The code is not read aloud. Inference (labelled): since the instructor later uses `age = input("What is your age? ")` [22:35]-[22:47], which returns a string, a working comparison would require converting to int (e.g. `int(input(...))` or `int(age)`) and a condition like `if age >= 18:` — but the threshold and exact expression are not stated in this video; the instructor defers conditions to the next video [24:50]-[24:51].

**Evidence (transcript):**
- [01:23]-[01:31] "what is your name I'm gonna put Tim what is your age let's put 19 and says you are old enough to play"
- [22:35]-[22:47] "let's say age equals input ... I'm gonna put what is your age"
- [24:46]-[24:51] "in the next video we're gonna ... talk a bit about conditions"

## 7. Instructor's full name or Replit username

**Answer (partial):** The transcript gives only the first name "Tim" (he types it as the player's name, [01:25], [21:16]). Full name / Replit username is not spoken — **insufficient evidence** from the transcript. Own knowledge (labelled, unverified against the video): this style and content matches Tim Ruscica, "Tech With Tim", whose Replit username is commonly "techwithtim" — but the video would need to be viewed to confirm what is actually shown on screen.

**Evidence (transcript):**
- [01:25] "what is your name I'm gonna put Tim"
- [06:01]-[06:05] "we select on our little logo you can see that's my little drawn picture of me" (no name read out)

## 8. Demo: after swimming across the lake

**Answer:** He manages to get across but is bitten by a fish and loses 5 health. He then notices a house and a river and is asked which to go to: the river or the house. (He picks the river, falls in, and loses.)

**Evidence (transcript):**
- [02:00]-[02:07] "I go across says you manage to get across but you were bit by a fish and lost five health you notice a house in a river which do you go to the river or the house"
- [02:07]-[02:11] "let's decide to go to the river and let's see you fell in the river and you lost"
