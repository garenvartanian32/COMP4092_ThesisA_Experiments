def _do_broker_main(self):
        # For Python 2.4, no way to retrieve ident except on thread.
        self._waker.broker_ident = thread.get_ident()
        try:
            while self._alive:
                self._loop_once()
            fire(self, 'shutdown')
            self._broker_shutdown()
        except Exception:
            LOG.exception('_broker_main() crashed')
        self._alive = False  # Ensure _alive is consistent on crash.
        self._exitted = True
        self._broker_exit()