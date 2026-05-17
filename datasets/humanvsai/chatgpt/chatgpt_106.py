def get_tile_neighbors(x, y, connectedness=8):
    neighbors = []
    if connectedness == 8:
        for i in range(x-1, x+2):
            if i < 0 or i > 2:
                continue
            for j in range(y-1, y+2):
                if j < 0 or j > 2:
                    continue
                if i == x and j == y:
                    continue
                neighbors.append((i,j))
    elif connectedness == 4:
        if x > 0:
            neighbors.append((x-1,y))
        if x < 2:
            neighbors.append((x+1,y))
        if y > 0:
            neighbors.append((x,y-1))
        if y < 2:
            neighbors.append((x,y+1))
    return neighbors
