def process(event_name, data):
    import ejson
    parsed_data = ejson.loads(data)
    for handler in event_handler_registry.get(event_name, []):
        handler(parsed_data)
event_handler_registry = {'user_created': [lambda x: print(f"User created: {x['name']}")], 'user_deleted': [lambda x: print(f"User deleted: {x['name']}")]}