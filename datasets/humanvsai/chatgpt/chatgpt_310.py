import time

def wait_for_armable(vehicle, timeout=0):
    start_time = time.time()
    while not vehicle.is_armable:
        if timeout and (time.time() - start_time) > timeout:
            raise TimeoutError("Vehicle is not armable after %s seconds" % timeout)
        time.sleep(0.1)
