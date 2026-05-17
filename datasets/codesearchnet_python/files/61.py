def randomSplit(self, weights, seed=None):
        """
        Randomly splits this RDD with the provided weights.

        :param weights: weights for splits, will be normalized if they don't sum to 1
        :param seed: random seed
        :return: split RDDs in a list

        >>> rdd = sc.parallelize(range(500), 1)
        >>> rdd1, rdd2 = rdd.randomSplit([2, 3], 17)
        >>> len(rdd1.collect() + rdd2.collect())
        500
        >>> 150 < rdd1.count() < 250
        True
        >>> 250 < rdd2.count() < 350
        True
        """
        s = float(sum(weights))
        cweights = [0.0]
        for w in weights:
            cweights.append(cweights[-1] + w / s)
        if seed is None:
            seed = random.randint(0, 2 ** 32 - 1)
        return [self.mapPartitionsWithIndex(RDDRangeSampler(lb, ub, seed).func, True)
                for lb, ub in zip(cweights, cweights[1:])]