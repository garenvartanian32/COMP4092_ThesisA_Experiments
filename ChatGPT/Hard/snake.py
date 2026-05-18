def snakefill(n):
    area = n * n
    length = 1
    eaten = 0

    while length * 2 <= area:
        length *= 2
        eaten += 1

    return eaten
