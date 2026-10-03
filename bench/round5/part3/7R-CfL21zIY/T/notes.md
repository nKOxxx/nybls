# Notes on program.py (reconstructed from transcript only)

## What this video actually builds

This is video 1 of a 3-part beginner series (Repl.it, "first game"). The code written in
this video is only the opening of a choose-your-own-adventure game. The full game with
health, left/right, lake, river/house branches is only *demoed* at [01:23]-[02:30] as a
preview of where the series ends up; its code is never shown or written in this video, so
it is NOT in program.py. Writing it would be guessing part 3's code.

## Evidence for each line

- `print("Welcome to my first game")` — [12:19]-[12:40]. Exact capitalization unknown;
  console readback [01:23] says "welcome to my first game", I chose a capital W.
- Multi-line comment on data types — [13:24]-[16:19]. He writes str/int/float/bool notes
  with example values ("hello", "hi", "989"; 6.0, 7.5, -9.8, -100.0; True/False), wraps
  them in triple quotes and says he leaves it near the bottom of the screen. Exact wording
  and position in the file are my choice; the transcript does not show the literal text.
- `name = input("What is your name? ")` — [20:40]-[21:04], including the trailing space.
- `age = input("What is your age? ")` — [22:35]-[22:47]. Trailing space assumed to match
  the name prompt; the transcript only confirms the question text.
- `print("Hello", name, "you are", age, "years old")` — [23:33]-[24:10], comma-separated
  print; final run [24:21] prints "hello Tim you are 19 years old". Capitalization of
  "Hello" is my choice.

## Things shown but not kept in the final version

- Scratch variable examples (`x = 5`, `print(x)`, `x = True`, `hello1 = 9`, `hello_world`,
  `yes = "hello"`, `hello = yes`, `hello = hello + 9`) at [16:43]-[20:05]. The run at
  [22:25] prints only the welcome line before asking the name, so these were removed or
  commented out; I omitted them.
- `print(name)` at [22:08] was a proof-of-concept; the final run [24:21] shows no bare
  name line, so it was replaced by the combined print.
- A `print("hello")` / `print("hello world")` test at [10:01] and [11:38], and a `#`
  single-line comment demo at [16:00] — not part of the final file.

## Unknowns

- Age is stored as a string (no `int()`), matching the video at this point; conversion is
  announced for the next video.
- Whether the triple-quoted comment sits above or below the input lines is not
  determinable; I placed it after the welcome print.
