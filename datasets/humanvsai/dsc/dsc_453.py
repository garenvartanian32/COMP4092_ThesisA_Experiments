def remove(self, key):
    """remove key from the namespace.  it is fine to remove a key multiple times."""
    if key in self:
        del self[key]