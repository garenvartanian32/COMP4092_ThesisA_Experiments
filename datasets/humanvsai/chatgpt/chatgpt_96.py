def mean_and_scales_normal_approximation(data):
    """
    Gets the mean and scales for normal approximating parameters.

    Args:
    data (numpy.ndarray): input dataset

    Returns:
    tuple: mean and scale values as a tuple
    """
    mean_value = np.mean(data)
    sd_value = np.std(data)
    return mean_value, sd_value
