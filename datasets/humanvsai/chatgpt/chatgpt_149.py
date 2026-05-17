def process_message_queue(queue):
    if queue:
        message = queue.pop(0)
        # process message
