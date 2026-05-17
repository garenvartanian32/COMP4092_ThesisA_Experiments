def sort_labeled_intervals(intervals, labels=None):
    import numpy as np
    sorted_indices = np.argsort(intervals[:, 0])
    intervals_sorted = intervals[sorted_indices]
    if labels is not None:
        labels_sorted = [labels[i] for i in sorted_indices]
        return (intervals_sorted, labels_sorted)
    else:
        return intervals_sorted
intervals = np.array([[1, 5], [3, 7], [2, 6]])
labels = ['a', 'b', 'c']
(sorted_intervals, sorted_labels) = sort_labeled_intervals(intervals, labels)