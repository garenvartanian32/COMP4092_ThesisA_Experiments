import threading
import time

class Scheduler:
    def __init__(self):
        self.channels = {}

    def schedule(self, func, delay, channel="default"):
        if channel in self.channels:
            self.channels[channel].cancel()

        timer = threading.Timer(delay, func)
        timer.start()

        self.channels[channel] = timer