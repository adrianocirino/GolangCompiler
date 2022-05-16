
from lexico import *
from parser import *

lexer = lex.lex()

data2 = '''
package main

import "fmt"

func main(){
  var numero int
  numero = 1
  fmt.Println(numero)
}

'''
lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=False)