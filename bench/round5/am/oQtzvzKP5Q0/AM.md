# Answers — oQtzvzKP5Q0 (fixed evidence pack: transcript.txt + 10 uniform stills)

Legend: SEEN = read directly from a frame or transcript line; INFERRED = my interpretation beyond what is literally shown.

## 1. EMA limitation and the finance-vs-FAME difference

**Limitation:** EMA suffers from an *inherent lag* in trend identification — the smoothed estimate trails the real data.
- SEEN: transcript [01:35]–[01:54] ("the main disadvantage and limitation is that it's actually can cause an inherent lag comparing with the real data"); slide in `am01_101s.png`: "Main limitation – it suffers from an inherent lag in trends identification" (with EMA/SMA and Window/Lag diagrams). Conclusions slide `am09_644s.png`: "We addresses a key limitation of the conventional EMA – trend identification lagging".

**Key difference from finance:** in finance TEMA is a *passive indicator* — it is compared with market changes but does not affect them; in FAME, TEMA *actively guides* the optimization and changes the network weights.
- SEEN: transcript [04:04]–[04:34]; slide `am03_237s.png` bullet "Active Guidance in Optimization: In finance, TEMA is used as a passive indicator ... However, in our FAME optimizer, TEMA actively guides the optimization process and affects the network weights."; `am09_644s.png` "The high-order EMA actively affects the network weights, instead of just forecasting them".

## 2. Paper title, three authors, institution

**Title (partial):** The talk is introduced as "Leveraging the Triple Exponential Moving Average for Fast Adaptive Moment Estimation" (transcript [00:17]–[00:24]). The optimizer is "FAME – Fast Adaptive Moment Estimation" (`am03_237s.png`). INFERRED: the talk title is probably the paper title, but no slide in the pack shows a paper title page, so I cannot confirm it is *exact*.

**Authors:** insufficient evidence. Only the speaker is named: "Dr. Assaf hugi" per the ASR transcript [00:09]–[00:13] (spelling is ASR output, likely not exact). No slide in the pack lists authors. The other two authors are not in the evidence.

**Institution (partial):** the speaker is introduced as "a senior lecturer at the school of computer science at Ariel" (transcript [00:13]–[00:17]). INFERRED: Ariel University. No slide shows an affiliation; whether all three authors share it is not determinable.

## 3. TEMA formula

**TEMA = 3·EMA1(x) − 3·EMA2(x) + EMA3(x)**
- SEEN: `am04_305s.png` ("High-order EMAs" slide: DEMA = 2EMA1(x) − EMA2(x); "Adding the last term to DEMA will supply the TEMA": 3EMA1(x) − 3EMA2(x) + EMA3(x)); repeated on `am05_373s.png` ("TEMA = 3EMA1(x) − 3EMA2(x) + EMA3(x)"). Transcript [05:33]–[05:53] describes the construction.
- Note: `am06_441s.png` also shows the expression "EMA1(x) − 2EMA2(x) + EMA3(x)", but it labels one of the lag-correcting *components* plotted on the right-hand chart, not TEMA itself (TEMA is labelled separately, as the blue line).

## 4. FAME moments and number of betas

**Construction (SEEN, `am05_373s.png`, "FAME Moments" slide):**
- First-order (Adam-style): m_t = β1·m_{t−1} + (1−β1)·g_t ; v_t = β2·v_{t−1} + (1−β2)·g_t²
- Second-order (EMA of the moments): dm_t = β3·dm_{t−1} + (1−β3)·m_t ; dv_t = β4·dv_{t−1} + (1−β4)·v_t
- Third-order: tm_t = β5·tm_{t−1} + (1−β5)·dm_t ; tv_t = β5·tv_{t−1} + (1−β5)·dv_t
- Combined with the TEMA coefficients:
  **m_FAME,t = 3·m_t − 3·dm_t + tm_t**
  **v_FAME,t = 3·v_t − 3·dv_t + tv_t**
- Transcript [06:14]–[06:48] matches ("similarly we can do that for EMA2 ... EMA3 ... put them in the equation of TEMA we can get those two equations ... the new equations for the first moment and the second moment").

