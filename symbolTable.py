symbolTable = []

INT = 'int'
FLOAT = 'float'
STRING = 'string'
BOOL = 'bool'
TYPE = 'type'
PARAMS = 'params'
FUNC = 'func'
BREAK = 'break'
IF = 'if'
FOR = 'for'
ELSE = 'else'
RETURN = 'return'
VAR = 'var'
TRUE = 'true'
FALSE = 'false'
PRINTLN = 'println'
BINDABLE = 'bindable'
SCOPE = 'scope'
YES = 'yes'
NO = 'no'
USED = 'used'
SWITCHTYPE = 'switchtype'
NEWTYPE = 'newtype'
Number = [INT]
TiposPrimitivos = [INT, BOOL, STRING]

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

def endScope():
    global symbolTable
    lista_dicionario = []
    for i in symbolTable[-1]:
        if(type(symbolTable[-1][i]) == type({})):
            if (symbolTable[-1][i][USED] == NO):
                lista_dicionario.append(i)
    symbolTable = symbolTable[0:-1]
    return lista_dicionario

def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VAR, TYPE: type, USED: NO} 


def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNC, PARAMS: params, TYPE: returnType} 


def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if(bindableName in symbolTable[i].keys()):
            symbolTable[i][bindableName][USED] = YES
            return symbolTable[i][bindableName]
    return None


def varCheck(listVar):
    if(listVar != None):
        for k in range(len(listVar)):
            print('[Erro]:',listVar[k], 'declarada mas nao usada')

def addNewType(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: NEWTYPE, TYPE: type, USED: NO}

def getNewType(NewType):
    if (NewType not in TiposPrimitivos):
            NewType = getBindable(NewType)
            if (NewType != None):
                return NewType[TYPE]
            else:
                return NewType
    else:
        return NewType