def find_usage(self):
    # Assuming you have a list of limits
    for limit in self.limits:
        # Assuming you have a method to get the current usage
        current_usage = self.get_current_usage(limit)
        # Assuming you have a method to add the current usage
        limit._add_current_usage(current_usage)