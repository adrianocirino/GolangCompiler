# -------------------------
# ExpressionLanguageParser.py
#----------------------

import ply.yacc as yacc
from lexico import *

# abstrata             #concreta
def p_programaGO(p):
  '''programaGO : defpackage defimport funcdecls'''
  pass

def p_defpackage(p):
  '''defpackage : PACKAGE ID'''
  pass

def p_defimport(p):
  '''defimport : IMPORT STRING'''
  pass
  
def p_funcdecl(p):
    '''funcdecl : FUNC ID signature body'''
    pass
  
def p_funcdecls(p):
    '''funcdecls : funcdecl
                 | funcdecl funcdecls'''
    pass

def p_signature(p):
  '''signature : LPAREN sigparams RPAREN 
               | LPAREN sigparams RPAREN funcreturn 
               | LPAREN RPAREN
               | LPAREN RPAREN funcreturn '''
  pass

def p_sigparams(p):
  '''sigparams : ID type
               | ID type COMMA sigparams'''
  pass

def p_funcreturn(p):
  '''funcreturn : type
                | LPAREN type RPAREN'''
  pass

def p_body(p):
  '''body : LCHAVES stms RCHAVES
          | LCHAVES RCHAVES'''
  pass

def p_stms(p):
    '''stms : statement 
            | statement stms
            | statement NEWLINE stms
            | statement NEWLINE'''
    pass
  
def p_statement(p):
    '''statement : statement1'''
    pass

#duvida statement1  IF LPAREN exp RPAREN body ELSE body IF LPAREN exp RPAREN body 
def p_statement1(p):
  '''statement1 : IF exp body ELSE body
                | IF exp body
                | declaration
                | for
                | callFunc
                | callFuncPS
                | return
                | break'''
  pass

def p_for(p):
  '''for : FOR body
         | FOR exp body
         | FOR exp SEMICOLON exp SEMICOLON exp body''' 
  pass

def p_declaration(p):
    '''declaration : VAR ID type 
                   | VAR ID type ASSIGN exp
                   | VAR ID type COLONEQ exp
                   | VAR ID type SEMICOLON
                   | VAR ID type ASSIGN exp SEMICOLON
                   | VAR ID type COLONEQ exp SEMICOLON'''
    pass
  
def p_type(p):
    '''type : INT
            | STRING
            | BOOL'''
    pass

def p_exp_exp1(p):
  '''exp : exp1'''
  pass
  
 #precedencia 
  # () 
  # Operadores unario ! ++ --  not incremento decremento
  # * / % mult div modulo
  # + - adiçao sub
  # < > <= >= menor maior 
  # == =! igual diferente
  # &  and
  # | or
  # = =+ =- atribuiçao 

def p_exp1(p):
    ''' exp1 : exp1 ASSIGN exp2
             | exp1 COLONEQ exp2
             | exp2'''
    pass

def p_exp2(p):
    '''exp2 : exp2 OR exp3
            | exp3'''
    pass
  
def p_exp3(p):
    '''exp3 : exp3 AND exp4
            | exp4'''
    pass
#parei aqui
def p_exp4(p):
  '''exp4 : exp4 EQUALS exp5
          | exp4 DIFFERENT exp5
          | exp5'''
  pass

def p_exp5(p):
  '''exp5 : exp5 LESS exp6
          | exp5 GREATER exp6
          | exp5 LESS_EQUAL exp6
          | exp5 GREATER_EQUAL exp6
          | exp6'''
  pass

def p_exp6(p):
  '''exp6 : exp6 PLUS exp7
          | exp6 MINUS exp7
          | exp7'''
  pass

def p_exp7(p):
  '''exp7 : exp7 TIMES exp8
          | exp7 DIVIDE exp8
          | exp7 MOD exp8
          | exp8'''
  pass

def p_exp8(p):
  '''exp8 : exp8 DPLUS
          | exp8 DMINUS
          | exp9'''
  pass

def p_exp9(p):
  '''exp9 : NOT exp9
          | NUMBER
          | STRING
          | ID 
          | TRUE
          | FALSE
          | LPAREN exp RPAREN'''
  pass
# | 
def p_return(p):
    '''return : RETURN exp
              | RETURN
              | RETURN exp SEMICOLON
              | RETURN SEMICOLON'''
    pass
  
def p_break(p):
    '''break : BREAK
             | BREAK SEMICOLON'''
    pass

def p_callFunc(p):
    '''callFunc : ID LPAREN params RPAREN
                | ID LPAREN RPAREN
                | ID LPAREN params RPAREN SEMICOLON
                | ID LPAREN RPAREN SEMICOLON'''
    pass

def p_callFuncPS(p):
    '''callFuncPS : ID DOT ID LPAREN params RPAREN
                  | ID DOT ID LPAREN RPAREN
                  | ID DOT ID LPAREN params RPAREN SEMICOLON
                  | ID DOT ID LPAREN RPAREN SEMICOLON'''
    pass
def p_params(p):
    '''params : exp COMMA params
              | exp'''
    pass
  
def p_error(p):
    print("Syntax error in input!")

#parser = yacc.yacc()
#parser.parse(debug = True)




