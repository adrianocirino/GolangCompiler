# -------------------------
# ExpressionLanguageParser.py
#----------------------

import ply.yacc as yacc
from lexico import *

def p_programaGO(p):
  '''programaGO : defpackage defimport funcdecls'''
  pass

def p_defpackage(p):
  '''defpackage : PACKAGE ID'''
  pass

def p_defimport(p):
  '''defimport : IMPORT ID'''
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
                | LPAREN type RPAREN '''
  pass

def p_body(p):
  '''body : LCHAVES stms RCHAVES
          | LCHAVES RCHAVES'''
  pass

def p_stms(p):
    '''stms : statement 
            | statement stms'''
    pass
  
def p_statement(p):
    '''statement : statement1
                 | statement2'''
    pass
#não é obrigatorio parenteses, é obrigatorio colchetes
def p_statement1(p):
  '''statement1 : IF LPAREN exp RPAREN statement1 ELSE statement1
                | IF exp statement1 ELSE statement1
                | declaration
                | for
                | statement1
                | statement2
                | return'''
  pass

def p_statement2(p):
  '''statement2 : IF LPAREN exp RPAREN statement 
                | IF exp statement 
                | IF exp statement1 ELSE statement2
                | IF LPAREN exp RPAREN statement1 ELSE statement2'''
  pass
# for{}
# for i < 5{}
# for for i := 0; i < 15; i++
# for range sharks 
# for indice, valor := range serie
def p_for(p):
  '''for : FOR
         | FOR exp 
         | FOR exp SEMICOLON exp SEMICOLON exp
         | FOR RANGE exp 
         | FOR exp COMMA exp ASSIGN RANGE exp''' 
  pass

  
#atribuição de duas formas = ou :=
def p_declaration(p):
    '''declaration : ID type
                   | ID type ASSIGN exp
                   | ID type COLONEQ exp'''
    pass
  
def p_type(p):
    '''type : INT
            | STRING
            | VAR
            | BOOL'''
    pass

def p_exp_exp1(p):
  '''exp : exp1'''
  pass
  
def p_exp1(p):
  '''exp1 : NUMBER
          | STRING
          | ID 
          | TRUE
          | FALSE
          | LPAREN exp RPAREN
          | exp2'''
  pass

#ver precedencia 
  # () [] 
  # Operadores unario  ++ --  incremento decremento
  # * / % mult div modulo
  # + - adiçao sub
  # < > <= >= menor maior 
  # == =! igual diferente
  # &  and
  # | or
  # &&
  # || 
  # = =+ =- atribuiçao 
  # , 

def p_exp2(p):
  '''exp2 : exp2 DPLUS
          | exp2 DMINUS
          | NOT exp2
          | exp3'''
  pass

def p_exp3(p):
  '''exp3 : exp3 TIMES exp4
          | exp3 DIVIDE exp4
          | exp3 MOD exp4
          | exp4'''
  pass

def p_exp4(p):
  '''exp4 : exp4 PLUS exp5
          | exp4 MINUS exp5
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
  '''exp6 : exp6 EQUALS exp7
          | exp6 DIFFERENT exp7
          | exp7'''
  pass

def p_exp7(p):
    '''exp7 : exp7 AND exp8
            | exp8'''
    pass

def p_exp8(p):
    '''exp8 : exp8 OR exp9
            | exp9'''
    pass
  
def p_exp9(p):
    ''' exp9 : exp9 ASSIGN exp1
             | exp9 COLONEQ exp1
             | exp1'''
    pass
  
def p_return(p):
    '''return : RETURN exp
              | RETURN'''
    pass
def p_error(p):
    print("Syntax error in input!")

#FOR estrutura
#RANGE

parser = yacc.yacc()
parser.parse(debug = True)




