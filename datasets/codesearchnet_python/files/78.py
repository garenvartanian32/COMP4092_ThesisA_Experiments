def aggregate(self, zeroValue, seqOp, combOp):
        """
        Aggregate the elements of each partition, and then the results for all
        the partitions, using a given combine functions and a neutral "zero
        value."

        The functions C{op(t1, t2)} is allowed to modify C{t1} and return it
        as its result value to avoid object allocation; however, it should not
        modify C{t2}.

        The first function (seqOp) can return a different result type, U, than
        the type of this RDD. Thus, we need one operation for merging a T into
        an U and one operation for merging two U

        >>> seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
        >>> combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
        >>> sc.parallelize([1, 2, 3, 4]).aggregate((0, 0), seqOp, combOp)
        (10, 4)
        >>> sc.parallelize([]).aggregate((0, 0), seqOp, combOp)
        (0, 0)
        """
        seqOp = fail_on_stopiteration(seqOp)
        combOp = fail_on_stopiteration(combOp)

        def func(iterator):
            acc = zeroValue
            for obj in iterator:
                acc = seqOp(acc, obj)
            yield acc
        # collecting result of mapPartitions here ensures that the copy of
        # zeroValue provided to each partition is unique from the one provided
        # to the final reduce call
        vals = self.mapPartitions(func).collect()
        return reduce(combOp, vals, zeroValue)