# Answers

1. Chinchilla: 20 tokens per parameter [51:30-51:39]. With inference cost considered, lecturer says about 150 tokens per parameter (150:1), what best production models are trained on [52:15-52:39]. Evidence: transcript.

2. Llama 3 400B [56:41-58:16]: about 26 million GPU-hours by his back-of-envelope (16,000 H100s, ~70 days; Meta reportedly said 30 million). Rental rate assumed about $2 per H100-hour (a lower bound). Rental cost about $52 million. Salaries: 50 employees at $500k/year = about $25 million. Total about $75 million (he says he may be off by ~10M). Evidence: transcript.

3. [10:51-12:19] Whole words as tokens: a typo gives a word with no token, so the model cannot be fed it; also words don't work for languages without spaces such as Thai (tokens are more general than words). Characters as tokens: works, but sequences get very long and transformer cost grows quadratically with sequence length. Tokenizers (e.g. BPE) merge common subsequences, ~3-4 letters per token on average, to handle both problems.

4. Not used for academic benchmarking [20:59-21:07, 25:16-25:50]: it depends on the tokenizer (perplexity ranges from 1 to vocabulary size, so a 100k-token vocab has a worse upper bound than a 10k one) and on the evaluation data; still used in LLM development. Not usable post-PPO [88:03-89:50]: aligned models are not calibrated, they don't output real distributions, they optimize for one thing; the PPO optimum collapses toward a near-delta on one answer, giving ~zero likelihood to semantically different answers; they are trained as policies, not by maximum likelihood.

5. Slide "Data" (frame f_2330000_1568.png, ~38:50): besides The Pile (280B tokens) and C4 (150B tokens | 800GB): Dolma (3T tokens) and FineWeb (15T tokens).

6. Slide 59 table (frame f_5560000_1568.png, ~92:40): Mixtral-8x7B-Instruct-v0.1: concise 13.7, standard 18.3, verbose 24.6. (Verbose digits slightly dark on the thumbnail; 24.6 is my reading, moderate confidence; not zoomed.)

7. Slide 68 (frame f_6045000_1568.png): matrix multiplications use bf16 instead of fp32; "decimal precision doesn't matter except exp & updates". Speech [100:42-101:24]: weights stored in 32 bits, cast to 16 bits just before computation, all computation in 16 bits, weight updates done in 32 bits. So format = bf16. Other tensors: only partly determined. Weights/updates are 32-bit (speech, and slide's "exp & updates" exceptions). The slide shows no further recipe list (a second frame at 101:00 was a near-duplicate), and the lecturer does not name other 16-bit tensors beyond "all the computation". Insufficient evidence for a more specific list than that.

8. LIMA [65:19-65:41], slide 43 (frame f_3935000_1568.png): tested 2K, 4K, 8K, 16K, 32K training examples. Generation quality essentially flat (very slight decline, within error bars); scaling doesn't help. Quality about 3.8 on the y-axis (points ~3.83-3.86).

## Evidence strip
- [39:40] Pile composition treemap (no sizes)
- [92:40] AlpacaEval concise/standard/verbose table
- [100:45] Systems: low precision slide (AMP)
- [65:35] LIMA SFT quantity plot
- [38:50] Data slide with dataset sizes
- [101:20] lecturer on camera (wasted)
- [101:00] near-duplicate of 100:45 slide
Transcript carried Q1-4 fully (0 images).
