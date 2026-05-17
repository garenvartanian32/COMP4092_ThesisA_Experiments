def sort_cyclic_graph_best_effort(graph, pick_first='head'):
    ordered = []
    visited = set()
    # Go first on the pick_first chain then go back again on the others
    # that were not visited. Given the way the graph is built both chains
    # will always contain all the elements.
    if pick_first == 'head':
        fst_attr, snd_attr = ('head_node', 'update_node')
    else:
        fst_attr, snd_attr = ('update_node', 'head_node')
    current = FIRST
    while current is not None:
        visited.add(current)
        current = getattr(graph[current], fst_attr)
        if current not in visited and current is not None:
            ordered.append(current)
    current = FIRST
    while current is not None:
        visited.add(current)
        current = getattr(graph[current], snd_attr)
        if current not in visited and current is not None:
            ordered.append(current)
    return ordered