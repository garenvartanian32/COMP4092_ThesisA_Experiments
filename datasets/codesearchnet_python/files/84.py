def histogram(self, buckets):
        """
        Compute a histogram using the provided buckets. The buckets
        are all open to the right except for the last which is closed.
        e.g. [1,10,20,50] means the buckets are [1,10) [10,20) [20,50],
        which means 1<=x<10, 10<=x<20, 20<=x<=50. And on the input of 1
        and 50 we would have a histogram of 1,0,1.

        If your histogram is evenly spaced (e.g. [0, 10, 20, 30]),
        this can be switched from an O(log n) inseration to O(1) per
        element (where n is the number of buckets).

        Buckets must be sorted, not contain any duplicates, and have
        at least two elements.

        If `buckets` is a number, it will generate buckets which are
        evenly spaced between the minimum and maximum of the RDD. For
        example, if the min value is 0 and the max is 100, given `buckets`
        as 2, the resulting buckets will be [0,50) [50,100]. `buckets` must
        be at least 1. An exception is raised if the RDD contains infinity.
        If the elements in the RDD do not vary (max == min), a single bucket
        will be used.

        The return value is a tuple of buckets and histogram.

        >>> rdd = sc.parallelize(range(51))
        >>> rdd.histogram(2)
        ([0, 25, 50], [25, 26])
        >>> rdd.histogram([0, 5, 25, 50])
        ([0, 5, 25, 50], [5, 20, 26])
        >>> rdd.histogram([0, 15, 30, 45, 60])  # evenly spaced buckets
        ([0, 15, 30, 45, 60], [15, 15, 15, 6])
        >>> rdd = sc.parallelize(["ab", "ac", "b", "bd", "ef"])
        >>> rdd.histogram(("a", "b", "c"))
        (('a', 'b', 'c'), [2, 2])
        """

        if isinstance(buckets, int):
            if buckets < 1:
                raise ValueError("number of buckets must be >= 1")

            # filter out non-comparable elements
            def comparable(x):
                if x is None:
                    return False
                if type(x) is float and isnan(x):
                    return False
                return True

            filtered = self.filter(comparable)

            # faster than stats()
            def minmax(a, b):
                return min(a[0], b[0]), max(a[1], b[1])
            try:
                minv, maxv = filtered.map(lambda x: (x, x)).reduce(minmax)
            except TypeError as e:
                if " empty " in str(e):
                    raise ValueError("can not generate buckets from empty RDD")
                raise

            if minv == maxv or buckets == 1:
                return [minv, maxv], [filtered.count()]

            try:
                inc = (maxv - minv) / buckets
            except TypeError:
                raise TypeError("Can not generate buckets with non-number in RDD")

            if isinf(inc):
                raise ValueError("Can not generate buckets with infinite value")

            # keep them as integer if possible
            inc = int(inc)
            if inc * buckets != maxv - minv:
                inc = (maxv - minv) * 1.0 / buckets

            buckets = [i * inc + minv for i in range(buckets)]
            buckets.append(maxv)  # fix accumulated error
            even = True

        elif isinstance(buckets, (list, tuple)):
            if len(buckets) < 2:
                raise ValueError("buckets should have more than one value")

            if any(i is None or isinstance(i, float) and isnan(i) for i in buckets):
                raise ValueError("can not have None or NaN in buckets")

            if sorted(buckets) != list(buckets):
                raise ValueError("buckets should be sorted")

            if len(set(buckets)) != len(buckets):
                raise ValueError("buckets should not contain duplicated values")

            minv = buckets[0]
            maxv = buckets[-1]
            even = False
            inc = None
            try:
                steps = [buckets[i + 1] - buckets[i] for i in range(len(buckets) - 1)]
            except TypeError:
                pass  # objects in buckets do not support '-'
            else:
                if max(steps) - min(steps) < 1e-10:  # handle precision errors
                    even = True
                    inc = (maxv - minv) / (len(buckets) - 1)

        else:
            raise TypeError("buckets should be a list or tuple or number(int or long)")

        def histogram(iterator):
            counters = [0] * len(buckets)
            for i in iterator:
                if i is None or (type(i) is float and isnan(i)) or i > maxv or i < minv:
                    continue
                t = (int((i - minv) / inc) if even
                     else bisect.bisect_right(buckets, i) - 1)
                counters[t] += 1
            # add last two together
            last = counters.pop()
            counters[-1] += last
            return [counters]

        def mergeCounters(a, b):
            return [i + j for i, j in zip(a, b)]

        return buckets, self.mapPartitions(histogram).reduce(mergeCounters)