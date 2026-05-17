def samples_by_indices(self, indices):
    """Gather a batch of samples by indices, applying any index
        mapping defined by the underlying data sources.

        Parameters
        ----------
        indices: 1D-array of ints or slice
            An index array or a slice that selects the samples to retrieve

        Returns
        -------
        nested list of arrays
            A mini-batch"""

    # Assuming that self.data is a list of samples
    if isinstance(indices, slice):
        return self.data[indices]
    elif isinstance(indices, list):
        return [self.data[i] for i in indices]
    else:
        raise ValueError("indices must be a list or a slice")