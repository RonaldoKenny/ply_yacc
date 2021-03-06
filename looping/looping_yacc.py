from ply import yacc
import looping_lex

tokens = looping_lex.tokens
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
    if p[3] == "integer":
        variables[p[2]] = 0
    elif p[3] == "real":
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
                    | condition statement
                    | loop statement
                    | '''
    if(len(p) > 1):
        if(p[1] != None):
            p[0] = p[1]
            return p[0]
        
def p_print(p):
    'print : WRITELN LPAREN STRING RPAREN SEMICOLON'
    print(p[3][1:-1])

def p_print_without_ln(p):
    'print : WRITE LPAREN STRING COMMA STRING RPAREN SEMICOLON'
    print((str(variables[p[3]]) + p[5][1:-1]))

def p_print_var(p):
    'print_var : WRITELN LPAREN STRING COMMA STRING RPAREN SEMICOLON'
    print(p[3][1:-1] + str(variables[p[5]]))

def p_assign(p):
    'assign : STRING ASSIGN expression SEMICOLON'
    variables[p[1]] = p[3]
    p[0] = p[3]
    return p[0]

def p_assign_no_semicolon(p):
    'assign : STRING ASSIGN expression'
    variables[p[1]] = p[3]
    p[0] = p[3]
    
def p_loop(p):
    'loop : FOR statement TO expression DO BEGIN condition END SEMICOLON'
    while(p[2] < p[4]):
        #p_condition(p)
        p[2] = p[2] + 1

def p_condition(p):
    'condition : IF compare THEN BEGIN statement END SEMICOLON'
    p[0] = p[5]
    if(p[2]):
        p_statements(p)
        

def p_compare(p):
    'compare : LPAREN STRING MOD NUMBER RPAREN NOTEQUAL NUMBER'
    if(p[2] == '>'):
        p[0] = variables[p[1]] > variables[p[3]]
        p[0] = True
        return p[0]
    if(p[6] == '<>'):
        # print('Enter Mod')
        # print('the p[2] is', p[2], 'while the p4 is', p[4], 'when the p7 is', p[7])
        p[0] = (variables[p[2]]%p[4]) != p[7]
        p[0] = True
        return p[0]
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
parser.parse(looping_lex.data)
