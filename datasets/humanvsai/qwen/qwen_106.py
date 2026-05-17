def get_neighbors(self, connectedness=8):
    if connectedness not in [4, 8]:
        raise ValueError('Connectedness must be 4 or 8')