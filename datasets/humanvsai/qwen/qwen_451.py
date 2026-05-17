def np2str(value):
    import numpy as np
    if not isinstance(value, np.ndarray):
        raise ValueError('value is not a numpy array')
    if value.size != 1:
        raise ValueError('value is array larger than 1-element')
    if not isinstance(value.item(), np.string_):
        raise ValueError('value is not of type numpy.string_')
    return value.item().decode('utf-8')

def str2np(value):
    """Convert a str to `numpy.string_`.

    Args:
        value (str): string to convert

    Returns:
        ndarray: 1-element numpy array of type `numpy.string_`"""
    import numpy as np
    return np.array([value.encode('utf-8')], dtype=np.string_)