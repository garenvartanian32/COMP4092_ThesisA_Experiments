def parse(s):
        """Parse a string representation back into the Vector.

        >>> Vectors.parse('[2,1,2 ]')
        DenseVector([2.0, 1.0, 2.0])
        >>> Vectors.parse(' ( 100,  [0],  [2])')
        SparseVector(100, {0: 2.0})
        """
        if s.find('(') == -1 and s.find('[') != -1:
            return DenseVector.parse(s)
        elif s.find('(') != -1:
            return SparseVector.parse(s)
        else:
            raise ValueError(
                "Cannot find tokens '[' or '(' from the input string.")