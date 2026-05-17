def max(self, key=None):
        """
        Find the maximum item in this RDD.

        :param key: A function used to generate key for comparing

        >>> rdd = sc.parallelize([1.0, 5.0, 43.0, 10.0])
        >>> rdd.max()
        43.0
        >>> rdd.max(key=str)
        5.0
        """
        if key is None:
            return self.reduce(max)
        return self.reduce(lambda a, b: max(a, b, key=key))