def start(self):
    self.client_thread = threading.Thread(target=self.run_client)
    self.client_thread.start()
    self.client_thread.join()