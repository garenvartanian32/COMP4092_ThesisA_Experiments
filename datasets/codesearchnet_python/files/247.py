def coalesce(self, numPartitions):
        """
        Returns a new :class:`DataFrame` that has exactly `numPartitions` partitions.

        :param numPartitions: int, to specify the target number of partitions

        Similar to coalesce defined on an :class:`RDD`, this operation results in a
        narrow dependency, e.g. if you go from 1000 partitions to 100 partitions,
        there will not be a shuffle, instead each of the 100 new partitions will
        claim 10 of the current partitions. If a larger number of partitions is requested,
        it will stay at the current number of partitions.

        However, if you're doing a drastic coalesce, e.g. to numPartitions = 1,
        this may result in your computation taking place on fewer nodes than
        you like (e.g. one node in the case of numPartitions = 1). To avoid this,
        you can call repartition(). This will add a shuffle step, but means the
        current upstream partitions will be executed in parallel (per whatever
        the current partitioning is).

        >>> df.coalesce(1).rdd.getNumPartitions()
        1
        """
        return DataFrame(self._jdf.coalesce(numPartitions), self.sql_ctx)