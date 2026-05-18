def snake(num_rows, num_cols):
    grid = []
    count = 1
    for row in range(num_rows):
        current_row = list(range(count, count + num_cols))
        if row % 2 == 1:          # odd rows run right→left
            current_row.reverse()
        grid.append(current_row)
        count += num_cols
    return grid