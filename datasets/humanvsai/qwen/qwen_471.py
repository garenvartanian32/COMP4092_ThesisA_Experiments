def intern_atom(self, name, only_if_exists=0):
    if only_if_exists and name not in self.atoms:
        return X.NONE
    atom_number = self.atoms.get(name, len(self.atoms))
    if name not in self.atoms:
        self.atoms[name] = atom_number
    return atom_number