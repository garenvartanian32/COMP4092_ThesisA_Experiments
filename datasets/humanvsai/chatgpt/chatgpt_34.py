import numpy as np
from matplotlib import pyplot as plt

def lrelfreq(inlist, numbins=10, defaultreallimits=None):
    values, bins, _ = plt.hist(inlist, bins=numbins, range=defaultreallimits)
    binsize = bins[1] - bins[0]
    freqs = np.divide(values, np.sum(values))
    cumfreqs = np.cumsum(freqs)
    return cumfreqs.tolist(), bins[0], binsize, [values[i]-cumfreqs[i-1]*len(inlist) for i in range(len(values)) if i > 0]
