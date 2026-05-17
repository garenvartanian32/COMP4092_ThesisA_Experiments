def trainRegressor(cls, data, categoricalFeaturesInfo, numTrees, featureSubsetStrategy="auto",
                       impurity="variance", maxDepth=4, maxBins=32, seed=None):
        """
        Train a random forest model for regression.

        :param data:
          Training dataset: RDD of LabeledPoint. Labels are real numbers.
        :param categoricalFeaturesInfo:
          Map storing arity of categorical features. An entry (n -> k)
          indicates that feature n is categorical with k categories
          indexed from 0: {0, 1, ..., k-1}.
        :param numTrees:
          Number of trees in the random forest.
        :param featureSubsetStrategy:
          Number of features to consider for splits at each node.
          Supported values: "auto", "all", "sqrt", "log2", "onethird".
          If "auto" is set, this parameter is set based on numTrees:
          if numTrees == 1, set to "all";
          if numTrees > 1 (forest) set to "onethird" for regression.
          (default: "auto")
        :param impurity:
          Criterion used for information gain calculation.
          The only supported value for regression is "variance".
          (default: "variance")
        :param maxDepth:
          Maximum depth of tree (e.g. depth 0 means 1 leaf node, depth 1
          means 1 internal node + 2 leaf nodes).
          (default: 4)
        :param maxBins:
          Maximum number of bins used for splitting features.
          (default: 32)
        :param seed:
          Random seed for bootstrapping and choosing feature subsets.
          Set as None to generate seed based on system time.
          (default: None)
        :return:
          RandomForestModel that can be used for prediction.

        Example usage:

        >>> from pyspark.mllib.regression import LabeledPoint
        >>> from pyspark.mllib.tree import RandomForest
        >>> from pyspark.mllib.linalg import SparseVector
        >>>
        >>> sparse_data = [
        ...     LabeledPoint(0.0, SparseVector(2, {0: 1.0})),
        ...     LabeledPoint(1.0, SparseVector(2, {1: 1.0})),
        ...     LabeledPoint(0.0, SparseVector(2, {0: 1.0})),
        ...     LabeledPoint(1.0, SparseVector(2, {1: 2.0}))
        ... ]
        >>>
        >>> model = RandomForest.trainRegressor(sc.parallelize(sparse_data), {}, 2, seed=42)
        >>> model.numTrees()
        2
        >>> model.totalNumNodes()
        4
        >>> model.predict(SparseVector(2, {1: 1.0}))
        1.0
        >>> model.predict(SparseVector(2, {0: 1.0}))
        0.5
        >>> rdd = sc.parallelize([[0.0, 1.0], [1.0, 0.0]])
        >>> model.predict(rdd).collect()
        [1.0, 0.5]
        """
        return cls._train(data, "regression", 0, categoricalFeaturesInfo, numTrees,
                          featureSubsetStrategy, impurity, maxDepth, maxBins, seed)