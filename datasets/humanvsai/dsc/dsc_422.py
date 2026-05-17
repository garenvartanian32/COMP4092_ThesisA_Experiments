import json

# This is a dictionary that will serve as our event handler registry
event_handlers = {}

def process(event_name, data):
    """Iterates over the event handler registry and execute each found
    handler.

    It takes the event name and its its `data`, passing the return of
    `json.loads(data)` to the found handlers."""

    # Check if the event is in our registry
    if event_name in event_handlers:
        # If it is, execute the handler with the data
        event_handlers[event_name](json.loads(data))
    else:
        # If it's not, print an error message
        print(f"No handler found for event: {event_name}")

# Here's an example of how you might add a handler to the registry
def handle_my_event(data):
    print(f"Handling my event with data: {data}")

event_handlers['my_event'] = handle_my_event

# Now you can process events
process('my_event', json.dumps({'key': 'value'}))