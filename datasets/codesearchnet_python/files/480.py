def toSparse(self):
        """Convert to SparseMatrix"""
        if self.isTransposed:
            values = np.ravel(self.toArray(), order='F')
        else:
            values = self.values
        indices = np.nonzero(values)[0]
        colCounts = np.bincount(indices // self.numRows)
        colPtrs = np.cumsum(np.hstack(
            (0, colCounts, np.zeros(self.numCols - colCounts.size))))
        values = values[indices]
        rowIndices = indices % self.numRows

        return SparseMatrix(self.numRows, self.numCols, colPtrs, rowIndices, values)