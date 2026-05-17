def from_arrays_of_labels(cls, arrayOfLabels, inputCols, outputCols=None,
                              handleInvalid=None):
        """
        Construct the model directly from an array of array of label strings,
        requires an active SparkContext.
        """
        sc = SparkContext._active_spark_context
        java_class = sc._gateway.jvm.java.lang.String
        jlabels = StringIndexerModel._new_java_array(arrayOfLabels, java_class)
        model = StringIndexerModel._create_from_java_class(
            "org.apache.spark.ml.feature.StringIndexerModel", jlabels)
        model.setInputCols(inputCols)
        if outputCols is not None:
            model.setOutputCols(outputCols)
        if handleInvalid is not None:
            model.setHandleInvalid(handleInvalid)
        return model