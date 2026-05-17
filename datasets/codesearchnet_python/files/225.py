def fMeasure(self, label, beta=None):
        """
        Returns f-measure.
        """
        if beta is None:
            return self.call("fMeasure", label)
        else:
            return self.call("fMeasure", label, beta)