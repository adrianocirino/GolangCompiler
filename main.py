
from lexico import *
from parser import *
lexer = lex.lex()

data2 = '''
package main

import "fmt"

func main() {
	var tamanho int = 20
	for i := 1; i < tamanho; i=0 {
		if i%2 == 0 {
			fmt.Println(i)
		}

		if i == 11 {
			return;
		}
	}
    break;
}
'''
lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=False)

visitor2 = vs.GoSemanticVisitor()

visitor = vis.Visitor()
result.accept(visitor)



