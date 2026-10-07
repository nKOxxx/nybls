# Answers

1. Web address: web.mit.edu/18.06 [00:26-00:44]. Textbook: "Introduction to Linear Algebra" (the lecturer's own book) [00:18-00:23]. The author name is not stated in the transcript. He says the video-viewing address will be given later [00:47-00:53].

2. Equations: 2x - y = 0 and -x + 2y = 3 [02:30-02:43]. Solution: x = 1, y = 2, point (1, 2), where the two lines meet [07:55-08:08]. Check: 2(1) - 2 = 0 [implied], and -1 + 4 = 3 [08:10-08:14].

3. Column picture: x*(column 1) + y*(column 2) = b, with x = 1 and y = 2: one of column 1 plus two of column 2 [11:58-12:04]. Column 1 = (2, -1) [11:10], column 2 = (-1, 2) [11:32], right-hand side b = (0, 3) [09:18-09:21, 13:34-13:37]. Check from speech: 2 - 2 = 0 and -1 + 4 = 3 [13:46-13:55].

4. All combinations of the two columns fill the whole plane, so any right-hand side b can be reached [14:53-15:03].

5. A, row by row: [2 -1 0; -1 2 -1; 0 -3 4] [16:48-17:06], with b = (0, -1, 4) [17:16]. Solution: (x, y, z) = (0, 0, 1) [24:50-25:01]. It is easy to see because b is exactly column 3 of A, so you take none of columns 1 and 2 and one of column 3 [24:40-25:11].

6. New b = (1, 1, -3), built by adding column 1 and column 2 (2,-1,0)+(-1,2,-3) [26:34-26:49]. Solution: x = 1, y = 1, z = 0 (one of column 1, one of column 2, none of column 3) [26:55-27:05, 27:31-27:40]. Note: the vector is read from his speech ("a one and a one and a minus three"); not seen on screen.

7. Ax = b fails to have a solution for every b when the columns do not span the whole space, e.g. the three columns lie in the same plane [31:06-31:12]. Such a matrix is called singular (not invertible) [32:11-32:16]. His example: column 3 is the sum of column 1 and column 2 [31:28-31:33]; then only b in that plane are reachable. Also the 9x9 case where the ninth column equals the eighth [33:50-34:10]. The good case is called non-singular / invertible [30:17].

8. His favorite way is by columns: A times x is a linear combination of the columns of A [36:50-37:01, 38:21-38:36]. For [2 5; 1 3] times (1, 2): one of column 1 (2,1) plus two of column 2 (5,3) gives (12, 7) [37:17-37:28]. Other way: row at a time, each row dot the vector: 2*1 + 5*2 = 12 and 1*1 + 3*2 = 7 [37:37-38:05]. Matrix entries layout (rows 2 5 / 1 3) is inferred from "2 5 1 3" [36:17] plus the column arithmetic, consistent with his result.
