def relfreq(inlist, numbins=10, defaultreallimits=None):
    h, l, b, e = histogram(inlist, numbins, defaultreallimits)
    for i in range(len(h)):
        h[i] = h[i] / float(len(inlist))
    return h, l, b, e