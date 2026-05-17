def has_material(self, new_material):
    """Determine whether we already have a material of this name."""
    if new_material in self.materials:
        return True
    else:
        return False