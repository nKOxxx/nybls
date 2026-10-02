# Answers — Wlu4MsBnjuk ("ASMR Programming - Coding a Snake Game - No Talking")

No speech in this video (transcript UNRELIABLE, whisper looped on "(keyboard clicking)"); everything below is read from frames.

1. **Editor:** Visual Studio Code (dark theme; VS Code activity bar with Explorer/Search/Source Control/Run/Extensions/Testing/Python icons, PROBLEMS/TERMINAL/OUTPUT/DEBUG CONSOLE panel). **File:** `snake.py` — shown in the editor tab and in the breadcrumb "snake.py > ..." [01:30], [18:47], [24:04]. The traceback path confirms it lives in a folder named `snake`.

2. **First line (line 1):** `import pygame, sys, time, random` [01:30], unchanged at [24:04]. Language: **Python** (the file is `.py`, the terminal runs `python3 snake.py`, and pygame prints "Python 3.9.3"). Game library: **pygame** (terminal banner at [24:04]: "pygame 2.1.0 (SDL 2.0.16, Python 3.9.3)").

3. **Traceback** [18:47] (printed after Ctrl‑C, shown as `^CTraceback (most recent call last):`):
   - File path and line: `File "/Users/servetg/Desktop/snake/snake.py", line 130, in <module>`
   - Line of code it points to: `fps_controller.tick(speed)`
   - Exception type: `KeyboardInterrupt`
   (The same traceback is visible again in the terminal at [21:33] after a later run was stopped.)

4. **frame_size_x / frame_size_y:**
   - First written near the start [01:30]: `frame_size_x = 720` and `frame_size_y= 480` (lines 7–8; note no space before `=` on the y line). Still 720/480 at [18:51] and at [21:23].
   - Intermediate edit at [21:28]–[21:38]: changed to `1440` / `960` (contact-sheet resolution).
   - **Last edit visible at the end of the video:** `frame_size_x = 1380` and `frame_size_y= 840` (lines 7–8 at [23:31]; after the comments are inserted they sit at lines 12–13 [23:58] / line 14 for x at [24:04]).

5. **Comments typed at the top of the file in the final minute** (lines 5 and 7, inserted above `speed = 15`) [23:46]–[24:04]:
   - Line 5: `# THANKS FOR WATHING, WHAT KIND OF GAMES U WANT TO SEE NEXT TIME? PLEASE STATE IT IN THE COMM` — this is everything that is visible; the line continues past the right edge of the recorded editor area (the video frame crops the editor at that point, and the view never scrolls horizontally), so any characters after "COMM" (presumably "COMMENTS") are not shown on screen and cannot be confirmed. Misspellings as typed: "WATHING" (for WATCHING), "U" (for YOU).
   - Line 7: `# CHEERSS` (double S as typed).
   Partial on this item only: the tail of line 5 is physically outside the recorded frame.

## Evidence strip

- [00:30–05:30] sheet_000: VS Code, snake.py being written from scratch; line 1 import, speed, frame sizes, pygame.init, colors, init_vars.
- [06:30–11:30] sheet_001: game loop, key handling, movement, eating apple, spawn food.
- [08:10, 16:29–17:31] sheet_002: first runs of the game (small "Snake Game" window), terminal "python3 snake.py" with pygame banner.
- [18:02–20:53] sheet_003: game at score 4, traceback partially visible at 18:47, game window runs.
- [01:30] zoom lines 1–6: `import pygame, sys, time, random`, `speed = 15`, `#windows sizes`.
- [18:47] zoom terminal: "snake.py", line 130, i" fragment.
- [21:15–23:49] sheet_004: larger game windows (score 7, 24, 42), comment being typed at 23:49, `frame_size_x = 1380`.
- [01:30] zoom lines 2–7: `frame_size_x = 720`.
- [18:47] frame: full traceback — path /Users/servetg/Desktop/snake/snake.py line 130 in <module>, `fps_controller.tick(speed)`, KeyboardInterrupt; code lines 98–117.
- [18:51] frame: editor scrolled to top, `speed = 20`, `frame_size_x = 720`, `frame_size_y= 480`; same traceback below.
- [24:04] zoom lines 2–14: comment line 5, `# CHEERSS`, `speed = 15`, `frame_size_x = 1380`.
- [24:04] frame: full final editor view; comment cut at "IN THE COMM" at the frame edge; terminal shows pygame 2.1.0 banner.
- [21:18–21:43] sheet_005: 720/480 at 21:23, changed to 1440/960 at 21:28–21:38, traceback again at 21:33, `clear` typed at 21:38.
- [23:23–24:01] sheet_006: score 42 run, 1380/840 at 23:31, "# THANKS |" at 23:38, comment growing at 23:46/23:53, "# CHEERSS" at 24:01.
- [23:31] zoom lines 1–5: import line, `speed = 15`, `#windows sizes`.
- [23:58] frame: `frame_size_x = 1380`, `frame_size_y= 840` at lines 12–13 below the comments; comment line cut at "COMM".
- [23:53], [24:01] frames: near-duplicates of sheet tiles (no new information).

## Ledger

watched 24 min · examined 18 images (~20,784 visual tokens, ≈$0.04 at sonnet-5 input rate) of ~36,137 total frames · budget 18/97 units
