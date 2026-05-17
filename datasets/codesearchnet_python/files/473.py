def dense(*elements):
        """
        Create a dense vector of 64-bit floats from a Python list or numbers.

        >>> Vectors.dense([1, 2, 3])
        DenseVector([1.0, 2.0, 3.0])
        >>> Vectors.dense(1.0, 2.0)
        DenseVector([1.0, 2.0])
        """
        if len(elements) == 1 and not isinstance(elements[0], (float, int, long)):
            # it's list, numpy.array or other iterable object.
            elements = elements[0]
        return DenseVector(elements)