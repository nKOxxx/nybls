# Answers


## 1. EMA limitation, and the FAME-vs-finance difference

**Limitation:** the exponential moving average suffers from an *inherent lag* in trend identification — the smoothed estimate trails the real data.
- Seen: transcript [01:32]–[01:44] ("main disadvantage and limitation is that it's actually can cause an inherent lag comparing with the real data"); slide bullet "Main limitation – it suffers from an inherent lag in trends identification" in u03_79s.png / u04_101s.png / u05_124s.png; Conclusions slide u27_622s.png "a key limitation of the conventional EMA – trend identification lagging".

**Key difference vs. finance:** in finance the (triple) EMA is a *passive indicator* — it is compared against market changes but does not affect them; in FAME the TEMA *actively guides the optimization process and changes the network weights*.
- Seen: transcript [04:04]–[04:34]; slide bullet "Active Guidance in Optimization: In finance, TEMA is used as a passive indicator ... in our FAME optimizer, TEMA actively guides the optimization process and affects the network weights" in u10_237s.png / u11_260s.png / u12_282s.png.

## 2. Paper title, three authors, institution

**Insufficient evidence for the exact paper title and for three authors.** No title/author slide is among the 30 frames (u02_56s.png shows the speaker with no slide; u03_79s.png is already the EMA slide), and the transcript never names the paper or co-authors.

What the evidence does give:
- Talk title as read by the session chair: "leveraging the triple exponential moving average for fast adaptive moment estimation" — transcript [00:17]–[00:24]. Inferred: the paper title is likely similar, but I cannot confirm the exact wording.
- Speaker: "Dr Assaf hugi" (ASR spelling; surname spelling unverified), "senior lecturer at the school of computer science at Ariel" — transcript [00:09]–[00:17]. Inferred: "Ariel" is presumably Ariel University, but the transcript only says "Ariel".
- Other authors: not stated anywhere in the transcript or frames. The speaker says "our project"/"our paper" ([00:55], [05:07]) which implies co-authors, but no names.

## 3. TEMA formula

**TEMA = 3·EMA1(x) − 3·EMA2(x) + EMA3(x)**

- Seen: u13_305s.png / u14_328s.png / u15_350s.png ("High-order EMAs" slide: "Adding the last term to DEMA will supply the TEMA: 3EMA1(x) − 3EMA2(x) + EMA3(x)"), and repeated on the "FAME Moments" slide u16_373s.png / u17_395s.png as "TEMA = 3EMA1(x) − 3EMA2(x) + EMA3(x)".
- Context seen on the same slide: EMA_k = EMA applied k times; DEMA = 2EMA1(x) − EMA2(x). Transcript [05:22]–[05:53] describes the same construction without the coefficients.

## 4. FAME moments and number of betas

From the "FAME Moments" slide (u16_373s.png, u17_395s.png; transcript [05:57]–[06:51]):

First-order (standard Adam EMAs):
- m_t = β1·m_{t−1} + (1−β1)·g_t
- v_t = β2·v_{t−1} + (1−β2)·g_t²

Second-order (EMA2, EMA of the first-order terms):
- dm_t = β3·dm_{t−1} + (1−β3)·m_t
- dv_t = β4·dv_{t−1} + (1−β4)·v_t

Third-order (EMA3):
- tm_t = β5·tm_{t−1} + (1−β5)·dm_t
- tv_t = β5·tv_{t−1} + (1−β5)·dv_t

FAME moments (TEMA combination):
- **m_FAME,t = 3·m_t − 3·dm_t + tm_t**
- **v_FAME,t = 3·v_t − 3·dv_t + tv_t**

**Number of beta hyperparameters: five (β1…β5) as written on the slide.** Seen: the slide uses β1, β2, β3, β4, β5, with β5 appearing in both the tm_t and tv_t lines. Inferred/caveat: the reuse of β5 for both third-order terms may be a slide typo for a sixth β (β6), given that the first and second orders each use separate betas for m and v; the slide as shown has five distinct symbols. The transcript does not state a count.

## 5. Evaluation size

**6 datasets, 15 architectures, compared against 6 optimizers.**
- Seen: slide text "The FAME was evaluated on 6 datasets using 15 architectures and was thoroughly compared with 6 optimizers" in u10_237s.png / u11_260s.png / u12_282s.png.
- Transcript [04:42]–[04:55] confirms "15 different architectures, six different data sets" and names Adam, SGD, AdamW as comparison optimizers (optimizer count only on the slide).

## 6. CIFAR-100, ResNet-18 accuracies

From the image-classification table (u20_463s.png, u21_486s.png, u22_508s.png, u23_531s.png), row "Resnet-18" under CIFAR-100:
- **FAME: 0.723 ± 0.006** (bold)
- **Adam: 0.708 ± 0.008**
- **SGD + Momentum: 0.693 ± 0.019**

Caveat: the table text is small at the 1568-px frame width and I could not zoom; the digits above are my best reading and are consistent across the four frames showing the slide, but the last decimal places carry some OCR-style uncertainty. The transcript gives no numbers for this row.

## 7. Percentage claim and the exceptions in the image-classification table

**Percentage: 83%** — transcript [09:04]–[09:12] ("in 83% of the architectures we actually were better than Adam and SGD").

**Exceptions (seen in the table, u20_463s.png etc., bold marks the best column):**
- **MobileNet (CIFAR-100): SGD + Momentum won** — 0.644 ± 0.011 bold vs. FAME 0.612 ± 0.005, Adam 0.601 ± 0.007.
- **DenseNet-201 (CIFAR-100): Adam won** — 0.742 ± 0.006 bold vs. FAME 0.739 ± 0.005, SGD+M 0.733 ± 0.006.

Inferred consistency check: the table has 12 architecture rows (1 CIFAR-10 + 11 CIFAR-100); 10/12 = 83%, matching the spoken figure.

## 8. Ablation: both moments vs. first only; fourth order (QEMA)

**Both moments beat first-moment-only: yes.** Transcript [09:47]–[10:11] ("to do that on both equations is much better"); table "TEMA for different Moments" in u25_576s.png / u26_599s.png shows "Our FAME" bold on every row vs. "Partial FAME".

**Going to fourth order (QEMA) does not help further: no.** In the "High-Order EMAs" table (same frames) QEMA is below FAME on every row; transcript [10:14]–[10:38] says FAME's results were better than EMA, DEMA and the fourth order.

**MS-COCO mAP numbers (seen, u25_576s.png / u26_599s.png):**
- Adam (plain EMA): **0.265 ± 0.021**
- Partial FAME (TEMA on first moment only): **0.504 ± 0.006**
- Full FAME: **0.529 ± 0.003**
- QEMA (fourth order): **0.495 ± 0.005**
- (For completeness, DEMA on the same row: 0.317 ± 0.004; the high-order table lists the MS-COCO architecture as YOLOv5-n.)

Caveat: same small-text reading limitation as Q6; these values were consistent across both frames showing the slide.

---
