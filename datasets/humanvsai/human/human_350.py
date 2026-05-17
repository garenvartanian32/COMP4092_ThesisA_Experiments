def Remove(self, row):
        if row == 0 or row > self.size:
            raise TableError("Attempt to remove header row")
        new_table = []
        # pylint: disable=E1103
        for t_row in self._table:
            if t_row.row != row:
                new_table.append(t_row)
                if t_row.row > row:
                    t_row.row -= 1
        self._table = new_table