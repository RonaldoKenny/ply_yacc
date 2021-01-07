from ply import yacc
import conditional

tokens = conditional.tokens
variables = {}

# custom functions starts from here

def p_writeln_expression(p):
    'statement : WRITELN LPAREN STRING RPAREN SEMICOLON statement'
    print(p[3][1:-1])

def p_writeln_params(p):
    'statement : WRITELN LPAREN STRING COMMA STRING RPAREN SEMICOLON statement'
    print(p[3][1:-1],variables[p[5]])

def p_program_name(p):
    'statement : PROGRAM STRING SEMICOLON statement'

def p_begin(p):
    'statement : BEGIN statement'
    print('This is the begin')

def p_end(p):
    'statement : END FULLSTOP'
    print('This is the end')

def p_var_int(p):
    'statement : VAR STRING COLON INTEGER SEMICOLON statement'
    variables[p[2]] = 0

def p_var_real(p):
    'statement : VAR STRING COLON REAL SEMICOLON statement'
    variables[p[2]] = 0

def p_assign(p):
    'statement : STRING ASSIGN expression SEMICOLON statement'
    variables[p[1]] = p[3]
    print(variables)

def p_compare(p):
    'statement : IF LPAREN statement MORETHAN statement RPAREN THEN'
    begin_count = 0
    end_count = 0
    if(p[3] > p[5]):
        pass

    # How to compare?
# ends here

def p_expression_plus(p):
    'expression : expression PLUS term'
    print(p[0],p[1],p[2],p[3])
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

def p_factor_var(p):
    'factor : STRING'
    p[0] = variables[p[1]]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)
 
# Build the parser
parser = yacc.yacc(debug=True)
parser.parse(conditional.data)
