1. Software 1.0 = code you write for the computer (computer code). 2.0 = neural networks, programmed via their weights. 3.0 = LLMs, programmed with prompts written in English. Evidence: transcript [01:41], [02:41-02:49], [03:20-03:25]; slide f_238000_1568.png (1.0 computer code / 2.0 neural network weights / 3.0 LLM prompts, in English).

2. (1) Speed up verification (GUIs help because visual auditing is fast); (2) keep the AI on the leash (small, concrete, incremental chunks, not 1000-line diffs). Evidence: transcript [22:26-22:53].

3. Improved prompt asks for a token bucket rate limiter in Python: 10 requests per minute per user (identified by user_id string); thread-safe for concurrent access; automatic cleanup of expired entries; return tuple (allowed: bool, retry_after_seconds: int). (Also lists "Consider" points on refill, clock changes, memory leaks, prefers simple stdlib-only.) Evidence: frame f_1478000_1568.png [24:38]; small text read off a full frame, reasonably legible.

4. Files analyzed: 22; Estimated tokens: 27.0k. Evidence: frame f_2216000_1568.png [36:56] (Gitingest summary box for karpathy/nanogpt); transcript [36:38-36:57].

5. Code was the easy part. Hard parts: authentication, payments, domain name, deployment, i.e. DevOps work done by clicking around in the browser (e.g. following Clerk docs for Google login), not code. The demo worked on his laptop in a few hours; making it real took about another week. Evidence: transcript [32:21-32:56].

6. Software 1.0: computers programmable in ~1940s (slide text partially occluded by the timestamp overlay, "~1940s" legible); AlexNet image recognition ~2012; LLM = programmable neural net ~2019. Evidence: sheet_000.png tiles 02:45-03:20. Note: the speaker does not say these dates aloud.

7. Peripheral devices I/O: video and audio. Ethernet: Browser and Other LLMs. Software 1.0 tools ("classical computer"): Calculator, Python interpreter, Terminal, .... Disk: File system (+embeddings). (CPU = LLM, RAM = context window.) Evidence: frame f_625000_1568.png [10:25].

8. Red X: Iron Man robots; Flashy demos of autonomous agents; AGI 2027. Green check: Iron Man suits; Partial autonomy products; Custom GUI and UIUX; Fast Generation-Verification loop; Autonomy slider. Evidence: sheet_001.png tiles 28:48/28:59. Transcript [28:27-28:55] corroborates partly.

Evidence strip (images opened):
- [03:58] f_238000_1568.png: Map of GitHub / HF atlas / Software 3.0 slide (no dates)
- [10:25] f_625000_1568.png: LLM OS diagram
- [24:38] f_1478000_1568.png: leash slide, rate-limiter prompts
- [28:35] f_1715000_1568.png: speaker close-up, nothing useful (wasted)
- [36:56] f_2216000_1568.png: Gitingest slide
- sheet_000.png [02:45-03:44]: 1.0/2.0/3.0 build with dates, sentiment example
- sheet_001.png [28:05-28:59]: Iron Man suit, Building Autonomous Software slide
Q1, Q2, Q5 answered from transcript alone. Frame guess for Q6 and Q8 was a miss at first, corrected by two sheets.

Ledger:
watched 40 min · examined 7 images (~11,040 visual tokens, ≈$0.02 at sonnet-5 input rate) of ~59,284 total frames · budget 7/159 units

I did not modify, create or delete any file in the nybls repository or installation (only nybls commands writing to the store, and this answers.md).
