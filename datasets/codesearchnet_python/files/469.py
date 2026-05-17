def dot(self, other):
        """
        Dot product with a SparseVector or 1- or 2-dimensional Numpy array.

        >>> a = SparseVector(4, [1, 3], [3.0, 4.0])
        >>> a.dot(a)
        25.0
        >>> a.dot(array.array('d', [1., 2., 3., 4.]))
        22.0
        >>> b = SparseVector(4, [2], [1.0])
        >>> a.dot(b)
        0.0
        >>> a.dot(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]))
        array([ 22.,  22.])
        >>> a.dot([1., 2., 3.])
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> a.dot(np.array([1., 2.]))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> a.dot(DenseVector([1., 2.]))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        >>> a.dot(np.zeros((3, 2)))
        Traceback (most recent call last):
            ...
        AssertionError: dimension mismatch
        """

        if isinstance(other, np.ndarray):
            if other.ndim not in [2, 1]:
                raise ValueError("Cannot call dot with %d-dimensional array" % other.ndim)
            assert len(self) == other.shape[0], "dimension mismatch"
            return np.dot(self.values, other[self.indices])

        assert len(self) == _vector_size(other), "dimension mismatch"

        if isinstance(other, DenseVector):
            return np.dot(other.array[self.indices], self.values)

        elif isinstance(other, SparseVector):
            # Find out common indices.
            self_cmind = np.in1d(self.indices, other.indices, assume_unique=True)
            self_values = self.values[self_cmind]
            if self_values.size == 0:
                return 0.0
            else:
                other_cmind = np.in1d(other.indices, self.indices, assume_unique=True)
                return np.dot(self_values, other.values[other_cmind])

        else:
            return self.dot(_convert_to_vector(other))