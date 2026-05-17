def treeReduce(self, f, depth=2):
        """
        Reduces the elements of this RDD in a multi-level tree pattern.

        :param depth: suggested depth of the tree (default: 2)

        >>> add = lambda x, y: x + y
        >>> rdd = sc.parallelize([-5, -4, -3, -2, -1, 1, 2, 3, 4], 10)
        >>> rdd.treeReduce(add)
        -5
        >>> rdd.treeReduce(add, 1)
        -5
        >>> rdd.treeReduce(add, 2)
        -5
        >>> rdd.treeReduce(add, 5)
        -5
        >>> rdd.treeReduce(add, 10)
        -5
        """
        if depth < 1:
            raise ValueError("Depth cannot be smaller than 1 but got %d." % depth)

        zeroValue = None, True  # Use the second entry to indicate whether this is a dummy value.

        def op(x, y):
            if x[1]:
                return y
            elif y[1]:
                return x
            else:
                return f(x[0], y[0]), False

        reduced = self.map(lambda x: (x, False)).treeAggregate(zeroValue, op, op, depth)
        if reduced[1]:
            raise ValueError("Cannot reduce empty RDD.")
        return reduced[0]