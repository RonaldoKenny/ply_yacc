from ply import yacc
import statement_lex

tokens = statement_lex.tokens

# custom functions starts from here

def p_program_name(p):
    'start : program BEGIN statement END FULLSTOP'

def p_program(p):
    'program : PROGRAM STRING SEMICOLON'
    print("Program: " + p[2])

def p_writeln_expression(p):
    'statement : WRITELN LPAREN STRING RPAREN SEMICOLON'
    print(p[3][1:-1])

# ends here

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)
 
# Build the parser
parser = yacc.yacc(debug = True, start = 'start', write_tables = False)

parser.parse(statement_lex.data)