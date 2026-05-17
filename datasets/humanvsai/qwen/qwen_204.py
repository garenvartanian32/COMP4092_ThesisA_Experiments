def length(time_flags):
    base_length = 8
    bytes_per_flag = 4
    return base_length + time_flags * bytes_per_flag