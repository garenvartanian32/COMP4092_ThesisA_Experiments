def sort_cyclic_graph_best_effort(graph, pick_first='head'):
    sorted_nodes = []
    visited = set()
    temp_mark = set()

    def dfs(node):
        if node in temp_mark:
            return False
        if node in visited:
            return True
        temp_mark.add(node)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        temp_mark.remove(node)
        visited.add(node)
        sorted_nodes.append(node)
        return True
    for node in graph:
        if node not in visited:
            if not dfs(node):
                if pick_first == 'head':
                    sorted_nodes.append(node)
                elif pick_first == 'tail':
                    sorted_nodes.insert(0, node)
                else:
                    raise ValueError("pick_first must be 'head' or 'tail'")
    return sorted_nodes