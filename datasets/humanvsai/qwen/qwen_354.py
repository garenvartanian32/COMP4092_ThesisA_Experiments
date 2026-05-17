def sort_columns(self, column, key=None, reverse=False):
    self.data.sort(key=lambda x: key(x[column]) if key else x[column], reverse=reverse)