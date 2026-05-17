def deps_list(self):
        assert self.final, 'Call build() before using the graph.'
        out = []
        for node in nx.topological_sort(self.graph):
            deps = [v for k, v in self.graph.out_edges([node])]
            out.append((node, deps))
        return out