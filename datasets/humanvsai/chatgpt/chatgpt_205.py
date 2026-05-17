import queue, threading

def remove_from_queue(Q, block=False, timeout=None):
    try:
        if block:
            if timeout == None:
                item = Q.get(True)
            else:
                item = Q.get(True, timeout)
        else:
            item = Q.get(False)
    except queue.Empty:
        raise queue.Empty("The queue is empty!")
    return item
