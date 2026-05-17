class MyClass:
    def __init__(self):
        self.atoms = {}
        self.NONE = 'X.NONE'

    def intern_atom(self, name, only_if_exists=False):
        if name in self.atoms:
            return self.atoms[name]
        elif only_if_exists:
            return self.NONE
        else:
            atom_number = len(self.atoms)
            self.atoms[name] = atom_number
            return atom_number