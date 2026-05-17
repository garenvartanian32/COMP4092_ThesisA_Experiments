def call(self, methodname, *args, **kwargs):
        for plugin in self._plugins:
            method = getattr(plugin, methodname, None)
            if method is None:
                continue
            yield method(*args, **kwargs)