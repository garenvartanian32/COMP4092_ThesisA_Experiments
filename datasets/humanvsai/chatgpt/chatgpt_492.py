import matplotlib.pyplot as plt

def plot_histogram_all_groups(data):
    plt.hist(data, bins=10)
    plt.show()
