def require_scalar(self, *args):
    if not self.is_scalar():
        raise ValueError('Node is not a scalar')
    if args:
        if not isinstance(self.value, args):
            raise ValueError(f'Node value is not one of the expected types: {args}')
    return self