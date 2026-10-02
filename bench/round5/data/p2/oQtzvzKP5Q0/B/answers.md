# Answers — oQtzvzKP5Q0 (IMVC 2024 talk, Assaf Hoogi, FAME optimizer)

Mode: answer mode (specific questions). Round 0 transcript read in full; it carries Q1, Q5 (partly), Q7 (percentage) and the qualitative half of Q8. Everything else (authors, formulas, table values) is on slides only, so frames/zooms were spent there.

## 1. EMA limitation and the finance difference

**Limitation:** EMA smooths noise well, but its main disadvantage is an **inherent lag** relative to the real data [01:27]–[01:58]; the goal is an adaptive optimizer that responds faster to quick changes and "reduce[s] the lag as much as we can" [02:21]–[02:41]. Slide at [01:35] (sheet tile): "Main limitation – it suffers from an inherent lag in trends identification".

**Key difference vs finance:** In finance TEMA/DEMA is a **passive indicator** — it describes the trend but does not influence it. In FAME, TEMA **actively guides the optimization**: it changes the network weights and affects the learning process [04:00]–[04:36]. Slide at [04:45] (f_285000_1568.png): "Active Guidance in Optimization: In finance, TEMA is used as a passive indicator ... in our FAME optimizer, TEMA actively guides the optimization process and affects the network weights."

Evidence: transcript [01:27]–[02:41], [04:00]–[04:36]; sheet_000.png tile 01:35; f_285000_1568.png.

## 2. Paper title, authors, institution

- **Title (as on the title slide):** "Improving Gradient-Trend Identification with Finance-Inspired FAME Optimizer"
- **Authors:** Roi Peleg*, Teddy Lazebnik^, Assaf Hoogi*
- **Institution:** Ariel University — *School of Computer Science (slide text reads "Computer Science School of Computer Science"), ^Mathematics department.

Note: the session chair introduces the talk as "Leveraging the triple exponential moving average for fast adaptive moment estimation" [00:17]–[00:24], which may be the programme title rather than the paper title; the slide title above is what the speaker shows. The title slide is branded "IMVC 2023" inside an "IMVC 2024" stream overlay — the paper slide may be reused from the earlier year.

Evidence: f_65000_1568.png [01:05]; transcript [00:09]–[00:24].

## 3. TEMA formula

TEMA = **3·EMA1(x) − 3·EMA2(x) + EMA3(x)**, where EMA_k = EMA applied k times (EMA(EMA(...EMA(x)))). Built up on the slide as: lag-correcting term EMA(x − EMA1(x)) = EMA1(x) − EMA2(x); DEMA = 2·EMA1(x) − EMA2(x); adding the next lag term gives TEMA.

Evidence: f_330000_1568.png [05:30] "High-order EMAs" slide; also repeated on f_400000_1568.png [06:40]; transcript [05:11]–[05:53].

## 4. FAME moments and number of betas

From the "FAME Moments" slide [06:40]:

