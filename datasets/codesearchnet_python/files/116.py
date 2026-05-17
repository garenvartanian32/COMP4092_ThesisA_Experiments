def meanApprox(self, timeout, confidence=0.95):
        """
        .. note:: Experimental

        Approximate operation to return the mean within a timeout
        or meet the confidence.

        >>> rdd = sc.parallelize(range(1000), 10)
        >>> r = sum(range(1000)) / 1000.0
        >>> abs(rdd.meanApprox(1000) - r) / r < 0.05
        True
        """
        jrdd = self.map(float)._to_java_object_rdd()
        jdrdd = self.ctx._jvm.JavaDoubleRDD.fromRDD(jrdd.rdd())
        r = jdrdd.meanApprox(timeout, confidence).getFinalValue()
        return BoundedFloat(r.mean(), r.confidence(), r.low(), r.high())