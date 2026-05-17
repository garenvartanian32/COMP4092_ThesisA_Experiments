def get_first_var(name: str, recurse: bool = True):
    if recurse:
        frame = inspect.currentframe()
        while frame:
            if name in frame.f_locals:
                return frame.f_locals[name]
            frame = frame.f_back
    elif name in inspect.currentframe().f_locals:
        return inspect.currentframe().f_locals[name]
