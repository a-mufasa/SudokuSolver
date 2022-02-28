def forward_check(sudoku, x, value, assignment):
    for n in sudoku.neighbors[x]:
        if n not in assignment:
            if value in sudoku.domains[n]:
                sudoku.domains[n].remove(value)  # remove value from neighbor's domain
                sudoku.pruned[x].append((n, value))  # add the neighbor and value to pruned dict


def backtrack(assignment, sudoku):
    if len(assignment) == len(sudoku.positions):  # if complete
        return assignment
    var = MRV(assignment, sudoku)
    for value in sudoku.domains[var]:
        if sudoku.is_valid(assignment, var, value):
            sudoku.set_value(var, value, assignment)
            result = backtrack(assignment, sudoku)
            if result:
                return result
            sudoku.undo_value(var, assignment)
    return False


# select the variable (x) with the fewest legal values in its domain
def MRV(assignment, sudoku):
    unassigned_pos = []
    for p in sudoku.positions:
        if p not in assignment:
            unassigned_pos.append(p)
    return min(unassigned_pos, key=lambda x: len(sudoku.domains[x]))

