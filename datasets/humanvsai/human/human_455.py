def get(self, key, default=None):
        if self.in_memory:
            return self._memory_db.get(key, default)
        else:
            db = self._read_file()
            return db.get(key, default)