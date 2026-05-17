import numpy as np
import matplotlib.pyplot as plt

def normal_hist_2d(size):
    x, y = np.random.normal(size=(2, size))
    bins = np.linspace(-5, 5, 50)
    plt.hist2d(x, y, bins=bins, cmap='Blues')
    plt.colorbar()
    plt.show()
