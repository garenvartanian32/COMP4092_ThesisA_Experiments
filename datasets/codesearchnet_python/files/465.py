def parse(s):
        """
        Parse string representation back into the DenseVector.

        >>> DenseVector.parse(' [ 0.0,1.0,2.0,  3.0]')
        DenseVector([0.0, 1.0, 2.0, 3.0])
        """
        start = s.find('[')
        if start == -1:
            raise ValueError("Array should start with '['.")
        end = s.find(']')
        if end == -1:
            raise ValueError("Array should end with ']'.")
        s = s[start + 1: end]

        try:
            values = [float(val) for val in s.split(',') if val]
        except ValueError:
            raise ValueError("Unable to parse values from %s" % s)
        return DenseVector(values)