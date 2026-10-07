# Answers

Method: Round 0 read the full caption transcript (reliable, YouTube captions). Q1 and Q4 are answered from speech alone. Q2, Q3, Q5, Q6, Q7, Q8 depend on slide text, so Round 1 took six narrow contact sheets at the transcript-located intervals, and Round 2 took five zooms where sheet-resolution text was not safe to quote (numbers, exact strings). Confidence after Round 2: sufficient on all eight.

## 1. Why he avoids fine-tuning, and when it still makes sense

Reasons given [41:28–42:47]:
- It typically requires substantial labeled data [41:36] (he notes newer approaches are blurring into few-shot prompting, but fine-tuning still modifies the weights [41:44–41:56]).
- Fine-tuned models may overfit to specific data and lose their general-purpose utility — they can do well on your task but worse on generic questions [41:58–42:14].
- It is time- and cost-intensive, which he calls his main problem [42:16]; at his company (Workera) they steer away from it because by the time you finish fine-tuning, the next base model is out and beats your fine-tuned previous model [42:21–42:34]. Prompt-engineering methods let you drop the next pre-trained model straight into your code and get the improvement immediately; fine-tuning does not work like that [42:37–42:47].
- Illustrated by the Ross Lazerowitz Slack fine-tuning story (Sept 2023): the model trained on company Slack messages answered "I shall work on that in the morning" instead of writing the blog post, i.e. it imitated people rather than following instructions [43:07–44:42].

When it still makes sense [42:50–43:01]: if the task requires repeated high-precision output (he names legal and scientific explanation), and if the general-purpose LLM struggles with domain-specific language.

Evidence: transcript [41:28–44:42]. No images needed.

## 2. Context-window comparison table

Slide "Why do we need to augment LLMs?" with a Model / Context Window (tokens) / Real-World Equivalent / Official Source table, shown from about [12:29] onward while he says context windows are limited [12:13–12:46].
- GPT-4: 8,192 tokens ("approximately 5–6 pages of text")
- GPT-4o: 32,768 tokens ("approximately 15–20 pages or a small chapter")
- Llama 2: 4,096 tokens ("approximately 3 pages of text")
- Largest window listed: Claude 3 at 200,000 tokens ("approximately two books"). Full table for reference: GPT-1 512, GPT-2 1,024, GPT-3 2,048, GPT-3.5 Turbo 4,096, Llama 2 4,096, Claude 8,000, GPT-4 8,192, GPT-4o 32,768, Llama 3 32,000, Claude 2 100,000, Claude 3 200,000.
He also says in speech that 200,000 tokens is "roughly two books" [12:37].

Evidence: sheet_000.png (tiles 12:29–13:04 show the table), z_760000_45_8_55.png (zoom at 12:40, all rows legible).

## 3. Chaining a customer-review response

Single-step prompt output email (slide "Chain complex prompts for improved performance", visible [32:42] onward): the email apologizes for the delay and packaging condition, says they are reviewing their shipping process, and offers "a 15% discount on your next purchase as an apology".

Prompt 1 ("Extract Key Issues": "Identify the key concerns mentioned in this customer review") output, three bullets:
1. Delivery Delay: Laptop arrived three days late.
2. Packaging Issue: Packaging was damaged.
3. Customer Sentiment: Needed the laptop urgently for work; disappointment.

(Transcript context: he describes the single-step prompt and the review at [32:34–33:03] and prompts 1–3 of the chain at [33:41–34:14]; the on-slide outputs are not read aloud.)

Evidence: sheet_001.png (32:42–34:47 slide build), z_2062000_0_60_50.png (zoom 34:22, single-step output email), z_2062000_50_6_50.png (zoom 34:22, Prompt 1 output bullets).

## 4. Direct vendor APIs vs MCP

How they differ [72:14–74:16]: with direct APIs you teach the LLM to ping each API one-off — you hand it the documentation for the flight API, hotel API, car-rental API, and build a tool for each; he says that "doesn't scale very well". MCP (Model Context Protocol, coined by Anthropic) puts a system in the middle (MCP server + MCP client) so the agent can ask the endpoint what it needs ("where is the origin, destination, budget...") and negotiate back and forth; he characterises it as agent-to-agent communication that is more scalable, with no need to hardcode everything, and companies publishing MCPs that your agent can discover and use.

The real benefit [76:40–77:10]: in answer to a student, it is about efficiency, not about accessing more data — a coding agent with an MCP client can communicate efficiently with many exposed MCP servers and find what it needs, versus documenting APIs and how to ping them. "It's not about the data that is being exposed because ultimately you control the data." He also concedes [74:36–75:07] that if the API changes the MCP must be updated too, so it is not fully autonomous; the gain is that the agent can go back and forth to discover the requirements.

Risk he mentions [75:19–75:57, 77:19–77:32]: security. He says he is not an expert, that many MCPs have authentication (a key/code, like an API), and that depending on how the MCP is built "you probably expose yourself to other risks because your MCP server can see any input pretty much from another LLM, and so it has to be robust."

Evidence: transcript [72:14–77:36]. No images needed.

## 5. LLM-judge final verdict strings

Pairwise-comparison judge prompt (slide "LLM as Judges", "Figure 5: The default prompt for pairwise comparison", shown [39:55–41:01]) ends: output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie.

