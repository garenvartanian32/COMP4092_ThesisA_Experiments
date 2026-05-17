def _add_uid(self, uid, skip_handle=False):
    if skip_handle:
        self._add_uid_to_field(uid, 'url')
    else:
        self._add_uid_to_field(uid, 'handle')

def _add_uid_to_field(self, uid, field):
    """Add unique identifier to the specified field."""
    if field not in self._fields:
        raise ValueError(f"Field '{field}' does not exist in the object.")
    if uid in self._fields[field]:
        raise ValueError(f"UID '{uid}' already exists in the field '{field}'.")
    self._fields[field].append(uid)