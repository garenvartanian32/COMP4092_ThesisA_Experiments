def range(cls, dataset, dimension):
    if not isinstance(dataset, np.ndarray):
        raise TypeError('Dataset must be a numpy array.')
    if dimension >= dataset.ndim or dimension < 0:
        raise ValueError('Dimension out of range.')
    return np.max(dataset, axis=dimension) - np.min(dataset, axis=dimension)
import numpy as np
dataset_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])