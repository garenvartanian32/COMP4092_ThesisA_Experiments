def sudoku_solver(grid):
    """
    Return a solution point for a Sudoku grid.
    
    Parameters:
    -----------
    grid: list[list[int]]
        A 9x9 grid representing the Sudoku puzzle, with 0 indicating an empty cell.
        
    Returns:
    --------
    list[list[int]] or bool
        If a solution exists, return the solved grid. Otherwise, return False.
    """
    def is_valid(row, col, n):
        # check if n is already in row
        if n in grid[row]:
            return False
        
        # check if n is already in column
        if n in [grid[i][col] for i in range(9)]:
            return False
        
        # check if n is already in 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col+3):
                if grid[i][j] == n:
                    return False
        
        return True
    
    def solve_sudoku():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            grid[row][col] = num
                            if solve_sudoku():
                                return True
                            grid[row][col] = 0
                    return False
        return True
    
    if solve_sudoku():
        return grid
    else:
        return False
