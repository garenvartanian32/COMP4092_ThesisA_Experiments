def request_finished(key):
    with event_lock:
        threads[key] = threads[key][1:]
        if threads[key]:
            threads[key][0].run()