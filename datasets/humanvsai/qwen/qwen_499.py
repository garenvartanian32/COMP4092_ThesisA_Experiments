def _start_nodes_parallel(self, nodes, max_thread_pool_size):
    import multiprocessing
    from concurrent.futures import ThreadPoolExecutor
    started_nodes = set()

    def start_node(node):
        try:
            node.start()
            started_nodes.add(node)
        except Exception as e:
            print(f'Failed to start node {node}: {e}')
    with ThreadPoolExecutor(max_workers=max_thread_pool_size) as executor:
        executor.map(start_node, nodes)
    return started_nodes