def _get_storage(self):
    storage = self.storage
    if storage is None:
        return None
    return storage.json