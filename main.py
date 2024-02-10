from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser
from meu_ArithmeticVisitor import ArithmeticVisitor


def main(): 
    print ('\n\n\n\tPara sair pressione ENTER sem digitar nada.')
    visitor = ArithmeticVisitor()
    visitor.debbuging = True

    '''expression = 'a = true'
    deque(expression, visitor)
    expression = 'if (a & true) { a\nb = 2 } else {a = 1}'
    deque(expression, visitor)'''

    expression = input(' '*11)
    while expression != "":
        result = deque(expression, visitor)
        if result is not None:
            print(f'resultado: {result}',)
        expression = input(' '*11)
    

    print(visitor.get_variables())
    print ('\tAplicação finalizada..')
    print('\n'*3)


def deque(expression, visitor):
    lexer = ArithmeticLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.program()

    return visitor.visit(tree)




if __name__ == '__main__':
    main()