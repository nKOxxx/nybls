1. Reasons [41:28-42:30]: needs substantial labeled data; fine-tuned models can overfit to specific data and lose general-purpose utility (Slack fine-tuning example, "I shall work on that in the morning", [43:18-44:30]); time and cost intensive (his main problem), and by the time you finish the next base model is out and beats your tuned one, whereas with prompting you just swap in the new model. Still makes sense [42:45]: when the task requires repeated high-precision output (e.g. legal, scientific explanation), and when a general-purpose LLM struggles with domain-specific language. Evidence: transcript only.

2. Slide [12:25, frame f_745000]: GPT-4 = 8,192; GPT-4o = 32,768; Llama 2 = 4,096. Largest listed: Claude 3 at 200,000 tokens (Claude 2 100,000 next).

3. Single-step email offered a 15% discount on the next purchase as an apology [zoom 34:39]. First chained prompt extracted: Delivery Delay (laptop arrived three days late), Packaging Issue (packaging damaged), Customer Sentiment (needed the laptop urgently for work; disappointment) [sheet 33:34-34:39; slide text small, read at sheet resolution, high but not zoomed confidence].

4. [72:20-77:30] API approach: you teach the LLM each API one-off (docs and tools for flight, hotel, car-rental APIs); doesn't scale well. MCP: a server/client layer in between, so the agent talks to the endpoint and negotiates what it needs (agent-to-agent style); no hard-coding everything. Real benefit: efficiency/scalability, not access to more data (you control exposed data); he concedes that if the API changes the MCP still has to be updated. Risks: security is not his expertise; MCPs often need authentication, and an MCP server can see any input from another LLM so it must be robust, exposing you to other risks.

5. Frame f_2400000 (40:00, Figures 5 and 8 pairwise prompts): "[[A]]" if A is better, "[[B]]" if B is better, "[[C]]" for a tie. (Single-answer grading uses "[[rating]]", not asked.)

6. Slide [78:38-79:48, zoom 79:48]: direct flights with Air France and Delta starting at $500; 4-star hotels near the Eiffel Tower starting at $180 per night; activities Eiffel Tower, Louvre Museum, Notre-Dame. Memory stored: "User prefers direct flights", "User likes 4-star hotels near landmarks", "User has interest in cultural attractions".

7. Slide [86:05]: "I need to change my shipping address for order A127. I moved to 325 Mission Street." Decomposition (spoken [87:50-89:30]; slide not viewed): extract info (intent, order number, new address); look up the customer record in the database; check policy (is address change allowed or a fixed data point); draft response email; send the email. (He later maps these to LLM, tool/DB lookup+update, LLM draft, email tool.)

8. [94:50-102:30] Worth it mainly for parallelism (things that run independently with some syncs), and for reusability of an agent across teams (e.g. a design agent used by marketing and product); also easier debugging of specialized agents. Patterns on slide [101:45, frame f_6105000]: Flat, Hierarchical, Sequential, Parallel. Smart-home agents: climate, lighting, security, energy management, entertainment, notification, orchestrator. He picks hierarchical (user talks to the orchestrator), possibly with flat-style links between e.g. climate and energy.

Images examined: f_745000 (12:25 slide), f_1995000 (33:15, lecturer only, wasted), f_2400000 (40:00 slide), sheet_000 (32:50-34:39), sheet_001 (77:51-79:48), zoom 79:48, zoom 34:39, f_5165000 (86:05), f_6105000 (101:45).

Ledger:
watched 110 min · examined 9 images (~13,061 visual tokens, ≈$0.03 at sonnet-5 input rate) of ~164,846 total frames · budget 9/200 units

I did not modify any tool file (or anything in the nybls repo).
