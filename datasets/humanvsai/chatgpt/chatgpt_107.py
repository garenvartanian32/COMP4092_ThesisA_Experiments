def concatenate_line_strings(self, other: Union['LineString', np.ndarray, Iterable[Tuple[float, float]]]) -> 'LineString':
        new_coords = []
        if not isinstance(other, np.ndarray):
            other = np.array(other, dtype=np.float32)

        if other.ndim == 1:
            # assume xy mode
            new_coords.append(other)
        else:
            # xymode
            new_coords.extend(other)

        if new_coords:
            # ensure final coordinate of self is equal to first coordinate of other
            if not np.allclose(self.coords[-1], new_coords[0]):
                # the casting here is necessary because LineString assumes np.float64
                # as input data type whereas the data type from our image coordinates
                # is np.float32
                middle_coords = np.tile(self.coords[-1], (len(new_coords), 1)).astype(np.float64)
                new_coords = [middle_coords[0]] + new_coords
            else:
                new_coords = new_coords[1:]

        return LineString(self.coords + new_coords, label=self.label)
