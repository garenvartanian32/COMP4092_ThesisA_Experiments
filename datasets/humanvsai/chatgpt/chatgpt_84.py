def find_coastal_coords(grid):
    coastal_coords = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                for direction in ['N', 'S', 'E', 'W']:
                    coastal_coords.append((grid[i][j], direction))
    return coastal_coords
