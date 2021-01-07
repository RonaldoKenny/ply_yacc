
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BEGIN COLON COMMA DIVIDE ELSE END EQUAL EXCLAMATION FULLSTOP IF INTEGER LESSTHAN LPAREN MINUS MORETHAN NUMBER PLUS PROGRAM REAL RPAREN SEMICOLON SINGLEQUOTE STRING THEN TIMES VAR WHILE WRITELNstatement : WRITELN LPAREN STRING RPAREN SEMICOLON statementstatement : WRITELN LPAREN STRING COMMA STRING RPAREN SEMICOLON statementstatement : PROGRAM STRING SEMICOLON statementstatement : BEGIN statementstatement : END FULLSTOPstatement : VAR STRING COLON INTEGER SEMICOLON statementstatement : VAR STRING COLON REAL SEMICOLON statementstatement : STRING ASSIGN expression SEMICOLON statementstatement : IF LPAREN statement MORETHAN statement RPAREN THENexpression : expression PLUS termexpression : expression MINUS termexpression : termexpression : statementterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : STRINGfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'WRITELN':([0,5,10,15,22,24,29,38,39,48,49,56,],[2,2,2,2,2,2,2,2,2,2,2,2,]),'PROGRAM':([0,5,10,15,22,24,29,38,39,48,49,56,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'BEGIN':([0,5,10,15,22,24,29,38,39,48,49,56,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'END':([0,5,10,15,22,24,29,38,39,48,49,56,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'VAR':([0,5,10,15,22,24,29,38,39,48,49,56,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'STRING':([0,4,5,7,9,10,15,22,24,28,29,30,31,32,33,38,39,48,49,56,],[3,11,3,14,16,17,3,17,3,40,3,43,43,43,43,3,3,3,3,3,]),'IF':([0,5,10,15,22,24,29,38,39,48,49,56,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,12,13,35,41,51,53,54,57,58,],[0,-4,-5,-3,-8,-1,-6,-7,-9,-2,]),'LPAREN':([2,8,10,22,30,31,32,33,],[9,15,22,22,22,22,22,22,]),'ASSIGN':([3,17,],[10,10,]),'FULLSTOP':([6,],[13,]),'NUMBER':([10,22,30,31,32,33,],[23,23,23,23,23,23,]),'SEMICOLON':([11,12,13,17,18,19,20,21,23,27,35,36,37,41,42,43,44,45,46,47,51,52,53,54,57,58,],[24,-4,-5,-18,29,-13,-12,-16,-17,39,-3,48,49,-8,-10,-18,-11,-14,-15,-19,-1,56,-6,-7,-9,-2,]),'PLUS':([12,13,17,18,19,20,21,23,34,35,41,42,43,44,45,46,47,51,53,54,57,58,],[-4,-5,-18,30,-13,-12,-16,-17,30,-3,-8,-10,-18,-11,-14,-15,-19,-1,-6,-7,-9,-2,]),'MINUS':([12,13,17,18,19,20,21,23,34,35,41,42,43,44,45,46,47,51,53,54,57,58,],[-4,-5,-18,31,-13,-12,-16,-17,31,-3,-8,-10,-18,-11,-14,-15,-19,-1,-6,-7,-9,-2,]),'MORETHAN':([12,13,26,35,41,51,53,54,57,58,],[-4,-5,38,-3,-8,-1,-6,-7,-9,-2,]),'RPAREN':([12,13,16,17,19,20,21,23,34,35,40,41,42,43,44,45,46,47,50,51,53,54,57,58,],[-4,-5,27,-18,-13,-12,-16,-17,47,-3,52,-8,-10,-18,-11,-14,-15,-19,55,-1,-6,-7,-9,-2,]),'COLON':([14,],[25,]),'COMMA':([16,],[28,]),'TIMES':([17,20,21,23,42,43,44,45,46,47,],[-18,32,-16,-17,32,-18,32,-14,-15,-19,]),'DIVIDE':([17,20,21,23,42,43,44,45,46,47,],[-18,33,-16,-17,33,-18,33,-14,-15,-19,]),'INTEGER':([25,],[36,]),'REAL':([25,],[37,]),'THEN':([55,],[57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,5,10,15,22,24,29,38,39,48,49,56,],[1,12,19,26,19,35,41,50,51,53,54,58,]),'expression':([10,22,],[18,34,]),'term':([10,22,30,31,],[20,20,42,44,]),'factor':([10,22,30,31,32,33,],[21,21,21,21,45,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> WRITELN LPAREN STRING RPAREN SEMICOLON statement','statement',6,'p_writeln_expression','conditional_yacc.py',10),
  ('statement -> WRITELN LPAREN STRING COMMA STRING RPAREN SEMICOLON statement','statement',8,'p_writeln_params','conditional_yacc.py',14),
  ('statement -> PROGRAM STRING SEMICOLON statement','statement',4,'p_program_name','conditional_yacc.py',18),
  ('statement -> BEGIN statement','statement',2,'p_begin','conditional_yacc.py',21),
  ('statement -> END FULLSTOP','statement',2,'p_end','conditional_yacc.py',25),
  ('statement -> VAR STRING COLON INTEGER SEMICOLON statement','statement',6,'p_var_int','conditional_yacc.py',29),
  ('statement -> VAR STRING COLON REAL SEMICOLON statement','statement',6,'p_var_real','conditional_yacc.py',33),
  ('statement -> STRING ASSIGN expression SEMICOLON statement','statement',5,'p_assign','conditional_yacc.py',37),
  ('statement -> IF LPAREN statement MORETHAN statement RPAREN THEN','statement',7,'p_compare','conditional_yacc.py',42),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','conditional_yacc.py',52),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','conditional_yacc.py',57),
  ('expression -> term','expression',1,'p_expression_term','conditional_yacc.py',61),
  ('expression -> statement','expression',1,'p_expression_statement','conditional_yacc.py',66),
  ('term -> term TIMES factor','term',3,'p_term_times','conditional_yacc.py',71),
  ('term -> term DIVIDE factor','term',3,'p_term_div','conditional_yacc.py',76),
  ('term -> factor','term',1,'p_term_factor','conditional_yacc.py',80),
  ('factor -> NUMBER','factor',1,'p_factor_num','conditional_yacc.py',84),
  ('factor -> STRING','factor',1,'p_factor_var','conditional_yacc.py',88),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','conditional_yacc.py',93),
]
