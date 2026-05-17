def randomSplit(self, weights, seed=None):
        """Randomly splits this :class:`DataFrame` with the provided weights.

        :param weights: list of doubles as weights with which to split the DataFrame. Weights will
            be normalized if they don't sum up to 1.0.
        :param seed: The seed for sampling.

        >>> splits = df4.randomSplit([1.0, 2.0], 24)
        >>> splits[0].count()
        2

        >>> splits[1].count()
        2
        """
        for w in weights:
            if w < 0.0:
                raise ValueError("Weights must be positive. Found weight value: %s" % w)
        seed = seed if seed is not None else random.randint(0, sys.maxsize)
        rdd_array = self._jdf.randomSplit(_to_list(self.sql_ctx._sc, weights), long(seed))
        return [DataFrame(rdd, self.sql_ctx) for rdd in rdd_array]