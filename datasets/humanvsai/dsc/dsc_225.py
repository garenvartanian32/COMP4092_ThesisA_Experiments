import h5py

def create_dataset(group, dataset_name):
    """Create an empty dataset in a group."""
    group.create_dataset(dataset_name, shape=(0,), maxshape=(None,), dtype='f')