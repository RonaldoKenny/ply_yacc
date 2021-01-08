from ply import yacc
import conditional

tokens = conditional.tokens
variables = {}
check = {}

# custom functions starts from here

def p_start(p):
    'start : program declare BEGIN statement END FULLSTOP'

def p_program(p):
    'program : PROGRAM STRING SEMICOLON'
    print("Program: " + p[2])

def p_declare(p):
    '''declare  : VAR initialize declare
                | initialize declare
                | '''

def p_initialize(p):
    'initialize : STRING COLON dataypes SEMICOLON'
    if p[3] == "integer":
        variables[p[1]] = 0
    elif p[3] == "real":
        variables[p[1]] = 0.0
    check[p[1]] = -1

def p_datatype(p):
    '''dataypes : INTEGER
                | REAL'''
    p[0] = p[1]

def p_statements(p):
    '''statement    : assign statement
                    | print statement
                    | print_var statement
                    | condition statement
                    | '''

def p_print(p):
    'print : WRITELN LPAREN STRING RPAREN SEMICOLON'
    print(p[3][1:-1])

def p_print_var(p):
    'print_var : WRITELN LPAREN STRING COMMA STRING RPAREN SEMICOLON'
    if check[p[5]] != 0:
        print(p[3][1:-1] + str(variables[p[5]]))

def p_assign(p):
    'assign : STRING ASSIGN expression SEMICOLON'
    if isinstance(p[3], int):
        variables[p[1]] = p[3]
    else:
        if check[p[3]] != 0:
            variables[p[1]] = variables[p[3]]
            check[p[1]] = 1
        else: 
            check[p[1]] = 0

def p_if(p):
    'condition : IF expression then else'

def p_compare(p):
    '''expression : STRING MORETHAN STRING'''
    if(p[2] == '>'):
        if variables[p[1]] > variables[p[3]]:
            check[p[1]] = 1
            check[p[3]] = 0
        else:
            check[p[1]] = 0
            check[p[3]] = 1

def p_then(p):
    '''then : THEN BEGIN statement END'''

def p_else(p):
    '''else : ELSE BEGIN statement END SEMICOLON'''

# ends here

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

def p_factor_var(p):
    'factor : STRING'
    p[0] = p[1]

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