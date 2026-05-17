def convert_yielded(yielded):
    if isinstance(yielded, list):
        return tornado.gen.maybe_future([convert_yielded(i) for i in yielded])
    elif isinstance(yielded, dict):
        return tornado.gen.maybe_future({k: convert_yielded(v) for (k, v) in yielded.items()})
    elif isinstance(yielded, tornado.concurrent.Future):
        return tornado.gen.maybe_future(yielded)
    else:
        raise TypeError('Unsupported yielded object type: %s' % type(yielded).__name__)