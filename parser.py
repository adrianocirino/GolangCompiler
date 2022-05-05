# -------------------------
# ExpressionLanguageParser.py
#----------------------

import ply.yacc as yacc
from lexico import *

# package main

# import "fmt"

# func main() {
#   
# }

def p_funcdecl(p):
    '''funcdecl : FUNC ID signature body'''

def p_signature(p):
  '''signature : LPAREN sigparams RPAREN
               | LPAREN RPAREN '''

# func repeat(word string, reps int) (string, error) {
def p_sigparams(p):
  '''sigparams : ID type
                 | ID type COMMA sigparams'''

def p_body(p):
  '''body : LCHAVES stms RCHAVES
          | LCHAVES stms RCHAVES functionDecl'''

def p_stms(p):
    '''stms: statement SEMICOLON
                     | statement SEMICOLON stms'''
def p_statement(p):
    '''statement : exp
                 | declaration
                 | for
                 | if
                 | return '''
  
def p_declaration(p):
    '''declaration : typeDecl '''  
  
def p_typeDecl(p):
   '''typeDecl : ID type'''

def p_type(p):
    '''type : INT
            | STRING
            | VAR
            | BOOL'''
  
def p_exp_exp1(p):
   '''exp : exp1'''
   pass

def p_exp2(p):
  '''exp1 : exp2'''
  pass

def p_exp3(p):
  '''exp2 : NUMBER'''
  pass

def p_exp_plus(p):
    '''exp : exp PLUS exp1'''
    pass

def p_exp_minus(p):
    '''exp : exp MINUS exp1 '''
    pass
  
def p_exp_times(p):
    '''exp1 : exp1 TIMES exp2'''
    pass
  
def p_exp_divide(p):
    '''exp1 : exp1 DIVIDE exp2'''
    pass

def p_exp(p):
    '''expression : expression OR exp1
                  | exp1'''

def p_exp1(p):
    '''exp1 : exp1 AND exp2
            | exp2'''
 
# def p_exp_equals(p):
#     '''exp : exp EQUALS exp1'''
#     pass

# def p_exp_different(p):
#     '''exp : exp DIFFERENT exp1'''
#     pass
  
parser = yacc.yacc()
parser.parse(debug = True)




