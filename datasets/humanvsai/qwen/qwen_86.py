def merge(self, another):
    if not isinstance(another, ValidationResultGraph):
        raise TypeError('The argument must be an instance of ValidationResultGraph')
    for node in another.nodes:
        if node not in self.nodes:
            self.nodes.add(node)
        for edge in another.edges[node]:
            if edge not in self.edges[node]:
                self.edges[node].add(edge)
    return self