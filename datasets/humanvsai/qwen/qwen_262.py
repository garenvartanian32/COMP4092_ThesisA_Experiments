def filtered(self, indices):
    if not indices:
        return self
    if not all((isinstance(i, int) and 0 <= i < self.tot_sites for i in indices)):
        return self
    if len(set(indices)) != len(indices):
        return self
    return self._filtered(indices)

def _filtered(self, indices):
    pass