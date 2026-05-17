def broker_thread_main():
    while not shutdown.is_set():
        events = selector.select(timeout=1)
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)
