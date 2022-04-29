# -------------------------
# ExpressionLanguageParser.py
#----------------------

import ply.yacc as yacc
import ply.lex as lex
from lexico import tokens

def p_exp_exp1(p):
   '''exp : exp1'''


def p_exp_plus(p):
    '''exp : exp PLUS exp1'''

def p_exp_minus(p):
    '''exp : exp MINUS exp1 '''
  
def p_exp_times(p):
    '''exp : exp TIMES exp1'''
  
def p_exp_divide(p):
    '''exp : exp DIVIDE exp1'''
 
def p_exp_equals(p):
    '''exp : exp EQUALS exp1'''

def p_exp_different(p):
    '''exp : exp DIFFERENT exp1'''
  
parser = yacc.yacc()




