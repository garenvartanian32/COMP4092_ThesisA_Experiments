def sample(self, withReplacement, fraction, seed=None):
        """
        Return a sampled subset of this RDD.

        :param withReplacement: can elements be sampled multiple times (replaced when sampled out)
        :param fraction: expected size of the sample as a fraction of this RDD's size
            without replacement: probability that each element is chosen; fraction must be [0, 1]
            with replacement: expected number of times each element is chosen; fraction must be >= 0
        :param seed: seed for the random number generator

        .. note:: This is not guaranteed to provide exactly the fraction specified of the total
            count of the given :class:`DataFrame`.

        >>> rdd = sc.parallelize(range(100), 4)
        >>> 6 <= rdd.sample(False, 0.1, 81).count() <= 14
        True
        """
        assert fraction >= 0.0, "Negative fraction value: %s" % fraction
        return self.mapPartitionsWithIndex(RDDSampler(withReplacement, fraction, seed).func, True)