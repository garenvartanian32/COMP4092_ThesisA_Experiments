def p_formula_atom(self, p):
    p[0] = p[1]

def p_formula_not(self, p):
    """formula : NOT formula"""
    p[0] = ('not', p[2])

def p_formula_and(self, p):
    """formula : formula AND formula"""
    p[0] = ('and', p[1], p[3])

def p_formula_or(self, p):
    """formula : formula OR formula"""
    p[0] = ('or', p[1], p[3])

def p_formula_implies(self, p):
    """formula : formula IMPLIES formula"""
    p[0] = ('implies', p[1], p[3])

def p_formula_iff(self, p):
    """formula : formula IFF formula"""
    p[0] = ('iff', p[1], p[3])

def p_formula_parentheses(self, p):
    """formula : LPAREN formula RPAREN"""
    p[0] = p[2]