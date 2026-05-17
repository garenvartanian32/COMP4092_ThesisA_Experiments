def to_displacements(self):
        if not self.coords_are_displacement:
            displacements = np.subtract(self.frac_coords, np.roll(self.frac_coords, 1, axis=0))
            displacements[0] = np.zeros(np.shape(self.frac_coords[0]))
            # Deal with PBC
            displacements = [np.subtract(item, np.round(item)) for item in displacements]
            self.frac_coords = displacements
            self.coords_are_displacement = True
        return