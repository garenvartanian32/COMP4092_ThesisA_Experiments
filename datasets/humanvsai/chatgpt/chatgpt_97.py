import threading

class DelayedFunctionRunner:
    def __init__(self):
        self.timer = None
        self._lock = threading.Lock()

    def _run_func(self, func,time):
        try:
            func()
        finally:
            with self._lock:
                if self.timer is threading.current_thread():
                    self.timer = None

    def run_later(self, func, time, channel):
        with self._lock:
            if self.timer is not None:
                self.timer.cancel()
            self.timer = threading.Timer(time, self._run_func, args=(func, time))
        self.timer.start()
