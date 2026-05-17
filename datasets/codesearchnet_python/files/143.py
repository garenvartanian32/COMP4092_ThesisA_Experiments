def trainRegressor(cls, data, categoricalFeaturesInfo,
                       impurity="variance", maxDepth=5, maxBins=32, minInstancesPerNode=1,
                       minInfoGain=0.0):
        """
        Train a decision tree model for regression.

        :param data:
          Training data: RDD of LabeledPoint. Labels are real numbers.
        :param categoricalFeaturesInfo:
          Map storing arity of categorical features. An entry (n -> k)
          indicates that feature n is categorical with k categories
          indexed from 0: {0, 1, ..., k-1}.
        :param impurity:
          Criterion used for information gain calculation.
          The only supported value for regression is "variance".
          (default: "variance")
        :param maxDepth:
          Maximum depth of tree (e.g. depth 0 means 1 leaf node, depth 1
          means 1 internal node + 2 leaf nodes).
          (default: 5)
        :param maxBins:
          Number of bins used for finding splits at each node.
          (default: 32)
        :param minInstancesPerNode:
          Minimum number of instances required at child nodes to create
          the parent split.
          (default: 1)
        :param minInfoGain:
          Minimum info gain required to create a split.
          (default: 0.0)
        :return:
          DecisionTreeModel.

        Example usage:

        >>> from pyspark.mllib.regression import LabeledPoint
        >>> from pyspark.mllib.tree import DecisionTree
        >>> from pyspark.mllib.linalg import SparseVector
        >>>
        >>> sparse_data = [
        ...     LabeledPoint(0.0, SparseVector(2, {0: 0.0})),
        ...     LabeledPoint(1.0, SparseVector(2, {1: 1.0})),
        ...     LabeledPoint(0.0, SparseVector(2, {0: 0.0})),
        ...     LabeledPoint(1.0, SparseVector(2, {1: 2.0}))
        ... ]
        >>>
        >>> model = DecisionTree.trainRegressor(sc.parallelize(sparse_data), {})
        >>> model.predict(SparseVector(2, {1: 1.0}))
        1.0
        >>> model.predict(SparseVector(2, {1: 0.0}))
        0.0
        >>> rdd = sc.parallelize([[0.0, 1.0], [0.0, 0.0]])
        >>> model.predict(rdd).collect()
        [1.0, 0.0]
        """
        return cls._train(data, "regression", 0, categoricalFeaturesInfo,
                          impurity, maxDepth, maxBins, minInstancesPerNode, minInfoGain)