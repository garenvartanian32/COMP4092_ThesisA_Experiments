def to_displacements(self):
    # Assuming self is a list of tuples, where each tuple represents a point in 2D space
    # and the list represents the trajectory of an object
    displacements = []
    for i in range(1, len(self)):
        # Calculate the displacement between the current point and the previous point
        displacement = ((self[i][0] - self[i-1][0])**2 + (self[i][1] - self[i-1][1])**2)**0.5
        displacements.append(displacement)
    return displacements