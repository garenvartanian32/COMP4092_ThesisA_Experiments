def approxNearestNeighbors(self, dataset, key, numNearestNeighbors, distCol="distCol"):
        """
        Given a large dataset and an item, approximately find at most k items which have the
        closest distance to the item. If the :py:attr:`outputCol` is missing, the method will
        transform the data; if the :py:attr:`outputCol` exists, it will use that. This allows
        caching of the transformed data when necessary.

        .. note:: This method is experimental and will likely change behavior in the next release.

        :param dataset: The dataset to search for nearest neighbors of the key.
        :param key: Feature vector representing the item to search for.
        :param numNearestNeighbors: The maximum number of nearest neighbors.
        :param distCol: Output column for storing the distance between each result row and the key.
                        Use "distCol" as default value if it's not specified.
        :return: A dataset containing at most k items closest to the key. A column "distCol" is
                 added to show the distance between each row and the key.
        """
        return self._call_java("approxNearestNeighbors", dataset, key, numNearestNeighbors,
                               distCol)