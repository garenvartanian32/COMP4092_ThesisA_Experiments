def reset_environment(blocking=True):
    if blocking:
        # blocking implementation
        new_observation = # implementation
        return new_observation
    else:
        # non-blocking implementation
        def callable_func():
            new_observation = # implementation
            return new_observation
        return callable_func
