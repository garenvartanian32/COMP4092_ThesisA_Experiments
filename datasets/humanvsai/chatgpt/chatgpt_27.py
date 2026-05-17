def is_valid_time(timestamp):
    timeranges = [
        (0, 3600),   # 0:00 - 1:00
        (14400, 18000),  # 4:00 - 5:00
        (32400, 36000)  # 9:00 - 10:00
    ]
    for start_time, end_time in timeranges:
        if start_time <= timestamp <= end_time:
            return True
    return False
