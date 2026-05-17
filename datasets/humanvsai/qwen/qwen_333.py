def request_finished(key):
    queue = get_queue()
    if key in queue:
        queue.remove(key)
        print(f'Removed {key} from queue.')
    else:
        print(f'{key} not found in queue.')

def get_queue():
    """Get the queue of data source keys.

    :return: list of data source keys"""
    return ['source1', 'source2', 'source3']