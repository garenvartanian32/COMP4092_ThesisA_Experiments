def process(event_name, data):
    deserialized = loads(data)
    event_cls = find_event(event_name)
    event = event_cls(event_name, deserialized)
    try:
        event.clean()
    except ValidationError as exc:
        if os.environ.get('EVENTLIB_RAISE_ERRORS'):
            raise
        else:
            logger.warning(
                "The event system just got an exception while cleaning "
                "data for the event '{}'\ndata: {}\nexc: {}".format(
                    event_name, data, str(exc)))
            return
    for handler in find_handlers(event_name):
        try:
            handler(deserialized)
        except Exception as exc:
            logger.warning(
                (u'One of the handlers for the event "{}" has failed with the '
                 u'following exception: {}').format(event_name, str(exc)))
            if getsetting('DEBUG'):
                raise exc
    event._broadcast()