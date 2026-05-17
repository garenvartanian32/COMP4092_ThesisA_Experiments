def save(self, sc, path):
        """Save an IsotonicRegressionModel."""
        java_boundaries = _py2java(sc, self.boundaries.tolist())
        java_predictions = _py2java(sc, self.predictions.tolist())
        java_model = sc._jvm.org.apache.spark.mllib.regression.IsotonicRegressionModel(
            java_boundaries, java_predictions, self.isotonic)
        java_model.save(sc._jsc.sc(), path)