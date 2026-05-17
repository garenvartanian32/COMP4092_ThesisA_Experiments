def mock(name):

    def decorator(func):

        def wrapper(self, *args, **kwargs):
            is_mocked = hasattr(self, f'is_mocked_{name}')
            if not is_mocked:
                setattr(self, f'is_mocked_{name}', True)
                result = func(self, *args, **kwargs)
                return result
            else:
                raise ValueError(f'{name} is already mocked')
        return wrapper
    return decorator