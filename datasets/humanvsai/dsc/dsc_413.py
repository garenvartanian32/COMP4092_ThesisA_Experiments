def make_proxy_method(cls, name):
    """Creates a proxy function that can be used by Flasks routing. The
    proxy instantiates the class and calls the appropriate method.

    :param cls: the class to create a proxy for
    :param name: the name of the method to create a proxy for
    """
    def proxy(*args, **kwargs):
        instance = cls()
        return getattr(instance, name)(*args, **kwargs)
    return proxy