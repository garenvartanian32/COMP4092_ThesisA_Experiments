def boolean_difference(self, mesh, inplace=False):
    if inplace:
        self.boolean_difference(mesh, inplace=True)
        return None
    else:
        result = self.boolean_difference(mesh, inplace=False)
        return result