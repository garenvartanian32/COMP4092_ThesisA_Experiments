def range(cls, dataset, dimension):
    """Computes the range along a particular dimension."""
    values = [row[dimension] for row in dataset]
    return max(values) - min(values)