def is_periodic_image(self, other, tolerance=1e-08, check_lattice=True):
    if check_lattice and self.lattice != other.lattice:
        return False
    frac_diff = self.frac_coords - other.frac_coords
    return np.allclose(frac_diff - np.round(frac_diff), 0, atol=tolerance)