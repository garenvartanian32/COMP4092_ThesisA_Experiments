def make_proxy_method(cls, name):

    def proxy(*args, **kwargs):
        instance = cls()
        return instance.__getattribute__(name)(*args, **kwargs)
    return proxy