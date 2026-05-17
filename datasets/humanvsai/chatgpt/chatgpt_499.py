from multiprocessing.pool import ThreadPool

def start_nodes(nodes):
    started_nodes = set()
    with ThreadPool(processes=len(nodes)) as pool:
        for node in nodes:
            if some_condition(node): # check if node meets some condition to be started
                pool.apply_async(start_node_function, args=(node,)) # start node in separate thread
                started_nodes.add(node)
    return started_nodes
