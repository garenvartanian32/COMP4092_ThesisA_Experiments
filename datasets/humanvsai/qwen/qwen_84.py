def coastal_coords():
    grid_size = 10
    coastal_coordinates = []
    for tile_id in range(grid_size * grid_size):
        row = tile_id // grid_size
        col = tile_id % grid_size
        if row == 0:
            coastal_coordinates.append((tile_id, 'N'))
        if row == grid_size - 1:
            coastal_coordinates.append((tile_id, 'S'))
        if col == 0:
            coastal_coordinates.append((tile_id, 'W'))
        if col == grid_size - 1:
            coastal_coordinates.append((tile_id, 'E'))
    return coastal_coordinates