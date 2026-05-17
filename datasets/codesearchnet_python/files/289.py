def asDict(self, sample=False):
        """Returns the :class:`StatCounter` members as a ``dict``.

        >>> sc.parallelize([1., 2., 3., 4.]).stats().asDict()
        {'count': 4L,
         'max': 4.0,
         'mean': 2.5,
         'min': 1.0,
         'stdev': 1.2909944487358056,
         'sum': 10.0,
         'variance': 1.6666666666666667}
        """
        return {
            'count': self.count(),
            'mean': self.mean(),
            'sum': self.sum(),
            'min': self.min(),
            'max': self.max(),
            'stdev': self.stdev() if sample else self.sampleStdev(),
            'variance': self.variance() if sample else self.sampleVariance()
        }