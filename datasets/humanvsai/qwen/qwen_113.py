def merge_limits(axes, xlim=True, ylim=True):
    if xlim:
        x_min = min((ax.get_xlim()[0] for ax in axes))
        x_max = max((ax.get_xlim()[1] for ax in axes))
        for ax in axes:
            ax.set_xlim(x_min, x_max)