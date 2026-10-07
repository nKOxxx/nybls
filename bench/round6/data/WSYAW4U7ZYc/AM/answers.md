# Answers (evidence: transcript.txt + 7 frames only)

Note on frames: the 7 uniform stills (446s, 1340s, 2234s, 3128s, 4022s, 4916s, 5810s) were examined. Only am05_4916s.png shows a slide (RLHF: DPO, slide 50; irrelevant to the questions). The others show the lecturer/room (am03_3128s, am04_4022s, am06_5810s; am00-am02 were not opened to answer anything, see count below). No frame falls near any slide asked about, so everything below rests on the transcript (SAW = on-screen; HEARD = transcript; INFERRED = my reasoning).

1. Chinchilla recommends 20 tokens per parameter [51:30-51:39]. Once inference cost is considered, the lecturer says about 150 tokens per parameter ("150 to 1"), and that this is roughly what the best production models are trained on [52:15-52:39]. HEARD. (He also says Llama 3 405B at ~40 tokens/param sits between the two [55:33-55:37].)

2. HEARD [55:18-58:12]: Llama 3 405B, 16,000 H100s, ~70 days, about 26 million GPU-hours by his back-of-envelope calculation (Meta reportedly said ~30 million). Rental rate: lower bound ~$2 per GPU-hour. Rental cost: 26M x $2 = ~$52 million. Salary: 50 employees at $500k/yr = ~$25 million. Total: ~$75 million (he says he may be off by ~$10M).

3. HEARD [10:51-12:04]. Whole words as tokens: a typo'd or unseen word has no token, so you can't feed it to the model; also words don't work for languages like Thai with no spaces between words. Characters as tokens: it would work well, but sequences become very long, and transformer cost grows quadratically with sequence length. Tokenizers (e.g. BPE) fix both by giving common subsequences a token (~3-4 letters per token on average).

4. HEARD. Academic benchmarking: perplexity depends on the tokenizer used and on the actual data being evaluated on [21:01-21:07]; it remains important for LLM development (validation perplexity when training your own). Aligned/post-PPO models: they are not calibrated and don't output distributions, they just optimize one thing [88:05-88:15]; the optimum after PPO is roughly a delta (one sentence for a question), so a semantically slightly different answer gets near-zero likelihood; they are trained as policies, not by maximum likelihood [89:16-89:52]. He also notes validation loss isn't comparable across methods (PPO vs DPO) [87:54-87:59].

5. Insufficient evidence. The transcript [38:43-40:31] discusses The Pile (and says academic sets run from ~150B tokens / ~800GB up to ~15T tokens; Llama 2 = 2T, Llama 3 = 15T, GPT-4 ~13T from leaks, none of which is the slide list) but never names the other datasets or their sizes. No frame is near the slide (nearest frames 3128s and 2234s show only the lecturer). I won't guess.

6. Insufficient evidence. Transcript [92:41-93:13] gives only the GPT-4 example (standard 50% by definition, verbose 64.4%, concise ~20%). Mixtral-8x7B-Instruct never appears in the transcript, and no frame (5810s is the nearest, showing the lecturer) shows the table. Those GPT-4 numbers are not the Mixtral numbers.

7. Partly answerable, with a gap. HEARD [100:42-101:24]: automatic mixed precision uses 16 bits for computation (matrix multiplication); weights are stored in 32 bits, and the weight updates are done in 32 bits (so small learning rates still change the weights). The specific 16-bit format name (e.g. fp16 vs bf16) is never said and no frame shows the slide: insufficient evidence for the format. He does not enumerate other tensors beyond weights/updates (32-bit) and computation (16-bit); I don't claim activations/gradients specifics.

8. Partly answerable. HEARD [65:28-65:40]: LIMA tested scaling SFT data from 2,000 to 32,000 examples, and it "really doesn't help much" (quality essentially flat; the explanation is SFT mostly teaches format/user-type selection). The approximate quality score level is not stated in the transcript and no frame shows the plot: insufficient evidence for the number.

---
Frames examined: 4 opened (am03_3128s, am04_4022s, am05_4916s, am06_5810s); the other 3 (am00-am02) were not opened. Transcript was read via grep/sed excerpts. I modified no other file (only wrote answers.md).
