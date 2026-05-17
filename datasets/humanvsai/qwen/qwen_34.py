def relfreq(inlist, numbins=10, defaultreallimits=None):
    from scipy.stats import histogram
    (scores, lowerreallimit, binsize, extrapoints) = histogram(inlist, numbins=numbins, defaultreallimits=defaultreallimits)
    relfreqs = [float(score) / len(inlist) for score in scores]
    return (relfreqs, lowerreallimit, binsize, extrapoints)