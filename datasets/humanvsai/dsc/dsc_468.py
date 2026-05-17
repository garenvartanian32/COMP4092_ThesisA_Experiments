class Message:
    def __init__(self):
        self.thread_id = None

    def set_thread(self, value: str):
        """Set thread id of the message

        Args:
            value (str): the thread id
        """
        self.thread_id = value