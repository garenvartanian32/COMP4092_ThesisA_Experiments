import matplotlib.pyplot as plt

def set_axis_limits(axes, xlim=True, ylim=True, xmin=None, xmax=None, ymin=None, ymax=None):
    """
    Set maximum and minimum limits from list of axis objects to each axis

    Args
    ----
    axes: iterable
        list of `matplotlib.pyplot` axis objects whose limits should be modified
    xlim: bool, optional
        Flag to set modification of x axis limits (default True)
    ylim: bool, optional
        Flag to set modification of y axis limits (default True)
    xmin: float, optional
        Minimum value of x axis
    xmax: float, optional
        Maximum value of x axis
    ymin: float, optional
        Minimum value of y axis
    ymax: float, optional
        Maximum value of y axis
    """
    for ax in axes:
        if xlim:
            if xmin is not None:
                ax.set_xlim(left=xmin)
            if xmax is not None:
                ax.set_xlim(right=xmax)
        if ylim:
            if ymin is not None:
                ax.set_ylim(bottom=ymin)
            if ymax is not None:
                ax.set_ylim(top=ymax)
