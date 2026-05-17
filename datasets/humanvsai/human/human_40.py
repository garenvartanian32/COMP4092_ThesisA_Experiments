def intersect(self, *queries):
        q = self._clone()
        q.intersections += queries
        return q