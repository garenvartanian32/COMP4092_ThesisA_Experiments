def _process_queue(self):
    if self.queue:
        message = self.queue.pop(0)
        self._handle_message(message)

def _handle_message(self, message):
    """Handle the message."""
    print(f'Handling message: {message}')

class MessageQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, message):
        """Add a message to the queue."""
        self.queue.append(message)

    def process_queue(self):
        """Process all messages in the queue."""
        while self.queue:
            self._process_queue()
mq = MessageQueue()