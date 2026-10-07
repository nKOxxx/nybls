# Ground truth — OH-5LJFiYHA (Korean lecture, Linear Algebra I ch. 1: Matrices)

Author evidence: transcript.txt (Korean Whisper output; lines [14:00]–[16:24] are a
degenerate repetition loop "다이앵글라이 전부 다 0이고 ..." and carry no content) and
grid/g_NNNNNs.png every 16 s (last frame g_01856s.png; video ~31 min).

Note for graders: the transcript is Korean with English technical terms transliterated
(e.g. "토이플릿스" = Toeplitz, "쇼 프로덕트" = Schur product). Searching for English key
terms in the transcript will not hit; search the Korean/transliterated forms listed.

---

## Q1. Textbook title, authors, publisher, year — **B**

**Answer:** "Linear Algebra I: Basic Concepts" by Kazuo Murota and Masaaki Sugihara,
World Scientific, 2022.

**Evidence:**
- Frames: g_00032s.png (title + "Kazuo Murota / Masaaki Sugi"), g_00048s.png
  ("Masaaki Sugihara", "World Scientific ,"), g_00064s.png (full block incl. "2022").
- Transcript: [00:00] "리니얼 엘지 브라 원이라는 교재 ... 부재가 베이식 컨셉트"
  (Linear Algebra I, subtitle Basic Concepts); [00:17] "저자가 2명인데 카즈오헤 수기하라"
  (two authors, garbled as "Kazuo-he Sugihara" — Murota is never spoken intelligibly);
  [00:39] "출판사가 월드 사이언티팩" (World Scientific); [00:49] "2022년".

**Why B:** title, publisher, year and "two authors" are in speech, but the author names
are garbled in speech ("카즈오헤 수기하라" merges two names and drops "Murota"); the
correct names Kazuo Murota and Masaaki Sugihara are legible only on the board.

**Key terms:** Murota, Sugihara, Kazuo, Masaaki, World Scientific, 2022, Basic Concepts.

**Partial:** title + publisher + year correct but authors missing or given as a single
garbled name (e.g. "Kazuo Sugihara"); or one author only.

---

## Q2. Section numbers and titles covered — **B** (mostly visual)

**Answer:** The board shows these section headings in order:
- Chapter 1. Matrices
- 1.1.2 Block Matrices
- 1.2 Operations on Matrices
- 1.2.1 Sum, Scalar multiple
- 1.2.2 Product
- 1.2.3 Direct Sum
- 1.2.4 Kronecker Product (Tensor Product)
- 1.2.5 Hadamard product (Schur)
(No "1.1.1" heading is written; the opening matrix-definition material is under
"Chapter 1. Matrices".)

**Evidence:**
- Frames: g_00112s.png ("Chapter 1. Matrices"), g_00464s.png ("1.1.2 Block Matrices"),
  g_01040s.png ("1.2 Operations on Matrices"), g_01056s.png / g_01072s.png
  ("1.2.1 Sum, Scalar multiple"), g_01088s.png ("1.2.2 Product"), g_01664s.png
  ("1.2.3 Direct Sum"), g_01712s.png ("1.2.4 Kronecker Product / Tensor Product"),
  g_01808s.png / g_01824s.png ("1.2.5 Hadamard product / Schur").
- Transcript: only [01:43] "챕터원" (chapter one) and [28:01] "1.2.4 의 행렬 두 개의 그
  크로네커 프로덕트" are spoken. 1.1.2, 1.2, 1.2.1, 1.2.2, 1.2.3, 1.2.5 are never spoken.

**Key terms:** 1.1.2, 1.2.1, 1.2.2, 1.2.3, 1.2.5, "Operations on Matrices",
"Block Matrices", "Direct Sum".

**Partial:** correct list of topics in order but with section numbers missing or wrong;
or only 1.2.4 identified (what the transcript alone yields).

---

## Q3. How many ways to multiply, and what are they — **S**

**Answer:** Four ways:
1. entry-by-entry via inner (dot) products of a row of the first and a column of the
   second (a11 = 1·5 + 2·7);
2. each column of the product as a linear combination of the columns of the first
   matrix, weighted by the corresponding column of the second;
