import numpy as np

def sort_labeled_intervals(intervals, labels=None):
    # Sort the intervals by the start time
    sort_indices = np.lexsort((intervals[:, 0], intervals[:, 1]))
    intervals_sorted = intervals[sort_indices]

    # If labels are provided, sort them accordingly
    if labels is not None:
        labels_sorted = [labels[i] for i in sort_indices]
        return intervals_sorted, labels_sorted
    else:
        return intervals_sorted