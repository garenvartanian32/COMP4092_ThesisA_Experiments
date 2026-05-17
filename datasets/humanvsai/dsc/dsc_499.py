import concurrent.futures

def _start_nodes_parallel(self, nodes, max_thread_pool_size):
    # Create a ThreadPoolExecutor with a maximum number of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_thread_pool_size) as executor:
        # Submit each node to the executor
        futures = {executor.submit(node.start) for node in nodes}

        # Wait for all futures to complete
        concurrent.futures.wait(futures)

        # Return the set of nodes that were actually started
        return {node for future in futures if future.result() for node in nodes if node.is_started()}