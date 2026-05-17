def remove_finished_thread(queue: dict, key: str) -> None:
    """
    Remove finished Thread from queue.
    :param queue: a dictionary representing the queue of threads
    :param key: data source key
    :return: None
    """
    if key in queue:
        thread = queue[key]
        if not thread.is_alive():
            del queue[key]
