class Query:
    def __init__(self, query):
        self.query = query
    
    def intersection(self, *queries):
        for q in queries:
            self.query = set(self.query) & set(q.query)
        
        return Query(list(self.query))
