def helper_function(num_list):
    """
    This function takes a list of numbers as input and returns the sum, mean, and maximum value of the list.
    """
    total_sum = sum(num_list)
    list_mean = sum(num_list) / len(num_list)
    list_max = max(num_list)
    return total_sum, list_mean, list_max
