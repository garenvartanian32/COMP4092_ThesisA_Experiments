def train(cls, data, iterations=100, step=1.0, miniBatchFraction=1.0,
              initialWeights=None, regParam=0.0, regType=None, intercept=False,
              validateData=True, convergenceTol=0.001):
        """
        Train a linear regression model using Stochastic Gradient
        Descent (SGD). This solves the least squares regression
        formulation

            f(weights) = 1/(2n) ||A weights - y||^2

        which is the mean squared error. Here the data matrix has n rows,
        and the input RDD holds the set of rows of A, each with its
        corresponding right hand side label y.
        See also the documentation for the precise formulation.

        :param data:
          The training data, an RDD of LabeledPoint.
        :param iterations:
          The number of iterations.
          (default: 100)
        :param step:
          The step parameter used in SGD.
          (default: 1.0)
        :param miniBatchFraction:
          Fraction of data to be used for each SGD iteration.
          (default: 1.0)
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
            - "l2" for using L2 regularization
            - None for no regularization (default)
        :param intercept:
          Boolean parameter which indicates the use or not of the
          augmented representation for training data (i.e., whether bias
          features are activated or not).
          (default: False)
        :param validateData:
          Boolean parameter which indicates if the algorithm should
          validate data before training.
          (default: True)
        :param convergenceTol:
          A condition which decides iteration termination.
          (default: 0.001)
        """
        warnings.warn(
            "Deprecated in 2.0.0. Use ml.regression.LinearRegression.", DeprecationWarning)

        def train(rdd, i):
            return callMLlibFunc("trainLinearRegressionModelWithSGD", rdd, int(iterations),
                                 float(step), float(miniBatchFraction), i, float(regParam),
                                 regType, bool(intercept), bool(validateData),
                                 float(convergenceTol))

        return _regression_train_wrapper(train, LinearRegressionModel, data, initialWeights)