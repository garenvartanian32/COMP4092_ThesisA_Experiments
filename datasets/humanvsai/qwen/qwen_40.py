def intersect(self, *queries):
    if not queries:
        return self
    result = self
    for query in queries:
        result = result & query
    return result