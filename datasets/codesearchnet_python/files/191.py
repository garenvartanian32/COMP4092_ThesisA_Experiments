def call(self, name, *a):
        """Call method of java_model"""
        return callJavaFunc(self._sc, getattr(self._java_model, name), *a)