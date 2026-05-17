def draw_cross(self, position, color=(255, 0, 0), radius=4):
        y, x = position
        for xmod in np.arange(-radius, radius+1, 1):
            xpos = x + xmod
            if xpos < 0:
                continue  # Negative indices will draw on the opposite side.
            if xpos >= self.shape[1]:
                continue  # Out of bounds.
            self[int(y), int(xpos)] = color
        for ymod in np.arange(-radius, radius+1, 1):
            ypos = y + ymod
            if ypos < 0:
                continue  # Negative indices will draw on the opposite side.
            if ypos >= self.shape[0]:
                continue  # Out of bounds.
            self[int(ypos), int(x)] = color