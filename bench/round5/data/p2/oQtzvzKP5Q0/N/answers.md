# Answers (no-video arm: metadata + own knowledge only)

Evidence available: video.txt only (Title: "IMVC 2024 - Assaf Hoogi, Ariel University / Lecture, Slides"; Channel: Ortra Meeting Point; Duration: 11:19). No frames, no transcript. Anything below marked [own knowledge] is recalled from general knowledge and is UNVERIFIED against this video; anything marked [metadata] comes from video.txt.

1. EMA limitation / difference from finance
   - Partial, [own knowledge]: the standard limitation of an EMA is lag — it smooths but responds slowly to changes in the underlying signal (here, the gradient), so an optimizer built on EMA moments (Adam-style) adapts late to trend changes. A triple EMA (TEMA) is a lag-reduction technique from technical analysis of financial time series.
   - What the speaker says is the key difference between FAME's use of TEMA and the finance use: insufficient evidence. I cannot see or hear the talk, and I do not reliably recall the specific contrast he draws.

2. Paper title, three authors, institution
   - [metadata]: the speaker is Assaf Hoogi, Ariel University, so Hoogi is an author and Ariel University is the institution.
   - [own knowledge, uncertain]: I recall an arXiv paper titled approximately "FAME: Fast Adaptive Moment Estimation based on Triple Exponential Moving Average" (2023), with Assaf Hoogi as senior author and Roi Peleg among the co-authors; I believe Teddy Lazebnik is also a co-author. I am not confident in the exact title wording or the exact author list (I may be conflating versions with different author counts). Treat the author list as insufficient evidence beyond Hoogi / Ariel University.

3. TEMA formula
   - [own knowledge, standard finance definition, not from the video]: TEMA = 3·EMA1 − 3·EMA2 + EMA3, where EMA2 = EMA(EMA1) and EMA3 = EMA(EMA2). Whether the slides use exactly this form: insufficient evidence.

4. m_FAME, v_FAME, number of betas
   - Insufficient evidence. The natural construction is to replace Adam's EMA of the gradient (first moment) and of the squared gradient (second moment) with the TEMA combination of first-, second- and third-order EMA terms (3·E1 − 3·E2 + E3 for each), but I cannot confirm the exact formulas the speaker shows or how many distinct beta hyperparameters the full scheme uses. [own knowledge, uncertain]

5. Evaluation size (datasets / architectures / optimizers)
   - Insufficient evidence from the video. [own knowledge, uncertain]: my recollection of the paper's abstract is on the order of ~6 benchmark datasets, ~14 architectures, and ~6 compared optimizers, but I cannot verify these numbers and they should not be relied on.

6. CIFAR-100 / ResNet-18 accuracies (FAME vs Adam vs SGD+Momentum)
   - Insufficient evidence. Specific numbers are not recoverable from metadata or reliable memory.

7. Percentage of architectures where FAME won; exceptions and winning optimizer
   - Insufficient evidence. I do not know the percentage he gives or which architectures/optimizer are the exceptions.

8. Ablation (TEMA on both moments vs first only; QEMA; MS-COCO mAP numbers)
   - Insufficient evidence for the numbers. [own knowledge, uncertain]: I vaguely recall the paper reporting that applying TEMA to both moments helps over applying it to the first moment only, and that going to fourth order (QEMA) does not improve further, but I cannot confirm this or give the MS-COCO mAP values for Adam, partial FAME, full FAME and QEMA.
