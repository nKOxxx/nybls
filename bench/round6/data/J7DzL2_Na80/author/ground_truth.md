# Ground truth (Gilbert Strang, MIT 18.06 Lecture 1)

Note: the grid covers only 0-1980 s; the video runs to about 2390 s, so Q8 evidence is transcript-only.

## Q1. Label: S
Answer: web.mit.edu/18.06 ; text is "Introduction to Linear Algebra" (Strang's book).
Evidence: transcript [00:18]-[00:44] ("introduction to linear algebra", "web.mit.edu/18.06"). Frame g_00020s.png shows the same on the board ("Text: Introduction to Linear Algebra", "http://web.mit.edu/18.06") and the book cover.
Partial: URL only or book only.

## Q2. Label: S
Answer: 2x - y = 0 and -x + 2y = 3 ; solution point x=1, y=2, where the two lines meet; check: -1 + 4 = 3.
Evidence: [02:30]-[02:43] equations; [07:51]-[08:17] solution and check. Frame g_00220s.png shows the equations and matrix form; g_00500s.png shows the plot with box x=1, y=2.
Partial: solution without equations, or the reverse.

## Q3. Label: S
Answer: 1 times column 1 plus 2 times column 2; column 1 = (2, -1), column 2 = (-1, 2), b = (0, 3). x=1, y=2.
Evidence: [11:10]-[12:09] and [13:56]-[14:11]. Frames g_00780s.png, g_00500s.png show 1[2,-1] + 2[-1,2] = [0,3].
Partial: coefficients 1 and 2 without the vectors.

## Q4. Label: S
Answer: Every right-hand side; the combinations fill the whole plane.
Evidence: [14:45]-[15:06] ("any right-hand side at all", "fill the whole plane").
Partial: "everything" without "plane / 2D".

## Q5. Label: S
Answer: A = [[2,-1,0],[-1,2,-1],[0,-3,4]] (equations 2x-y=0, -x+2y-z=-1, -3y+4z=4). Solution x=0, y=0, z=1, because the right-hand side b is exactly column 3 of A (one of column 3, none of the others).
Evidence: [15:42]-[16:14] equations; [16:46]-[17:06] matrix; [24:44]-[25:21] solution reason. Frames g_00740s.png and g_01000s.png (board shows the equations, A, and "x=0 y=0 z=1").
Partial: solution without the reason, or only part of the matrix.

## Q6. Label: B (vector and construction are spoken; the board in g_01620s.png also shows it, so S would suffice from speech)
Answer: b = (1, 1, -3), made by adding column 1 and column 2 of A; solution x=1, y=1, z=0 (one of column 1, one of column 2, none of column 3).
Evidence: [26:34]-[27:08] ("a one and a one and a minus three", "adding this one to this one"); [27:35]-[27:40]. Frame g_01620s.png shows the vector (1,1,-3) and "z=0".
Key terms: 1, 1, -3, column 1 plus column 2, z=0.
Partial: vector correct but no solution, or solution without construction.

## Q7. Label: S
Answer: It fails when the three columns lie in the same plane (e.g. column 3 is the sum of column 1 and column 2); then combinations only fill that plane and only b in the plane are reachable. Such a matrix is singular / not invertible. The good case is non-singular / invertible.
Evidence: [30:17]-[30:23], [31:06]-[32:22].
Partial: "dependent columns" without singular/invertible naming.

## Q8. Label: S
Answer: Favorite way is by columns: 1 times first column plus 2 times second column = (12, 7) (first component 2+10=12, second 1+6=7). The other way is row at a time, by dot products: 2*1+5*2=12, 1*1+3*2=7. A times x is a combination of the columns of A.
Evidence: [36:11]-[38:05], [38:21]-[38:30] (no grid frames cover this part).
Partial: result (12,7) without the method.
