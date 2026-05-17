def slice(self, begin, end):
        """
        Return all the RDDs between 'begin' to 'end' (both included)

        `begin`, `end` could be datetime.datetime() or unix_timestamp
        """
        jrdds = self._jdstream.slice(self._jtime(begin), self._jtime(end))
        return [RDD(jrdd, self._sc, self._jrdd_deserializer) for jrdd in jrdds]