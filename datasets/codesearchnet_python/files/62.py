def takeSample(self, withReplacement, num, seed=None):
        """
        Return a fixed-size sampled subset of this RDD.

        .. note:: This method should only be used if the resulting array is expected
            to be small, as all the data is loaded into the driver's memory.

        >>> rdd = sc.parallelize(range(0, 10))
        >>> len(rdd.takeSample(True, 20, 1))
        20
        >>> len(rdd.takeSample(False, 5, 2))
        5
        >>> len(rdd.takeSample(False, 15, 3))
        10
        """
        numStDev = 10.0

        if num < 0:
            raise ValueError("Sample size cannot be negative.")
        elif num == 0:
            return []

        initialCount = self.count()
        if initialCount == 0:
            return []

        rand = random.Random(seed)

        if (not withReplacement) and num >= initialCount:
            # shuffle current RDD and return
            samples = self.collect()
            rand.shuffle(samples)
            return samples

        maxSampleSize = sys.maxsize - int(numStDev * sqrt(sys.maxsize))
        if num > maxSampleSize:
            raise ValueError(
                "Sample size cannot be greater than %d." % maxSampleSize)

        fraction = RDD._computeFractionForSampleSize(
            num, initialCount, withReplacement)
        samples = self.sample(withReplacement, fraction, seed).collect()

        # If the first sample didn't turn out large enough, keep trying to take samples;
        # this shouldn't happen often because we use a big multiplier for their initial size.
        # See: scala/spark/RDD.scala
        while len(samples) < num:
            # TODO: add log warning for when more than one iteration was run
            seed = rand.randint(0, sys.maxsize)
            samples = self.sample(withReplacement, fraction, seed).collect()

        rand.shuffle(samples)

        return samples[0:num]