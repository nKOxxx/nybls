# Ground truth (video: Stanford lecture "Building LLMs")

## Q1 — label S
Answer: Chinchilla optimum is 20 tokens per parameter. With inference cost considered, about 150 tokens per parameter (150:1); that is roughly what the best production models use now.
Evidence: transcript [51:27] "20 tokens for every parameter that you train"; [52:15]-[52:33] "around 150 ... tokens per parameter ... 150 to 1, that's around what the best models are trained on right now".
Partial: only one of the two numbers correct (20 or 150).

## Q2 — label S
Answer: ~26 million GPU hours (16,000 H100s, ~70 days; Meta said ~30M actually). Rental lower bound ~$2 per H100-hour. 26M x $2 = ~$52M. Salary: 50 employees at $500k/year = ~$25M. Total ~ $75M (he says off by ~10M).
Evidence: transcript [56:41]-[58:16] ("26 million GPU hours", "$2 per hour", "52 million dollars", "50 employees 500k per year ... 25 million", "around 75 million dollars").
Partial: total $75M and $52M GPU cost without the salary assumption, or missing the $2/hr rate.

## Q3 — label S
Answer: Whole words: a typo has no token, so the word can't be fed in; also words don't work for languages without spaces such as Thai; tokens are more general than words. Characters: sequences become super long, and transformer cost grows quadratically with sequence length. Tokenizers (e.g. BPE) give common subsequences a token, ~3-4 letters on average.
Evidence: transcript [10:53]-[12:19].
Partial: only one option's problem given, or only the typo/quadratic point.

## Q4 — label S
Answer: Not used in academic benchmarking because it depends on the tokenizer (vocabulary size is its upper bound, e.g. 10k vs 100k tokens) and on the evaluation data. Not usable for aligned/PPO models because they are not calibrated: they are trained as policies, not by maximum likelihood, so they don't give meaningful distributions/likelihoods (optimum collapses toward a single output, near-zero likelihood to semantically different answers).
Evidence: transcript [20:59]-[21:09], [25:16]-[25:50]; [88:01]-[88:15], [89:14]-[89:52].
Partial: tokenizer dependence only, or calibration reason only.

## Q5 — label V
Answer: Dolma (3T tokens) and FineWeb (15T tokens). (Slide also lists C4 150B tokens / 800GB and The Pile 280B tokens.)
Evidence: frame g_02385s.png (slide "Data", "Common academic datasets"). Transcript does not name Dolma or FineWeb; at [38:51]-[38:56] he gives "150 billion tokens ... 800 gigabytes", "15 trillion tokens", and "the pile ... 280B" ([39:28], [39:54]) without naming Dolma/FineWeb or tying 3T to Dolma.
Key terms: Dolma, 3T tokens, FineWeb, 15T tokens.
Partial: one dataset right; or sizes without names.

## Q6 — label V
Answer: Mixtral-8x7B-Instruct-v0.1: concise 13.7, standard 18.3, verbose 24.6 (win rates, percent).
Evidence: frame g_05565s.png (slide "LLM evaluation: spurious correlation", AlpacaEval table). Transcript only discusses GPT-4 ([92:53]-[93:13]: 50%, 64.4% verbose, 20% concise); Mixtral is never mentioned in that context.
Key terms: Mixtral-8x7B-Instruct-v0.1, 13.7, 18.3, 24.6.
Partial: correct direction (verbose > standard > concise) with one or two correct numbers.

## Q7 — label V
Answer: bf16 (replacing fp32) for matrix multiplications; activations in bf16 (main memory gains) and gradients in bf16 (memory gains); weights are stored in fp32 and converted to bf16 before computation; master weights updated in fp32 (full precision).
Evidence: frame g_06042s.png (slide "Systems: low precision"). Transcript at [100:25]-[101:23] says only "16 bits" for computation and "32 bits" for stored weights and updates (and garbled "60 bits"); it never says bf16, activations or gradients.
Key terms: bf16, fp32, activations, gradients, master weights, Automatic Mixed Precision (AMP).
Partial: "bf16" plus only one of activations/gradients, or fp32-weights-only without bf16 name.

## Q8 — label B
Answer: Tested 2,000 to 32,000 SFT training examples (2K, 4K, 8K, 16K, 32K). Quality stays essentially flat (it doesn't help much; very slight downward drift within error bars) at roughly 3.8 on the "Generation Quality" axis. Interpretation: SFT mostly teaches format; the knowledge is already in the pretrained model.
Evidence: transcript [65:31]-[65:41] ("from 2,000 to 32,000, it really doesn't help much") and [65:43]-[66:27]; frame g_03922s.png (LIMA chart, y-axis Generation Quality ~3.8, x-axis 2K-32K).
Key terms for the on-screen part: ~3.8, Generation Quality, 2K 4K 8K 16K 32K.
Partial: flat/doesn't help with the 2K-32K range but no score; or score without the range/trend.
