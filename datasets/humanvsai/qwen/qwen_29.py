def _jitter(c, magnitude):
    (h, w) = c.shape[:2]
    for y in range(h):
        for x in range(w):
            dy = random.randint(-magnitude, magnitude)
            dx = random.randint(-magnitude, magnitude)
            (ny, nx) = (y + dy, x + dx)
            if 0 <= ny < h and 0 <= nx < w:
                c[y, x] = c[ny, nx]
    return c