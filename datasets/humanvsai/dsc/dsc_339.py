import numpy as np

def _f_cash_root(x, counts, bkg, model):
    """Function to find root of. Described in Appendix A, Stewart (2009).

    Parameters
    ----------
    x : float
        Model amplitude.
    counts : `~numpy.ndarray`
        Count map slice, where model is defined.
    bkg : `~numpy.ndarray`
        Background map slice, where model is defined.
    model : `~numpy.ndarray`
        Source template (multiplied with exposure).
    """
    # Calculate the model amplitude
    model_amplitude = x * model

    # Calculate the difference between the model and the counts
    difference = np.sum(model_amplitude - counts)

    # Return the difference
    return difference