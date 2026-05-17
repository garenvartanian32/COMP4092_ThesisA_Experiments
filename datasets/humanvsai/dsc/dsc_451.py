import numpy as np

def np2str(value):
    """Convert an `numpy.string_` to str.

    Args:
        value (ndarray): scalar or 1-element numpy array to convert

    Raises:
        ValueError: if value is array larger than 1-element or it is not of
                    type `numpy.string_` or it is not a numpy array
    """
    if not isinstance(value, np.ndarray):
        raise ValueError("Input is not a numpy array")
    if value.dtype != np.dtype('S'):
        raise ValueError("Input is not of type numpy.string_")
    if value.size > 1:
        raise ValueError("Input is larger than 1-element")
    return value.astype(str).item()