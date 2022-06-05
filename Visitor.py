from abstrataVisitor import abstrataVisitor
global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor (abstrataVisitor):

  def visitprogramaGOCONCRETA (self, programaGOCONCRETA):
    programaGOCONCRETA.defpackage.accept(self)
    programaGOCONCRETA.defimport.accept(self)
    programaGOCONCRETA.funcdecls.accept(self)

  def visitdefpackageCONCRETA (self, defpackageCONCRETA):
    print ('package ', end='', sep='')
    print(defpackageCONCRETA.id, end = '', sep='')
    print('')

  def visitdefimportCONCRETA (self, defimportCONCRETA):
    print ('import ', end='', sep='')
    print(defimportCONCRETA.string, end = '', sep='')
    print('')

  def visitfuncdecltCONCRETA (self, funcdecltCONCRETA):
    print(funcdecltCONCRETA.func, end = ' ', sep=' ')
    print(funcdecltCONCRETA.id, end = ' ', sep=' ')
    if (funcdecltCONCRETA.signature != None):
      funcdecltCONCRETA.signature.accept(self)
    print('()')
    funcdecltCONCRETA.body.accept(self)

  def visitfuncdeclsCONCRETA (self, funcdeclsCONCRETA):
    funcdeclsCONCRETA.funcdecl.accept(self)
    
  def visitfuncdeclsCONCRETA2 (self, funcdeclsCONCRETA2):
    funcdeclsCONCRETA2.funcdecl.accept(self)
    funcdeclsCONCRETA2.funcdecls.accept(self)

  def visitsignatureCONCRETA (self, signatureCONCRETA):
      if (signatureCONCRETA.sigparams != None):
        signatureCONCRETA.sigparams.accept(self)
      
  def visitsignatureCONCRETA2 (self, signatureCONCRETA2):
    if (signatureCONCRETA2.sigparams != None):
      signatureCONCRETA2.sigparams.accept(self)
      signatureCONCRETA2.funcreturn.accept(self)
     
  def visitsignatureCONCRETA3 (self, signatureCONCRETA3):
    if (signatureCONCRETA3.funcreturn != None):
      signatureCONCRETA3.funcreturn.accept(self)
    
  def visitsigparamsCONCRETA(self, sigparamsCONCRETA):
        print('(', end = '', sep='')
        print(blank(), sigparamsCONCRETA.id,' ', end = '', sep='')
        print(sigparamsCONCRETA.type, end = '', sep='')
        print(') ', end = '', sep='')

  def visitsigparamsCONCRETA2(self, sigparamsCONCRETA2):
     if(sigparamsCONCRETA2.sigparams != None):
        print(blank(), sigparamsCONCRETA2.id, '',end = '', sep='')
        print(sigparamsCONCRETA2.type,' ',end = '', sep='')
        sigparamsCONCRETA2.sigparams.accept(self)

  def visitfuncreturnCONCRETA(self, funcreturnCONCRETA):
      if(funcreturnCONCRETA!= None):
        print(funcreturnCONCRETA.type, end = '', sep='')

  def visitbodyCONCRETA(self, bodyCONCRETA):
    print('')
    global tab
    tab =  tab + 3
    print('{')
    if(bodyCONCRETA.stms!=None): 
      bodyCONCRETA.stms.accept(self)
    tab =  tab - 3
    print (blank(), '} ', sep='')

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
    print('')
    print(blank(), 'if (', end = '', sep='')
    ifCONCRETA.exp.accept(self)
    print (')', end='', sep='')
    ifCONCRETA.body.accept(self)
    if(ifCONCRETA.body2!=None):
      print('')
      print('else')
      ifCONCRETA.body2.accept(self)

  #duvida pode fazer esse if?
  def visitdeclarationCONCRETA(self, declarationCONCRETA):
    print(blank(), declarationCONCRETA.var,' ', end = '', sep='')
    print(declarationCONCRETA.id,' ', end = '', sep='')
    print(declarationCONCRETA.type,' ' ,end = '', sep='')
    if(declarationCONCRETA.exp!= None):
      declarationCONCRETA.exp.accept(self)

  def visitforGOCONCRETA(self, forGOCONCRETA):
    print('')
    print(blank(), 'for', end='', sep='')
    forGOCONCRETA.body.accept(self)
    
  def visitforGOCONCRETA2(self, forGOCONCRETA2):
    print('')
    print(blank(), 'for (', end='', sep='')
    forGOCONCRETA2.exp.accept(self)
    print (')', end='', sep='')
    forGOCONCRETA2.body.accept(self)

  def visitforGOCONCRETA3(self, forGOCONCRETA3):
    print('')
    print(blank(), 'for (' , end='', sep='')
    forGOCONCRETA3.exp1.accept(self)
    print('; ', end='', sep='')
    forGOCONCRETA3.exp2.accept(self)
    print('; ', end='', sep='')
    forGOCONCRETA3.exp3.accept(self)
    print (')', end='', sep='')
    forGOCONCRETA3.body.accept(self)

  def visitcallFuncCONCRETA(self, callFuncCONCRETA):
    print(blank(), callFuncCONCRETA.id, end = '', sep='')
    callFuncCONCRETA.params.accept(self)

  def visitcallFuncPSCONCRETA(self, callFuncPSCONCRETA):
    print(blank(), callFuncPSCONCRETA.id1,'.', end = '', sep='')
    print(callFuncPSCONCRETA.id2, end = '', sep='')
    print('(', end = '', sep='')
    callFuncPSCONCRETA.params.accept(self)
    print(')')

  def visitreturnCONCRETA(self, returnCONCRETA):
    print(blank(), 'return', end = '', sep='')
    if(returnCONCRETA.exp!= None):
      returnCONCRETA.exp.accept(self)
    print('; ', end='', sep='')

  def visitbreakCONCRETA(self, breakCONCRETA):
    print(blank(), 'break;')
  
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
    print(' = ', end='')
    expASSIGN.exp2.accept(self)

  def visitexpCOLONEQ(self, expCOLONEQ):
    expCOLONEQ.exp1.accept(self)
    print(' := ', end='')
    expCOLONEQ.exp2.accept(self)

  def visitexpOR(self, expOR):
    expOR.exp1.accept(self)
    print(' || ', end='')
    expOR.exp2.accept(self)

  def visitexpAND(self, expAND):
    expAND.exp1.accept(self)
    print(' && ', end='')
    expAND.exp2.accept(self)
  
  def visitexpEQUALS(self, expEQUALS):
    expEQUALS.exp1.accept(self)
    print(' == ', end='')
    expEQUALS.exp2.accept(self)

  def visitexpDIFFERENT(self, expDIFFERENT):
    expDIFFERENT.exp1.accept(self)
    print(' != ', end='')
    expDIFFERENT.exp2.accept(self)

  def visitexpLESS(self, expLESS):
    expLESS.exp1.accept(self)
    print(' < ', end='')
    expLESS.exp2.accept(self)

  def visitexpGREATER(self, expGREATER):
    expGREATER.exp1.accept(self)
    print(' > ', end='')
    expGREATER.exp2.accept(self)

  def visitexpLESS_EQUAL(self, expLESS_EQUAL):
    expLESS_EQUAL.exp1.accept(self)
    print(' <= ', end='')
    expLESS_EQUAL.exp2.accept(self)

  def visitexpGREATER_EQUAL(self, expGREATER_EQUAL):
    expGREATER_EQUAL.exp1.accept(self)
    print(' >= ', end='')
    expGREATER_EQUAL.exp2.accept(self)

  def visitexpPLUS(self, expPLUS):
    expPLUS.exp1.accept(self)
    print(' + ', end='')
    expPLUS.exp2.accept(self)

  def visitexpMINUS(self, expMINUS):
    expMINUS.exp1.accept(self)
    print(' - ', end='')
    expMINUS.exp2.accept(self)

  def visitexpTIMES(self, expTIMES):
    expTIMES.exp1.accept(self)
    print(' * ', end='')
    expTIMES.exp2.accept(self)

  def visitexpDIVIDE(self, expDIVIDE):
    expDIVIDE.exp1.accept(self)
    print(' / ', end='')
    expDIVIDE.exp2.accept(self)

  def visitexpMOD(self, expMOD):
    expMOD.exp1.accept(self)
    print(' % ', end='')
    expMOD.exp2.accept(self)

  def visitexpDPLUS(self, expDPLUS):
    expDPLUS.exp1.accept(self)
    print('++ ', end='')

  def visitexpDMINUS(self, expDMINUS):
    expDMINUS.exp1.accept(self)
    print('-- ', end='')

  def visitexpNOT(self, expNOT):
    print('! ', end='')
    expNOT.exp1.accept(self)

  def visitexpNUMBER(self, expNUMBER):
    print(expNUMBER.number, end='')

  def visitexpSTRING(self, expSTRING):
    print(expSTRING.string, end='')
    
  def visitexpID(self, expID):
    print(expID.id, end='')
    
  def visitexpTRUE(self, expTRUE):
    print(expTRUE.true, end='')

  def visitexpFALSE(self, expFALSE):
    print(expFALSE.false, end='')

  def visitparamsCONCRETA(self, paramsCONCRETA):
    paramsCONCRETA.exp.accept(self)
    if( paramsCONCRETA.params!= None):
      paramsCONCRETA.params.accept(self)