import threading

class WebSocketClient:
    def __init__(self):
        self.threads = []

    def start(self):
        # Assuming you have a method called `run` that handles the websocket connection
        thread = threading.Thread(target=self.run)
        self.threads.append(thread)
        thread.start()

    def run(self):
        # Your code to handle the websocket connection goes here
        pass