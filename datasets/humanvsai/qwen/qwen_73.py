def normal_h2(size):
    import numpy as np
    import matplotlib.pyplot as plt
    data_x = np.random.normal(0, 1, size)
    data_y = np.random.normal(0, 1, size)
    plt.hist2d(data_x, data_y, bins=30, cmap='Blues')
    plt.colorbar()
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('2D Histogram of Normally Distributed Data')
    plt.show()