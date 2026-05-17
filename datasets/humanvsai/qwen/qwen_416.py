def p_include_file(p):
    p[0] = ('include_file', p[1], p[3])

def p_program(p):
    """program : statement_list"""
    p[0] = ('program', p[1])

def p_statement_list(p):
    """statement_list : statement
                      | statement_list statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    """statement : assignment
                 | print_statement"""
    p[0] = p[1]

def p_assignment(p):
    """assignment : IDENTIFIER ASSIGN expression NEWLINE"""
    p[0] = ('assignment', p[1], p[3])

def p_print_statement(p):
    """print_statement : PRINT expression NEWLINE"""
    p[0] = ('print_statement', p[2])

def p_expression(p):
    """expression : term
                  | expression PLUS term
                  | expression MINUS term"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    """term : factor
            | term TIMES factor
            | term DIVIDE factor"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_factor(p):
    """factor : NUMBER
              | IDENTIFIER
              | LPAREN expression RPAREN"""
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]

def p_error(p):
    print('Syntax error in input!')
import ply.yacc as yacc
result = yacc.parse('include testfile\nx = 10\nprint x\n')