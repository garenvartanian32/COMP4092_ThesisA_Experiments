def flatten_array(grid):
    flattened = []
    for row in grid:
        for element in row:
            flattened.append(element)
    return flattened
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]