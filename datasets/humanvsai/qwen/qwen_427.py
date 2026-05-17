def _nestr(ins):
    if len(ins) < 2:
        raise ValueError('Stack must contain at least two strings to compare and pop.')
    a = ins.pop()
    b = ins.pop()
    if a != b:
        return True
    else:
        return False

def _nestr_eq(ins):
    """Compares & pops top 2 strings out of the stack.
    Temporal values are freed from memory. (a$ = b$)"""
    if len(ins) < 2:
        raise ValueError('Stack must contain at least two strings to compare and pop.')
    a = ins.pop()
    b = ins.pop()
    if a == b:
        return True
    else:
        return False

def _nestr_gt(ins):
    """Compares & pops top 2 strings out of the stack.
    Temporal values are freed from memory. (a$ > b$)"""
    if len(ins) < 2:
        raise ValueError('Stack must contain at least two strings to compare and pop.')
    a = ins.pop()
    b = ins.pop()
    if a > b:
        return True
    else:
        return False

def _nestr_lt(ins):
    """Compares & pops top 2 strings out of the stack.
    Temporal values are freed from memory. (a$ < b$)"""
    if len(ins) < 2:
        raise ValueError('Stack must contain at least two strings to compare and pop.')
    a = ins.pop()
    b = ins.pop()
    if a < b:
        return True
    else:
        return False

def _nestr_ge(ins):
    """Compares & pops top 2 strings out of the stack.
    Temporal values are freed from memory. (a$ >= b$)"""
    if len(ins) < 2:
        raise ValueError('Stack must contain at least two strings to compare and pop.')
    a = ins.pop()
    b = ins.pop()
    if a >= b:
        return True
    else:
        return False