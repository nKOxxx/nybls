# Answers

1. Web address: web.mit.edu/18.06 [00:26-00:44]. Textbook: "Introduction to Linear Algebra" [00:18-00:26] (author not named in the transcript; Strang is the lecturer, and from own knowledge the book is by Strang, but the transcript does not say so). The page has past exercises, MATLAB codes and the syllabus. He says the video-viewing address would be given later [00:51-00:57], and it is not given in this transcript.

2. Equations: 2x - y = 0 and -x + 2y = 3 [02:30-02:58]. Solution: the point (x, y) = (1, 2) [07:55-08:06]. Check: 2(1) - 2 = 0, and -1 + 4 = 3 [08:10-08:14]. (The transcript shows only the check of the second equation spoken aloud; the first follows from x=1, y=2 earlier at [05:30-05:36].)

3. The combination is 1 times column one plus 2 times column two [12:01-12:09]. Column one = (2, -1) [11:10], column two = (-1, 2) [11:32-11:35], right-hand side b = (0, 3) [14:08-14:11]. Check: 2 + (-2) = 0, and -1 + 4 = 3 [13:46-13:55].

4. Every right-hand side: the combinations fill the whole plane [14:53-15:03].

5. A, row by row: [2 -1 0], [-1 2 -1], [0 -3 4] [16:48-17:06]. Right-hand side b = (0, -1, 4) [17:16]. Solution (x, y, z) = (0, 0, 1) [24:53-25:01]. Easy to see because b is exactly column three of A ("specially chosen", [24:37-24:45]), so take none of columns 1 and 2 and one of column 3 [25:01-25:11].

6. New right-hand side (1, 1, -3) [26:34-26:43]. Built by adding the first two columns of A ("cooked it up by adding this one to this one", [26:46-26:49]). New solution: 1 of column one, 1 of column two, none of column three, so (x, y, z) = (1, 1, 0) [26:57-27:08; 27:31-27:40]. (He states the combination; the vector (1,1,0) is my reading of it.)

7. Ax = b fails to have a solution for every b when the columns do not give all of space, e.g. all three columns lie in the same plane [31:06-31:12]. Only b in that plane are reachable [31:53-32:09]. Such a matrix is singular, not invertible [32:11-32:23]. When it does work (for every b) it is non-singular / invertible [30:17-30:21]. His example: column three equals the sum of column one and column two [31:28-31:36]. Extension: in 9x9, if the ninth column equals the eighth, the combinations fill only an eight-dimensional plane in nine-space [33:50-35:06].

8. His favorite way: by columns. Ax is a linear combination of the columns of A [36:50-37:01; 38:21-38:36]. For the matrix [2 5; 1 3] (rows 2 5 and 1 3, as the later row computations show) times (1, 2): 1 of the first column (2, 1) plus 2 of the second column (5, 3) = (12, 7) [37:03-37:28]. Other way: by rows, each row dotted with x (dot products): 2*1+5*2 = 12, 1*1+3*2 = 7 [37:34-38:14].
