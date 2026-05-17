def cartesian(self, other):
        """
        Return the Cartesian product of this RDD and another one, that is, the
        RDD of all pairs of elements C{(a, b)} where C{a} is in C{self} and
        C{b} is in C{other}.

        >>> rdd = sc.parallelize([1, 2])
        >>> sorted(rdd.cartesian(rdd).collect())
        [(1, 1), (1, 2), (2, 1), (2, 2)]
        """
        # Due to batching, we can't use the Java cartesian method.
        deserializer = CartesianDeserializer(self._jrdd_deserializer,
                                             other._jrdd_deserializer)
        return RDD(self._jrdd.cartesian(other._jrdd), self.ctx, deserializer)