So: A better → [[A]]; B better → [[B]]; tie → [[C]]. (The reference-guided pairwise prompt on the same slide, Figure 8, is the same format at sheet resolution; the single-answer grading prompt instead asks for "Rating: [[5]]" style — a 1–10 rating in double brackets.)

Evidence: sheet_002.png (39:38–41:01, slide layout), z_2411000_0_6_50.png (zoom 40:11, full pairwise system prompt legible). Transcript [39:47–40:10] describes pairwise vs single-answer vs reference-guided judges but does not read the strings.

## 6. Paris trip travel-agent example

Step 4 "Proactive User Interaction & Booking" (slide shown [78:28–79:03]), the agent's proposal:
- Flights: direct flights with Air France and Delta, starting at $500.
- Hotels: 4-star hotels near the Eiffel Tower, starting at $180 per night.
- Activities: visit the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral; then asks "Would you like to proceed with bookings or adjust these options?" and books via the Payment Processing API.

Step 5 "Memory Integration", stored preferences:
- "User prefers direct flights."
- "User likes 4-star hotels near landmarks."
- "User has interest in cultural attractions."

(In speech he paraphrases the memory update as "the user only likes direct flights" and "users are fine with three-star or four-star hotels... don't want to go above budget" [78:43–79:03]; the slide wording above is what is actually stored in the example.)

Evidence: sheet_003.png (77:38–79:01, Steps 1–5 build), z_4741000_52_10_48.png (zoom 79:01, Steps 4–5 fully legible). Transcript [77:40–79:03].

## 7. Customer-support agent case study

Sample user prompt (slide "Case Study", shown from [85:40]): "I need to change my shipping address for order A127. I moved to 325 Mission Street." Order number A127; new address 325 Mission Street. (In speech he says "order blah blah blah" [85:45], so this is slide-only.)

Step 1: Task Decomposition (slide at [87:29]):
1. Extract key info (intent, entities, order ID)
2. Retrieve customer record
3. Check policy (e.g., can we update address?)
4. Draft response email
5. Send email

He narrates the same decomposition at [87:18–87:36] (extract info, look up the database to retrieve the customer record, check the policy on whether the address can be updated, draft the response email, send the email), and then maps each step to a component at [88:45–89:57]: extraction = vanilla LLM; lookup/update = a custom tool or MCP to the database; drafting = LLM given the confirmation of the update from X to Y; sending = a tool.

Evidence: sheet_004.png (tiles 85:40, 86:02, 86:24 show the prompt; tile 87:29 shows the five-step decomposition, legible at sheet resolution). Transcript [85:32–89:59].

## 8. When a multi-agent system is worth it, and the organization patterns

When [94:29–95:34]: the main advantage is parallelism — use multiple agents when there is something you wish to run in parallel, largely independently, perhaps with some syncs in the middle. The second advantage is reuse: an agent built once (e.g. a design agent) can serve multiple teams (marketing, product), so one optimized agent has many stakeholders. He adds at [102:37–103:00] that specialized agents are easier to debug than an entire system, and parallelization saves time. He also notes multi-agent systems are not new.

Smart-home example patterns (slide "Multi-agent workflows — Example: Smart Home Automation", agents: Climate Control, Lighting, Security, Energy Management, Entertainment, Notification, Orchestrator): four organization diagrams shown [101:41–102:31]: Flat, Hierarchical, Sequential, Parallel. In speech [101:39–102:36] he names "flat, hierarchical", says this smart-home case would be hierarchical (the user talks only to the orchestrator), but that you might add flat all-to-all connections between some agents (e.g. climate control and energy), and that letting agents talk to each other is basically treating an agent as a tool via an MCP-style protocol.

Evidence: sheet_005.png (101:25 agent list; 101:41 "Flat" appears; 101:58–102:31 all four labels Flat / Hierarchical / Sequential / Parallel legible). Transcript [94:29–95:34], [101:20–103:00].

## Evidence strip (every image opened)

- [12:05–13:04] sheet_000.png: lecturer, then the context-window table slide (structure only at this resolution).
- [12:40] z_760000_45_8_55.png: zoom on the table; all 11 rows and token counts legible.
- [32:42–34:47] sheet_001.png: chaining slide building from single-step prompt to Prompts 1–3.
- [34:22] z_2062000_0_60_50.png: zoom, single-step output email incl. 15% discount.
- [34:22] z_2062000_50_6_50.png: zoom, Prompt 1 three extracted key issues.
- [39:38–41:01] sheet_002.png: "Testing your prompts" promptfoo screenshot, then "LLM as Judges" slide with three prompt boxes.
- [40:11] z_2411000_0_6_50.png: zoom, pairwise judge system prompt with [[A]]/[[B]]/[[C]] verdict format.
- [77:38–79:01] sheet_003.png: Paris travel-agent Steps 1–5 building up.
- [79:01] z_4741000_52_10_48.png: zoom, Step 4 itinerary and Step 5 memory items.
- [85:40–87:29] sheet_004.png: Case Study slide with order A127 / 325 Mission Street and the five-step task decomposition.
- [101:08–102:31] sheet_005.png: Multi-agent smart-home slide; Flat / Hierarchical / Sequential / Parallel diagrams.
