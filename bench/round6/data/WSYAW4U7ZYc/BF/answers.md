# Answers — WSYAW4U7ZYc_bf (Stanford CS229 "Building LLMs" lecture, 104 min)

Method: Round 0 free transcript (captions, ~22k words) answered Q1–Q4 and Q7/Q8 in words; four targeted full-resolution frames were requested in one round for the four slide-only facts (dataset sizes, LIMA plot, AlpacaEval table, AMP slide). Evaluator after round 1: sufficient. No sheets, no zooms.

## 1. Chinchilla ratio vs. production ratio
- Chinchilla: **20 tokens per parameter** ("if you add one more parameter, you should train on 20 more tokens") [51:27]–[51:39].
- Once inference cost is considered: **~150 tokens per parameter ("150 to 1")**, which he says is roughly what the best production models are trained on [52:04]–[52:39].
- Evidence: transcript lines [51:27]–[52:39]. (Aside: he notes Llama 3 400B sits at ~40 tokens/param, between the two [55:24]–[55:44].)

## 2. Cost estimate for Llama 3 400B
- Compute: 16,000 H100s, ~70 days → **~26 million GPU-hours** by his back-of-envelope (Meta reported ~30M) [56:43]–[57:13].
- Rental rate: **~$2 per H100-hour** (he calls it a lower bound) [57:29]–[57:36].
- Rental cost: 26M × $2 = **~$52 million** [57:36]–[57:55].
- Salary: **50 employees × $500k/yr ≈ $25 million** [57:56]–[58:04].
- Total: **~$75 million**, "probably off by ~$10 million" [58:04]–[58:16].
- Evidence: transcript [56:43]–[58:16].

## 3. Why tokenizers, not words or characters
- **Whole words as tokens:** a typo produces a word with no token, so you cannot feed it to the model; and word-splitting by spaces does not generalize to languages such as Thai that have no spaces between words [10:53]–[11:34].
- **Characters as tokens:** it would work, but sequences become extremely long, and transformer cost grows quadratically with sequence length [11:36]–[12:01].
- Tokenizers (≈3–4 letters per token on average) address both [12:01]–[12:17].
- Evidence: transcript [10:51]–[12:17].

## 4. Perplexity: academic benchmarking and aligned models
- **Not used in academic benchmarking any more** because it depends on the tokenizer and on the data you evaluate on [20:59]–[21:07]; expanded in Q&A: perplexity ranges between 1 and vocabulary size, so a 100k-vocab tokenizer (his Gemini example) and a 10k-vocab tokenizer (his ChatGPT example) have different upper bounds and are not comparable [25:16]–[25:52]. He adds it is still used internally during development [21:09]–[21:15].
- **Cannot evaluate an aligned (post-PPO) model** because such models are no longer calibrated, do not give distributions, and "just optimize for one thing" [88:01]–[88:17]; in Q&A: the optimal PPO solution is essentially a delta on one answer, so a semantically slightly different reference answer gets ~zero likelihood; after PPO they are trained to be policies, not maximum-likelihood models [89:12]–[89:52].
- Evidence: transcript [20:59]–[21:15], [25:16]–[25:52], [87:52]–[89:52].

## 5. Open academic pre-training datasets on the slide
Slide 26 "Data" lists, besides C4 (150B tokens | 800GB) and The Pile (280B tokens):
- **Dolma — 3T tokens**
- **FineWeb — 15T tokens**
- Evidence: frame f_2335000_1568.png at [38:55] (slide text read directly); transcript corroborates the 150B→15T range [38:47]–[39:08].

## 6. AlpacaEval length-bias table, Mixtral-8x7B-Instruct-v0.1 row
- concise **13.7**, standard **18.3**, verbose **24.6**
- Evidence: frame f_5570000_1568.png at [92:50] (slide 59, "LLM evaluation: spurious correlation", table AlpacaEval LC [Dubois+ 2023]); the lecturer discusses the GPT-4 row in speech [92:38]–[93:11] but never speaks the Mixtral numbers, so these come from the slide only. Digits were legible at full-frame resolution.

## 7. Automatic Mixed Precision recipe
- 16-bit format: **bf16** (slide: "Matrix multiplications can use bf16 instead of fp32").
- Slide and speech give the split as: **weights stored in fp32**, converted to **bf16 just before computation**; the weight **updates are done in fp32** (so a small learning rate still changes the weights). The slide's stated exceptions to low precision are "exp & updates" (i.e. exponentials and updates stay fp32).
- Caveat: the slide (slide 68) does not enumerate further tensor categories (e.g. activations, gradients, optimizer states) beyond "weights in fp32, computation in bf16"; if the question expects such a list, the lecture does not provide it — insufficient evidence beyond the above.
- Evidence: frame f_6060000_1568.png at [101:00]; transcript [100:42]–[101:24].

## 8. LIMA SFT data-quantity experiment
- Range tested: **2K to 32K training examples** (x-axis: 2K, 4K, 8K, 16K, 32K).
- Result: generation quality is **flat** across the range — scaling the SFT data "really doesn't help much" [65:28]–[65:41].
- Quality score: roughly **3.8–3.9** on the "Generation Quality" axis (points ~3.82–3.86, error bars within ~3.75–3.95; axis 3.2–4.0).
- Evidence: frame f_3935000_1568.png at [65:35] (slide 43, LIMA [Zhou+ 2023]); transcript [65:19]–[65:41].

## Evidence strip
- [38:55] f_2335000_1568.png — slide 26 "Data": C4 150B|800GB, The Pile 280B, Dolma 3T, FineWeb 15T.
- [65:35] f_3935000_1568.png — slide 43 LIMA plot: generation quality ≈3.8 flat from 2K to 32K examples.
- [92:50] f_5570000_1568.png — slide 59 AlpacaEval concise/standard/verbose table; Mixtral row 13.7 / 18.3 / 24.6.
- [101:00] f_6060000_1568.png — slide 68 "Systems: low precision": bf16 matmuls, AMP weights fp32 → bf16 before computation.

## Ledger
watched 104 min · examined 4 images (~7,168 visual tokens, ≈$0.01 at sonnet-5 input rate) of ~156,438 total frames · budget 4/200 units

## Tool-file statement
I did not modify, create, or delete any file in the nybls repository or installation. The only file written is this answers.md. (Note: `nybls probe WSYAW4U7ZYc_bf` returns "error: not a file" when given a bare id; the store was already populated, so I read transcript.txt/scenes.json/manifest.json directly and used `nybls frames`/`nybls ledger` normally.)
