def start(self):
        super(BitfinexWSS, self).start()
        log.info("BitfinexWSS.start(): Initializing Websocket connection..")
        while self.conn is None:
            try:
                self.conn = create_connection(self.addr, timeout=10)
            except WebSocketTimeoutException:
                self.conn = None
                print("Couldn't create websocket connection - retrying!")
        log.info("BitfinexWSS.start(): Initializing receiver thread..")
        if not self.receiver_thread:
            self.receiver_thread = Thread(target=self.receive, name='Receiver Thread')
            self.receiver_thread.start()
        else:
            log.info("BitfinexWSS.start(): Thread not started! "
                     "self.receiver_thread is populated!")
        log.info("BitfinexWSS.start(): Initializing processing thread..")
        if not self.processing_thread:
            self.processing_thread = Thread(target=self.process, name='Processing Thread')
            self.processing_thread.start()
        else:
            log.info("BitfinexWSS.start(): Thread not started! "
                     "self.processing_thread is populated!")
        self.setup_subscriptions()