def mock(name: str) -> Callable[[Any], None]:
    def _(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            logger.info('STARTING: mock ' + name)
            is_mocked = False
            sanitized_name = name.replace('.', '_').strip('_')
            if name in self.mocks_mask:
                logger.info('STOPPING: mock ' + name + '—MASKED')
            elif getattr(self, '_is_mocked_' + sanitized_name, False):
                is_mocked = True
                logger.info('STOPPING: mock ' + name + '—EXISTS')
            else:
                func(self, *args, **kwargs)
                is_mocked = True
                logger.info('STOPPING: mock ' + name)
            setattr(self, '_is_mocked_' + sanitized_name, is_mocked)
            return is_mocked
        return wrapper
    return _