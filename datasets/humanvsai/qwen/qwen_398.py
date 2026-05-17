def p_func_args(self, p):
    p[0] = p[1] + [p[3]]

def p_func_args_single(self, p):
    """func_args : expression"""
    p[0] = [p[1]]

def p_func_args_empty(self, p):
    """func_args : empty"""
    p[0] = []

def p_empty(self, p):
    """empty :"""
    pass