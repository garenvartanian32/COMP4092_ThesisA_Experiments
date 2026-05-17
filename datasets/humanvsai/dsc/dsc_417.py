def p_formula_atom(self, p):
    """formula : ATOM
               | TRUE
               | FALSE"""
    if p[1] == 'ATOM':
        # Do something with the ATOM
    elif p[1] == 'TRUE':
        # Do something with TRUE
    elif p[1] == 'FALSE':
        # Do something with FALSE