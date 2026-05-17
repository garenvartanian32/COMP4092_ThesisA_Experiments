def sampleByKey(self, withReplacement, fractions, seed=None):
        """
        Return a subset of this RDD sampled by key (via stratified sampling).
        Create a sample of this RDD using variable sampling rates for
        different keys as specified by fractions, a key to sampling rate map.

        >>> fractions = {"a": 0.2, "b": 0.1}
        >>> rdd = sc.parallelize(fractions.keys()).cartesian(sc.parallelize(range(0, 1000)))
        >>> sample = dict(rdd.sampleByKey(False, fractions, 2).groupByKey().collect())
        >>> 100 < len(sample["a"]) < 300 and 50 < len(sample["b"]) < 150
        True
        >>> max(sample["a"]) <= 999 and min(sample["a"]) >= 0
        True
        >>> max(sample["b"]) <= 999 and min(sample["b"]) >= 0
        True
        """
        for fraction in fractions.values():
            assert fraction >= 0.0, "Negative fraction value: %s" % fraction
        return self.mapPartitionsWithIndex(
            RDDStratifiedSampler(withReplacement, fractions, seed).func, True)