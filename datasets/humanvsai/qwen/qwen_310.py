def wait_for_armable(self, timeout=None):
    start_time = time.time()
    while not self.vehicle.is_armable:
        if timeout is not None and time.time() - start_time > timeout:
            raise TimeoutError('Vehicle not armable within the specified timeout.')
        time.sleep(1)
    return True