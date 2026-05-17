def predict(self, x):
        """
        Predict labels for provided features.
        Using a piecewise linear function.
        1) If x exactly matches a boundary then associated prediction
        is returned. In case there are multiple predictions with the
        same boundary then one of them is returned. Which one is
        undefined (same as java.util.Arrays.binarySearch).
        2) If x is lower or higher than all boundaries then first or
        last prediction is returned respectively. In case there are
        multiple predictions with the same boundary then the lowest
        or highest is returned respectively.
        3) If x falls between two values in boundary array then
        prediction is treated as piecewise linear function and
        interpolated value is returned. In case there are multiple
        values with the same boundary then the same rules as in 2)
        are used.

        :param x:
          Feature or RDD of Features to be labeled.
        """
        if isinstance(x, RDD):
            return x.map(lambda v: self.predict(v))
        return np.interp(x, self.boundaries, self.predictions)