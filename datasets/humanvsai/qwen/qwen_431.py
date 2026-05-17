def _balance(self):
    unbalanced_charges = 0
    unbalanced_radicals = 0
    for atom in self.skin_atoms:
        if atom.charge != 0:
            unbalanced_charges += atom.charge
        if atom.radical != 0:
            unbalanced_radicals += atom.radical
    return (unbalanced_charges, unbalanced_radicals)