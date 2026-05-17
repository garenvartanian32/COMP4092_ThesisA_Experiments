import numpy as np
import matplotlib.pyplot as plt

def normal_h2(size):
    """A simple 2D histogram with normal distribution.

    Parameters
    ----------
    size : Number of points
    """
    # Generate some random data
    data = np.random.normal(0, 1, size)

    # Create a histogram
    plt.hist(data, bins=30, density=True)

    # Show the plot
    plt.show()

# Call the function
normal_h2(1000)