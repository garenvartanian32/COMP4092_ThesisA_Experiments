def are_sites_periodic_images(self, other, tolerance=1e-8, check_lattice=True):
    if check_lattice and self.lattice != other.lattice:
        return False
    frac_diff = np.array(self.frac_coords) - np.array(other.frac_coords)
    frac_diff -= np.round(frac_diff)
    cart_diff = self.lattice.get_cartesian_coords(frac_diff)
    return np.linalg.norm(cart_diff) < tolerance
