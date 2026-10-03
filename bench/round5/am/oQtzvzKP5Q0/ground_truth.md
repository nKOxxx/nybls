# Ground truth — oQtzvzKP5Q0 (IMVC 2024, Assaf Hoogi, FAME optimizer)

Video is ~11:15 long. Grid frames are at 5 s + 10 s steps (g_00005s ... g_00675s). Slides visible: title (g_00065s), EMA/lagging (g_00085s–g_00125s), research goal (g_00145s), finance-inspired (g_00165s–g_00225s), FAME overview (g_00245s–g_00295s), high-order EMAs (g_00315s–g_00345s), FAME moments (g_00355s–g_00405s), TEMA simulation (g_00415s–g_00455s), image classification results (g_00465s–g_00555s), object detection (g_00565s–g_00585s), ablation (g_00595s–g_00645s), conclusions (g_00655s–g_00665s), outro card (g_00675s).

---

## Q1 — EMA limitation and FAME vs finance use
**Label: S**

**Answer:** The main limitation of EMA is the inherent lag between the smoothed estimate and the real data (trend identification lagging); its advantage is that it smooths out noise/spikes. The key difference from finance: in finance the (T)EMA is only a passive indicator that describes/forecasts the trend without influencing it, whereas in FAME the TEMA actively guides the optimization — it changes the network weights and affects the learning process.

**Evidence:**
- Transcript [01:24]–[01:44]: "the main advantage is that it can actually smooth out the ... spikes in the ... noise in the data but the main disadvantage and limitation is that it's actually can cause an inherent leg comparing with the real data".
- Transcript [04:04]–[04:36]: "the main difference comparing with Finance is that it actively guides the optimization so it's actually change the network weights and ... affect the learning process while in finance it's only a passive indicator ... but it's not influence the trend and that's the main ... contribution".
- Also on screen: g_00085s (slide "Main limitation – it suffers from an inherent lag in trends identification"), g_00245s (FAME slide: "In finance, TEMA is used as a passive indicator ... in our FAME optimizer, TEMA actively guides the optimization process and affects the network weights").

**Partial:** naming only the lag or only the active/passive distinction.

---

## Q2 — Paper title, authors, institution
**Label: V**

**Answer:** Title: "Improving Gradient-Trend Identification with Finance-Inspired FAME Optimizer". Authors: Roi Peleg, Teddy Lazebnik, Assaf Hoogi. Institution: Ariel University (Peleg and Hoogi: School of Computer Science; Lazebnik: Mathematics department). (The title slide is branded IMVC 2023, reused at IMVC 2024.)

**Evidence:** g_00065s (title slide). Transcript only gives the speaker's name and Ariel ([00:09]–[00:17]: "Dr Assaf hugi a senior lecturer at the school of computer science at Ariel") and the spoken talk title "leveraging the triple exponential moving average for fast adaptive moment estimation" ([00:17]–[00:24]), which is NOT the paper title on the slide. Co-authors are never spoken.

**Key terms (search transcript):** "Improving Gradient-Trend Identification", "Finance-Inspired", "Roi Peleg", "Peleg", "Teddy Lazebnik", "Lazebnik", "Hoogi", "Ariel University", "Mathematics department".

**Partial:** speaker name + Ariel only, or the spoken session title instead of the slide title; missing one co-author.

---

## Q3 — TEMA formula
**Label: V**

**Answer:** TEMA = 3·EMA1(x) − 3·EMA2(x) + EMA3(x), where EMA_k means EMA applied k times (EMA2 = EMA(EMA(x)), etc.). (Intermediate: DEMA = 2·EMA1 − EMA2; lag-correcting term EMA1 − EMA2.)

**Evidence:** g_00315s / g_00345s (slide "High-order EMAs": "3EMA1(x) − 3EMA2(x) + EMA3(x)", "DEMA = 2EMA1(x) − EMA2(x)", "EMA_k = EMA(EMA ... (EMA(x))) k times"); g_00355s–g_00405s (FAME Moments slide repeats "TEMA = 3EMA1(x) − 3EMA2(x) + EMA3(x)"). Transcript [05:19]–[05:53] describes the construction qualitatively ("MMA K is to do K * m on Emma", "take this subtraction and add it to emma1", "the same way we are doing for TMA") but never states the coefficients 3, −3, +1.

**Key terms:** "3EMA1", "3 EMA", "minus 3", "2EMA1", "coefficient", "three times".

**Partial:** giving only DEMA = 2EMA1 − EMA2 or describing TEMA as "EMA plus lag-correcting terms" without coefficients.

---

## Q4 — FAME moment equations and number of betas
**Label: V**

**Answer:**
- Standard (Adam) EMA moments: m_t = β1·m_{t−1} + (1−β1)·g_t ; v_t = β2·v_{t−1} + (1−β2)·g_t².
- Second-order: dm_t = β3·dm_{t−1} + (1−β3)·m_t ; dv_t = β4·dv_{t−1} + (1−β4)·v_t.
- Third-order: tm_t = β5·tm_{t−1} + (1−β5)·dm_t ; tv_t = β5·tv_{t−1} + (1−β5)·dv_t.
- FAME moments: m_FAME,t = 3·m_t − 3·dm_t + tm_t ; v_FAME,t = 3·v_t − 3·dv_t + tv_t.
- Five beta hyperparameters (β1 … β5) as written on the slide (β5 is shared by tm and tv).

