def _from_java(cls, java_stage):
        """
        Given a Java TrainValidationSplitModel, create and return a Python wrapper of it.
        Used for ML persistence.
        """

        # Load information from java_stage to the instance.
        bestModel = JavaParams._from_java(java_stage.bestModel())
        estimator, epms, evaluator = super(TrainValidationSplitModel,
                                           cls)._from_java_impl(java_stage)
        # Create a new instance of this stage.
        py_stage = cls(bestModel=bestModel).setEstimator(estimator)
        py_stage = py_stage.setEstimatorParamMaps(epms).setEvaluator(evaluator)

        if java_stage.hasSubModels():
            py_stage.subModels = [JavaParams._from_java(sub_model)
                                  for sub_model in java_stage.subModels()]

        py_stage._resetUid(java_stage.uid())
        return py_stage