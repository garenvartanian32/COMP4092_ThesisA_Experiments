import numpy as np

def convert_numpy_string(value):
    if not isinstance(value, np.ndarray) or len(value) != 1 or not isinstance(value[0], np.string_):
        raise ValueError("Input value must be a 1-element numpy string array.")

    return value[0].decode('utf-8')
