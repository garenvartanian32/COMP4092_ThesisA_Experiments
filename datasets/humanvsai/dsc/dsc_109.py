def is_builtin(text):
    """Test if passed string is the name of a Python builtin object"""
    import builtins
    return hasattr(builtins, text)