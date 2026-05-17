import time

class Hamster:
    def __init__(self):
        self.last_activity = time.time()

    def check_hamster(self):
        """refresh hamster every x secs - load today, check last activity etc."""
        current_time = time.time()
        if current_time - self.last_activity > 60:  # 60 seconds
            self.last_activity = current_time
            print("Hamster is active")
        else:
            print("Hamster is inactive")