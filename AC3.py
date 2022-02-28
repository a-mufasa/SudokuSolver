def AC3(sudoku):
    queue = list(sudoku.regions)
    while queue:
        x, y = queue.pop(0)
        if AC3_revise(sudoku, x, y):
            if len(sudoku.domains[x]) == 0:
                return False
            for z in sudoku.neighbors[x]:
                if z != x:
                    queue.append([z, x])
    return True


def AC3_revise(sudoku, x, y):
    for a in sudoku.domains[x]:
        if not any([a != b for b in sudoku.domains[y]]):
            sudoku.domains[x].remove(a)
            return True
    return False
