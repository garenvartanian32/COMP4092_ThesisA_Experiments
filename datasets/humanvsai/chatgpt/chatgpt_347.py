def get_lock(key, session_id, seconds_to_lock, metadata):
    details = None
    try:
        lock = consul.Lock.acquire(key, session_id, lock_try_time=seconds_to_lock, lock_meta=metadata)
        if lock:
            details = lock.info
    except consul.ConsulException as e:
        if e.args[0] == 'Session {} is lost'.format(session_id):
            raise SessionLostConsulError('Consul session {} is lost'.format(session_id))
    return details
