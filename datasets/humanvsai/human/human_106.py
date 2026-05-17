def get_neighbors(self, connectedness=8):
        if connectedness not in [4, 8]:
            raise ValueError("only connectedness values 8 or 4 are allowed")
        unique_neighbors = {}
        # 4-connected neighborsfor pyramid
        matrix_offsets = [
            (-1, 0),  # 1: above
            (0, 1),   # 2: right
            (1, 0),   # 3: below
            (0, -1)   # 4: left
        ]
        if connectedness == 8:
            matrix_offsets.extend([
                (-1, 1),  # 5: above right
                (1, 1),   # 6: below right
                (1, -1),  # 7: below left
                (-1, -1)  # 8: above left
            ])
        for row_offset, col_offset in matrix_offsets:
            new_row = self.row + row_offset
            new_col = self.col + col_offset
            # omit if row is outside of tile matrix
            if new_row < 0 or new_row >= self.tp.matrix_height(self.zoom):
                continue
            # wrap around antimeridian if new column is outside of tile matrix
            if new_col < 0:
                if not self.tp.is_global:
                    continue
                new_col = self.tp.matrix_width(self.zoom) + new_col
            elif new_col >= self.tp.matrix_width(self.zoom):
                if not self.tp.is_global:
                    continue
                new_col -= self.tp.matrix_width(self.zoom)
            # omit if new tile is current tile
            if new_row == self.row and new_col == self.col:
                continue
            # create new tile
            unique_neighbors[(new_row, new_col)] = self.tp.tile(
                self.zoom, new_row, new_col
            )
        return unique_neighbors.values()