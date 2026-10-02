Answer all eight. State your answer and the evidence (timestamps and/or frame filenames). If your evidence does not determine an answer, say "insufficient evidence" rather than guessing. A confident wrong answer scores worse than an honest gap.

1. What is the main limitation of the exponential moving average (EMA) that this new optimizer is trying to fix, and what does the speaker say is the key difference between how FAME uses the triple EMA and how it is used in finance?

2. I want to look up the paper. What is its exact title, who are the three authors, and what institution are they from?

3. What is the actual formula for the triple exponential moving average (TEMA) in terms of EMA1, EMA2 and EMA3 (with the exact coefficients)?

4. If I wanted to implement FAME, how are its first and second moments (m_FAME and v_FAME) computed from the first-, second- and third-order EMA terms, and how many beta hyperparameters does the full scheme use?

5. How big was the evaluation: how many datasets, how many architectures, and how many other optimizers was FAME compared against?

6. On CIFAR-100 with ResNet-18, what test accuracy did FAME reach compared with Adam and SGD+Momentum?

7. The speaker claims FAME beat Adam and SGD on most architectures. What percentage does he give, and in the image-classification table, which architectures were the exceptions where FAME was not the best, and which optimizer won there?

8. From the ablation study: does applying TEMA to both moments beat applying it only to the first moment, and does going to an even higher order (fourth-order, QEMA) help further? Give the MS-COCO mAP numbers for Adam (plain EMA), partial FAME, full FAME and QEMA.
