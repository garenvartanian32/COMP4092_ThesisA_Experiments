import numpy as np
import matplotlib.pyplot as plt

def relfreq(inlist, numbins=10, defaultreallimits=None):
    hist, bin_edges = np.histogram(inlist, bins=numbins, range=defaultreallimits)
    hist = hist / len(inlist)
    return hist, bin_edges[0], bin_edges[1] - bin_edges[0], 0

# Example usage:
data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution
hist, lower_limit, bin_size, _ = relfreq(data, numbins=20)

plt.bar(np.arange(len(hist)), hist, width=0.8)
plt.xlabel('Bin')
plt.ylabel('Relative Frequency')
plt.title('Relative Frequency Histogram')
plt.xticks(np.arange(len(hist)), [f'{lower_limit + i*bin_size:.2f} - {lower_limit + (i+1)*bin_size:.2f}' for i in range(len(hist))], rotation='vertical')
plt.show()