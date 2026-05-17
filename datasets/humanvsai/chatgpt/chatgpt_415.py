def write_data_to_group(group, data, append=False):
    if append:
        group.create_dataset('data', data=data, maxshape=(None,))
    else:
        dset = group.require_dataset('data', shape=data.shape, dtype=data.dtype)
        dset[:] = data