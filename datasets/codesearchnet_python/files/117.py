def countApproxDistinct(self, relativeSD=0.05):
        """
        .. note:: Experimental

        Return approximate number of distinct elements in the RDD.

        The algorithm used is based on streamlib's implementation of
        `"HyperLogLog in Practice: Algorithmic Engineering of a State
        of The Art Cardinality Estimation Algorithm", available here
        <https://doi.org/10.1145/2452376.2452456>`_.

        :param relativeSD: Relative accuracy. Smaller values create
                           counters that require more space.
                           It must be greater than 0.000017.

        >>> n = sc.parallelize(range(1000)).map(str).countApproxDistinct()
        >>> 900 < n < 1100
        True
        >>> n = sc.parallelize([i % 20 for i in range(1000)]).countApproxDistinct()
        >>> 16 < n < 24
        True
        """
        if relativeSD < 0.000017:
            raise ValueError("relativeSD should be greater than 0.000017")
        # the hash space in Java is 2^32
        hashRDD = self.map(lambda x: portable_hash(x) & 0xFFFFFFFF)
        return hashRDD._to_java_object_rdd().countApproxDistinct(relativeSD)