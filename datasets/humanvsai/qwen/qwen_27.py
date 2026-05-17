def is_time_valid(self, timestamp):
    for (start, end) in self.timeranges:
        if start <= timestamp <= end:
            return True
    return False