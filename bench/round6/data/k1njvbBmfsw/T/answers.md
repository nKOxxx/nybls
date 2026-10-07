# Answers (source: transcript.txt only, plus labelled own knowledge)

## 1. Fine-tuning: reasons against, and when it still makes sense
Transcript [41:33]-[42:47]. Reasons he gives:
- Requires substantial labeled data typically (though newer approaches look more like few-shot prompting) [41:36].
- Fine-tuned models may overfit to specific data and lose general-purpose utility [41:58]-[42:12].
- Time and cost intensive, "that's my main problem" [42:16]. By the time you finish, the next model is out and beats your fine-tuned older one [42:25]-[42:32]. With prompting you can drop the next best pre-trained model straight into your code and it updates immediately; fine-tuning doesn't work like that [42:37]-[42:47].
- Illustration: the Slack fine-tuning example, where the model ended up acting like people ("I shall work on that in the morning") rather than following instructions [43:11]-[44:35].

Still makes sense [42:51]-[42:58]: (a) when the task requires repeated high-precision output, e.g. legal, scientific explanation; (b) when the general-purpose LLM struggles with domain-specific language.

## 2. Context window comparison (GPT-4, GPT-4o, Llama 2)
INSUFFICIENT EVIDENCE. The transcript has no per-model token limits. Spoken content only: best models are "somewhere in the hundreds of thousands of tokens max", and 200,000 tokens is "roughly two books" [12:15]-[12:43]. The specific comparison is presumably a slide that is not in the transcript, so I can't say which model is listed as largest. (Own knowledge, not the lecture: GPT-4o is 128k, GPT-4 is 8k/32k originally, Llama 2 is 4k, so GPT-4o would likely be the largest of the three. Unverified against the slide.)

## 3. Chained customer-review example
- Single-step prompt's generated email resolution: INSUFFICIENT EVIDENCE. The lecturer only says "the output is an email" [32:58]-[33:03]; its content isn't read aloud.
- Three key issues extracted by the first prompt: INSUFFICIENT EVIDENCE. The transcript names only the prompt ("Identify the key concerns mentioned in this customer review") [33:41]-[33:47]; output not read aloud. (Inference only: the review says the laptop arrived 3 days late, packaging was damaged, and it was needed urgently [32:48]-[32:58], but the transcript does not say this is what the extraction returned.)

## 4. Direct vendor APIs vs MCP
- API approach [72:34]-[73:09]: you teach the LLM to ping each API, giving the documentation for each (flight, hotel, car rental) and tools for each, one-off; "it doesn't scale very well."
- MCP [73:09]-[74:16]: a system in the middle (MCP server and client) that simplifies LLM-to-endpoint communication. The agent asks what the server needs (origin, destination, budget) and it responds; agent-to-agent style negotiation, so you don't hardcode everything; companies publish their MCPs.
- Real benefit [76:40]-[77:12]: efficiency, not access to more data (you control exposed data either way). He concedes that if an API changes, the MCP must be updated too [74:40]-[75:05].
- Risks [77:19]-[77:36]: you probably expose yourself to other risks, since the MCP server can see any input from another LLM, so it has to be robust. He also says many MCPs use authentication and admits he is not a security expert [75:43]-[75:57].

## 5. LLM judge verdict strings
INSUFFICIENT EVIDENCE. The lecture describes pairwise judging only conceptually ("here are two summaries, tell me which one is better") [39:44]-[39:58], plus single-answer grading 1-5 and rubrics [40:13]-[40:52]. No exact output strings ("A", "B", "tie" or otherwise) are spoken. The prompts are presumably on slides not in the transcript.

## 6. Paris trip example
- Concrete itinerary (airlines, flight price, hotel class, nightly price): INSUFFICIENT EVIDENCE. The transcript gives only the task (Paris, Dec 15-20, flights, hotels near the Eiffel Tower, must-visit itinerary) and the generic plan steps [77:40]-[78:33]. No airlines or prices are spoken.
- Memory updates [78:43]-[79:03]: the agent might store that the user only likes direct flights (next time only direct), that the user is fine with three-star or four-star hotels, and that they don't want to go above budget. These are framed as hypothetical ("might say", "or something like that").

## 7. Customer-support agent case study
- Order number and new address: INSUFFICIENT EVIDENCE. The sample is spoken as "I need to change my shipping address for order blah blah blah. I move to a new address." [85:43]-[85:51]; the real values are not in the transcript.
- Decomposed steps [87:11]-[87:36]: (1) extract info; (2) look up in the database to retrieve the customer record; (3) check the policy (are we allowed to update the address or is it a fixed data point); (4) draft the response email; (5) send the email. Designed workflow [89:00]-[89:57]: LLM extracts intent, order number and new address; a tool (possibly via MCP) looks up and updates the database; LLM drafts the confirmation email; a tool sends it.

## 8. Multi-agent: when worth it, and patterns for smart home
- Worth it when [94:52]-[95:34]: main advantage is parallelism (things you want to run independently in parallel, maybe with syncs in the middle). Second: reuse, where one agent (e.g. design) serves marketing and product teams. Later, advantages listed [102:40]-[102:57]: easier debugging of a specialized agent, parallelization, time gain.
- Patterns [101:40]-[102:36]: "flat" and "hierarchical" named as ways to organize. For the smart home he favors hierarchical, with an orchestrator as the single user-facing agent (for UX), possibly with added all-to-all/flat-style links between specific agents, e.g. climate control and energy. Agents talking to each other is basically MCP, treating the agent like a tool [102:21]-[102:36]. Agent list on his slide: climate control, lighting, security, energy management, entertainment, notification, energy saving, orchestrator [101:20]-[101:34]. Only flat and hierarchical are named; no other patterns are named in the transcript ("we didn't talk about the different interaction patterns" [101:36]).
