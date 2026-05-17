class PluginManager:
    def __init__(self, plugins):
        self.plugins = plugins

    def call(self, methodname, *args, **kwargs):
        for plugin in self.plugins:
            if hasattr(plugin, methodname):
                method = getattr(plugin, methodname)
                method(*args, **kwargs)