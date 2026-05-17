def to_displacements(self):
    displacements = []
    for i in range(1, len(self.positions)):
        displacement = self.positions[i] - self.positions[i - 1]
        displacements.append(displacement)
    return displacements