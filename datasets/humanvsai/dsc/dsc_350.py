def remove(self, row):
    if row < 1 or row >= len(self.table):
        raise TableError("Attempt to remove nonexistent or header row.")
    del self.table[row - 1]