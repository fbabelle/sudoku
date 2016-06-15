# sudoku
A small program to solve Sudoku.

Step 1
Storing unsolved sudoku matrixes in a csv file.
Column name: c1, c2, ... c9
Don't include row indexes.
Replace missing numbers with 0s. (Fill in the blanks with 0s.)
Leave 1 line blank between each sudoku matrix.

For example:
c1	c2	c3	c4	c5	c6	c7	c8	c9
4	0	0	0	0	7	0	0	0
2	3	0	0	9	0	0	0	4
0	0	6	4	0	0	2	0	0
3	0	8	0	1	0	9	0	0
9	0	2	0	0	0	1	0	8
0	0	5	0	8	0	4	0	7
0	0	7	0	0	8	6	0	0
8	0	0	0	4	0	0	7	1
0	0	0	2	0	0	0	0	3
								
0	0	4	6	0	7	0	0	0
2	0	6	0	0	3	0	8	1
0	0	3	0	0	1	0	0	0
0	3	0	5	0	0	8	0	9
0	0	9	0	3	0	1	0	0
6	0	8	0	0	9	0	3	0
0	0	0	1	0	0	2	0	0
8	1	0	7	0	0	3	0	6
0	0	0	3	0	5	7	0	0
								
5	0	0	0	9	0	2	0	1
0	0	2	0	0	7	0	0	8
0	8	0	0	0	0	3	0	0
0	1	4	0	0	5	0	0	0
0	0	0	9	0	3	0	0	0
0	0	0	8	0	0	9	4	0
0	0	3	0	0	0	0	6	0
6	0	0	2	0	0	1	0	0
8	0	9	0	6	0	0	0	5

Step 2
Change your csv file path.
Run the program with python idle. 2.7 version.
You will get another csv file with all the answers for sudoku matrixes under the same path.
