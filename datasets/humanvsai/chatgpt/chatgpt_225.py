import h5py

def create_empty_dataset(group_name, dataset_name, shape, dtype):
    with h5py.File('file.h5', 'a') as f:
        group = f[group_name]
        dataset = group.create_dataset(dataset_name, shape=shape, dtype=dtype)
