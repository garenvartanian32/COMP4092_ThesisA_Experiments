class Query:
    def __init__(self, data):
        self.data = set(data)

    def intersect(self, *queries):
        result = self.data
        for query in queries:
            result = result.intersection(query.data)
        return Query(result)

    def union(self, *queries):
        result = self.data
        for query in queries:
            result = result.union(query.data)
        return Query(result)