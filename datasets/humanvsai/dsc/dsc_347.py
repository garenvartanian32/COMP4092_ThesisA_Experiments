import consul

class ConsulLock:
    def __init__(self, host='localhost', port=8500, scheme='http'):
        self.consul = consul.Consul(host=host, port=port, scheme=scheme)

    def _acquire_lock(self, key, session_id, seconds_to_lock, metadata):
        try:
            # Try to create the lock
            self.consul.kv.put(key, None, acquire=session_id)
            # If the lock was successfully created, add metadata
            self.consul.kv.put(key + '/metadata', metadata)
            # Return details about the lock
            return {
                'key': key,
                'session_id': session_id,
                'seconds_to_lock': seconds_to_lock,
                'metadata': metadata
            }
        except consul.ConsulException as e:
            # If the lock couldn't be created, return None
            if e.args[0] == 500 and 'Failed to acquire lock' in e.args[1]:
                return None
            else:
                raise