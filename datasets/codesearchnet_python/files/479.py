def toArray(self):
        """
        Return an numpy.ndarray

        >>> m = DenseMatrix(2, 2, range(4))
        >>> m.toArray()
        array([[ 0.,  2.],
               [ 1.,  3.]])
        """
        if self.isTransposed:
            return np.asfortranarray(
                self.values.reshape((self.numRows, self.numCols)))
        else:
            return self.values.reshape((self.numRows, self.numCols), order='F')