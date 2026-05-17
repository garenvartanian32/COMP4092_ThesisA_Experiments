def sort_columns(self, column, key=None, reverse=False):
        if isinstance(column, (list, blist)):
            raise TypeError('Can only sort by a single column  ')
        sort = sorted_list_indexes(self._data[self._columns.index(column)], key, reverse)
        # sort index
        self._index = blist([self._index[x] for x in sort]) if self._blist else [self._index[x] for x in sort]
        # each column
        for c in range(len(self._data)):
            self._data[c] = blist([self._data[c][i] for i in sort]) if self._blist else [self._data[c][i] for i in sort]