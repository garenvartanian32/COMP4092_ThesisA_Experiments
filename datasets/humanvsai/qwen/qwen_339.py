def _f_cash_root(x, counts, bkg, model):
    return np.sum((counts - bkg - x * model) ** 2)

def find_root(x0, counts, bkg, model):
    """Find the root of the function `_f_cash_root` using scipy.optimize.minimize.

    Parameters
    ----------
    x0 : float
        Initial guess for the model amplitude.
    counts : `~numpy.ndarray`
        Count map slice, where model is defined.
    bkg : `~numpy.ndarray`
        Background map slice, where model is defined.
    model : `~numpy.ndarray`
        Source template (multiplied with exposure).

    Returns
    -------
    x : float
        Model amplitude that minimizes the function `_f_cash_root`.
    """
    result = scipy.optimize.minimize(_f_cash_root, x0, args=(counts, bkg, model))
    return result.x[0]
counts = np.array([10, 20, 30])
bkg = np.array([1, 2, 3])
model = np.array([0.5, 1, 1.5])
x0 = 1.0
x = find_root(x0, counts, bkg, model)