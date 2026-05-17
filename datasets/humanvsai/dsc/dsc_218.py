def is_periodic_image(self, other, tolerance=1e-8, check_lattice=True):
    if check_lattice and self.lattice != other.lattice:
        return False

    for i in range(3):
        dist = abs(self.coords[i] - other.coords[i])
        if dist > tolerance:
            return False

    return True