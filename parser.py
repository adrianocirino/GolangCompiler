# -------------------------
# ExpressionLanguageParser.py
#----------------------

import ply.yacc as yacc
from lexico import *
import sintaxeAbstrata as sa

# quantidade de paramentros for igual a 3
 # if (len(p) == 3):
 #        p[0] = [p[1]] + p[2] posição do paramentro
 #    else:
 #        p[0] = [p[1]]
# abstrata             #concreta
def p_programaGO(p):
  '''programaGO : defpackage defimport funcdecls'''
  p[0] = sa.programaGOCONCRETA(p[1], p[2], p[3])

def p_defpackage(p):
  '''defpackage : PACKAGE ID NEWLINE'''
  p[0] = sa.defpackageCONCRETA(p[2])

def p_defimport(p):
  '''defimport : IMPORT STRING NEWLINE'''
  p[0] = sa.defimportCONCRETA(p[2])

def p_funcdecl(p):
    '''funcdecl : FUNC ID signature NEWLINE body NEWLINE
                | FUNC ID signature body
                | FUNC ID signature body NEWLINE'''
    if(len(p) == 7):
      p[0] = sa.funcdecltCONCRETA(p[1], p[2], p[3], p[5])
    elif(len(p) == 6):
      p[0] = sa.funcdecltCONCRETA(p[1], p[2], p[3], p[4])
    else:
      p[0] = sa.funcdecltCONCRETA(p[1], p[2], p[3], p[4])
      
  
def p_funcdecls(p):
    '''funcdecls : funcdecl 
                 | funcdecl funcdecls '''
    if(len(p)== 2):
      p[0] = sa.funcdeclsCONCRETA(p[1])
    else:
      p[0] = sa.funcdeclsCONCRETA2(p[1], p[2])

#duvida
def p_signature(p):
  '''signature : LPAREN sigparams RPAREN 
               | LPAREN sigparams RPAREN funcreturn 
               | LPAREN RPAREN
               | LPAREN RPAREN funcreturn '''
  if(p[2] == 'sigparams'):
    p[0] = sa.signatureCONCRETA(p[2])
  elif(len(p) == 5): 
    p[0] = sa.signatureCONCRETA2(p[2], p[4])
 # elif(p[3] == 'funcreturn'):
    #p[0] = sa.signatureCONCRETA3(p[3])
  else:
    p[0] = sa.signatureCONCRETA(None)

def p_sigparams(p):
  '''sigparams : ID type
               | ID type COMMA sigparams'''
  if(len(p) == 3):
    p[0] = sa.sigparamsCONCRETA(p[1], p[2])
  else:
    p[0] = sa.sigparamsCONCRETA2(p[1], p[2], p[4])

def p_funcreturn(p):
  '''funcreturn : type
                | LPAREN type RPAREN'''
  if(len(p) == 2):
    p[0] = sa.funcreturnCONCRETA(p[1])
  else:
     p[0] = sa.funcreturnCONCRETA(p[2])
    
def p_body(p):
  '''body : LCHAVES  NEWLINE stms  RCHAVES
          | LCHAVES  NEWLINE RCHAVES'''
  if(len(p) == 5):
    p[0] = sa.bodyCONCRETA(p[3])
  else:
    p[0] = sa.bodyCONCRETA(None)

#duvida se posso fazer apenas 1 if nesse caso
def p_stms(p):
    '''stms : statement 
            | statement NEWLINE stms
            | statement NEWLINE'''
    if(len(p) == 4):
      p[0] = sa.stmsCONCRETA2(p[1], p[3])
    else: 
      p[0] = sa.stmsCONCRETA(p[1])
      
def p_statement(p):
    '''statement : statement1'''
    p[0] = sa.statementCONCRETA(p[1])

