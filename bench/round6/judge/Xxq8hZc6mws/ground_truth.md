# Ground truth — Xxq8hZc6mws (ESPN: #3 Kentucky at #7 Florida, women's volleyball, 5 sets)

Video is ~20:20 of condensed match highlights. Grid frames every 11 s (g_NNNNNs.png). Transcript is ASR with name errors ("Brooklyn delay" = Brooklyn DeLaye, "Tuzo/Tzo/Tuzzle" = Molly Tuzzo, "Guardy/Gardy" = Morgan Guardy, "Cheney/Chainy" = Cameron Chaney, "Odome" = O'Dome).

Label counts: S = 4 (Q4, Q6, Q7, Q8), V = 3 (Q1, Q2, Q5), B = 1 (Q3).

---

## Q1 — Match winner and set scores
**Label: V** (winner is inferable from speech; the per-set scores exist only on the scorebug)

**Answer:** Florida won 3-2. Set scores (Kentucky–Florida): 25-22 UK, 27-29 FLA, 21-25 FLA, 25-21 UK, 8-15 FLA.

**Evidence (frames):**
- g_00253s.png: scorebug "Kentucky 25 / Florida 22 — UK WINS SET 1"
- g_00616s.png: "Kentucky 27 / Florida 29 — FLA WINS SET 2"
- g_00946s.png: "21 / 24 — TIED 1-1 (FLA SET POINT)"; g_00957s.png: "21 / 25"; g_00968s.png: "FLA LEADS 2-1"
- g_01078s.png: "24 / 21 — FLA LEADS 2-1 (UK SET PT)"; g_01089s.png: "TIED 2-2"
- g_01210s.png: "Kentucky 8 / Florida 15 — FLA WINS MATCH"; records update to UK 11-3, FLA 12-1

**Evidence (transcript, partial only):** [10:27] "Second set is all orange"; [15:38] "Florida leads two"; [18:03] "Let's play five, shall we?"; [19:51] "First match ball opportunity"; [20:05]–[20:10] "Hoy digs it. Cheney of course ... put in the books." No set score is ever spoken except "27 apiece" [09:48] in set 2.

**Key terms:** 25-22, 29-27, 25-21, 25-21, 15-8, "FLA WINS MATCH", "UK WINS SET 1", "FLA WINS SET 2"

**Partial:** "Florida won in five" with no set scores, or correct winner with 1–3 wrong/missing set scores. Any answer giving Kentucky as winner is wrong.

---

## Q2 — Rankings and records coming in
**Label: V**

**Answer:** Kentucky ranked #3, record 11-2 overall (3-0 SEC). Florida ranked #7, record 11-1 overall (2-0 SEC).

**Evidence (frames):** Scorebug on every wide frame, e.g. g_00000s.png, g_00011s.png, g_00022s.png: "3 Kentucky ... 11-2 (3-0)" and "7 Florida ... 11-1 (2-0)". Post-match g_01210s.png shows updated 11-3 and 12-1 (confirms the pre-match figures).

**Transcript:** Does not state either record. The only ranking mention is garbled: [13:05] "17 this year now at number seven. They defeated Min Minnesota 3-1..." — "number seven" is consistent with Florida's rank but the records are not spoken.

**Key terms:** "3 Kentucky", "7 Florida", "11-2", "3-0", "11-1", "2-0"

**Partial:** Rankings correct but records missing or one record wrong; or records correct but rankings missing.

---

## Q3 — How set 2 ended
**Label: B**

**Answer:** Florida won set 2 by 29-27, after it went to extra points (tied 24-24, 26-26, 27-27). Set points along the way: Kentucky had 2, Florida had 3 (the on-screen "SET POINTS UK: 2 | FLA: 3" graphic at 27-28; Florida then converted that third one).

**Evidence (frames):**
- g_00517s.png: "24 / 24 — UK LEADS 1-0 (FLA SET PT)"; g_00528s.png, g_00539s.png, g_00550s.png: 24-24
- g_00561s.png: "25 / 24 (UK SET PT)"; g_00572s.png: "26 / 25 (UK SET PT)"; g_00583s.png: "26 / 26"
- g_00594s.png: "27 / 28 (FLA SET PT)"; g_00605s.png: same score with graphic "SET POINTS  UK: 2 | FLA: 3"
- g_00616s.png: "27 / 29 — FLA WINS SET 2"

**Evidence (transcript):** [08:35] "Set point number two."; [08:37]–[08:42] "Brooklyn delay with another block and we are tied. Going over time."; [09:24]–[09:28] "Three 0 run. Set point forward the other way."; [09:38]–[09:41] "Huge front row for Kentucky. Set point number two."; [09:48] "27 apiece."; [10:27] "Second set is all orange."; [14:52]–[14:57] "second set was won by Florida. They had two set point opportunities." (the "they" = Kentucky, i.e. UK had two set points and lost the set).

**Key terms:** 29-27, "27 apiece", "SET POINTS", "UK: 2", "FLA: 3", "FLA WINS SET 2"

**Partial:** Correct 29-27 but set-point counts missing; or "Florida won in extra points, Kentucky wasted two set points" without the 29-27 score or Florida's count of 3.

---

## Q4 — Commentator's mid-match MVP
**Label: S**

**Answer:** Taylor Parks, Florida's setter, jersey #20. Reasoning: her equal distribution across the net — "11 in the middle, so you're talking 33/33/33% across the net, try to defend that" — and "it's like she's got a little calculator in her head just running." The other commentator adds he could make a case for Brooklyn DeLaye as well.

**Evidence (transcript):** [11:43]–[11:49] "Also 11 in the middle. So you're talking 33 33 33% across the net. Try to defend that."; [11:56]–[11:58] "if I had to go MVP right now in this match, it's number 20."; [11:59]–[12:04] "Distribution, the equal distribution across the net. It's like she's got a little calculator in her head just running."; [12:07]–[12:09] "I mean, I can make a case for Brooklyn delay as well." Parks identified as setter elsewhere: [00:33] "set from Taylor Parks", [10:04]–[10:10] "Pandemonium off the parks block ... Serious center love for Taylor Parks".

**Evidence (frames, confirming #20 = Parks):** g_00594s.png and g_00605s.png show a Florida player in #20 with "PARKS" on the back; g_00616s.png shows #20 beside #25 ROTHE and #7 CHANEY.

**Key terms:** Taylor Parks, "number 20", "33 33 33", "calculator in her head", distribution

**Partial:** "Taylor Parks" with number but without the distribution reasoning; or "number 20" without the name.

---

## Q5 — Brooklyn Briscoe stat graphic
**Label: V**

**Answer:** 8 kills, .462 hitting percentage. The graphic appears in set 3 at 10-8 Kentucky.

**Evidence (frames):** g_00792s.png: lower-third "BROOKLYN BRISCOE — 8 Kills — .462 H[itting]" with scorebug "Kentucky 10 / Florida 8 — TIED 1-1 (BEST OF 5)".

**Transcript:** Never gives Briscoe's numbers. She is mentioned only in play calls: [00:30] "another transfer Brooklyn Brisco", [08:31] "put away by Brisco", [11:28] "King alongside Frisco", [11:50]–[11:53] "That's Parks next to Brisco", [12:17] "Brisco with the cover".

**Key terms:** Briscoe, "8 Kills", ".462"

**Partial:** One of the two numbers correct; or correct numbers with wrong set/score context.

---

## Q6 — Brooklyn DeLaye background
**Label: S**

**Answer:** 6'2" opposite; plays in the Canadian national team program ("the Canadian"); a transfer who stayed for this season; played all of last season with a torn meniscus, so viewers did not get to see her serve a season ago.

**Evidence (transcript):** [00:18]–[00:25] "The Canadian stayed for this season. The 6'2 opposite playing in the Canadian national team program."; [00:28]–[00:30] "Back slide again and it's good once more to another transfer Brooklyn Brisco" (context: DeLaye is also described as a transfer, "another transfer" being Briscoe); [01:16]–[01:24] "That's where Brooklyn delay is with this serve which we didn't get to see a season ago unfortunately as she played all last year with that torn meniscus."

**Frames:** No graphic for DeLaye. Kentucky jersey numbers visible (e.g. #6, #10, #17 DeLeye, #20 in g_00110s.png) — "#17 DeLeye" on g_00110s.png is her jersey, but the question's facts are speech-only.

**Key terms:** 6'2, opposite, Canadian national team, torn meniscus, "all last year"

**Partial:** Three of the four facts (height, position, Canada, meniscus).

---

## Q7 — Lily Hayes digs and USA prospects
**Label: S**

**Answer:** 16 digs (stated at [15:47] and again as "16 digs and a block" at [16:48]). The commentators say Hayes and Molly Tuzzo "could be in USA uniform sometime soon," that Hayes is a libero "who's playing for the USA," and that the national-team coach has been up to watch both of them.

**Evidence (transcript):** [01:04]–[01:08] "Hayes with that dig. Hayes and Tuzo could be in USA uniform sometime soon."; [05:24]–[05:28] "Lee Hayes or libero who's playing for the USA."; [05:29]–[05:30] "Yeah, coach Tyson's been up there to watch both of them actually." (ASR; the coach's name is garbled); [15:47]–[15:54] "Hayes with 16 digs. Those have been fun by themselves, but you could make a whole another highlight reel out of just for second contacts."; [16:46]–[16:48] "needs to be a little more than all right at 16 digs and a block."

**Frames:** No Hayes stat graphic in the grid.

**Key terms:** "16 digs", "USA uniform", "playing for the USA", "watch both of them"

**Partial:** 16 digs without the USA context, or the USA context without the dig count. Note: "Bella Lee only has six digs" [14:33] is about a different player (Florida's #21 Lee) and should not be confused.

---

## Q8 — Craig Skinner tenure and comment on Florida
**Label: S**

**Answer:** 22nd season. He said Florida "serve the crap out of the ball" — he expected the serving pressure.

**Evidence (transcript):** [01:11]–[01:13] "Carr with the kill out of the middle for Craig Skinner now in his 22nd season."; [01:44]–[01:51] "Craig Skinner right away when he talked about Florida said they serve the crap out of the ball. I mean, he expected it."

**Frames (supporting only):** g_01188s.png shows the Kentucky bench with the head coach (bald, glasses, "Kentucky Volleyball" quarter-zip) at Florida match point, 8-14 in set 5. No tenure graphic.

**Key terms:** "22nd season", "serve the crap out of the ball"

**Partial:** Either the season count or the serving quote alone.
