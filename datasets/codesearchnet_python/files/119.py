def mapPartitions(self, f, preservesPartitioning=False):
        """
        .. note:: Experimental

        Returns a new RDD by applying a function to each partition of the wrapped RDD,
        where tasks are launched together in a barrier stage.
        The interface is the same as :func:`RDD.mapPartitions`.
        Please see the API doc there.

        .. versionadded:: 2.4.0
        """
        def func(s, iterator):
            return f(iterator)
        return PipelinedRDD(self.rdd, func, preservesPartitioning, isFromBarrier=True)