# Nama: William Antony (2201767775)
# Nama: Limas Jaya Akeh (2201763240)
# Nama: Ronaldo Kenny Chandra (2201763234)
# Nama: Andreas Aditya Alvaro Haryanto (2201767655)
# Nama: Rio Nagano (2201767232)
# Nama: Muhammad Alvito Kuntjoro (2201788073)

# GROUP ASSIGNMENT - LEXER ANALYSER

from ply import lex, yacc

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'
t_SINGLEQUOTE = r'\''
t_COMMA = r','
t_EXCLAMATION = r'!'
t_FULLSTOP = r'\.'
t_ASSIGN = r':='
t_COLON = r'\:'

reserved = {
    'program' : 'PROGRAM', 
    'begin' : 'BEGIN', 
    'writeln' : 'WRITELN', 
    'end' : 'END',
    'var' : 'VAR',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'integer' : 'INTEGER',
    'real' : 'REAL'
}

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'STRING')    # Check for reserved words
     return t

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'STRING',
    'SEMICOLON',
    'SINGLEQUOTE',
    'COMMA',
    'ASSIGN',
    'EQUAL',
    'COLON',
    'EXCLAMATION',
    'FULLSTOP',
] + list(reserved.values())

lexer = lex.lex()

test = open("arithmetic.txt", "r")
data = test.read()

data = data.lower()

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)