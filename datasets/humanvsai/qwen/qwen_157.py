def search(self, pattern, start=None, limit=None, include_category=None):
    if not isinstance(pattern, str):
        raise ValueError('Pattern must be a string')
    if start is not None and (not isinstance(start, int)):
        raise ValueError('Start must be an integer')
    if limit is not None and (not isinstance(limit, int)):
        raise ValueError('Limit must be an integer')
    if include_category is not None and (not isinstance(include_category, list)):
        raise ValueError('Include_category must be a list')
    if include_category is not None:
        for category in include_category:
            if not isinstance(category, str):
                raise ValueError('Each element in include_category must be a string')
    results = self._search(pattern, start, limit, include_category)
    return results

def _search(self, pattern, start, limit, include_category):
    """Internal method to perform the actual search"""
    pass