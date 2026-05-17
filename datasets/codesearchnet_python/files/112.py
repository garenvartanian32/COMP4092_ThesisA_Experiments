def lookup(self, key):
        """
        Return the list of values in the RDD for key `key`. This operation
        is done efficiently if the RDD has a known partitioner by only
        searching the partition that the key maps to.

        >>> l = range(1000)
        >>> rdd = sc.parallelize(zip(l, l), 10)
        >>> rdd.lookup(42)  # slow
        [42]
        >>> sorted = rdd.sortByKey()
        >>> sorted.lookup(42)  # fast
        [42]
        >>> sorted.lookup(1024)
        []
        >>> rdd2 = sc.parallelize([(('a', 'b'), 'c')]).groupByKey()
        >>> list(rdd2.lookup(('a', 'b'))[0])
        ['c']
        """
        values = self.filter(lambda kv: kv[0] == key).values()

        if self.partitioner is not None:
            return self.ctx.runJob(values, lambda x: x, [self.partitioner(key)])

        return values.collect()