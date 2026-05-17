def trainClassifier(cls, data, numClasses, categoricalFeaturesInfo, numTrees,
                        featureSubsetStrategy="auto", impurity="gini", maxDepth=4, maxBins=32,
                        seed=None):
        """
        Train a random forest model for binary or multiclass
        classification.

        :param data:
          Training dataset: RDD of LabeledPoint. Labels should take values
          {0, 1, ..., numClasses-1}.
        :param numClasses:
          Number of classes for classification.
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
          if numTrees > 1 (forest) set to "sqrt".
          (default: "auto")
        :param impurity:
          Criterion used for information gain calculation.
          Supported values: "gini" or "entropy".
          (default: "gini")
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
        >>>
        >>> data = [
        ...     LabeledPoint(0.0, [0.0]),
        ...     LabeledPoint(0.0, [1.0]),
        ...     LabeledPoint(1.0, [2.0]),
        ...     LabeledPoint(1.0, [3.0])
        ... ]
        >>> model = RandomForest.trainClassifier(sc.parallelize(data), 2, {}, 3, seed=42)
        >>> model.numTrees()
        3
        >>> model.totalNumNodes()
        7
        >>> print(model)
        TreeEnsembleModel classifier with 3 trees
        <BLANKLINE>
        >>> print(model.toDebugString())
        TreeEnsembleModel classifier with 3 trees
        <BLANKLINE>
          Tree 0:
            Predict: 1.0
          Tree 1:
            If (feature 0 <= 1.5)
             Predict: 0.0
            Else (feature 0 > 1.5)
             Predict: 1.0
          Tree 2:
            If (feature 0 <= 1.5)
             Predict: 0.0
            Else (feature 0 > 1.5)
             Predict: 1.0
        <BLANKLINE>
        >>> model.predict([2.0])
        1.0
        >>> model.predict([0.0])
        0.0
        >>> rdd = sc.parallelize([[3.0], [1.0]])
        >>> model.predict(rdd).collect()
        [1.0, 0.0]
        """
        return cls._train(data, "classification", numClasses,
                          categoricalFeaturesInfo, numTrees, featureSubsetStrategy, impurity,
                          maxDepth, maxBins, seed)