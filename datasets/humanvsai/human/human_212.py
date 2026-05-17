def get_sitej(self, site_index, image_index):
        atoms_n_occu = self.s[site_index].species
        lattice = self.s.lattice
        coords = self.s[site_index].frac_coords + self.offsets[image_index]
        return PeriodicSite(atoms_n_occu, coords, lattice)