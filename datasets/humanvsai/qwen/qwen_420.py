def _get_mean(self, data, dctx, dists):
    mean = 0
    for i in range(len(data)):
        mean += data[i] * dists[i]
    mean /= sum(dists)
    return mean