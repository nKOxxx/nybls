# Answers

## Round 0 assessment (free)


**Evaluator after Round 0:** all eight questions are about what the lecturer *says* (equations, vectors, solutions, definitions, method). None is a visual-only question (no "what colour", "what is on the board that he does not say", "what does the slide show"). Classification: **sufficient**. Per the skill's governing rule (spend in inverse proportion to what the transcript carries), I requested **zero images**. The one place I considered a frame was the 3x3 third row, where the live dictation at [15:59]–[16:08] is jumbled ("minus 3Z minus 3Y's. I should keep the Y's in that line. And 4Z's is say four"), but he restates the full matrix row by row at [16:48]–[17:06], and that restatement is confirmed by two independent arithmetic checks (col1 + col2 = (1, 1, -3) at [26:34]; b = column 3 at [24:40]). A frame would add nothing the transcript does not already determine.

---

## 1. Course web address and textbook

**Answer:** The course web page is **web.mit.edu/18.06** [00:26]–[00:39] (he says it has past exercises, MATLAB codes and the syllabus). The textbook is **"Introduction to Linear Algebra"** (his own book; he holds it up as "this book") [00:18]–[00:23]. The course is MIT 18.06 Linear Algebra, lecturer Gilbert Strang [00:08]–[00:15]. He says a separate address for viewing the videotapes will be given later [00:47]–[00:53], but it is not given in this lecture.

**Evidence:** transcript [00:08]–[00:53]. Note: the edition of the book is not stated in speech; I did not spend a frame to read the cover since the question asks only which textbook.

## 2. First worked example: the two equations and the row-picture solution

**Answer:** The equations are
- **2x − y = 0**
- **−x + 2y = 3**

[02:27]–[02:43]. Coefficient matrix A = [[2, −1], [−1, 2]], unknown vector (x, y), right-hand side b = (0, 3) [03:05]–[03:29].

In the row picture he plots each equation as a line in the xy-plane. Line 1 (2x − y = 0) goes through the origin and through (1, 2) [05:02]–[05:38] (also checks (1/2, 1) [06:08]). Line 2 (−x + 2y = 3) does not pass through the origin; he plots (−3, 0) and (−1, 1) [06:37]–[07:18]. The lines meet at **(x, y) = (1, 2)** [07:55]–[08:01], which he checks in the second equation: −1 + 4 = 3 [08:10]–[08:14].

**Evidence:** transcript [02:27]–[08:14].

## 3. Column picture of the 2x2 example

**Answer:** The column form of the system is
x · (2, −1) + y · (−1, 2) = (0, 3)
[08:57]–[09:21]. So the two column vectors are **column 1 = (2, −1)** and **column 2 = (−1, 2)**, and the right-hand side is **b = (0, 3)** [11:03]–[11:32]. The combination that produces b is **1 × column 1 + 2 × column 2** (x = 1, y = 2) [12:01]–[12:04]. He draws it head-to-tail: start at (2, −1), add (−1, 2) twice, land on (0, 3) [12:19]–[13:37], and checks componentwise: 2 + (−2) = 0, −1 + 4 = 3 [13:42]–[13:55]. He calls this a "linear combination of the columns", "the most fundamental operation in the whole course" [09:47]–[10:04].

**Evidence:** transcript [08:43]–[14:11].

## 4. All combinations of the two columns

**Answer:** Taking all x and all y, the combinations of (2, −1) and (−1, 2) **fill the whole plane** — every right-hand side in R² is reachable [14:45]–[15:03]. He says this question ("what are all the achievable right-hand sides b?") will come up over and over [15:14]–[15:25].

**Evidence:** transcript [14:27]–[15:25].

## 5. The 3x3 example: matrix A, first solution, and why it is easy

**Answer:** The equations are 2x − y + 0z = 0; −x + 2y − z = −1; 0x − 3y + 4z = 4 [15:40]–[16:08], restated as the matrix [16:48]–[17:06]:

