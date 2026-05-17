def orc(self, path):
        """Loads ORC files, returning the result as a :class:`DataFrame`.

        >>> df = spark.read.orc('python/test_support/sql/orc_partitioned')
        >>> df.dtypes
        [('a', 'bigint'), ('b', 'int'), ('c', 'int')]
        """
        if isinstance(path, basestring):
            path = [path]
        return self._df(self._jreader.orc(_to_seq(self._spark._sc, path)))