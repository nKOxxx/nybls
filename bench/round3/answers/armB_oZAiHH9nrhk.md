# Arm B (iterative, pinned 0.8.0) — oZAiHH9nrhk (stock market, 24:37)
COST: 13 images, ~19,163 visual tokens (budget 13/99). No tool file modified.
1 presenter, maroon shirt, teal-lit studio, shelves/books/plant/LED strip; also read the
  creator's name off the disclaimer card (2)
2 title cards: found STOCK MARKET, "Chapter 1 / The Origin of Stock Market", "How the
  Stock Market Works", "Chapter 4 / Popularity", a full DISCLAIMER card, "To be
  continued....". Did NOT find the ground truth's DRHP / BOOK BUILDING PROCESS cards -
  which Arm A DID find. Honestly declined on the occluded red subtitle line (1)
3 generated B-roll: correct and extensive (2)
4 second person: found two real news-footage people (seated anchor 03:35, standing Hindi
  anchor 22:30) but not the ground truth's bearded man in yellow/olive against green (1)
5 microphone: FDUCE dynamic mic on a boom, read FROM A ZOOM (2)
SCORE 8/10 at 19,163 tokens — a TIE with Arm A's 8/10 at 53,760.

TWO FINDINGS THAT MATTER MORE THAN THE SCORE:
- **The transcript is degenerate.** Hindi/Urdu speech mis-ASR'd into pseudo-Latin, one line
  looping 01:48-24:35, 65 unique lines in 906. All five answers rest on frames alone. This
  is the ASR-guard failure mode reproducing inside the benchmark, and it is direct evidence
  for the inverse relationship between transcript quality and the value of looking.
- **The tile-snapping fix actively cost it Q2.** `frames --at 219` and `--at 1420/1470` were
  silently snapped to already-served timestamps, so it could not sample a nearby instant of
  the title animation to see past an occluding banknote. It reported this rather than
  patching the tool. The round-2 contamination fix has a real downside in production.
  Also `sheet --range 1320 1477` returned tiles spanning only 21:58-22:52, not the request.
