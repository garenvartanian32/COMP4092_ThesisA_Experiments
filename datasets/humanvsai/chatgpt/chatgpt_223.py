def configure_operation(func):
    def wrapper(resource):
        # Perform some configuration
        # ...
        # Call the passed function with the configured resource
        return func(resource)
    return wrapper
