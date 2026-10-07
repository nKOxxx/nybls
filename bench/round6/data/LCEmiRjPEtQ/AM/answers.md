# Answers

1. Software 1.0 = computer code, what you write is code that programs the computer. Software 2.0 = neural networks, what you write/produce is the weights (via an optimizer on data) that program the neural net. Software 3.0 = LLMs, what you write is prompts, in English, that program the LLM.
   Evidence: frame am00_169s.png (seen: "Software 1.0 computer code -> computer", "Software 2.0 weights -> neural net"); transcript [00:01:41]-[00:03:20] (1.0 code, 2.0 weights, "your prompts are now programs that program the LLM", "written in English"). 3.0 is from transcript only (not shown in a frame).

2. (1) Speed up verification (e.g. GUIs, visual representations, since looking at things is faster than reading text). (2) Keep the AI on the leash (small concrete incremental chunks, avoid huge diffs, concrete prompts).
   Evidence: transcript [22:26]-[22:53], [24:00]-[24:47].

3. Insufficient evidence. The transcript only says to be "more concrete" in prompts ([24:43]); the specific rate-limiter prompt details (limit, concurrency, cleanup, return value) are not in the transcript, and the only related frame (am04_1524s.png) shows the education "leash" slide, not the blog-post prompt.

4. Gitingest reports "Files analyzed: 22" and "Estimated tokens: 27.0k" (repository karpathy/nanogpt). Seen directly in frame am06_2201s.png (Summary box). Transcript [36:38]-[36:48] covers the URL swap.

5. Hard part: not the code but making it real: authentication, payments, domain name, and deployment, i.e. DevOps work done by clicking around in the browser, following instructions such as the Clerk library's step by step setup ("extreme slog"). Time: the demo worked on his laptop in a few hours; making it real took about another week.
   Evidence: transcript [32:21]-[32:56], [33:01]-[33:21].

6. Seen in am00_169s.png: Software 1.0 "became programmable in ~1940s"; Software 2.0 AlexNet for image recognition "~2012". The date attached to Software 3.0 / LLMs: insufficient evidence (that slide state is not in any frame, and the transcript gives no date for it; I will not guess).

7. Insufficient evidence. No frame shows the LLM OS diagram and the transcript ([10:02]-[12:19]) only compares context windows to memory and LLM to an OS; it does not enumerate the diagram's boxes (peripherals, Ethernet, Software 1.0 tools, disk).

8. Insufficient evidence. No frame shows the "Building Autonomous Software" slide and the transcript doesn't enumerate red-X / green-check items.

Frames examined: 7 (am00_169s through am06_2201s). I also read transcript.txt and index.json. I modified no other file (only created answers.md here).
