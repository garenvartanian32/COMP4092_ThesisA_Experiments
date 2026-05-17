def fallback_for_cycles(graph):
    """
    Fallback for cases in which the graph has cycles.
    """
    visited = set()
    path = set()

    def has_cycle(node):
        if node not in visited:
            visited.add(node)
            path.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited and has_cycle(neighbour) or neighbour in path:
                    return True
            path.remove(node)
        return False

    return has_cycle(list(graph.keys())[0])
