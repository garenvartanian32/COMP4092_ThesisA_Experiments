def source_setattr():
    def source_setattr(value, context, **_params):
        setattr(context["model"].source, context["key"], value)
        return _attr()
    return source_setattr