**Number of betas:** the slide shows **five distinct beta symbols, β1 … β5**. SEEN: β1, β2 for the first-order pair; β3, β4 for the second-order pair; β5 appears on *both* third-order equations (tm_t and tv_t). INFERRED/caveat: whether β5 shared by tm and tv is intentional or a slide typo (vs. a sixth β6) is not determinable from this pack; as written, the scheme uses five.

## 5. Evaluation size

**6 datasets, 15 architectures, compared against 6 optimizers.**
- SEEN: `am03_237s.png`: "The FAME was evaluated on 6 datasets using 15 architectures and was thoroughly compared with 6 optimizers." Transcript [04:42]–[04:45]: "15 different architectures, six different data sets".
- Named optimizers seen in the pack (INFERRED list of the 6, not confirmed complete): Adam, SGD(+Momentum), AdamW, AdaGrad, AdaBound, AdaHessian (`am07_508s.png` legend; `am08_576s.png` tables; transcript [08:29]–[08:36]).

## 6. CIFAR-100 / ResNet-18 accuracy

**FAME 0.723 ± 0.006 vs Adam 0.708 ± 0.008 vs SGD+Momentum 0.693 ± 0.019.**
- SEEN: table on `am07_508s.png`, row "CIFAR-100 / Resnet-18", columns "Our FAME / Adam / SGD + Momentum". Caveat: the table text is small at 1568 px width (no zoom permitted); the digits above are what I read, and they are consistent with neighbouring rows, but ±1 in the last digit of the std-dev is possible.

## 7. "Beat on most architectures" percentage and exceptions

**Percentage:** 83%. SEEN: transcript [09:04]–[09:12] ("in 83% of the architectures we actually were better than Adam and SGD").

**Exceptions in the image-classification table (`am07_508s.png`), SEEN (bold marks the best cell):**
- **MobileNet (CIFAR-100):** SGD + Momentum won, 0.644 ± 0.011 (FAME 0.612 ± 0.005, Adam 0.601 ± 0.007).
- **DenseNet-201 (CIFAR-100):** Adam won, 0.742 ± 0.006 (FAME 0.739 ± 0.005, SGD+Momentum 0.733 ± 0.006).
- All other rows (CIFAR-10 ResNet18; CIFAR-100 EfficientNet-b0/b3, DenseNet-121, SqueezeNet, ResNet-18/34, SEResNet-18, Inception-v3, WideResNet 40-4, RevViT) show FAME in bold.
- INFERRED/caveat: 11 of 13 rows ≈ 85%, not exactly 83%; the speaker's 83% may refer to the paper's full 15-architecture set rather than this slide. Same small-text caveat as Q6.

## 8. Ablation: TEMA on both moments vs first only; QEMA; MS-COCO mAP numbers

**Qualitative (SEEN, transcript only):**
- Applying TEMA to both moments beats applying it only to the first moment ("partial FAME"): [09:44]–[10:11] ("to do that on both equations is much better").
- Going to fourth order (QEMA, transcribed "kma ... the fourth order") does not help further; the speaker says FAME's (TEMA) results are better than EMA, DEMA and the fourth-order variant: [10:11]–[10:38].

**MS-COCO mAP numbers for Adam / partial FAME / full FAME / QEMA: insufficient evidence.** The ablation slides fall between `am08_576s.png` (576 s, object-detection results) and `am09_644s.png` (644 s, conclusions); no ablation slide is in the pack and the transcript gives no numbers. The only COCO numbers in the pack are the main (non-ablation) table on `am08_576s.png`: YOLOv5-s mAP@0.5 — FAME 0.569 ± 0.003, SGD 0.549 ± 0.005, Adam 0.265 ± 0.021, AdamW 0.446 ± 0.013; mAP@0.5:0.95 — FAME 0.375 ± 0.003, SGD 0.352 ± 0.005, Adam 0.121 ± 0.021, AdamW 0.271 ± 0.014. These are not the ablation rows and contain no partial-FAME or QEMA entries.

---
Frames examined: 10 of 10 (am00_33s through am09_644s), each opened once at native pack resolution; no crops, zooms or re-renders were produced. Transcript.txt read in full. I modified no file other than this answers.md.
