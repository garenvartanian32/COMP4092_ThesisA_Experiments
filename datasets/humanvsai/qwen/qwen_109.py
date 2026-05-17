def is_builtin(text):
    import builtins
    return text in dir(builtins)

def is_keyword(text):
    """Test if passed string is a Python keyword"""
    import keyword
    return keyword.iskeyword(text)

def is_identifier(text):
    """Test if passed string is a valid Python identifier"""
    import keyword
    if keyword.iskeyword(text):
        return False
    if not text.isidentifier():
        return False
    return True

def is_valid_name(text):
    """Test if passed string is a valid Python name (identifier or keyword)"""
    return is_identifier(text) or is_keyword(text)