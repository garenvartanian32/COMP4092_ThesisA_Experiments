def execute_handlers(event_name, data, handlers_registry):

    handlers = handlers_registry.get(event_name, [])

    for handler in handlers:
        try:
            handler(ejson.loads(data))
        except Exception as e:
            print(f"Error executing handler for event {event_name}: {str(e)}")