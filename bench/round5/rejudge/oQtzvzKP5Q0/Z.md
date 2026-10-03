# Answers

Evidence txt only, plus own general knowledge where explicitly labelled. Transcript is auto-captioned and garbled in places (e.g. "Emma" = EMA, "Thea"/"thema" = TEMA, "leg" = lag, "kma" = QEMA, "hugi" = Hoogi).

## 1. EMA limitation and the key difference from finance

**Answer.** The limitation is the inherent lag of the EMA estimate behind the real data: EMA smooths spikes/noise well, but the smoothed signal trails the true signal. FAME's goal is to be more responsive to quick changes and "reduce the lag as much as we can." The key difference from finance: in FAME the triple EMA *actively guides* the optimization (it changes the network weights and affects the learning process), whereas in finance the (double/triple) EMA is only a *passive indicator* that describes the trend without influencing it.

**Evidence (transcript).**
- [01:24]–[01:44]: "the main advantage is that it can actually smooth out the spikes in the noise in the data but the main disadvantage and limitation is that it's actually can cause an inherent lag comparing with the real data"
- [02:21]–[02:41]: goal is an adaptive optimizer "responsive to ... quick changes in the data" and "we want to reduce the lag as much as we can"
- [04:04]–[04:36]: "the main difference comparing with Finance is that it actively guides the optimization so it's actually change the network weights and ... affect the learning process while in finance it's only a passive indicator ... it's not influence the trend and that's the main ... contribution"

## 2. Paper title, authors, institution

**Answer.**
- Title (from transcript, host's introduction): "Leveraging the Triple Exponential Moving Average for Fast Adaptive Moment Estimation" [00:17]–[00:24].
- Speaker/author (transcript): Dr. Assaf Hoogi (captioned "Assaf hugi"), senior lecturer, School of Computer Science, Ariel (University) [00:09]–[00:17].
- The transcript does NOT name the other two authors. **Own knowledge (UNVERIFIED, not from transcript):** I believe the arXiv paper of that title (2023) is by Roi Peleg, Teddy Lazebnik and Assaf Hoogi, with the work from Ariel University (Israel). Treat the two co-author names and the exact arXiv title punctuation ("Fast-Adaptive") as unconfirmed by this evidence; verify on arXiv before citing.

## 3. TEMA formula

**Answer.** The transcript does not give the coefficients. It only describes the construction qualitatively: EMA_k is EMA applied k times; DEMA = EMA1 + (EMA1 − EMA2); TEMA built "the same way", "an integration of all those EMAs with some factors that actually scale" them [05:11]–[05:53], [06:19]–[06:32].

**Own knowledge (standard finance definition, not from transcript):** TEMA = 3·EMA1 − 3·EMA2 + EMA3. This is the conventional Mulloy (1994) TEMA; I infer the paper uses the same form because the speaker says it follows the finance definition, but the transcript itself does not state the numbers.

## 4. FAME moments and number of betas

**Answer.** The transcript says only that the Adam first- and second-moment EMA equations are written for EMA1, then "similarly" for EMA2 and EMA3, and that substituting these into the TEMA equation yields "two equations ... the new equations for the first moment and the second moment" [05:55]–[06:51]. No explicit formula and no count of beta hyperparameters is given.

**Own inference (from Q3's TEMA form, not stated in transcript):** m_FAME = 3·m1 − 3·m2 + m3 and v_FAME = 3·v1 − 3·v2 + v3, where m1/v1 are the standard Adam EMAs of the gradient and squared gradient, m2/v2 are EMAs of m1/v1, and m3/v3 are EMAs of m2/v2.

**Number of betas: insufficient evidence.** The transcript never says. I do not reliably recall whether the paper uses separate decay rates for each EMA order (which would give more than Adam's two) or reuses β1/β2 across orders, so I will not guess.

## 5. Scale of evaluation

**Answer.**
- Datasets: 6 ("six different data sets different tasks also") [04:45].
- Architectures: 15 ("we analyze 15 different architectures") [04:42].
- Number of other optimizers compared: **insufficient evidence** for an exact count. The transcript names Adam, SGD, AdamW [04:52]–[04:56], and later "Adam W, gr bound [likely AdaBound] and other optimizers" [08:29]–[08:36] and "other man" [08:26] (garbled; possibly another optimizer name). At least four are named (Adam, SGD/SGD+Momentum, AdamW, AdaBound), but the total is not stated.

## 6. CIFAR-100 / ResNet-18 accuracy


## 7. Percentage and exceptions

**Answer.**
- Percentage: 83% — "in 83% of the architectures we actually were better than Adam and SGD" [09:02]–[09:12].
- Exceptions and winning optimizer there: **insufficient evidence.** The transcript does not name the architectures where FAME lost or which optimizer won; that information is only in the on-screen table.

## 8. Ablation study

**Answer.**
- TEMA on both moments vs. first moment only: yes, the speaker says applying it to both is "much better" than "partial FAME" (TEMA only on the first moment, not the second) [09:44]–[10:11].
- Higher order (fourth order, "kma" = QEMA): the speaker compared EMA (Adam), DEMA (double), TEMA and the fourth order and says "in our case ... the results are actually better" [10:14]–[10:38], i.e. the transcript indicates the triple (FAME) came out ahead, so going to fourth order did not help further. This is the speaker's qualitative statement; the exact comparison direction is slightly ambiguous in the garbled captions.
- MS-COCO mAP numbers for Adam, partial FAME, full FAME, QEMA: **insufficient evidence.** No numbers are spoken; they are only on the slides.
