# Answers

1. Title: "Linear Algebra I: Basic Concepts". Authors: Kazuo Murota and Masaaki Sugihara. Publisher: World Scientific. Year: 2022.
   Evidence: frames/am00_186s.png (SEEN: handwritten title, both author names, "World Scientific, 2022"); transcript [00:00]-[00:49] (two authors, World Scientific, published 2022). Author spelling "Masaaki" is as written on the board (it reads "Masaaki Sugihara").

2. Only partly determined.
   - 1.1.2 Block Matrices (SEEN, am01_560s.png).
   - 1.2.3 Direct Sum (SEEN, am04_1680s.png; transcript [27:33]-[28:01]).
   - 1.2.4 Kronecker Product, also called tensor product (HEARD: transcript [28:01]-[28:12] says "1.2.4" then Kronecker product; no frame).
   - Chapter 1 is "Matrices" (am00_186s.png). The lecture also covers matrix basics/special matrices before 1.1.2 and matrix products before 1.2.3, but their section numbers and titles are not shown in the evidence: insufficient evidence for those. Inferred only: 1.1.1 likely covers basic definitions and 1.2.x the operations.

3. Four ways (transcript [18:13]-[18:20] "4가지 ... 반드시 알아야", recap [24:02]-[24:31] "네 가지 방법"):
   (1) entry by entry, each entry as a dot (inner) product of a row of A with a column of B ([18:28]-[18:51]);
   (2) columns of the product as linear combinations of the columns of the first matrix, weighted by the columns of the second ([19:20]-[20:58]);
   (3) rows of the product as linear combinations of the rows of the second matrix, weighted by the rows of the first ([20:58]-[22:21]);
   (4) as a sum of rank-one matrices (column of A times row of B) ([22:21]-[24:26]).
   am03_1307s.png (SEEN) shows way (3): a1^T = 1*[5 6] + 2*[7 8].

4. Rank-one matrices (transcript [22:39]-[23:16]; computed from column-times-row, inferred from spoken numbers, no frame shows it):
   (1;3)[5 6] = [[5, 6],[15, 18]]
   (2;4)[7 8] = [[14, 16],[28, 32]]
   Sum = [[19, 22],[43, 50]]. The lecturer says "14 28" then "16 32" for the second matrix's entries, i.e. columns (14,28) and (16,32).

5. A = [[1, 0],[0, 0]], B = [[0, 0],[1, 0]]; AB = 0. Term: "zero divisor" (transcript [25:04]-[25:54], spoken "zero diviser"). Caveat: the transcript gives A's and B's entries only as garbled digit runs ("1 0 0 0 0", "0 0 1 0"); I read them row-major as above and checked that AB is the zero matrix, which fits. Moderate confidence on the exact B; no frame shows it.

6. Insufficient evidence. The relevant passage ([13:52]-[14:00], "diagonal also all 0") is followed by a looping garbled transcript from about [14:00] to [16:24], and no frame lands there (nearest frames are 933s and 1307s). Inference from standard terminology only (not from the video): the word is probably "strictly" (strictly lower triangular). Not confirmed.

7. Block lower triangular matrix (SEEN: am02_933s.png, handwritten "block lower triangular matrix"; timestamp ~15:33 fits between the triangular-matrix discussion at ~13:00-14:00 and the sparse/dense talk at [16:24]). In the 3x3 block example the zero blocks are positions (1,2), (1,3) and (2,3), i.e. everything above the block diagonal; blocks A11, A21, A22, A31, A33 are nonzero (A32 is drawn blank, so its status is not shown; the visible A31 label is cut off as "A3").

8. Second name: Schur product ("Hadamard product, or Schur product", transcript [29:54]-[30:05], rendered by the auto-transcript as "쇼 프로덕트"; the "Schur" spelling is my inference from that phonetic rendering and the standard name). Result for (1 2; 3 4) and (5 6; 7 8): entrywise product = [[5, 12],[21, 32]] (transcript [30:21]-[30:38]: 1*5, 2*6, 3*7, 4*8).

Frames examined: 5 (am00_186s, am01_560s, am02_933s, am03_1307s, am04_1680s), plus the full transcript.txt.
I modified no other file; only answers.md was created.
