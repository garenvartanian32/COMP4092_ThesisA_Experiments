def setup_mocked_name(name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            setattr(wrapper, 'is_mocked_' + name, False)
            if name in self.mocked:
                setattr(wrapper, 'is_mocked_' + name, True)
                return func(self, *args, **kwargs)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
