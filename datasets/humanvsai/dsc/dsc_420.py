import numpy as np

def _get_mean(self, data, key, distances):
    """Returns the mean intensity measure level from the tables
        :param data:
            The intensity measure level vector for the given magnitude and IMT
        :param key:
            The distance type
        :param distances:
            The distance vector for the given magnitude and IMT"""

    # Check if data is not empty
    if len(data) > 0:
        # Calculate the mean
        mean = np.mean(data)
        return mean
    else:
        return None