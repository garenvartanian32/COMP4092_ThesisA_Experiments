import matplotlib.pyplot as plt

def format_legend(ax, cmap):
    handles, labels = ax.get_legend_handles_labels()
    order = [handle.properties()['color'] for handle in handles]
    colors = cmap(range(len(order)))
    color_map = dict(zip(order, colors))
    [handle.set_color(color_map[handle.properties()['color']]) for handle in handles]
    ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5))
