def recall(self, label=None):
        """
        Returns recall or recall for a given label (category) if specified.
        """
        if label is None:
            return self.call("recall")
        else:
            return self.call("recall", float(label))