#duvida apartir de declaração
def p_statement1(p):
  '''statement1 : IF exp body ELSE body
                | IF exp body
                | declaration
                | for
                | callFunc
                | callFuncPS
                | return
                | break'''
  if(len(p) == 6):
    p[0] = sa.ifCONCRETA(p[2], p[3], p[4])
  elif(len(p) == 4):
    p[0] = sa.ifCONCRETA(p[2], p[3], None)
  elif(p[1] == 'declaration'):
    p[0] = sa.declarationCONCRETA(p[1])
  elif(p[1] == 'for'):
    p[0] = sa.forCONCRETA(p[1])
  elif(p[1] == 'callFunc'):
    p[0] = sa.callFuncCONCRETAC(p[1])
  elif(p[1] == 'callFuncPS'):
    p[0] = sa.callFuncPSCONCRETA(p[1])
  elif(p[1] == 'return'):
    p[0] = sa.returnCONCRETA(p[1])
  elif(p[1] == 'break'):
    p[0] = sa.breakCONCRETA(p[1])
  else:
    print('Gerei None', p[1])
  
def p_for(p):
  '''for : FOR body
         | FOR exp body
         | FOR exp SEMICOLON exp SEMICOLON exp body''' 
  if(len(p) == 3):
    p[0] = sa.forGOCONCRETA(p[2])
  elif(len(p) == 4):
    p[0] = sa.forGOCONCRETA2(p[2], p[3])
  else:
    p[0] = sa.forGOCONCRETA3(p[2], p[4], p[6], p[7])

def p_declaration(p):
    '''declaration : VAR ID type 
                   | VAR ID type ASSIGN exp
                   | VAR ID type COLONEQ exp
                   | VAR ID type SEMICOLON
                   | VAR ID type ASSIGN exp SEMICOLON
                   | VAR ID type COLONEQ exp SEMICOLON'''
    if(len(p) == 4):
      p[0] = sa.declarationCONCRETA(p[1], p[2], p[3], None)
    elif(len(p) == 6):
      p[0] = sa.declarationCONCRETA(p[1], p[2], p[3], p[5])
    elif(len(p) == 7):
      p[0] = sa.declarationCONCRETA(p[1], p[2], p[3], p[5])
    else: 
      p[0] = sa.declarationCONCRETA(p[1], p[2], p[3], None)
    
def p_type(p):
    '''type : INT
            | STRING
            | BOOL'''
    if(p[1] == 'INT'):
      p[0] = sa.typeCONCRETA(p[1])
    elif(p[1] == 'STRING'):
      p[0] = sa.typeCONCRETA2(p[1])
    else:
      p[0] = sa.typeCONCRETA3(p[1])
    
def p_exp_exp1(p):
  '''exp : exp1'''
  p[0] = sa.expCONCRETA(p[1])
 
def p_exp1(p):
    ''' exp1 : exp1 ASSIGN exp2
             | exp1 COLONEQ exp2
             | exp2'''
    if(len(p) == 2):
      p[0] = p[1]
    elif(p[2] == 'ASSIGN'):
      p[0] = sa.expASSIGN(p[1], p[3])
    else: 
      p[0] = sa.expCOLONEQ(p[1], p[3])

def p_exp2(p):
    '''exp2 : exp2 OR exp3
            | exp3'''
    if(len(p) == 2):
      p[0] = p[1]
    else:
      p[0] = sa.expOR(p[1], p[3])
  
def p_exp3(p):
    '''exp3 : exp3 AND exp4
            | exp4'''
    if(len(p) == 2):
      p[0] = p[1]
    else:
      p[0] = sa.expAND(p[1], p[3])

def p_exp4(p):
  '''exp4 : exp4 EQUALS exp5
          | exp4 DIFFERENT exp5
          | exp5'''
  if(len(p) == 2):
      p[0] = p[1]
  elif(p[2] == 'EQUALS'):
      p[0] = sa.expEQUALS(p[1], p[3])
  else: 
      p[0] = sa.expDIFFERENT(p[1], p[3])

def p_exp5(p):
  '''exp5 : exp5 LESS exp6
          | exp5 GREATER exp6
          | exp5 LESS_EQUAL exp6
          | exp5 GREATER_EQUAL exp6
          | exp6'''
  if(len(p) == 2):
      p[0] = p[1]
  elif(p[2] == 'LESS'):
      p[0] = sa.expLESS(p[1], p[3])
  elif(p[2] == 'GREATER'): 
      p[0] = sa.expGREATER(p[1], p[3])
  elif(p[2] == 'LESS_EQUAL'): 
      p[0] = sa.expLESS_EQUAL(p[1], p[3])
  else:
      p[0] = sa.expGREATER_EQUAL(p[1], p[3])
  
