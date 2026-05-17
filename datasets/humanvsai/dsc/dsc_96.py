def get_means_and_scales(numbers):
    """Gets the mean and scales for normal approximating parameters"""
    mean = sum(numbers) / len(numbers)
    variance = sum([((x - mean) ** 2) for x in numbers]) / len(numbers)
    scale = variance ** 0.5
    return mean, scale