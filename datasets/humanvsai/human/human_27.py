def is_time_valid(self, timestamp):
        if self.is_time_day_valid(timestamp):
            for timerange in self.timeranges:
                if timerange.is_time_valid(timestamp):
                    return True
        return False