def p_exp6(p):
  '''exp6 : exp6 PLUS exp7
          | exp6 MINUS exp7
          | exp7'''
  if(len(p) == 2):
      p[0] = p[1]
  elif(p[2] == 'PLUS'):
      p[0] = sa.expPLUS(p[1], p[3])
  else: 
      p[0] = sa.expMINUS(p[1], p[3])

def p_exp7(p):
  '''exp7 : exp7 TIMES exp8
          | exp7 DIVIDE exp8
          | exp7 MOD exp8
          | exp8'''
  if(len(p) == 2):
      p[0] = p[1]
  elif(p[2] == 'TIMES'):
      p[0] = sa.expTIMES(p[1], p[3])
  elif(p[2] == 'DIVIDE'): 
      p[0] = sa.expDIVIDE(p[1], p[3])
  else:
      p[0] = sa.expMOD(p[1], p[3])

def p_exp8(p):
  '''exp8 : exp8 DPLUS
          | exp8 DMINUS
          | exp9'''
  if(len(p) == 2):
      p[0] = p[1]
  elif(p[2] == 'DPLUS'):
      p[0] = sa.expDPLUS(p[1])
  else: 
      p[0] = sa.expDMINUSMINUS(p[1])

def p_exp9(p):
  '''exp9 : NOT exp9
          | NUMBER
          | STRING
          | ID 
          | TRUE
          | FALSE
          | LPAREN exp RPAREN'''
  if(len(p) == 3):
      p[0] = sa.expNOT(p[2])
  elif(p[1] == 'NUMBER'):
      p[0] = sa.expNUMBER(p[1])
  elif(p[1] == 'STRING'):
      p[0] = sa.expSTRING(p[1])
  elif(p[1] == 'ID'):
      p[0] = sa.expID(p[1])
  elif(p[1] == 'TRUE'):
      p[0] = sa.expTRUE(p[1])
  elif(p[1] == 'FALSE'):
      p[0] = sa.expFALSE(p[1])

def p_return(p):
    '''return : RETURN exp
              | RETURN
              | RETURN exp SEMICOLON
              | RETURN SEMICOLON'''
    if(len(p) == 3 ):
      p[0] = sa.returnCONCRETA(p[2])
    elif(len(p) == 4):
      p[0] = sa.returnCONCRETA(p[2])
    elif(p[2] == 'SEMICOLON'):
      p[0] = sa.returnCONCRETA(None)
    else:
      p[0] = sa.returnCONCRETA(None)
      
def p_break(p):
    '''break : BREAK
             | BREAK SEMICOLON'''
    p[0] = sa.breakCONCRETA()
  
def p_callFunc(p):
    '''callFunc : ID LPAREN params RPAREN
                | ID LPAREN RPAREN
                | ID LPAREN params RPAREN SEMICOLON
                | ID LPAREN RPAREN SEMICOLON'''
    if(len(p) == 5 or len(p) == 6):
      p[0] = sa.callFuncCONCRETA(p[1], p[3])
    else:
      p[0] = sa.callFuncCONCRETA(p[1], None)
      

def p_callFuncPS(p):
    '''callFuncPS : ID DOT ID LPAREN params RPAREN
                  | ID DOT ID LPAREN RPAREN
                  | ID DOT ID LPAREN params RPAREN SEMICOLON
                  | ID DOT ID LPAREN RPAREN SEMICOLON'''
    
    if(len(p) == 7 or len(p) == 8):
      p[0] = sa.callFuncPSCONCRETA(p[1], p[3], p[5])
    else:
      p[0] = sa.callFuncPSCONCRETA(p[1],p[3], None)

def p_params(p):
    '''params : exp COMMA params
              | exp'''
    if(len(p) == 2):
      p[0] = sa.paramsCONCRETA(p[1], None)
    else:
      p[0] = sa.paramsCONCRETA(p[1], p[3])
  
def p_error(p):
    print("Syntax error in input!")

#parser = yacc.yacc()
#parser.parse(debug = True)




