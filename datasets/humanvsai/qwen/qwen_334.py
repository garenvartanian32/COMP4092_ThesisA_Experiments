def _do_broker_main(self):
    while not self.shutdown_flag:
        try:
            self._dispatch_io_events()
        except Exception as e:
            self.logger.error(f'Error in IO event dispatching: {e}')
            self.shutdown_flag = True