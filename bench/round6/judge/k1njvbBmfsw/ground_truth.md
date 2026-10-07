# Ground truth (video k1njvbBmfsw: Stanford CS230 "Beyond LLM", Kian Katanforoosh)

Note: grid frames are one per 55 s; slide frames cited below are those where the slide is shown full-screen.

## Q1. Label: S
Answer: Reasons: (a) requires substantial labeled data; (b) fine-tuned models may overfit to specific data and lose general-purpose utility; (c) time and cost intensive, and by the time you finish the next base model is out and beats your fine-tuned old one (prompt-engineering methods let you drop in the next pre-trained model immediately). Still makes sense when the task requires repeated high-precision output (e.g. legal, scientific explanation) and/or the general-purpose LLM struggles with domain-specific language.
Evidence: transcript [41:36]-[42:50] ("requires substantial label data", "overfit... losing their general purpose utility", "time and cost intensive", "by the time you're done fine-tuning your model, the next model is out"), [42:51]-[42:59] ("repeated high precision output such as legal scientific explanation", "domain specific language"). Slide frame g_02530s repeats the three limitations (not needed).
Partial: gives the three limitations but no "when it still makes sense" (or vice versa); or omits the "next model beats it" point.

## Q2. Label: V
Answer: GPT-4: 8,192 tokens; GPT-4o: 32,768 tokens; Llama 2: 4,096 tokens. Largest listed: Claude 3 at 200,000 tokens (approx. two books). (Table also: GPT-1 512, GPT-2 1,024, GPT-3 2,048, GPT-3.5 Turbo 4,096, Claude 8,000, Llama 3 32,000, Claude 2 100,000.)
Evidence: frames g_00715s and g_00770s (context-window table). Transcript only says [12:29]-[12:40] "hundreds of thousands of tokens max... 200,000 tokens is roughly two books"; it never states the GPT-4, GPT-4o or Llama 2 numbers.
Key terms: 8,192; 32,768; 4,096; Claude 3; 200,000; GPT-4o; Llama 2.
Partial: Claude 3/200,000 correct but model-specific numbers missing; or one of the three numbers wrong.

## Q3. Label: V
Answer: The single-step prompt's output email apologizes and offers a 15% discount on the customer's next purchase. The chain's first prompt extracted: Delivery Delay (laptop arrived three days late), Packaging Issue (packaging was damaged), Customer Sentiment (needed laptop urgently for work; disappointment).
Evidence: frame g_01980s (single-step output: "...offer you a 15% discount on your next purchase"); frame g_02035s (Prompt 1 output bullets with the three labels; Prompt 2 outline; Prompt 3 full email also with 15% discount). Transcript [32:48]-[34:14] describes laptop 3 days late, damaged packaging, urgent need, but never mentions the 15% discount or the bullet labels "Delivery Delay / Packaging Issue / Customer Sentiment".
Key terms: 15% discount; next purchase; Delivery Delay; Packaging Issue; Customer Sentiment.
Partial: discount right but issues only paraphrased as delay/packaging (without sentiment), or the reverse.

## Q4. Label: S
Answer: With plain APIs you teach the LLM how to call each API one-off (give each API's documentation: flight, hotel, car rental; build tools for each), which does not scale. With MCP (coined by Anthropic) there is an MCP server/client in the middle; the agent talks to the MCP endpoint agent-to-agent, asks what it needs, gets requirements back (origin, destination, budget) and negotiates, so nothing is hard-coded. Benefit is efficiency/scalability, not access to more data (you control the data exposed). If the API changes, the MCP must also be updated, but the agent can rediscover requirements. Risk: security; MCP servers can take input from other LLMs so must be robust; many have authentication, but he says he is not a security expert.
Evidence: transcript [72:14]-[74:16] (API one-off vs MCP server/client, "doesn't scale very well"), [76:40]-[77:35] ("about efficiency", "not about the data that is being exposed", "expose yourself to other risks... your MCP server can see any input from another LLM and so it has to be robust"), [75:21]-[75:57] (authentication, not an expert).
Partial: states one-off-vs-standardized and efficiency but not the security risk, or vice versa.

## Q5. Label: V
Answer: Pairwise comparison prompt: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. (Reference-guided pairwise prompt uses the same three tokens.) For reference, the single-answer grading prompt outputs "Rating: [[5]]" style on a scale of 1 to 10.
Evidence: frame g_02365s (Figures 5, 6, 8 from the MT-Bench LLM-as-judge paper). Transcript [39:43]-[41:05] describes pairwise, single-answer "from one to five" and rubric judges but never gives the bracket tokens; note the speaker's "one to five" is his own example, the slide says 1 to 10.
Key terms: [[A]]; [[B]]; [[C]]; tie; Rating: [[5]]; scale of 1 to 10.
Partial: knows format is double-square-bracket letters but gets tie token wrong (e.g. says [[T]]); or answers only with "A/B/tie" with no brackets.

## Q6. Label: B
Answer: Agent proposes: direct flights with Air France and Delta starting at $500; 4-star hotels near the Eiffel Tower starting at $180 per night; activities: Eiffel Tower, Louvre Museum, Notre-Dame Cathedral; then asks if the user wants to proceed and books via the Payment Processing API. Memory stored: user prefers direct flights; user likes 4-star hotels near landmarks; user has interest in cultural attractions.
Evidence: frame g_04730s (Steps 4 and 5). Transcript [77:40]-[79:03] covers the request (Paris, Dec 15th-20th, hotels near the Eiffel Tower), planning, proposal, and memory ("only likes direct flights", "three-star hotels or four-star hotels... not above budget") but never gives airlines, $500, $180, the three attractions, or "cultural attractions".
Key terms: Air France; Delta; $500; 4-star; $180 per night; Eiffel Tower; Louvre; Notre-Dame; direct flights; cultural attractions.
Partial: gets the memory preferences (direct flights, hotel class) from speech but not the itinerary specifics (or the reverse).

## Q7. Label: B
Answer: Sample request: "I need to change my shipping address for order A127. I moved to 325 Mission Street." Decomposition (5 steps): 1 extract key info (intent, entities, order ID); 2 retrieve customer record; 3 check policy (can we update the address?); 4 draft response email; 5 send email.
Evidence: frame g_05225s (slide with order A127, 325 Mission Street and the five steps). Transcript [85:43]-[85:51] only reads "order blah blah blah", and [87:13]-[87:34] gives the steps in speech (extract info, look up customer record, check policy, draft response email, send the email).
Key terms: A127; 325 Mission Street.
Partial: five steps right but order number/address missing, or the reverse.

## Q8. Label: B
Answer: Main advantage is parallelism (run things in parallel, with possible syncs); second advantage is reuse (an agent such as a design agent can serve marketing and product teams); also easier debugging of specialized agents and time savings from parallelization. Patterns on the slide: Flat, Hierarchical, Sequential, Parallel; for the smart home he judges hierarchical (an orchestrator talking to the user) most appropriate, possibly with extra links between e.g. climate control and energy agents.
Evidence: transcript [94:50]-[95:35] (parallelism, reuse), [101:46]-[102:20] (flat, hierarchical, orchestrator), [102:40]-[102:57] (debugging, parallelization); frame g_06105s shows all four patterns (Flat, Hierarchical, Sequential, Parallel) plus the agent list (Climate Control, Lighting, Security, Energy Management, Entertainment, Notification, Orchestrator). Speech never names Sequential or Parallel as patterns.
Key terms: Flat; Hierarchical; Sequential; Parallel.
Partial: reasons right with only flat/hierarchical named (speech-only), or four patterns with no reasons.
