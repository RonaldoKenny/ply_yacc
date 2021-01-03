from ply import yacc
import statement

tokens = statement.tokens

def p_expression_plus(p):
     'expression : expression PLUS term'
     p[0] = p[1] + p[3]
 
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_expression_statement(p):
    'expression : statement'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# custom functions starts from here

def p_writeln_expression(p):
    'statement : WRITELN LPAREN STRING RPAREN SEMICOLON statement'
    print(p[3][1:-1])

def p_program_name(p):
    'statement : PROGRAM STRING SEMICOLON statement'
    print("Program Name: " + p[2])

def p_begin(p):
    'statement : BEGIN statement'
    print("start here")

def p_end(p):
    'statement : END FULLSTOP'
    print("end here")

# ends here

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)
 
# Build the parser
parser = yacc.yacc()

# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
result = parser.parse(statement.data)