def f1Measure(self, label=None):
        """
        Returns f1Measure or f1Measure for a given label (category) if specified.
        """
        if label is None:
            return self.call("f1Measure")
        else:
            return self.call("f1Measure", float(label))