def _project_name(self):
    if self._requirement is None:
        raise ValueError('No requirement specified')
    return self._requirement.unsafe_name

def _project_name(self):
    """Return the inner Requirement's "unsafe name".

        Raise ValueError if there is no name."""
    if self._requirement is None:
        raise ValueError('No requirement specified')
    return self._requirement.unsafe_name