- EMA1 (Adam's moments): m_t = β1·m_{t−1} + (1−β1)·g_t ; v_t = β2·v_{t−1} + (1−β2)·g_t²
- EMA2: dm_t = β3·dm_{t−1} + (1−β3)·m_t ; dv_t = β4·dv_{t−1} + (1−β4)·v_t
- EMA3: tm_t = β5·tm_{t−1} + (1−β5)·dm_t ; tv_t = β5·tv_{t−1} + (1−β5)·dv_t
- **m_FAME,t = 3·m_t − 3·dm_t + tm_t**
- **v_FAME,t = 3·v_t − 3·dv_t + tv_t**

**Betas:** the slide uses **five** distinct hyperparameters β1…β5 (β5 is shared by both third-order terms tm and tv as written on the slide). The speaker does not state the count aloud; this is read off the slide.

Evidence: f_400000_1568.png [06:40]; transcript [05:57]–[06:51].

## 5. Evaluation size

**6 datasets, 15 architectures, compared with 6 optimizers.** Transcript [04:42]–[04:55] gives 15 architectures and 6 datasets and names Adam, SGD, AdamW; the slide at [04:45] adds "thoroughly compared with 6 optimizers". Other optimizers named later: AdamW, AdaBound ("gr bound" in transcript, [08:32]), SGD+Momentum.

Evidence: f_285000_1568.png [04:45]; transcript [04:42]–[04:55], [08:26]–[08:36].

## 6. CIFAR-100 / ResNet-18

From the image-classification table [08:25]:
- **FAME 0.723 ± 0.006**
- **Adam 0.708 ± 0.008**
- **SGD+Momentum 0.693 ± 0.019**

Evidence: z_505000_0_55_50.png (zoom of the results table at [08:25], row "CIFAR-100 / Resnet-18").

## 7. Percentage and exceptions

**Percentage:** "in 83% of the architectures we actually were better than Adam and SGD" [09:02]–[09:12].

**Exceptions in the image-classification table** (bold = best):
- **MobileNet** (CIFAR-100): **SGD+Momentum** won, 0.644 ± 0.011 vs FAME 0.612 ± 0.005, Adam 0.601 ± 0.007.
- **DenseNet-201** (CIFAR-100): **Adam** won, 0.742 ± 0.006 vs FAME 0.739 ± 0.005, SGD+M 0.733 ± 0.006.

All other rows shown (CIFAR-10 ResNet18; CIFAR-100 EfficientNet-b0/-b3, DenseNet-121, SqueezeNet, ResNet-18, ResNet-34, SEResNet-18, Inception-v3, WideResNet 40-4, RevViT) have FAME in bold. (Note: the slide table shows 13 rows, 11 of which FAME wins ≈ 85%; the 83% figure is the speaker's, presumably over the full set in the paper.)

Evidence: transcript [09:02]–[09:12]; z_505000_0_55_50.png [08:25].

## 8. Ablation: both moments vs first only; QEMA

**Both moments beats first-moment-only: yes.** Speaker: applying TEMA "on both equations is much better" [10:05]–[10:11]. Table "TEMA for different Moments" [10:10]:

| Dataset | Adam (original EMA) | Partial FAME | Our FAME |
|---|---|---|---|
| CIFAR-100 (acc) | 0.721 ± 0.008 | 0.729 ± 0.005 | **0.736 ± 0.006** |
| **MS-COCO (mAP)** | **0.265 ± 0.021** | **0.504 ± 0.006** | **0.529 ± 0.003** |
| PASCAL-VOC (mAP) | 0.662 ± 0.011 | 0.829 ± 0.008 | **0.851 ± 0.006** |
| CityScapes (mIoU) | 0.743 ± 0.008 | 0.751 ± 0.005 | **0.757 ± 0.005** |

**Does fourth order (QEMA) help further: no.** Table "High-Order EMAs" [10:10], MS-COCO row (YOLOv5-n): EMA 0.265 ± 0.021, DEMA 0.317 ± 0.004, **Our FAME (TEMA) 0.529 ± 0.003**, **QEMA 0.495 ± 0.005**. QEMA is also below FAME on CIFAR-100 (0.729 vs 0.736), PASCAL-VOC (0.834 vs 0.851) and Cityscapes (0.756 vs 0.757). Speaker: "in our case ... the results are actually better" [10:30]–[10:38].

**MS-COCO mAP summary:** Adam/plain EMA **0.265**, partial FAME **0.504**, full FAME **0.529**, QEMA **0.495**.

Evidence: transcript [09:44]–[10:38]; z_610000_0_25_75.png, z_610000_33_60_45.png, z_610000_55_60_23.png, z_610000_70_60_25.png (zooms of the ablation slide at [10:10]).

---

## Evidence strip

- [00:36, 01:35, 02:07, 05:18, 08:23, 10:08] sheet_000.png — coverage: intro, EMA-lag slide (x2), High-order EMAs formulas, image-classification results table, ablation tables.
- [01:05] f_65000_1568.png — title slide: title, three authors, Ariel University affiliations.
- [04:45] f_285000_1568.png — "FAME Optimizer" slide: passive vs active, 6 datasets / 15 architectures / 6 optimizers.
- [05:30] f_330000_1568.png — High-order EMAs: lag term, DEMA, TEMA = 3EMA1 − 3EMA2 + EMA3 (flagged NEAR-DUPLICATE of the sheet tile; the sheet tile was not legible for coefficients, so this was still needed).
- [06:40] f_400000_1568.png — FAME Moments: m/v, dm/dv, tm/tv with β1–β5; m_FAME, v_FAME.
- [08:25] z_505000_0_55_50.png — image-classification table, all rows legible.
- [10:10] z_610000_0_25_75.png — "TEMA for different Moments" ablation table.
- [10:10] z_610000_33_60_45.png — High-Order EMAs table, Dataset/Architecture/EMA/DEMA columns.
- [10:10] z_610000_55_60_23.png — same table shifted right; QEMA still cut off (my box was too far left — wasted unit).
- [10:10] z_610000_70_60_25.png — Our FAME and QEMA columns.

## Ledger

watched 11 min · examined 10 images (~14,056 visual tokens, ≈$0.03 at sonnet-5 input rate) of ~16,966 total frames · budget 10/46 units

## Tool files

I did not modify, create or delete any file in the nybls repository or installation. No tool bug encountered; the one wasted zoom (z_610000_55_60_23.png) was my mis-estimate of the table's horizontal position, not a tool fault. Note: `nybls probe oQtzvzKP5Q0` returns "error: not a file" for a bare id (it only accepts URLs/paths); I skipped probe since the store already held transcript.txt and scenes.json.