**Evidence:** g_00355s, g_00365s, g_00385s, g_00405s ("FAME Moments" slide, pink box with m_FAME and v_FAME). Transcript [05:57]–[06:51] only says Adam has two moments, "similarly we can do that for Emma 2 ... Emma 3", and "those two equations are the new equations for the first moment and the second moment" — no symbols or coefficients.

**Key terms:** "3m", "3dm", "tm", "dv", "tv", "beta 3", "beta 4", "beta 5", "β5", "five betas".

**Partial:** correct m_FAME/v_FAME form but wrong or missing beta count; or stating "TEMA applied to both moments" without the equations.

---

## Q5 — Scale of the evaluation
**Label: B**

**Answer:** 6 datasets, 15 architectures, compared against 6 optimizers.

**Evidence:**
- Transcript [04:42]–[04:45]: "we analyze 15 different architectures six different data sets"; [04:52]–[04:56] names only "Adam SGD Adam W" (and later [08:32] "Adam W gr bound and other optimizers") — the count "6 optimizers" is never spoken.
- g_00245s / g_00265s / g_00295s (FAME slide): "evaluated on 6 datasets using 15 architectures and was thoroughly compared with 6 optimizers".
- Consistent with the EfficientNet-B3 plot legend on g_00465s (our FAME, AdamW, AdaGrad, AdaBound, Adahessian) plus Adam and SGD elsewhere.

**Key terms:** "6 optimizers", "six optimizers", "compared with 6".

**Partial:** 15 architectures + 6 datasets with optimizer count missing or guessed as 3 (Adam, SGD, AdamW).

---

## Q6 — CIFAR-100 / ResNet-18 accuracy
**Label: V**

**Answer:** FAME 0.723 ± 0.006; Adam 0.708 ± 0.008; SGD+Momentum 0.693 ± 0.019.

**Evidence:** g_00465s–g_00555s (image-classification results table, row CIFAR-100 / Resnet-18). Transcript [08:00]–[08:08] mentions ImageNet with ResNet-18 and CIFAR-100 with ViT/EfficientNet but gives no numbers; "the table states all architecture that we actually tested only for CIFAR" ([08:12]–[08:18]).

**Key terms:** "0.723", "72.3", "0.708", "0.693".

**Partial:** FAME value correct but a baseline missing/wrong; or confusing with the ResNet-34 row (0.736 / 0.721 / 0.698).

---

## Q7 — "83%" claim and the exceptions in the table
**Label: B**

**Answer:** He says FAME was better than Adam and SGD in 83% of the architectures. In the table the two exceptions are: MobileNet (CIFAR-100), where SGD+Momentum is best (0.644 ± 0.011 vs FAME 0.612 ± 0.005, Adam 0.601 ± 0.007); and DenseNet-201 (CIFAR-100), where Adam is best (0.742 ± 0.006 vs FAME 0.739 ± 0.005, SGD 0.733 ± 0.006). FAME is bold/best on the other 10 of 12 rows (10/12 ≈ 83%).

**Evidence:**
- Transcript [09:02]–[09:12]: "in the table you can see that actually in 83% of the architectures we actually were better than Adam and Sgt".
- Table on g_00465s–g_00555s: bold entries in the SGD+Momentum column for MobileNet (0.644) and the Adam column for DenseNet-201 (0.742).

**Key terms:** "MobileNet", "DenseNet-201", "DenseNet", "0.644", "0.742", "exception".

**Partial:** 83% only, or naming one of the two exceptions, or naming them without the winning optimizer.

---

## Q8 — Ablation: both moments vs partial, and vs QEMA
**Label: B**

**Answer:** Yes on both counts: applying TEMA to both moments (full FAME) beats applying it only to the first moment (partial FAME), and FAME (third order) also beats the fourth-order QEMA, as well as EMA and DEMA, on every dataset shown. MS-COCO mAP (YOLOv5-n): Adam / plain EMA 0.265 ± 0.021; Partial FAME 0.504 ± 0.006; Our FAME 0.529 ± 0.003; QEMA 0.495 ± 0.005 (DEMA 0.317 ± 0.004).

**Evidence:**
- Transcript [09:44]–[10:38]: "the partial frame is actually when we took the Triple exponential moving average only for the first moment not for the second one and you can see that actually to do that on both equations is much better ... we compare to Dema which is the double exponential and we compare to kma which is the fourth order ... the results are actually better". The qualitative conclusions are spoken; no numbers are spoken.
- g_00595s–g_00645s (Ablation Study slide): left table "TEMA for different Moments" (MS-COCO mAP: ADAM 0.265, Partial FAME 0.504, Our FAME 0.529); right table "High-Order EMAs" (MS-COCO YOLOv5-n: EMA 0.265, DEMA 0.317, Our FAME 0.529, QEMA 0.495).

**Key terms:** "0.504", "0.529", "0.495", "0.265", "QEMA", "Partial FAME".

**Partial:** correct qualitative conclusions (both moments better; QEMA not better) without the numbers, or numbers from a different dataset row (e.g. CIFAR-100: 0.721 / 0.729 / 0.736 / 0.729).

---

## Label tally
S: 1 (Q1). V: 4 (Q2, Q3, Q4, Q6). B: 3 (Q5, Q7, Q8).
