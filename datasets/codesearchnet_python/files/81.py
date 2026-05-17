def min(self, key=None):
        """
        Find the minimum item in this RDD.

        :param key: A function used to generate key for comparing

        >>> rdd = sc.parallelize([2.0, 5.0, 43.0, 10.0])
        >>> rdd.min()
        2.0
        >>> rdd.min(key=str)
        10.0
        """
        if key is None:
            return self.reduce(min)
        return self.reduce(lambda a, b: min(a, b, key=key))