- Row 1: **(2, −1, 0)**
- Row 2: **(−1, 2, −1)**
- Row 3: **(0, −3, 4)**

Right-hand side **b = (0, −1, 4)** [17:13]–[17:16].

Solution: **(x, y, z) = (0, 0, 1)** [24:50]–[25:17].

Why it is easy: in the column picture, b = (0, −1, 4) is **exactly the third column of A** ("that right-hand side that I'm trying to get is actually one of these columns" [24:33]–[24:45]), so the right combination is none of column 1, none of column 2, one of column 3. He admits he "made it work that way just so we would get an answer" [25:16]–[25:17]. He had abandoned the row picture (three planes meeting in a point) without locating that point [21:35]–[21:58]; the column picture makes it visible.

**Evidence:** transcript [15:35]–[25:26]. Cross-check: column 3 read at [22:29]–[22:35] is (0, −1, 4), equal to b — consistent with rows above.

## 6. The second, "special" right-hand side

**Answer:** He keeps the same A and changes b to **(1, 1, −3)** [26:34]–[26:39]. He built it by **adding column 1 and column 2** of A: (2, −1, 0) + (−1, 2, −3) = (1, 1, −3) — "I just cooked it up by adding this one to this one" [26:46]–[26:49]. New solution: one of column 1, one of column 2, none of column 3, i.e. **(x, y, z) = (1, 1, 0)** [26:55]–[27:08]. In the row picture that means three new planes meeting at this new point; in the column picture the same three columns combined differently [27:12]–[27:40].

**Evidence:** transcript [26:14]–[27:45]. Arithmetic independently confirms the matrix in Q5 (0 + (−3) = −3 in the third component).

## 7. When Ax = b has no solution for some b; what the matrix is called

**Answer:** Ax = b is solvable for every b exactly when the combinations of the columns **fill the whole space** (for 3x3, all of three-dimensional space) [28:40]–[29:10]. It fails when the columns do not fill the space — for 3x3, **when the three columns all lie in the same plane**; then every combination stays in that plane and any b outside the plane is unreachable [31:06]–[32:09]. Such a matrix is **singular / not invertible** [32:11]–[32:19]; the good case (his example A) is **non-singular, invertible** [30:17]–[30:21].

His example of how it could happen: **if column 3 is the sum of column 1 and column 2** [31:28]–[31:33] — it then "contributes nothing new". He also gives the 9x9 version: if the ninth column equals the eighth, the combinations fill only an eight-dimensional plane inside nine-dimensional space [33:50]–[35:06]; a random MATLAB 9x9 matrix would almost certainly be invertible [33:32]–[33:48].

**Evidence:** transcript [27:51]–[35:30].

## 8. Multiplying a matrix by a vector: his favorite way, the result, and the other way

**Answer:** Example: A = [[2, 5], [1, 3]] (rows (2, 5) and (1, 3)), x = (1, 2) [36:16]–[36:23]. His favorite way is **a column at a time**: Ax = 1 × (first column) + 2 × (second column) = 1·(2, 1) + 2·(5, 3) [36:47]–[37:12]. First component 2 + 10 = 12, second component 1 + 6 = 7, so **Ax = (12, 7)** [37:17]–[37:28]. His slogan: "A times x is a combination of the columns of A" [38:21]–[38:34].

The other way is **a row at a time, as dot products**: row 1 · x = 2·1 + 5·2 = 12; row 2 · x = 1·1 + 3·2 = 7 [37:34]–[38:14]. He notes that if b were (12, 7), the solution would of course be (1, 2) [39:01]–[39:07].

**Evidence:** transcript [35:49]–[39:07]. The row layout (2, 5 / 1, 3) is fixed by his row-wise dot products, not just by the order "2 5 1 3" he dictates at [36:17].

---

## Evidence strip

No images examined. Every answer rests on the caption transcript (`transcript.txt`, source `video.en.vtt`), with timestamps cited inline above. Confidence after Round 0: sufficient for all eight; no `partial` answers.