3. each row of the product as a linear combination of the rows of the second matrix,
   weighted by the corresponding row of the first;
4. the sum of rank-one matrices (column of the first times row of the second).

**Evidence:**
- Transcript: [18:13] "행렬 곱하는 방법 그 4가지 ... 반드시 알고 있어야"; [18:28]–[18:51]
  inner product, "1 곱하기 5 더하기 2 곱하기 7"; [19:20]–[20:45] columns as linear
  combinations with weights; [20:58]–[22:16] rows as linear combinations of the second
  matrix's rows; [22:21] "네 번째 방법은 ... 랭크1 매트릭스의 썸"; summary
  [23:55]–[24:31] "네 가지 방법이 있겠습니다 이건 전부 다 알아둬야".
- Frames (corroborating): g_01120s.png–g_01136s.png (a11 = 1·5 + 2·7),
  g_01200s.png–g_01248s.png (a1 = [1;3]·5 + [2;4]·7, a2 = [1;3]·6 + [2;4]·8),
  g_01296s.png–g_01328s.png (a1^T = 1·[5 6] + 2·[7 8], a2^T = 3·[5 6] + 4·[7 8]),
  g_01360s.png–g_01408s.png (rank-one sum).

**Partial:** says "four" and names three correctly; or names all four without the
count; or lists the methods but confuses which matrix supplies the weights.

---

## Q4. The two rank-one matrices in the worked example — **B**

**Answer:** [1;3]·[5 6] = (5 6; 15 18) and [2;4]·[7 8] = (14 16; 28 32).
(Their sum (19 22; 43 50) is the product; the lecturer does not write the sum.)

**Evidence:**
- Frames: g_01360s.png ([1;3][5 6] + [2;4]...), g_01376s.png (first result
  "5 6 / 15 18"), g_01392s.png (second result "14 16 / 28 32"), g_01408s.png
  (both circled, labelled "rank-one matrix").
- Transcript: [22:39] "1 3 하고 여기 5 6 ... 2 4 하고 7 8"; [22:56] "5 6 ... 3배 하니까
  15 18"; [23:08] "2 4 해 가지고 7 하면은 14 28 이렇게 되고 8 곱하면 16 32" (second
  matrix read column-wise); [23:21] "랭크1 매트릭스죠".

**Why B:** the numbers are spoken, but the second matrix is read out column-by-column
("14 28 ... 16 32"), so the row/column arrangement (14 16; 28 32) is only unambiguous
from the board.

**Key terms:** 15 18, 14 16, 28 32, rank-one.

**Partial:** correct factors ([1;3][5 6] and [2;4][7 8]) but the 2x2 results not
given or one entry wrong; or the second matrix written transposed (14 28; 16 32).

---

## Q5. Zero-divisor example — **B**

**Answer:** A = (1 0; 0 0), B = (0 0; 1 0); AB = (0 0; 0 0). Such A and B are called
**zero divisors**. He contrasts this with real numbers where a·b = 0 implies a = 0 or
b = 0, which fails for matrices.

**Evidence:**
- Frames: g_01536s.png (A and B written in yellow under "A = O or B = O"),
  g_01552s.png ("zero divisor" arrow to A, "AB = [0 0; 0 0]"),
  g_01568s.png (adds "a·b = 0 ⇒ a = 0 or b = 0" boxed).
- Transcript: [25:04]–[25:13] AB = zero matrix does not imply A or B zero;
  [25:25] "zero diviser 가 있다"; [25:36] "a 를 ... 1 0 0 0 0 을 잡고 b 를 이거를
  0 0 1 0 으로 잡아 버리면 ... 0 0 0 0 0 이 나오거든요"; [25:47] "0 diviser 라고
  얘기합니다"; [26:06]–[26:15] real-number contrast.

**Why B:** the term and the idea are spoken, but A is spoken as "1 0 0 0 0" (five
digits) so the exact 2x2 A = (1 0; 0 0) is only certain from the board; B = (0 0; 1 0)
is spoken as "0 0 1 0" and matches the board.

**Key terms:** zero divisor, 1 0 0 0, 0 0 1 0.

