def draw_cross(self, position, color=(255, 0, 0), radius=4):
    (row, col) = position
    for i in range(-radius, radius + 1):
        self.set_pixel((row + i, col), color)
        self.set_pixel((row, col + i), color)