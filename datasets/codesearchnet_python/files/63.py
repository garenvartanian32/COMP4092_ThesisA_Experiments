def _computeFractionForSampleSize(sampleSizeLowerBound, total, withReplacement):
        """
        Returns a sampling rate that guarantees a sample of
        size >= sampleSizeLowerBound 99.99% of the time.

        How the sampling rate is determined:
        Let p = num / total, where num is the sample size and total is the
        total number of data points in the RDD. We're trying to compute
        q > p such that
          - when sampling with replacement, we're drawing each data point
            with prob_i ~ Pois(q), where we want to guarantee
            Pr[s < num] < 0.0001 for s = sum(prob_i for i from 0 to
            total), i.e. the failure rate of not having a sufficiently large
            sample < 0.0001. Setting q = p + 5 * sqrt(p/total) is sufficient
            to guarantee 0.9999 success rate for num > 12, but we need a
            slightly larger q (9 empirically determined).
          - when sampling without replacement, we're drawing each data point
            with prob_i ~ Binomial(total, fraction) and our choice of q
            guarantees 1-delta, or 0.9999 success rate, where success rate is
            defined the same as in sampling with replacement.
        """
        fraction = float(sampleSizeLowerBound) / total
        if withReplacement:
            numStDev = 5
            if (sampleSizeLowerBound < 12):
                numStDev = 9
            return fraction + numStDev * sqrt(fraction / total)
        else:
            delta = 0.00005
            gamma = - log(delta) / total
            return min(1, fraction + gamma + sqrt(gamma * gamma + 2 * gamma * fraction))