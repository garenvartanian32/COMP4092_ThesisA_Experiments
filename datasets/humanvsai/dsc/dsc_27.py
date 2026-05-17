def is_time_valid(self, timestamp):
    """Check if time is valid for one of the timerange.

    :param timestamp: time to check
    :type timestamp: int
    :return: True if one of the timerange is valid for t, False otherwise
    :rtype: bool"""

    # Assuming you have a list of tuples, where each tuple represents a time range
    time_ranges = [(8, 10), (12, 14), (15, 17)]

    for start, end in time_ranges:
        if start <= timestamp < end:
            return True

    return False