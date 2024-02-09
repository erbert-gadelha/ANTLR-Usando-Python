from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser
from meu_ArithmeticVisitor import ArithmeticVisitor


def main():
    print ('\n\n\n\tPara sair pressione ENTER sem digitar nada.')
    visitor = ArithmeticVisitor()
    visitor.debbuging = False

    '''expressions = [
        "x = 5",
        "y = x + 3",
        "y * 2"
    ]

    for expression in expressions:
        #print(f'         < {expression}')
        print(f' <         {expression}')
        result = funct(expression, visitor)
        print(f'resultado: {result}\n')'''


    expression = input(' '*11)
    while expression != "":
        result = funct(expression, visitor)
        print(f'resultado: {result}',)
        expression = input(' '*11)

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