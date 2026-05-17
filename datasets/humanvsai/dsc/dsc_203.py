import inspect
from module_name import BaseCollector

def get_collectors_from_module(mod):
    """Locate all of the collector classes within a given module"""
    collectors = []
    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj) and issubclass(obj, BaseCollector) and obj != BaseCollector:
            collectors.append(obj)
    return collectors