def Remove(self, row):
    if row < 1:
        raise TableError('Cannot remove header row or a row before it.')
    if row > len(self.rows):
        raise TableError('Cannot remove a nonexistent row.')
    del self.rows[row - 1]