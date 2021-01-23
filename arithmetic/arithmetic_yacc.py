from ply import yacc
import arithmetic_lex

tokens = arithmetic_lex.tokens
variables = {}

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
    if p[4] == "integer":
        variables[p[2]] = 0
    elif p[4] == "real":
        variables[p[2]] = 0.0
    # print(p[2] + ' is now initialized')

def p_datatype(p):
    '''dataypes : INTEGER
                | REAL'''
    p[0] = p[1]

def p_statements(p):
    '''statement    : assign statement
                    | print statement
                    | print_var statement
                    | '''

def p_print(p):
    'print : WRITELN LPAREN STRING RPAREN SEMICOLON'
    print(p[3][1:-1])

def p_print_var(p):
    'print_var : WRITELN LPAREN STRING COMMA STRING RPAREN SEMICOLON'
    print(p[3][1:-1] + str(variables[p[5]]))

def p_assign(p):
    'assign : STRING ASSIGN expression SEMICOLON'
    variables[p[1]] = p[3]

# ends here

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)
 
# Build the parser
parser = yacc.yacc()
parser.parse(arithmetic_lex.data)