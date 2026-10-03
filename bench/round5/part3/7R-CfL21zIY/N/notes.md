# Notes — 7R-CfL21zIY (Tech With Tim, "Python Beginner Project Tutorial #1 - Your First Python Project", 25:04)

Evidence available: title, channel, duration only. The video itself was not watched; no transcript or frames.

## What I assumed
- From general knowledge of Tech With Tim's beginner-project series, the first project is a
  terminal **number guessing game**: user picks an upper bound, the program picks a random
  integer in range, the user guesses with above/below hints, and the guess count is printed.
  This identification is UNVERIFIED from the evidence here — it could instead be another of
  his first-project staples (quiz game, rock-paper-scissors, mad libs).

## Details chosen by me, not determined by the evidence
- Exact prompt and message strings ("Type a number: ", "Make a guess: ", "You got it!",
  "You were above/below the number!", "You got it in N guesses").
- Input validation via `str.isdigit()` with `quit()` on bad top-of-range input and
  `continue` on a bad guess.
- Range `random.randint(0, top_of_range)` (inclusive of 0) rather than 1..n.
- Variable names (`top_of_range`, `random_number`, `guesses`, `user_guess`).
- No replay loop and no function/`main()` wrapper, matching a 25-minute single-script beginner tutorial.
