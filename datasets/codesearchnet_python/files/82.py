def sum(self):
        """
        Add up the elements in this RDD.

        >>> sc.parallelize([1.0, 2.0, 3.0]).sum()
        6.0
        """
        return self.mapPartitions(lambda x: [sum(x)]).fold(0, operator.add)