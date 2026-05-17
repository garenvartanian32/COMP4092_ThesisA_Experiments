def create_setter(source, name):
    def setter(context, value):
        setattr(source, context[name], value)
    return setter
