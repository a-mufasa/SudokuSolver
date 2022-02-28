from forward_checking import *
import itertools

rows = '123456789'  # Row labels
columns = 'abcdefghi'  # Column labels


class Sudoku:
    AC3_finish = False  # if we are done after AC3 (before other algorithms)

    def __init__(self, puzzle_input):
        board = list(puzzle_input)
        self.positions, self.regions, = [], []  # lists
        self.domains, self.neighbors, self.pruned = {}, {}, {}  # dicts

        self.positions = self.concatenate(columns, rows)  # list of all possible positions on the grid (ex: a1, a2, ...)
        self.domains = self.set_domains(board)
        self.pruned = self.set_pruned(board)
        self.create_regions()
        self.find_neighbors()

    def set_domains(self, board):
        domain = {}
        for i, v in enumerate(self.positions):
            if board[i] == '0':  # if position has a 0, we set it's domain to 1-9
                domain[v] = list(range(1, 10))
            else:
                domain[v] = [int(board[i])]  # otherwise, it's domain is itself
        return domain

    def set_pruned(self, board):
        pruned = {}
        for i, v in enumerate(self.positions):
            if board[i] == '0':
                pruned[v] = list()
            else:
                pruned[v] = [int(board[i])]
        return pruned

    def create_regions(self):
        row_block = [self.concatenate(columns, r) for r in rows]  # Row regions
        col_block = [self.concatenate(c, rows) for c in columns]  # Column regions
        boxes = [self.concatenate(c, r) for c in ('abc', 'def', 'ghi') for r in ('123', '456', '789')]  # 3x3 grids
        blocks = (row_block + col_block + boxes)

        # loop through blocks and create all of the possible constraining regions (append them to regions list)
        for b in blocks:
            combinations = self.permute(b)
            for c in combinations:
                if [c[0], c[1]] not in self.regions:
                    self.regions.append([c[0], c[1]])

    # loop through all possible positions in the puzzle and append next element in region to neighbors list
    def find_neighbors(self):
        for p in self.positions:
            self.neighbors[p] = list()
            for r in self.regions:
                if p == r[0]:
                    self.neighbors[p].append(r[1])

    # puzzle is invalid if neighbor contains value of the key (loops the items w/in assignment dictionary)
    def is_valid(self, assignment, x, value):
        for key, val in assignment.items():
            if val == value and key in self.neighbors[x]:
                return False
        return True

    # returns false if a position in the puzzle has a domain > 1 ; only called before back tracking
    def is_solved(self):
        for p in self.positions:
            if len(self.domains[p]) > 1:
                return False
        return True

    # assigns value to a variable and forward checks to see if it should be removed
    def set_value(self, x, value, assignment):
        assignment[x] = value
        forward_check(self, x, value, assignment)

    # adds the pruned value (from forward check) back to variable neighbor's domain then removes variable from
    # pruned dict and deletes variable from assignment dict
    def undo_value(self, x, assignment):
        if x in assignment:
            for (N, val) in self.pruned[x]:
                self.domains[N].append(val)
            self.pruned[x] = []
            del assignment[x]

    def output(self):
        solution = list()
        if self.AC3_finish:
            for p in self.positions:
                solution.append(self.domains[p][0])
        else:
            for p in self.positions:
                solution.append(self.domains[p])
        for i in range(9):
            print(*solution[i * 9:(i * 9) + 9])

    # The following static methods do not depend state of Sudoku object
    @staticmethod
    def concatenate(x, y):
        combined = []
        for a in x:
            for b in y:
                combined.append(a + b)
        return combined

    @staticmethod
    def permute(i):
        per = []
        for x in range(0, len(i)+1):
            if x == 2:
                for y in itertools.permutations(i, x):
                    per.append(y)
        return per



