def _to_java(self):
        """
        Transfer this instance to a Java TrainValidationSplitModel. Used for ML persistence.
        :return: Java object equivalent to this instance.
        """

        sc = SparkContext._active_spark_context
        # TODO: persst validation metrics as well
        _java_obj = JavaParams._new_java_obj(
            "org.apache.spark.ml.tuning.TrainValidationSplitModel",
            self.uid,
            self.bestModel._to_java(),
            _py2java(sc, []))
        estimator, epms, evaluator = super(TrainValidationSplitModel, self)._to_java_impl()

        _java_obj.set("evaluator", evaluator)
        _java_obj.set("estimator", estimator)
        _java_obj.set("estimatorParamMaps", epms)

        if self.subModels is not None:
            java_sub_models = [sub_model._to_java() for sub_model in self.subModels]
            _java_obj.setSubModels(java_sub_models)

        return _java_obj