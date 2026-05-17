def add_record(self, schema, _bump_stack_level=False):
    if _bump_stack_level:
        frame = inspect.currentframe().f_back.f_back
    else:
        frame = inspect.currentframe().f_back
    cls = frame.f_locals.get('cls', None)
    if cls is None:
        raise ValueError('Could not find class in frame')
    self.record_store[schema] = cls
    return cls