def get_collectors_from_module(mod):
    for attrname in dir(mod):
        attr = getattr(mod, attrname)
        # Only attempt to load classes that are infact classes
        # are Collectors but are not the base Collector class
        if ((inspect.isclass(attr) and
             issubclass(attr, Collector) and
             attr != Collector)):
            if attrname.startswith('parent_'):
                continue
            # Get class name
            fqcn = '.'.join([mod.__name__, attrname])
            try:
                # Load Collector class
                cls = load_dynamic_class(fqcn, Collector)
                # Add Collector class
                yield cls.__name__, cls
            except Exception:
                # Log error
                logger.error(
                    "Failed to load Collector: %s. %s",
                    fqcn, traceback.format_exc())
                continue