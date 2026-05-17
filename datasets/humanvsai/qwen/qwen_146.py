def find_usage(self):
    for limit in self.limits:
        if limit.region == self.region:
            current_usage = self._get_current_usage(limit)
            limit._add_current_usage(current_usage)