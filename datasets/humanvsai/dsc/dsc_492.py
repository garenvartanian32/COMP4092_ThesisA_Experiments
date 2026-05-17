import matplotlib.pyplot as plt

def plot(self, axis, ith_plot, total_plots, limits):
    """Plot the histogram as a whole over all groups.

    Do not plot as individual groups like other plot types."""

    # Assuming 'self' is a pandas DataFrame
    plt.hist(self[axis], bins=total_plots)
    plt.xlim(limits)
    plt.title('Histogram of ' + axis)
    plt.show()