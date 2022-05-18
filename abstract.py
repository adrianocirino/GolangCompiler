from abc import abstractmethod
from abc import ABCMeta

#abstrata definição do programa
class programaGO(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 
 
#concreta definição do programa
class programaGOCONCRETA(programaGO):
  def __init__(self, defpackage, defimport, funcdecls):
    self.defpackage = defpackage
    self.defimport = defimport
    self.funcdecls = funcdecls
  def accept(self, visitor):
    return visitor.visitprogramaGOCONCRETA(self)

#abstrata Package
class defpackage(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta duvida passa o package?
class defpackageCONCRETA(defpackage):
  def __init__(self, package , id):
    self.package = package
    self.id = id
  def accept(self, visitor):
    return visitor.visitpackageCONCRETA(self)

#abstrata Import
class defimport(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta Import
class defimportCONCRETA(defimport):
  def __init__(self, string):
    self.string = string
  def accept(self, visitor):
    return visitor.visitdefimportCONCRETA(self)

#abstrata funções
class funcdecl(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta funções
class funcdecltCONCRETA(funcdecl):
  def __init__(self, func, id, signature, body):
    self.func = func
    self.id = id
    self.signature = signature
    self.body = body
  def accept(self, visitor):
    return visitor.visitfuncdecltCONCRETA(self)

#abstrata
class funcdecls(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas 
class funcdeclsCONCRETA(funcdecls):
  def __init__(self, funcdecl):
    self.funcdecl = funcdecl
  def accept(self, visitor):
    return visitor.visitfuncdeclsCONCRETA(self)

class funcdeclsCONCRETA2(funcdecls):
  def __init__(self, funcdecl, funcdecls):
    self.funcdecl = funcdecl
    self.funcdecls = funcdecls
  def accept(self, visitor):
    return visitor.visitfuncdeclsCONCRETA2(self)

#abstrata assinatura de função
class signature(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas assinatura de função
class signatureCONCRETA(signature):
  def __init__(self, sigparams):
    self.sigparams = sigparams
  def accept(self, visitor):
    return visitor.visitsignatureCONCRETA(self)

class signatureCONCRETA2(signature):
  def __init__(self, sigparams, funcreturn):
    self.sigparams = sigparams
    self.funcreturn = funcreturn
  def accept(self, visitor):
    return visitor.visitsignatureCONCRETA2(self)

class signatureCONCRETA3(signature):
  def __init__(self, funcreturn):
    self.funcreturn = funcreturn
  def accept(self, visitor):
     return visitor.visitsignatureCONCRETA3(self)

#abstrata paramentros de função
class sigparams(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas paramentros da função
class sigparamsCONCRETA(sigparams):
  def __init__(self, id , type):
    self.id = id
    self.type = type
  def accept(self, visitor):
    return visitor.visitsigparamsCONCRETA(self)

class sigparamsCONCRETA2(sigparams):
  def __init__(self, id , type, sigparams ):
    self.id = id
    self.type = type
    self.sigparams = sigparams
  def accept(self, visitor):
    return visitor.visitsigparamsCONCRETA2(self)

#abstrata returno da função
class funcreturn(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta
class funcreturnCONCRETA(funcreturn):
  def __init__(self, type):
    self.type = type
  def accept(self, visitor):
    return visitor.visitfuncreturnCONCRETA(self)

#abstrata corpo da função
class body(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas corpo da função
class bodyCONCRETA(body):
  def __init__(self, stms):
    self.stms = stms
  def accept(self, visitor):
    return visitor.visitbodyCONCRETA(self)

#abstrata comandos
class stms(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas comandos
class stmsCONCRETA(stms):
  def __init__(self, statement):
    self.statement = statement
  def accept(self, visitor):
    return visitor.visitstmsCONCRETA(self)

class stmsCONCRETA2(stms):
  def __init__(self, statement, stms):
    self.statement = statement
    self.stms = stms
  def accept(self, visitor):
    return visitor.visitstmsCONCRETA2(self)

#abstrata comandos
class statement(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 
 
#concreta comandos
class statementCONCRETA(statement):
  def __init__(self, statement1):
    self.statement1 = statement1
  def accept(self, visitor):
    return visitor.visitstatementCONCRETA(self)

#abstrata comandos
class statement1(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta comando IF
class statement1CONCRETAIF(statement1):
  def __init__(self,  exp , body, body2):
    self.exp = exp
    self.body = body
    self.body2 = body2
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETAIF(self)

 #duvidas comandos Declaração
class statement1CONCRETADE(statement1):
  def __init__(self, declaration):
    self.declaration = declaration
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETADE(self)

#Chamada de função
class statement1CONCRETACALL(statement1):
  def __init__(self, callFunc):
    self.callFunc = callFunc
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETACALL(self)

class statement1CONCRETACALLPS(statement1):
  def __init__(self, callFuncPS):
    self.callFunc = callFuncPS
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETACALLPS(self)

# return duvidas
class statement1CONCRETARETURN(statement1):
  def __init__(self, return1):
    self.return1 = return1
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETARETURN(self)

#break duvidas
class statement1CONCRETABREAK(statement1):
  def __init__(self, break1):
    self.break1 = break1
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETABREAK(self)

#abstrata FOR
class forGO(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas FOR
class forGOCONCRETA(forGO):
  def __init__(self, body):
    self.body = body
  def accept(self, visitor):
    return visitor.visitforGOCONCRETA(self)

class forGOCONCRETA2(forGO):
  def __init__(self, exp, body):
    self.exp = exp
    self.body = body
  def accept(self, visitor):
    return visitor.visitforGOCONCRETA2(self)

class forGOCONCRETA3(forGO):
  def __init__(self, exp1, exp2, exp3, body):
    self.exp1 = exp1
    self.exp2 = exp2
    self.exp3 = exp3
    self.body = body
  def accept(self, visitor):
    return visitor.visitforGOCONCRETA2(self)

#abstrata Declaração
class declaration(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas Declaração
class declarationCONCRETA(forGO):
  def __init__(self, var, id, type):
    self.var = var
    self.id = id
    self.type = type
  def accept(self, visitor):
    return visitor.visitdeclarationCONCRETA(self)

class declarationCONCRETA2(forGO):
  def __init__(self, var, id, type, exp):
    self.var = var
    self.id = id
    self.type = type
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitdeclarationCONCRETA2(self)

 #abstrata Type
class type(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta INT
class typeCONCRETA(type):
  def __init__(self, int):
    self.int = int
  def accept(self, visitor):
    return visitor.visittypeCONCRETA(self)   

#concreta STRING
class typeCONCRETA2(type):
  def __init__(self, string):
    self.string = string
  def accept(self, visitor):
    return visitor.visittypeCONCRETA2(self)   

#concreta BOOL
class typeCONCRETA3(type):
  def __init__(self, bool):
    self.bool = bool
  def accept(self, visitor):
    return visitor.visittypeCONCRETA3(self)   

#abstrata Expressões
class exp(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
class expASSIGN(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpASSIGN(self)
    
#duvidas se cria concreta dessa regra exp2
class expASSIGN2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpASSIGN2(self)   

class expOR(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpOR(self)

class expOR2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpOR2(self) 

class expAND(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpAND(self)

class expAND2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpAND2(self) 

class expEQUALS(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpEQUALS(self)
    
class expDIFFERENT(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDIFFERENT(self)

class expDIFFERENT2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDIFFERENT2(self) 

class expLESS(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpLESS(self)

class expGREATER(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpGREATER(self)

class expLESS_EQUAL(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpLESS_EQUAL(self)

class expGREATER_EQUAL(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpGREATER_EQUAL(self)

class expGREATER_EQUAL2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpGREATER_EQUAL2(self) 

class expPLUS(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpPLUS(self)

class expMINUS(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpMINUS(self)

class expMINUS2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpMINUS2(self) 

class expTIMES(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpTIMES(self)

class expDIVIDE(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDIVIDE(self)

class expMOD(exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpMOD(self)

class expMOD2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpMOD2(self) 

class expDPLUS(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDPLUS(self) 

class expDMINUS(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDMINUS(self) 

class expDMINUS2(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDMINUS2(self) 

# DUVIDA EXP9 ULTIMA CAMADA
class expNOT(exp):
  def __init__(self, exp2):
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpDMINUS(self) 

class expNUMBER(exp):
  def __init__(self, number):
    self.number = number
  def accept(self, visitor):
    return visitor.visitexpNUMBER(self) 

class expSTRING(exp):
  def __init__(self, string):
    self.string = string
  def accept(self, visitor):
    return visitor.visitexpSTRING(self) 

class expID(exp):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitexpID(self) 

class expTRUE(exp):
  def __init__(self, true):
    self.true = true
  def accept(self, visitor):
    return visitor.visitexpTRUE(self) 

class expFALSE(exp):
  def __init__(self, false):
    self.false = false
  def accept(self, visitor):
    return visitor.visitexpFALSE(self) 

#abstrata Return
class returnAbs(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta Return
class returnCONCRETA(returnAbs):
  def __init__(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitreturnCONCRETA(self)    

# duvida criar break?
# abstrata chamada de função
class callFunc(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta chamada de função
class callFuncCONCRETA(callFunc):
  def __init__(self, params):
    self.params = params
  def accept(self, visitor):
    return visitor.visitcallFuncCONCRETA(self) 

#abstrata 
class callFuncPS(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta
class callFuncPSCONCRETA(callFuncPS):
  def __init__(self, params):
    self.params = params
  def accept(self, visitor):
    return visitor.visitcallFuncPSCONCRETA(self) 

#abstrata paramentros
class params(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta
class paramsCONCRETA(params):
  def __init__(self, exp ,params):
    self.exp = exp
    self.params = params
  def accept(self, visitor):
    return visitor.visitparamsCONCRETA(self) 
