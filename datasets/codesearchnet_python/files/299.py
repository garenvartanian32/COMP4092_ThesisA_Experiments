def train(cls, data, iterations=100, initialWeights=None, regParam=0.0, regType="l2",
              intercept=False, corrections=10, tolerance=1e-6, validateData=True, numClasses=2):
        """
        Train a logistic regression model on the given data.

        :param data:
          The training data, an RDD of LabeledPoint.
        :param iterations:
          The number of iterations.
          (default: 100)
        :param initialWeights:
          The initial weights.
          (default: None)
        :param regParam:
          The regularizer parameter.
          (default: 0.0)
        :param regType:
          The type of regularizer used for training our model.
          Supported values:

            - "l1" for using L1 regularization
            - "l2" for using L2 regularization (default)
            - None for no regularization
        :param intercept:
          Boolean parameter which indicates the use or not of the
          augmented representation for training data (i.e., whether bias
          features are activated or not).
          (default: False)
        :param corrections:
          The number of corrections used in the LBFGS update.
          If a known updater is used for binary classification,
          it calls the ml implementation and this parameter will
          have no effect. (default: 10)
        :param tolerance:
          The convergence tolerance of iterations for L-BFGS.
          (default: 1e-6)
        :param validateData:
          Boolean parameter which indicates if the algorithm should
          validate data before training.
          (default: True)
        :param numClasses:
          The number of classes (i.e., outcomes) a label can take in
          Multinomial Logistic Regression.
          (default: 2)

        >>> data = [
        ...     LabeledPoint(0.0, [0.0, 1.0]),
        ...     LabeledPoint(1.0, [1.0, 0.0]),
        ... ]
        >>> lrm = LogisticRegressionWithLBFGS.train(sc.parallelize(data), iterations=10)
        >>> lrm.predict([1.0, 0.0])
        1
        >>> lrm.predict([0.0, 1.0])
        0
        """
        def train(rdd, i):
            return callMLlibFunc("trainLogisticRegressionModelWithLBFGS", rdd, int(iterations), i,
                                 float(regParam), regType, bool(intercept), int(corrections),
                                 float(tolerance), bool(validateData), int(numClasses))

        if initialWeights is None:
            if numClasses == 2:
                initialWeights = [0.0] * len(data.first().features)
            else:
                if intercept:
                    initialWeights = [0.0] * (len(data.first().features) + 1) * (numClasses - 1)
                else:
                    initialWeights = [0.0] * len(data.first().features) * (numClasses - 1)
        return _regression_train_wrapper(train, LogisticRegressionModel, data, initialWeights)