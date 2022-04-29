# Analisador Lexico 

import ply.lex as lex

#Palavras reservadas
reserved = {
   
    'int': 'INT',
    'var': 'VAR',
    'string': 'STRING',
    'bool' : 'BOOL',
    'struct': 'STRUCT',
    'true': 'TRUE',
    'false': 'FALSE',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'func': 'FUNC',
    'map' : 'MAP',
    'package': 'PACKAGE',
    'import' : 'IMPORT',
    'return': 'RETURN',
    'range': 'RANGE',
    'type': 'TYPE',
  
}

# Lista nomes de Tokens 
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'DIFFERENT',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LCHAVES',
    'RCHAVES',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'AND',
    'OR',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'MOD',
    'DPLUS',
    'DMINUS',
    'COLONEQ',
    'exp1'
] 

# Regras para expressões regulares 
t_PLUS          = r'\+'
t_MINUS         = r'\-'
t_TIMES         = r'\*'
t_DIVIDE        = r'\/'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_EQUALS        = r'\=='
t_DIFFERENT    = r'\!='
t_ASSIGN        = r'\='
t_GREATER       = r'\>'
t_LESS          = r'\<'
t_GREATER_EQUAL = r'\>='
t_LESS_EQUAL    = r'\<='
t_AND           = r'\&&'
t_OR            = r'\|\|'
t_LCHAVES       = r'\{'
t_RCHAVES       = r'\}'
t_SEMICOLON     = r'\;'
t_COLON         = r'\:'
t_COMMA         = r'\,'
t_MOD           = r'\%'
t_DPLUS         = r'\+\+'
t_DMINUS        = r'\-\-'
t_COLONEQ       = r'\:\='

tokens = tokens + list(reserved.values())

# Identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    
    return t

# Numeros  
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# String 
def t_STRING(t):
    r'\".*\"'
    return t
  
# Função para pular linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função para comentarios
def t_coment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

# Função de tratamento de erros
def t_error(t):
     print(str(t.value) + 'Invalid token')

# Ignorando tabulações e espaçoS
t_ignore  = ' \t'

#TESTE
data = 'OIIUUU  12 * 4 \"kamila" '

lexer = lex.lex()
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break  
    print(tok)
    