import math

def get_group_num(num_channels):
    # GroupNorm divides channels into groups of size gn (gn= num_channels//2 for odd cases).
    gn = num_channels // 2 if num_channels % 2 else num_channels // 2
    # Minimum number of channels for a valid GroupNorm operation is gn.
    gn = max(gn, 1)
    num_groups = math.ceil(num_channels / gn)
    return num_groups
