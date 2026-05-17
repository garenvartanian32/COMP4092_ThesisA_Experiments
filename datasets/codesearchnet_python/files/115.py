def sumApprox(self, timeout, confidence=0.95):
        """
        .. note:: Experimental

        Approximate operation to return the sum within a timeout
        or meet the confidence.

        >>> rdd = sc.parallelize(range(1000), 10)
        >>> r = sum(range(1000))
        >>> abs(rdd.sumApprox(1000) - r) / r < 0.05
        True
        """
        jrdd = self.mapPartitions(lambda it: [float(sum(it))])._to_java_object_rdd()
        jdrdd = self.ctx._jvm.JavaDoubleRDD.fromRDD(jrdd.rdd())
        r = jdrdd.sumApprox(timeout, confidence).getFinalValue()
        return BoundedFloat(r.mean(), r.confidence(), r.low(), r.high())