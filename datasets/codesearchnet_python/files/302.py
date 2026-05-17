def load(cls, sc, path):
        """
        Load a model from the given path.
        """
        java_model = sc._jvm.org.apache.spark.mllib.classification.SVMModel.load(
            sc._jsc.sc(), path)
        weights = _java2py(sc, java_model.weights())
        intercept = java_model.intercept()
        threshold = java_model.getThreshold().get()
        model = SVMModel(weights, intercept)
        model.setThreshold(threshold)
        return model