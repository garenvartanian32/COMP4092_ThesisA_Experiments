import queue

class MessageProcessor:
    def __init__(self):
        self.message_queue = queue.Queue()

    def _process_queue(self):
        if not self.message_queue.empty():
            message = self.message_queue.get()
            # Process the message here
            print(f"Processing message: {message}")