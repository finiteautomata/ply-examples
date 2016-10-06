"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from lexer import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_plus(p):
    'expression : expression MINUS term'
    p[0] = p[1] + p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'



# Build the parser
parser = yacc.yacc(debug=True)

if __name__ == '__main__':
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue

        result = parser.parse(s)
        print(result)
