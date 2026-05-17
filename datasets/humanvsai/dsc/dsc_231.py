import numpy as np

def cat_core(list_of_columns, sep):
    """Auxiliary function for :meth:`str.cat`

    Parameters
    ----------
    list_of_columns : list of numpy arrays
        List of arrays to be concatenated with sep;
        these arrays may not contain NaNs!
    sep : string
        The separator string for concatenating the columns

    Returns
    -------
    nd.array
        The concatenation of list_of_columns with sep"""

    # Convert each array in list_of_columns to string
    list_of_columns = [np.array([str(i) for i in arr]) for arr in list_of_columns]

    # Concatenate the arrays with the separator
    result = np.char.add(list_of_columns[0], sep)
    for i in range(1, len(list_of_columns)):
        result = np.char.add(result, list_of_columns[i])
        if i < len(list_of_columns) - 1:
            result = np.char.add(result, sep)

    return result