# Ground truth (video d95J8yzvjbQ, The Thinking Game documentary on DeepMind/Demis Hassabis, ~83 min)

Authoring note: frames viewed were a sample of the grid, not every frame; screen-text answers below were read from the frames cited. Transcript line timestamps are as in transcript.txt.

## Q1 — Label: S
Answer: CASP is held every 2 years; teams are given amino acid sequences of about 100 proteins and try to predict folding computationally; the structures were already determined experimentally in the lab but not yet public and serve as gold standard; accuracy is scored and a score over 90 would be expected to count as a solution.
Evidence: [52:03]-[52:46] "CASP is a community-wide assessment that's held every 2 years. Teams are given the amino acid sequences of about 100 proteins ... you would expect a score of over 90 to be a solution".
Partial: gets 90 threshold and every 2 years but not ~100 proteins/input (or vice versa).

## Q2 — Label: S
Answer: Trained first on 100,000 games played by strong amateurs (mimicking human players), then reinforcement learning by playing against different versions of itself many millions of times and learning from errors. AlphaGo put 1 in 10,000 probability on a human playing move 37.
Evidence: [16:47]-[17:05] "showing it 100,000 games that strong amateurs have played ... plays against different versions of itself many millions of times"; [17:37]-[17:56] "1 in 10,000 probability that move 37 would have been played by a human player".
Partial: only training or only 1 in 10,000.

## Q3 — Label: S
Answer: Most accurate system, predicting structures for 25 out of 43 proteins in the hardest category (state-of-the-art); beat second team by nearly 50%. Still disappointing because the predictions were no more useful than previous methods / not good enough for a biologist's practical use ("best in the world at a problem the world's not good at"; "we knew we sucked").
Evidence: [56:14]-[56:28]; [56:56]-[57:05]; [57:11]-[57:37].
Partial: 25 of 43 without the reason, or reason without the number.

## Q4 — Label: S
Answer: Chess/Go offer effectively unlimited data (play as many games as compute allows). Proteins have a small fixed dataset determined by half a century of slow lab experiments; each structure can take months or years, sometimes never determined, so training sets are small.
Evidence: [50:20]-[50:59].
Partial: says data is limited without the contrast or the lab-experiment cause.

## Q5 — Label: S
Answer: Decided to make it open: release predictions for all known protein sequences rather than build a submit-your-protein service, make code open and predictions easy to access; released structures of 200 million proteins.
Evidence: [74:56]-[75:41] ("fold everything and then give it to everyone in the world"; "make this open"); [75:55] "They released the structures of 200 million proteins."
Partial: open release without the 200 million figure.

## Q6 — Label: V
Answer: Producers listed in the end credits are Greg Kohs and Tara Struthers (PRODUCTION block); an earlier card reads "produced by GARY KRIEG".
Evidence: frames g_04859s.png (credit roll: "Producer GREG KOHS", "Producer TARA STRUTHERS"), g_04816s.png ("produced by GARY KRIEG", Nobel ceremony footage). Transcript has no credits (only music after 80:16).
Key terms: Greg Kohs, Tara Struthers, Gary Krieg, producer.
Partial: any one correct credited producer name.

## Q7 — Label: V
Answer: "New Enzyme Discovery Could Help Handle Plastic Pollution Crisis", from AZO Materials.
Evidence: frame g_04601s.png (~76:41). Transcript at that point has only music/"To me, it's just crazy"; no mention of enzyme or AZO. (Earlier at [46:43] speaker says hypothetically a protein that "breaks down plastic" — not the headline.)
Key terms: enzyme discovery, plastic pollution crisis, AZO Materials.
Partial: plastic/enzyme topic without outlet, or outlet only.

## Q8 — Label: B
Answer: Team reported 100,000 concurrent users (an earlier line says "655 users current" and "loads of activity in Japan"). On screen: a wall display with a world map of user dots and a dashboard whose #1 page title is "AlphaFold Prot...ture Database" (Protein Structure Database, truncated) and #1 event name "molstar"; a video-call tile labelled "Demis Hassabis" shows him joining remotely.
Evidence: transcript [76:20]-[76:27] "655 users current. Currently have 100,000 concurrent users"; frame g_04558s.png (map, "Views by Page title and screen name #1 AlphaFold Prot...ture Database", "Event count by Event name #1 molstar", tile "Demis Hassabis").
Key terms (screen part): AlphaFold Protein Structure Database, molstar, Demis Hassabis, video call, world map.
Partial: 100,000 only, or the screen details only.
