def _start_nodes_parallel(self, nodes, max_thread_pool_size):
        # Create one thread for each node to start
        thread_pool_size = min(len(nodes), max_thread_pool_size)
        thread_pool = Pool(processes=thread_pool_size)
        log.debug("Created pool of %d threads", thread_pool_size)
        # pressing Ctrl+C flips this flag, which in turn stops the main loop
        # down below
        keep_running = True
        def sigint_handler(signal, frame):
            """
            Makes sure the cluster is saved, before the sigint results in
            exiting during node startup.
            """
            log.error(
                "Interrupted: will save cluster state and exit"
                " after all nodes have started.")
            keep_running = False
        # intercept Ctrl+C
        with sighandler(signal.SIGINT, sigint_handler):
            result = thread_pool.map_async(self._start_node, nodes)
            while not result.ready():
                result.wait(1)
                # check if Ctrl+C was pressed
                if not keep_running:
                    log.error("Aborting upon user interruption ...")
                    # FIXME: `.close()` will keep the pool running until all
                    # nodes have been started; should we use `.terminate()`
                    # instead to interrupt node creation as soon as possible?
                    thread_pool.close()
                    thread_pool.join()
                    self.repository.save_or_update(self)
                    # FIXME: should raise an exception instead!
                    sys.exit(1)
            # keep only nodes that were successfully started
            return set(node for node, ok
                       in itertools.izip(nodes, result.get()) if ok)