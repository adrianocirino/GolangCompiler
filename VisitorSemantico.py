from abstrataVisitor import abstrataVisitor
import symbolTable as st
from Visitor import Visitor

import sintaxeAbstrata as sa

def coercion(type1, type2):
  if (type1 == st.INT and type2 == st.INT):
      return st.INT
  else:
    return None

class GoSemanticVisitor(abstrataVisitor):
  def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

  def visitprogramaGOCONCRETA (self, programaGOCONCRETA):
    programaGOCONCRETA.defpackage.accept(self)
    programaGOCONCRETA.defimport.accept(self)
    programaGOCONCRETA.funcdecls.accept(self)

  def visitdefpackageCONCRETA (self, defpackageCONCRETA):
    return [defpackageCONCRETA.id, defpackageCONCRETA.type]

  def visitdefimportCONCRETA (self, defimportCONCRETA):
    return [defimportCONCRETA.id, defimportCONCRETA.type]
    

  def visitfuncdecltCONCRETA (self, funcdecltCONCRETA):
    if (funcdecltCONCRETA.signature != None):
      funcdecltCONCRETA.signature.accept(self)
    funcdecltCONCRETA.body.accept(self)

  def visitfuncdeclsCONCRETA (self, funcdeclsCONCRETA):
    funcdeclsCONCRETA.funcdecl.accept(self)
    
  def visitfuncdeclsCONCRETA2 (self, funcdeclsCONCRETA2):
    funcdeclsCONCRETA2.funcdecl.accept(self)
    funcdeclsCONCRETA2.funcdecls.accept(self)

  def visitsignatureCONCRETA (self, signatureCONCRETA):
      params = {}
      if (signatureCONCRETA.sigParams!= None):
        params = signatureCONCRETA.sigParams.accept(self)
        st.addFunction(signatureCONCRETA.id, params, signatureCONCRETA.type)
      else:
        st.addFunction(signatureCONCRETA.id, params, signatureCONCRETA.type)
      st.beginScope(signatureCONCRETA.id)
      for k in range(0, len(params), 2):
        st.addVar(params[k], params[k+1])

    
      
  def visitsignatureCONCRETA2 (self, signatureCONCRETA2):    
    params = {}
    if (signatureCONCRETA2.sigParams!= None):
      params = signatureCONCRETA2.sigParams.accept(self)
      params = signatureCONCRETA2.funcreturn.accept(self)
      st.addFunction(signatureCONCRETA2.id, params, signatureCONCRETA2.type)
    else:
      st.addFunction(signatureCONCRETA2.id, params, signatureCONCRETA2.type)
    st.beginScope(signatureCONCRETA2.id)
    for k in range(0, len(params), 2):
      st.addVar(params[k], params[k+1])
      
     
  def visitsignatureCONCRETA3 (self, signatureCONCRETA3):
    params = {}
    if (signatureCONCRETA3.funcreturn!= None):
      params = signatureCONCRETA3.funcreturn.accept(self)
      st.addFunction(signatureCONCRETA3.id, params, signatureCONCRETA3.type)
    else:
      st.addFunction(signatureCONCRETA3.id, params, signatureCONCRETA3.type)
    st.beginScope(signatureCONCRETA3.id)
    for k in range(0, len(params), 2):
      st.addVar(params[k], params[k+1])
    
  def visitsigparamsCONCRETA(self, sigparamsCONCRETA):
        return [sigparamsCONCRETA.id, sigparamsCONCRETA.type]

  def visitsigparamsCONCRETA2(self, sigparamsCONCRETA2):
      return sigparamsCONCRETA2.id, sigparamsCONCRETA2.type + sigparamsCONCRETA2.sigParams.accept(self)

  def visitfuncreturnCONCRETA(self, funcreturnCONCRETA):
      if(funcreturnCONCRETA!= None):
        return [funcreturnCONCRETA.id, funcreturnCONCRETA.type]

  def visitbodyCONCRETA(self, bodyCONCRETA):
    if(bodyCONCRETA.stms!=None): 
      bodyCONCRETA.stms.accept(self)

  def visitstmsCONCRETA(self, stmsCONCRETA):
   if(stmsCONCRETA.statement!=None):
     stmsCONCRETA.statement.accept(self)

  def visitstmsCONCRETA2(self, stmsCONCRETA2): 
    stmsCONCRETA2.statement.accept(self)
    if(stmsCONCRETA2.stms!=None):
      stmsCONCRETA2.stms.accept(self)
    
  def visitstatementCONCRETA(self, statementCONCRETA):
    if(statementCONCRETA.statement1!=None):
      statementCONCRETA.statement1.accept(self)

  def visitifCONCRETA(self, ifCONCRETA):
        st.beginScope(st.IF)
        ifCONCRETA.Expression.accept(self)
        ifCONCRETA.Block.accept(self)
        st.varCheck(st.endScope())
        if(ifCONCRETA.body2!=None):
          ifCONCRETA.body2.accept(self)
          st.varCheck(st.endScope())

  def visitforGOCONCRETA(self, forGOCONCRETA):
        st.beginScope(st.FOR)
        forGOCONCRETA.body.accept(self)
        st.varCheck(st.endScope())

  def visitforGOCONCRETA2(self, forGOCONCRETA2):
        st.beginScope(st.FOR)
        forGOCONCRETA2.exp.accept(self)
        forGOCONCRETA2.body.accept(self)
        st.varCheck(st.endScope())

  
  def visitforGOCONCRETA3(self, forGOCONCRETA3):
        st.beginScope(st.FOR)
        forGOCONCRETA3.exp1.accept(self)
        forGOCONCRETA3.exp2.accept(self)
        forGOCONCRETA3.exp3.accept(self)
        forGOCONCRETA3.body.accept(self)
        st.varCheck(st.endScope())

  def visitcallFuncCONCRETA(self, callFuncCONCRETA):
    callFuncCONCRETA.params.accept(self)
    
  def visitdeclarationCONCRETA(self, declarationCONCRETA):
    if(declarationCONCRETA.exp!= None):
      declarationCONCRETA.exp.accept(self)

  def visitcallFuncPSCONCRETA(self, callFuncPSCONCRETA):
    callFuncPSCONCRETA.params.accept(self)

  def visitreturnCONCRETA(self, returnCONCRETA):
    if(returnCONCRETA.exp!= None):
      returnCONCRETA.exp.accept(self)

  def visitbreakCONCRETA(self, breakCONCRETA):
    return [breakCONCRETA.id, breakCONCRETA.type]
  
  def visittypeCONCRETA(self, typeCONCRETA):
    typeCONCRETA.int.accept(self)

  def visittypeCONCRETA2(self, typeCONCRETA2):
    typeCONCRETA2.string.accept(self)

  def visittypeCONCRETA3(self, typeCONCRETA3):
    typeCONCRETA3.bool.accept(self)

  def visitexp(self, expCONCRETA):
    expCONCRETA.exp1.accept(self)

  def visitexpASSIGN(self, expASSIGN):
    expASSIGN.exp1.accept(self)
    expASSIGN.exp2.accept(self)

  def visitexpCOLONEQ(self, expCOLONEQ):
    expCOLONEQ.exp1.accept(self)
    expCOLONEQ.exp2.accept(self)

  def visitexpOR(self, expOR):
    expOR.exp1.accept(self)
    expOR.exp2.accept(self)

  def visitexpAND(self, expAND):
    expAND.exp1.accept(self)
    expAND.exp2.accept(self)
  
  def visitexpEQUALS(self, expEQUALS):
    expEQUALS.exp1.accept(self)
    expEQUALS.exp2.accept(self)

  def visitexpDIFFERENT(self, expDIFFERENT):
    expDIFFERENT.exp1.accept(self)
    expDIFFERENT.exp2.accept(self)

  def visitexpLESS(self, expLESS):
    expLESS.exp1.accept(self)
    expLESS.exp2.accept(self)

  def visitexpGREATER(self, expGREATER):
    expGREATER.exp1.accept(self)
    expGREATER.exp2.accept(self)

  def visitexpLESS_EQUAL(self, expLESS_EQUAL):
    expLESS_EQUAL.exp1.accept(self)
    expLESS_EQUAL.exp2.accept(self)

  def visitexpGREATER_EQUAL(self, expGREATER_EQUAL):
    expGREATER_EQUAL.exp1.accept(self)
    expGREATER_EQUAL.exp2.accept(self)

  def visitexpPLUS(self, expPLUS):
    expPLUS.exp1.accept(self)
    expPLUS.exp2.accept(self)

  def visitexpMINUS(self, expMINUS):
    expMINUS.exp1.accept(self)
    expMINUS.exp2.accept(self)

  def visitexpTIMES(self, expTIMES):
    expTIMES.exp1.accept(self)
    expTIMES.exp2.accept(self)

  def visitexpDIVIDE(self, expDIVIDE):
    expDIVIDE.exp1.accept(self)
    expDIVIDE.exp2.accept(self)

  def visitexpMOD(self, expMOD):
    expMOD.exp1.accept(self)
    expMOD.exp2.accept(self)

  def visitexpDPLUS(self, expDPLUS):
    expDPLUS.exp1.accept(self)

  def visitexpDMINUS(self, expDMINUS):
    expDMINUS.exp1.accept(self)

  def visitexpNOT(self, expNOT):
    expNOT.exp1.accept(self)

  def visitexpNUMBER(self, expNUMBER):
    return [expNUMBER.id, expNUMBER.type]

  def visitexpSTRING(self, expSTRING):
    return [expSTRING.id, expSTRING.type]
    
  def visitexpID(self, expID):
    return [expID.id, expID.type]
    
  def visitexpTRUE(self, expTRUE):
    return [expTRUE.id, expTRUE.type]

  def visitexpFALSE(self, expFALSE):
    return [expFALSE.id, expFALSE.type]

  def visitparamsCONCRETA(self, paramsCONCRETA):
    paramsCONCRETA.exp.accept(self)
    if( paramsCONCRETA.params!= None):
      paramsCONCRETA.params.accept(self)
