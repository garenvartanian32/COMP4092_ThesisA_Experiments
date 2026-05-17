def gather_samples(indices):
    # assuming data_sources is a list of data sources
    batch = []
    for data_source in data_sources:
        if isinstance(indices, slice):
            samples = data_source[indices]
        else:
            samples = data_source[list(indices)]
        batch.append(samples)
    return batch
