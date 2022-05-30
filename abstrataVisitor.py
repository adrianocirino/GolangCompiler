from abc import abstractmethod
from abc import ABCMeta

class abstrataVisitor(metaclass = ABCMeta):

     @abstractmethod
     def visitprogramaGOCONCRETA (self, programaGO):
         pass

     @abstractmethod 
     def visitdefpackageCONCRETA(self, defpackage):
         pass

     @abstractmethod 
     def visitdefimportCONCRETA(self, defimport):
         pass

     @abstractmethod 
     def visitfuncdecltCONCRETA(self, funcdecl):
         pass

     @abstractmethod 
     def visitfuncdeclsCONCRETA(self, funcdecls):
         pass

     @abstractmethod 
     def visitfuncdeclsCONCRETA2(self, funcdecls):
         pass

     @abstractmethod 
     def visitsignatureCONCRETA(self, signature):
         pass

     @abstractmethod 
     def visitsignatureCONCRETA2(self, signature):
         pass

     @abstractmethod 
     def visitsignatureCONCRETA3(self, signature):
         pass

     @abstractmethod 
     def visitsigparamsCONCRETA(self, sigparams):
         pass

     @abstractmethod 
     def visitsigparamsCONCRETA2(self, sigparams):
         pass

     @abstractmethod 
     def visitfuncreturnCONCRETA(self, funcreturn):
         pass

     @abstractmethod 
     def visitbodyCONCRETA(self, body):
         pass

     @abstractmethod 
     def visitstmsCONCRETA(self, stms):
         pass

     @abstractmethod 
     def visitstmsCONCRETA2(self, stms):
         pass

     @abstractmethod 
     def visitstatementCONCRETA(self, statement):
         pass

     @abstractmethod 
     def visitifCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visitdeclarationCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visitforGOCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visitforGOCONCRETA2(self, statement1):
         pass

     @abstractmethod 
     def visitforGOCONCRETA3(self, statement1):
         pass

     @abstractmethod 
     def visitcallFuncCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visitcallFuncPSCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visitreturnCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visitbreakCONCRETA(self, statement1):
         pass

     @abstractmethod 
     def visittypeCONCRETA(self, type):
         pass

     @abstractmethod 
     def visittypeCONCRETA2(self, type):
         pass

     @abstractmethod 
     def visittypeCONCRETA3(self, type):
         pass

     @abstractmethod 
     def visitexp(self, exp):
         pass

     @abstractmethod 
     def visitexpASSIGN(self, exp):
         pass

     @abstractmethod 
     def visitexpCOLONEQ(self, exp):
         pass

     @abstractmethod 
     def visitexpOR(self, exp):
         pass

     @abstractmethod 
     def visittypeCONCRETA3(self, type):
         pass