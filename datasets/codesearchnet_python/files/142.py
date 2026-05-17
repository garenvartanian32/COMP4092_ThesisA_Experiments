def trainClassifier(cls, data, numClasses, categoricalFeaturesInfo,
                        impurity="gini", maxDepth=5, maxBins=32, minInstancesPerNode=1,
                        minInfoGain=0.0):
        """
        Train a decision tree model for classification.

        :param data:
          Training data: RDD of LabeledPoint. Labels should take values
          {0, 1, ..., numClasses-1}.
        :param numClasses:
          Number of classes for classification.
        :param categoricalFeaturesInfo:
          Map storing arity of categorical features. An entry (n -> k)
          indicates that feature n is categorical with k categories
          indexed from 0: {0, 1, ..., k-1}.
        :param impurity:
          Criterion used for information gain calculation.
          Supported values: "gini" or "entropy".
          (default: "gini")
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

        >>> from numpy import array
        >>> from pyspark.mllib.regression import LabeledPoint
        >>> from pyspark.mllib.tree import DecisionTree
        >>>
        >>> data = [
        ...     LabeledPoint(0.0, [0.0]),
        ...     LabeledPoint(1.0, [1.0]),
        ...     LabeledPoint(1.0, [2.0]),
        ...     LabeledPoint(1.0, [3.0])
        ... ]
        >>> model = DecisionTree.trainClassifier(sc.parallelize(data), 2, {})
        >>> print(model)
        DecisionTreeModel classifier of depth 1 with 3 nodes

        >>> print(model.toDebugString())
        DecisionTreeModel classifier of depth 1 with 3 nodes
          If (feature 0 <= 0.5)
           Predict: 0.0
          Else (feature 0 > 0.5)
           Predict: 1.0
        <BLANKLINE>
        >>> model.predict(array([1.0]))
        1.0
        >>> model.predict(array([0.0]))
        0.0
        >>> rdd = sc.parallelize([[1.0], [0.0]])
        >>> model.predict(rdd).collect()
        [1.0, 0.0]
        """
        return cls._train(data, "classification", numClasses, categoricalFeaturesInfo,
                          impurity, maxDepth, maxBins, minInstancesPerNode, minInfoGain)