import time

class Vehicle:
    def __init__(self):
        self.is_armable = False

    def wait_for_armable(self, timeout=None):
        start_time = time.time()
        while not self.is_armable:
            if timeout is not None and time.time() - start_time > timeout:
                raise TimeoutError("Vehicle is not armable after timeout seconds.")
            # You might need to add some delay here to avoid busy waiting
            time.sleep(0.1)

# Usage
vehicle = Vehicle()
try:
    vehicle.wait_for_armable(timeout=5)
except TimeoutError:
    print("Timeout occurred")