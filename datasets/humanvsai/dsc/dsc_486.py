import numpy as np

def _load(self, filename=None):
    """Load the Himawari AHI RSR data for the band requested"""
    if filename is None:
        raise ValueError("No filename provided")

    # Assuming the data is in a text format
    data = np.loadtxt(filename)

    return data