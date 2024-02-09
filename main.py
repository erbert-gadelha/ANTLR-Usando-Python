from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser
from meu_ArithmeticVisitor import ArithmeticVisitor


def main():
    print ('\n\n\n\tPara sair pressione ENTER sem digitar nada.')
    visitor = ArithmeticVisitor()
    
    '''result = funct("a = 5", visitor)
    result = funct("b = 7", visitor)
    result = funct("c = a * b", visitor)'''

    print (f'\tresultado: {funct("a=2", visitor)}')
    print (f'\tresultado: {funct("a+2", visitor)}')

    #expression = input(" [in] < ")
    expression = ''
    while expression != "":
        result = funct(expression, visitor)
        print("[out] >", result)
        expression = input(" [in] < ")

    print(visitor.get_variables())
    print ('\tAplicação finalizada..')
    print('\n'*3)


def funct(expression, visitor):
    lexer = ArithmeticLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.program()

    return visitor.visit(tree)




if __name__ == '__main__':
    main()