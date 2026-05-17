def sort_cyclic_graph_best_effort(graph, pick_first='head'):
    """Fallback for cases in which the graph has cycles."""
    visited = set()
    sorted_graph = []

    def dfs(node):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)
        sorted_graph.append(node)

    if pick_first == 'head':
        for node in graph:
            if node not in visited:
                dfs(node)
    elif pick_first == 'tail':
        for node in reversed(graph):
            if node not in visited:
                dfs(node)
    else:
        raise ValueError("pick_first must be either 'head' or 'tail'")

    return sorted_graph