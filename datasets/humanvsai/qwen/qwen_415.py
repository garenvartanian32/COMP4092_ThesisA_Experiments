def write_to(self, group, append=False):
    if append:
        self._append_to_group(group)
    else:
        self._write_to_group(group)

def _write_to_group(self, group):
    """Write the data to the group, overwriting any existing data."""
    pass

def _append_to_group(self, group):
    """Append the data to the group."""
    pass