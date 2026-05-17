def locate_collector_classes(module):
    import inspect
    return [obj for name, obj in inspect.getmembers(module) if (
        isinstance(obj, type) and not inspect.isabstract(obj) and (
            "Collector" in name or "collector" in name)
    )]
