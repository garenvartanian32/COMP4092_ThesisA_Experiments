def open(self, name, mode='r', *args, **kwargs):
    if mode not in ('r', 'rb'):
        raise ValueError('Unsupported mode: {}'.format(mode))
    try:
        resource = self.find_resource(name)
        if resource is None:
            raise IOError('Resource not found: {}'.format(name))
        return self.open_resource(resource, mode, *args, **kwargs)
    except Exception as e:
        raise IOError('Failed to open resource: {}'.format(e))