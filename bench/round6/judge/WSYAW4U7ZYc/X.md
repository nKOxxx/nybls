# Answers

1. Chinchilla: 20 tokens per parameter [51:33-51:39] ("20 tokens for every parameter"). Once inference cost is considered, about 150 tokens per parameter [52:15-52:33] ("150 to 1, that's around what the best models are trained on right now ... in production"). Transcript-stated.

2. [55:18-58:14] Llama 3 405B, 15.6T tokens, FLOPs ~ 6*N*P = 3.8e25. 16,000 H100s, ~70 days, ~26 million GPU hours (he notes Meta said ~30M). Rental rate: ~$2 per H100-hour (lower bound) -> 26M x $2 = ~$52 million. Salary: 50 employees x $500k/year = ~$25 million. Total ~ $75 million (he says he may be off by ~10M). Transcript-stated.

3. [10:51-12:19] Whole words as tokens: typos have no token so you can't feed them in; also words don't work for languages like Thai with no spaces between words. Characters as tokens: it works but sequences become super long, and transformer complexity grows quadratically with sequence length. Tokenizers (e.g. BPE) give common subsequences tokens, ~3-4 letters per token on average.

4. Not used for academic benchmarking [20:59-21:07]: it depends on the tokenizer used and on the dataset evaluated on. Example [25:16-25:42]: perplexity ranges 1 to vocab size, so a 100k-vocab tokenizer has a worse upper bound than a 10k one. Not usable on aligned/post-PPO models [88:05-88:17, 89:14-89:50]: such models are not calibrated and don't give distributions; PPO trains them as policies, not by maximum likelihood, optimizing for a single most-likely output, so the likelihood of semantically different answers can be ~zero and perplexity is not meaningful.

5. Insufficient evidence. The transcript only discusses The Pile (shown with arXiv, PubMed Central, Wikipedia, Stack Exchange, GitHub, books; "280B" mentioned at [39:54]) and general scale (150B tokens / 800GB up to 15T tokens). The slide's other dataset names and token counts are not spoken in the transcript. C4 is not mentioned either.

6. Insufficient evidence. The transcript only gives the GPT-4 example [92:46-93:13]: standard 50% (vs itself), verbose 64.4%, concise ~20%. Mixtral-8x7B-Instruct-v0.1 numbers are on the slide table but not spoken.

7. Transcript says 16 bits for computation (matrix multiplication) [100:25-101:24] but does not name the format (bfloat16 vs FP16) -> insufficient evidence from the transcript for the format name (own knowledge: commonly FP16 or bfloat16; not verified from this video). Per the transcript: weights are stored in 32 bits, cast to 16 bits just before computation, computation done in 16 bits, and weight updates done in 32 bits (so small learning rates still make a difference). The transcript does not enumerate other specific tensors (e.g. activations, gradients, optimizer state) beyond weights/updates; the spoken text doesn't cover them -> insufficient for a finer breakdown.

8. [65:25-65:41] LIMA: scaling SFT data from 2,000 to 32,000 examples "really doesn't help much" (generation quality essentially flat across the range; he says scaling laws don't help here). The approximate quality score level is not stated in the transcript (it is on a plot) -> insufficient evidence for the score value.
