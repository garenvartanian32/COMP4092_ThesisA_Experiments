import numpy as np

def sort_intervals(intervals: np.ndarray, labels: list = None):
    sorted_idxs = np.argsort(intervals[:, 0])
    intervals_sorted = intervals[sorted_idxs]
    if labels is not None:
        labels_sorted = [labels[idx] for idx in sorted_idxs]
        return intervals_sorted, labels_sorted
    return intervals_sorted
