def get_analysis_result_range(parent_result: float, duplicate_result: float, variation: float) -> dict:
    """
    Returns the valid result range for this analysis duplicate, based on both on the result and duplicate variation
    set in the original analysis. A Duplicate will be out of range if its result does not match with the result for the
    parent analysis plus the duplicate variation in % as the margin error.
    
    :param parent_result: The original result from the analysis
    :type parent_result: float
    
    :param duplicate_result: The result from the duplicate analysis
    :type duplicate_result: float
    
    :param variation: The variation percentage set in the original analysis
    :type variation: float
    
    :return: A dictionary with the keys min and max
    :rtype: dict
    """
    margin_error = parent_result * (variation/100)
    result_min = parent_result - margin_error
    result_max = parent_result + margin_error
    return {'min': result_min, 'max': result_max}
