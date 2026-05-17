import numpy as np

def cat_auxiliary(list_of_columns, sep):
    return np.array([sep.join([str(e) for e in row]) for row in np.array(list_of_columns).T])
