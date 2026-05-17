def solve(self, grid):
    """Return a solution point for a Sudoku grid."""
    find = self.find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if self.valid(grid, i, (row, col)):
            grid[row][col] = i

            if self.solve(grid):
                return True

            grid[row][col] = 0

    return False