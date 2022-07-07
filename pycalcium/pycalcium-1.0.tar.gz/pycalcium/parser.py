import ply.yacc as yacc
def p_error(p):
    print("Syntax Error!")
def p_expression_add(p):
    'expression : expression ADD term'
    p[0] = p[1] + p[3]
def p_expression_sub(p):
    'expression : expression SUB term'
    p[0] = p[1] - p[3]
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
def p_term_mul(p):
    'term : term MUL factor'
    p[0] = p[1] * p[3]
def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
def p_factor_int(p):
    'factor : INT'
    p[0] = p[1]
def p_factor_float(p):
    'factor : FLOAT'
    p[0] = p[1]
def p_factor_expression(p):
    'factor : LPAR expression RPAR'
    p[0] = p[2]
def p_factor_expression_square(p):
    'factor : LSQU expression RSQU'
    p[0] = p[2]
def p_term_power(p):
    'term : factor POWER factor'
    p[0] = p[1] ** p[3]