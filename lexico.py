# Analisador Lexico 

import ply.lex as lex

#Palavras reservadas
reserved = {
   
    'int': 'INT',
    'var': 'VAR',
    'string': 'STRING',
    'bool' : 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'func': 'FUNC',
    'package': 'PACKAGE',
    'import' : 'IMPORT',
    'break'  : 'BREAK',
    'return': 'RETURN'  
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
    'NOT',
    'AND',
    'OR',
    'SEMICOLON',
    'COMMA',
    'MOD',
    'DPLUS',
    'DMINUS',
    'COLONEQ',
    'NEWLINE',
    'DOT'
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
t_NOT           = r'\!'
t_AND           = r'\&&'
t_OR            = r'\|\|'
t_LCHAVES       = r'\{'
t_RCHAVES       = r'\}'
t_SEMICOLON     = r'\;'
t_COMMA         = r'\,'
t_MOD           = r'\%'
t_DPLUS         = r'\+\+'
t_DMINUS        = r'\-\-'
t_COLONEQ       = r'\:\='
t_DOT           = r'\.'

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
    r'\".*?\"'
    return t

# Função para pular linha
def t_newline(t):
    r'\n\s*'
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

#data = '12 * 4 '

#lexer = lex.lex()
#lexer.input(data)

