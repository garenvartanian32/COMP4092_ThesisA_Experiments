def find_root(x, counts, bkg, model):
    func = x * model + bkg
    return counts - func
