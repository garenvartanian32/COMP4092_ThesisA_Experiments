def binify(data, bins):
    if bins is None:
        raise ValueError('Must specify "bins"')
    if isinstance(data, pd.DataFrame):
        binned = data.apply(lambda x: pd.Series(np.histogram(x, bins=bins,
                                                             range=(0, 1))[0]))
    elif isinstance(data, pd.Series):
        binned = pd.Series(np.histogram(data, bins=bins, range=(0, 1))[0])
    else:
        raise ValueError('`data` must be either a 1d vector or 2d matrix')
    binned.index = bin_range_strings(bins)
    # Normalize so each column sums to 1
    binned = binned / binned.sum().astype(float)
    return binned