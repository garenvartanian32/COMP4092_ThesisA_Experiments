def sort_labeled_intervals(intervals, labels=None):
    idx = np.argsort(intervals[:, 0])
    intervals_sorted = intervals[idx]
    if labels is None:
        return intervals_sorted
    else:
        return intervals_sorted, [labels[_] for _ in idx]