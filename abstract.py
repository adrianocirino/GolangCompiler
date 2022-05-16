from abc import abstractmethod
from abc import ABCMeta

#abstrata
class programaGO(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta
class programaGOCONCRETA(programaGO):
  def __init__(self, defpackage, defimport, funcdecls):
    self.defpackage = defpackage
    self.defimport = defimport
    self.funcdecls = funcdecls
  def accept(self, visitor):
    return visitor.visitprogramaGOCONCONCRETA(self)

#abstrata
class defpackage(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta
class defpackageCONCRETA(defpackage):
  def __init__(self, package , id):
    self.package = package
    self.id = id
  def accept(self, visitor):
    return visitor.visitpackageCONCRETA(self)

#abstrata
class defimport(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta duvida import parametro
class defimportCONCRETA(defimport):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitdefimportCONCRETA(self)

#abstrata
class funcdecl(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta 
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

#concretas duvida
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

#abstrata
class signature(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
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

#abstrata
class sigparams(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
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

#abstrata
class funcreturn(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
class funcreturnCONCRETA(funcreturn):
  def __init__(self, type):
    self.type = type
  def accept(self, visitor):
    return visitor.visitfuncreturnCONCRETA(self)

#abstrata
class body(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
class bodyCONCRETA(body):
  def __init__(self, stms):
    self.stms = stms
  def accept(self, visitor):
    return visitor.visitbodyCONCRETA(self)

#abstrata
class stms(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
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

#abstrata
class statement(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta
class statementCONCRETA(statement):
  def __init__(self, statement1):
    self.statement1 = statement1
  def accept(self, visitor):
    return visitor.visitstatementCONCRETA(self)

class statement1(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concreta duvida erros statement1 if, for, return, break
class statement1CONCRETAIF(statement1):
  def __init__(self,  exp , body):
    self.exp = exp
    self.body = body
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETAIF(self)

class statement1CONCRETADE(statement1):
  def __init__(self, declaration):
    self.declaration = declaration
  def accept(self, visitor):
    return visitor.visitstatement1CONCRETADE(self)

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

#abstrata
class forGO(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
class forGOCONCRETA(forGO):
  def __init__(self, body):
    self.body = body
  def accept(self, visitor):
    return visitor.visitforGOCONCRETA(self)

#duvida exp exp 
class forGOCONCRETA2(forGO):
  def __init__(self, exp, body):
    self.exp = exp
    self.body = body
  def accept(self, visitor):
    return visitor.visitforGOCONCRETA2(self)

#abstrata
class declaration(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
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

 #abstrata
class type(mataclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass 

#concretas
class typeCONCRETA(type):
  def __init__(self, int):
    self.int = int
  def accept(self, visitor):
    return visitor.visittypeCONCRETA(self)   

class typeCONCRETA2(type):
  def __init__(self, string):
    self.string = string
  def accept(self, visitor):
    return visitor.visittypeCONCRETA2(self)   

class typeCONCRETA3(type):
  def __init__(self, bool):
    self.bool = bool
  def accept(self, visitor):
    return visitor.visittypeCONCRETA3(self)   

#abstrata
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



