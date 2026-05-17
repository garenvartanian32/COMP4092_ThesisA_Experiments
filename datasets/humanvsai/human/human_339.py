def _f_cash_root(x, counts, bkg, model):
    return np.sum(model * (counts / (x * model + bkg) - 1.0))