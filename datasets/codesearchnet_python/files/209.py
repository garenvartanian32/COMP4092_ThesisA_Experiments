def union(self, other):
        """
        Return a new DStream by unifying data of another DStream with this DStream.

        @param other: Another DStream having the same interval (i.e., slideDuration)
                     as this DStream.
        """
        if self._slideDuration != other._slideDuration:
            raise ValueError("the two DStream should have same slide duration")
        return self.transformWith(lambda a, b: a.union(b), other, True)