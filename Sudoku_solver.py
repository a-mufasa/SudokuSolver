from Utility import Sudoku
from AC3 import *
from forward_checking import *
import sys


def sudoku_solver(puzzle):

    if AC3(puzzle):  # Arc Consistency must return true first
        if puzzle.is_solved():
            puzzle.AC3_finish = True
            return puzzle
        else:
            assignment = dict()
            for p in puzzle.positions:
                if len(puzzle.domains[p]) == 1:
                    assignment[p] = puzzle.domains[p][0]
            assignment = backtrack(assignment, puzzle)
            if assignment:
                for d in puzzle.domains:
                    if len(d) > 1:
                        puzzle.domains[d] = assignment[d]
                return puzzle
            else:
                print("No solution for inputted puzzle (Backtrack Fails)")
                sys.exit(0)
    else:
        print("No solution for inputted puzzle (AC3 Fails)")
        sys.exit(0)


def input_file():
    # takes in the filename inputted by the user
    text_in = sys.argv[1]

    file = open(text_in, 'r')
    sudoku_puzzle = file.read()
    sudoku_puzzle = sudoku_puzzle.replace('\n', '').replace(' ', '')
    file.close()

    # creates the sudoku puzzle from the inputted file/string
    return Sudoku(sudoku_puzzle)


if __name__ == '__main__':
    initial_S = input_file()
    solution_S = sudoku_solver(initial_S)
    solution_S.output()
