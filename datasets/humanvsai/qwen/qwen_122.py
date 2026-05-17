def call(self, methodname, *args, **kwargs):
    for plugin in self.plugins:
        if hasattr(plugin, methodname):
            getattr(plugin, methodname)(*args, **kwargs)