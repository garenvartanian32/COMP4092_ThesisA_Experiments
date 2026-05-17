def solve(self, grid):

    def is_valid(row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        (start_row, start_col) = (3 * (row // 3), 3 * (col // 3))
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            grid[row][col] = num
                            if backtrack():
                                return True
                            grid[row][col] = 0
                    return False
        return True
    if backtrack():
        return grid
    else:
        return None