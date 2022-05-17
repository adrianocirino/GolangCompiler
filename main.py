
from lexico import *
from parser import *

lexer = lex.lex()

data2 = '''
package main

import "fmt"

func main() {
  var numero int = 1
  fmt.Println(numero)
  if 7%2 == 0 {
        fmt.Println("7 é par")
    } else {
        fmt.Println("7 é ímpar")
    }
  for j := 7; j <= 9; j++ {
        fmt.Println(j)
    }
}
'''
lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=False)