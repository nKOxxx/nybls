# Ground truth

## Q1 — S
Answer: 1.0 = code you write for the computer (computer code programs the computer); 2.0 = neural networks, i.e. the weights, which you get by tuning datasets and running an optimizer (not writing directly); 3.0 = LLMs, programmed by prompts written in English.
Evidence: transcript [01:41]-[01:51] ("software 1.0 is the code you write for the computer. Software 2.0 are basically neural networks... the weights"), [03:15]-[03:25] ("software 3.0... your prompts are now programs that program the LLM"), [03:25] prompts in English. Frame g_00200s.png agrees.
Partial: gets the three mappings but misses one of code/weights/prompts.

## Q2 — S
Answer: (1) speed up verification a lot, e.g. with GUIs (visual diffs use the "computer vision GPU" in your head); (2) keep the AI on the leash (don't accept 1,000-line diffs; work in small incremental chunks, concrete prompts).
Evidence: transcript [22:26]-[22:53] ("two major ways... speed up the verification... GUIs"; "keep the AI on the leash"), [23:03]-[24:10].
Partial: only one of the two.

## Q3 — V
Answer: Implement a token bucket rate limiter in Python with: 50 requests per minute per user (identifier user_id: string); thread-safe for concurrent access; automatic cleanup of expired entries; return tuple (allowed: bool, retry_after_seconds: int). Also lists considerations (refill gradually vs all at once, clock changes, memory leaks from inactive users) and "prefer simple, readable implementation over premature optimization". The weaker prompt is "Write a Python rate limiter that limits users to 50 requests per minute."
Evidence: frame g_01460s.png (slide "Example: keeping agents on the leash"; blog "AI-assisted coding for teams that can't get away with vibes"). Transcript [24:30]-[24:47] only says generally that being more concrete increases probability of verification; no rate limiter details.
Key terms: token bucket, Python, 50 requests per minute, user_id, thread-safe, expired entries, retry_after_seconds, tuple.
Partial: token bucket + 50 req/min per user, without the rest.

## Q4 — V
Answer: 22 files analyzed; estimated tokens 27.0k (repository karpathy/nanogpt).
Evidence: frame g_02200s.png (Gitingest summary: "Files analyzed: 22", "Estimated tokens: 27.0k"). Transcript [36:38]-[36:57] describes the URL swap and concatenation but gives no numbers.
Key terms: 22, 27.0k, Files analyzed, Estimated tokens, gitingest.com/karpathy/nanogpt.
Partial: one of the two numbers.

## Q5 — B
Answer: The code was the easy part; the demo ran on his laptop in a few hours. Making it real (authentication, payments, domain name, Vercel/versatile deployment) was hard, mostly clicking through browser DevOps and following instructions (e.g. Clerk's Google login docs), and took about another week. On the slide, the checklist is: LLM API keys, Flux (image generation) API keys, running locally (green check, "ez"), Vercel deployments, domain names, authentication (most distressed emoji), payments.
Evidence: transcript [32:21]-[33:00] ("code was the easy part", "demo working on my laptop in a few hours... took me a week"), [33:04]-[33:33] (Clerk instructions); frame g_01940s.png (checklist with emoji, "Most of the work was in the browser clicking things").
Key terms (slide-only part): LLM API keys, Flux API keys, Running locally (ez) checked, Vercel deployments, Domain names, Authentication (worst emoji), Payments.
Partial: hard parts and hours-vs-week without the slide items, or the reverse.

## Q6 — V
Answer: computers became programmable in ~1940s (Software 1.0); AlexNet image recognition ~2012 (Software 2.0, fixed function neural net); LLM ~2019 ("LLM = programmable neural net!", Software 3.0).
Evidence: frame g_00200s.png. Transcript [02:49]-[03:15] mentions AlexNet and programmable neural nets but no years.
Key terms: ~1940s, ~2012, ~2019, AlexNet, fixed function neural net.
Partial: two of three dates.

## Q7 — V
Answer: Peripheral devices I/O: video and audio. "Ethernet" side: Browser and Other LLMs. Software 1.0 tools ("classical computer"): Calculator, Python interpreter, Terminal. "Disk": File system (+embeddings). Also CPU = LLM, RAM = context window.
Evidence: frame g_00620s.png. Transcript [10:06]-[10:28] only states LLM = CPU-equivalent and context windows = memory, plus generic "tool use and multi-modalities".
Key terms: video, audio, Browser, Other LLMs, Calculator, Python interpreter, Terminal, File system, embeddings, Ethernet, Disk.
Partial: gets most boxes but misses e.g. the Ethernet mapping or the disk label.

## Q8 — B
Answer: Red X: Iron Man robots; flashy demos of autonomous agents; AGI 2027. Green check: Iron Man suits; partial autonomy products; custom GUI and UIUX; fast generation-verification loop; autonomy slider.
Evidence: frame g_01720s.png (slide "Building Autonomous Software"). Transcript [28:21]-[28:55] states less Iron Man robots / more Iron Man suits, less flashy demos / more partial autonomy products, custom GUIs, fast generation-verification loop, autonomy slider; "AGI 2027" is never spoken (closest: [27:33] "2025 is the year of agents... decade of agents").
Key terms (V part): AGI 2027.
Partial: all spoken items right but no "AGI 2027".
