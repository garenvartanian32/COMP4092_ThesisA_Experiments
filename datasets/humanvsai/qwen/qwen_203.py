def get_collectors_from_module(mod):
    import inspect
    import types
    collectors = []
    for (name, obj) in inspect.getmembers(mod):
        if inspect.isclass(obj) and issubclass(obj, Collector) and (obj is not Collector):
            collectors.append(obj)
    return collectors

def load_collectors_from_package(package_name):
    """Load all collector classes from a package"""
    import pkgutil
    import importlib
    collectors = []
    package = importlib.importmodule(package_name)
    for (_, modname, ispkg) in pkgutil.iter_modules(package.__path__):
        if not ispkg:
            mod = importlib.importmodule(f'{package_name}.{modname}')
            collectors.extend(get_collectors_from_module(mod))
    return collectors