def trainClassifier(cls, data, categoricalFeaturesInfo,
                        loss="logLoss", numIterations=100, learningRate=0.1, maxDepth=3,
                        maxBins=32):
        """
        Train a gradient-boosted trees model for classification.

        :param data:
          Training dataset: RDD of LabeledPoint. Labels should take values
          {0, 1}.
        :param categoricalFeaturesInfo:
          Map storing arity of categorical features. An entry (n -> k)
          indicates that feature n is categorical with k categories
          indexed from 0: {0, 1, ..., k-1}.
        :param loss:
          Loss function used for minimization during gradient boosting.
          Supported values: "logLoss", "leastSquaresError",
          "leastAbsoluteError".
          (default: "logLoss")
        :param numIterations:
          Number of iterations of boosting.
          (default: 100)
        :param learningRate:
          Learning rate for shrinking the contribution of each estimator.
          The learning rate should be between in the interval (0, 1].
          (default: 0.1)
        :param maxDepth:
          Maximum depth of tree (e.g. depth 0 means 1 leaf node, depth 1
          means 1 internal node + 2 leaf nodes).
          (default: 3)
        :param maxBins:
          Maximum number of bins used for splitting features. DecisionTree
          requires maxBins >= max categories.
          (default: 32)
        :return:
          GradientBoostedTreesModel that can be used for prediction.

        Example usage:

        >>> from pyspark.mllib.regression import LabeledPoint
        >>> from pyspark.mllib.tree import GradientBoostedTrees
        >>>
        >>> data = [
        ...     LabeledPoint(0.0, [0.0]),
        ...     LabeledPoint(0.0, [1.0]),
        ...     LabeledPoint(1.0, [2.0]),
        ...     LabeledPoint(1.0, [3.0])
        ... ]
        >>>
        >>> model = GradientBoostedTrees.trainClassifier(sc.parallelize(data), {}, numIterations=10)
        >>> model.numTrees()
        10
        >>> model.totalNumNodes()
        30
        >>> print(model)  # it already has newline
        TreeEnsembleModel classifier with 10 trees
        <BLANKLINE>
        >>> model.predict([2.0])
        1.0
        >>> model.predict([0.0])
        0.0
        >>> rdd = sc.parallelize([[2.0], [0.0]])
        >>> model.predict(rdd).collect()
        [1.0, 0.0]
        """
        return cls._train(data, "classification", categoricalFeaturesInfo,
                          loss, numIterations, learningRate, maxDepth, maxBins)