**Partial:** term "zero divisor" correct with one matrix right; or both matrices right
but term given only as "not commutative"/"nilpotent" (wrong concept).

---

## Q6. Qualifier for lower triangular with zero diagonal — **V**

**Answer:** "strictly" — i.e. a strictly lower triangular matrix (diagonal entries also
zero). The lecturer writes "strictly" in yellow with a caret in front of "Lower
triangular matrix" and circles the diagonal (3, 4, 5) of the lower triangular example
(3 0 0; 6 4 0; 8 7 5).

**Evidence:**
- Frames: g_00816s.png (lower triangular example 3 0 0 / 6 4 0 / 8 7 5),
  g_00832s.png ("strictly" inserted with caret, diagonal 3,4,5 circled),
  g_00848s.png ("strictly" circled).
- Transcript: [13:53]–[13:55] "가끔 이제 그 여기도 전부 다 0인 경우가 있습니다"
  (sometimes these [diagonal entries] are all zero too) — then from [13:58] to [16:24]
  the transcript collapses into the repeated string "다이앵글라이 전부 다 0이고"; the
  word "strictly" (or any transliteration such as "스트릭틀리") never appears.

**Key terms:** strictly, strictly lower triangular, 스트릭틀리 (none present in
transcript).

**Partial:** says the diagonal is zero / describes the concept but cannot name the
qualifier; "insufficient evidence" is honest but scores below the correct word.

---

## Q7. Matrix type after triangular, before sparse — **V**

**Answer:** **Block lower triangular matrix.** In his 3x3 block example the blocks
above the diagonal are zero: positions (1,2), (1,3) and (2,3) are O; the diagonal and
below (A11, A21, A22, A31, A32, A33) are nonzero blocks.

**Evidence:**
- Frames: g_00896s.png ("block lower trian..." heading starting), g_00912s.png (title
  "block lower triangular matrix" + empty 3x3 grid), g_00928s.png (A11, O, O / A21,
  A22, O / A31, A32, A33), g_00944s.png (six nonzero blocks circled), g_00960s.png–
  g_00992s.png (same board, then "large-scale matrix" and "sparse matrix" added).
- Transcript: this whole span [14:00]–[16:24] is the degenerate repetition loop; "block
  lower triangular", "블럭 로어", "블록 하삼각" do not appear. Sparse/dense resumes at
  [16:24].

**Key terms:** block lower triangular, 블럭 로어 트라이앵글러, A11 A21 A22 A31 A32 A33
(none present in transcript for this span).

**Partial:** names "block lower triangular" without the zero-block positions; or
says "block triangular" (missing lower); or gives positions only.

---

## Q8. Second name for Hadamard product, and the example result — **S**

**Answer:** Also called the **Schur product**. Notation A∘B. For (1 2; 3 4) and
(5 6; 7 8) the result is (1·5 2·6; 3·7 4·8) = (5 12; 21 32), i.e. entrywise product.

**Evidence:**
- Transcript: [29:54] "하다마드 프로덕트 또는 쇼 프로덕트" (Hadamard or "Schur" product,
  transliterated 쇼); [30:17]–[30:35] "1 2 3 4 ... 5 6 7 8 ... 1 곱하기 5 ... 2 곱하기 6 ...
  3 곱하기 7 ... 4 곱하기 8"; [30:35] "각자 그 자리에 있는 것끼리 곱을 하는 거".
- Frames (corroborating): g_01824s.png ("1.2.5 Hadamard product / Schur", "A∘B"),
  g_01840s.png / g_01856s.png (result written as 1·5 2·6 / 3·7 4·8).

**Note:** the board writes the products unevaluated (1·5 etc.); the evaluated
(5 12; 21 32) is arithmetic from that. Accept either form.

**Partial:** "Schur" correct but result wrong (e.g. gives the ordinary product
(19 22; 43 50)); or result right but second name missing.

---

## Label summary
| Q | Label |
|---|-------|
| 1 | B |
| 2 | B (6 of 7 section numbers screen-only) |
| 3 | S |
| 4 | B |
| 5 | B |
| 6 | V |
| 7 | V |
| 8 | S |
