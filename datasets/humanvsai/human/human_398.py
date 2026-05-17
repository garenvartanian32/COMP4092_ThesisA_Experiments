def p_func_args(self, p):
        'func_args : func_args COMMA expression'
        p[0] = p[1] + (p[3],)
        p.set_lineno(0, p.lineno(1))