Answer all eight. State your answer and the evidence (timestamps and/or frame filenames). If your evidence does not determine an answer, say "insufficient evidence" rather than guessing. A confident wrong answer scores worse than an honest gap.

1. If I'm planning a training run, how many training tokens per parameter does the Chinchilla result recommend, and what ratio does the lecturer say the best production models actually use once inference cost is considered?

2. How does the lecturer estimate the cost of training Llama 3 400B? I want the GPU-hours figure, the hourly rental rate he assumes, the resulting rental cost, the salary assumption, and the overall total.

3. Why do LLMs use tokenizers instead of treating each whole word as a token, or each character as a token? Give the problem with each option.

4. Why isn't perplexity used for academic benchmarking any more, and why can't it be used to evaluate an aligned (post-PPO) model? Give the reasons the lecturer gives.

5. The lecture lists common open academic pre-training datasets with their sizes. Which datasets named on the slide besides The Pile and C4 are listed, and how many tokens does each have?

6. In the AlpacaEval length-bias table shown in the lecture, what win rates does Mixtral-8x7B-Instruct-v0.1 get when the judged model is prompted to be concise, standard, and verbose?

7. In the Automatic Mixed Precision recipe for training, which 16-bit format is used, and besides matrix multiplications, which other tensors are kept in 16-bit and which are kept in 32-bit?

8. In the supervised fine-tuning data-quantity experiment (LIMA), what range of training-example counts was tested, what happened to generation quality across that range, and roughly what quality score did it sit at?
