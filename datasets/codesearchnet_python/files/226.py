def precision(self, label=None):
        """
        Returns precision or precision for a given label (category) if specified.
        """
        if label is None:
            return self.call("precision")
        else:
            return self.call("precision", float(label))