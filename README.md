# SudokuSolver
9x9 Sudoku Puzzle Solver using AC3, Backtracking, and Forward Checking Algorithms in Python

Inputs are taken as text files where 0's represent an empty square of the grid. Any user test cases should be written
into a TEXT FILE with the same FORMAT as shown below.

An example of the acceptable input format for the text file is:

5 3 4 6 7 8 9 0 0  
6 7 2 1 9 5 3 4 8  
1 9 8 3 4 2 5 6 7  
8 5 9 7 6 1 4 2 3  
4 2 6 8 5 3 7 9 1  
7 1 3 9 2 4 8 5 6  
9 6 1 5 3 7 2 8 4  
2 8 7 4 1 9 6 3 5  
3 4 5 2 8 6 1 7 9  

To run your test case, open the Terminal (make sure the directory is correct) and type in (replace filename w/ your
file's name):

**'python Sudoku_solver.py filename.txt'**

I provided an example input file named "input-test.txt". Feel free to use that file and just replace it's contents 
in the same format and run the command using "input-test" in place of filename (shown later).

In addition to AC3 and backtracking + forward checking (with pruning), I chose to use the MRV Variable Ordering
Heuristic which selects the variable with the fewest legal values in its domain (function is in forward_checking.py and
is called within the backtracking function).

Outside resources that helped with coding in Python and understanding the problem:  
Functions of the itertools library (used for permutation): https://docs.python.org/3/library/itertools.html  
Backtracking: https://www.geeksforgeeks.org/backtracking-introduction/  
