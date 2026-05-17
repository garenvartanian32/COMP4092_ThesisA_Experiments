def load(cls, sc, path):
        """Load the LDAModel from disk.

        :param sc:
          SparkContext.
        :param path:
          Path to where the model is stored.
        """
        if not isinstance(sc, SparkContext):
            raise TypeError("sc should be a SparkContext, got type %s" % type(sc))
        if not isinstance(path, basestring):
            raise TypeError("path should be a basestring, got type %s" % type(path))
        model = callMLlibFunc("loadLDAModel", sc, path)
        return LDAModel(model)