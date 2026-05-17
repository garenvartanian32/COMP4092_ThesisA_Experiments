def compute_range(data, axis):
    """Computes the range along a particular dimension.
    
    Args:
    data (numpy.ndarray): The input data.
    axis (int): The axis along which to compute the range.
    
    Returns:
    numpy.ndarray: The range of values along the specified axis.
    """
    return np.ptp(data, axis=axis)
