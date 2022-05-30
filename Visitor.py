from abstrataVisitor import abstrataVisitor
global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class visitor (abstrataVisitor):

  def visitprogramaGOCONCRETA (self, programaGOCONCRETA):
    programaGOCONCRETA.defpackage.accept(self)
    programaGOCONCRETA.defimport.accept(self)
    programaGOCONCRETA.funcdecls.accept(self)

  def visitdefpackageCONCRETA (self, defpackageCONCRETA):
   # print (blank(), 'package', end='', sep='')
    print(defpackageCONCRETA.id, '(', end = '', sep='')

  def visitdefimportCONCRETA (self, defimportCONCRETA):
   # print (blank(), 'import', end='', sep='')
    print(defimportCONCRETA.string, '(', end = '', sep='')

  def visitfuncdecltCONCRETA (self, funcdecltCONCRETA):
    print(funcdecltCONCRETA.func, end = '', sep='')
    print(funcdecltCONCRETA.id, end = '', sep='')
    funcdecltCONCRETA.signature.accept(self)
    funcdecltCONCRETA.body.accept(self)

  def visitfuncdeclsCONCRETA (self, funcdeclsCONCRETA):
    funcdeclsCONCRETA.funcdecl.accept(self)
    
  def visitfuncdeclsCONCRETA2 (self, funcdeclsCONCRETA2):
    funcdeclsCONCRETA2.funcdecl.accept(self)
    funcdeclsCONCRETA2.funcdecls.accept(self)

  def visitsignatureCONCRETA (self, signatureCONCRETA):
    signatureCONCRETA.sigparams.accept(self)

  def visitsignatureCONCRETA2 (self, signatureCONCRETA2):
    signatureCONCRETA2.sigparams.accept(self)
    signatureCONCRETA2.funcreturn.accept(self)
     
  def visitsignatureCONCRETA3 (self, signatureCONCRETA3):
    signatureCONCRETA3.funcreturn.accept(self)
    
  def visitsigparamsCONCRETA(self, sigparamsCONCRETA):
      print('(')
      if(sigparamsCONCRETA!= None):
        print(sigparamsCONCRETA.id, end = '', sep='')
        print(sigparamsCONCRETA.type, end = '', sep='')
      print(')')

  def visitsigparamsCONCRETA2(self, sigparamsCONCRETA2):
      print('(')
      if(sigparamsCONCRETA2!= None):
        print(sigparamsCONCRETA2.id, end = '', sep='')
        print(sigparamsCONCRETA2.type,',',end = '', sep='')
        sigparamsCONCRETA2.sigparams.accept(self)
      print(')')

  def visitfuncreturnCONCRETA(self, funcreturnCONCRETA):
      if(funcreturnCONCRETA!= None):
        print(funcreturnCONCRETA.type, end = '', sep='')

  def visitbodyCONCRETA(self, bodyCONCRETA):
    print('{')
    bodyCONCRETA.stms.accept(self)
    print('}')

  def visitstmsCONCRETA(self, stmsCONCRETA):
    stmsCONCRETA.statement.accept(self)

  def visitstmsCONCRETA2(self, stmsCONCRETA2):
    stmsCONCRETA2.statement.accept(self)
    stmsCONCRETA2.stms.accept(self)
    
  def visitstatementCONCRETA(self, statementCONCRETA):
    statementCONCRETA.statement1.accept(self)

  def visitifCONCRETA(self, ifCONCRETA):
    print('if')
    ifCONCRETA.exp.accept(self)
    ifCONCRETA.body.accept(self)
    ifCONCRETA.body2.accept(self)

  #duvida pode fazer esse if?
  def visitdeclarationCONCRETA(self, declarationCONCRETA):
    print(declarationCONCRETA.var, end = '', sep='')
    print(declarationCONCRETA.id, end = '', sep='')
    print(declarationCONCRETA.type, end = '', sep='')
    if(declarationCONCRETA.exp!= None):
       print(declarationCONCRETA.exp, end = '', sep='')

  def visitforGOCONCRETA(self, forGOCONCRETA):
    print('for')
    forGOCONCRETA.body.accept(self)
    
  def visitforGOCONCRETA2(self, forGOCONCRETA2):
    print('for')
    forGOCONCRETA2.exp.accept(self)
    forGOCONCRETA2.body.accept(self)

  def visitforGOCONCRETA3(self, forGOCONCRETA3):
    print('for')
    forGOCONCRETA3.exp1.accept(self)
    forGOCONCRETA3.exp2.accept(self)
    forGOCONCRETA3.exp3.accept(self)
    forGOCONCRETA3.body.accept(self)

  def visitcallFuncCONCRETA(self, callFuncCONCRETA):
    print(callFuncCONCRETA.id, end = '', sep='')
    callFuncCONCRETA.params.accept(self)

  def visitcallFuncPSCONCRETA(self, callFuncPSCONCRETA):
    print(callFuncPSCONCRETA.id1, end = '', sep='')
    print(callFuncPSCONCRETA.id2, end = '', sep='')
    callFuncPSCONCRETA.params.accept(self)

  def visitreturnCONCRETA(self, returnCONCRETA):
    print('return')
    returnCONCRETA.exp.accept(self)

  def visitbreakCONCRETA(self, breakCONCRETA):
    print('break')
  
  def visittypeCONCRETA(self, typeCONCRETA):
    typeCONCRETA.int.accept(self)

  def visittypeCONCRETA2(self, typeCONCRETA2):
    typeCONCRETA2.string.accept(self)

  def visittypeCONCRETA3(self, typeCONCRETA3):
    typeCONCRETA3.bool.accept(self)

  
    
    
    
    
    
    
    
    

  

  
  

  
        

      
      