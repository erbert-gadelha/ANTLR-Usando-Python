from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser


class ArithmeticVisitor:

    def __init__(self):
        self.debbuging = True
        self.variables = {}


    def visit(self, ctx, depth=0):

        if ctx is not None:
            self.print_color(f'<{ctx.__class__.__name__} (\033[92m{ctx.getText()}\033[93m)>', depth, 0)


        if isinstance(ctx, ArithmeticParser.ProgramContext):
            return self.visitProgram(ctx,depth)
        elif isinstance(ctx, ArithmeticParser.StatementContext):
            return self.visitStatement(ctx,depth)
        elif isinstance(ctx, ArithmeticParser.AssignmentContext):
            return self.visitAssignment(ctx,depth)

        elif isinstance(ctx, ArithmeticParser.ExprContext):
            return self.visitExpr(ctx,depth)
        elif isinstance(ctx, ArithmeticParser.TermContext):
            return self.visitTerm(ctx,depth)
        elif isinstance(ctx, ArithmeticParser.FactorContext):
            return self.visitFactor(ctx,depth)
        elif isinstance(ctx, TerminalNode):
            print (f'Node terminal: [{ctx.getText()}]')
            return self.get_variable(ctx.getText())



    def visitProgram(self, ctx, depth):
        
        child = ctx.getChild(0)
        result = self.visit(child, depth+1)

        self.print_color(f'[end of program]', depth, 1)

        return result

    def visitStatement(self, ctx,depth):
        #self.print_color(f'[statement : \"{ctx.getText()}\"]', depth, 1)

        child = ctx.getChild(0)
        return self.visit(child, depth+1)


    def visitAssignment(self, ctx,depth):
        #self.print_color(f'[assignment : \"{ctx.getText()}\"]', depth, 1)

        var = ctx.getChild(0).getText()
        expr = self.visit(ctx.getChild(2), depth+1)

        self.set_variable(var, expr)

        return expr

    def visitExpr(self, ctx, depth):
        #self.print_color(f'[expr : \"{ctx.getText()}\"]', depth, 1)
        result = self.visit(ctx.getChild(0), depth+1)
        
        for i in range(1, ((ctx.getChildCount()+1)/2).__int__() ):
            child = self.visit(ctx.getChild(i*2), depth+1)
            op = ctx.getChild(i*2-1).getText()

            if op == '+':
                result += child
            else:
                result -= child
                
        return result

    def visitTerm(self, ctx, depth):
        #self.print_color(f'[term : \"{ctx.getText()}\"]', depth, 1)
        result = self.visit(ctx.getChild(0), depth+1)

        for i in range(1, ((ctx.getChildCount()+1)/2).__int__() ):
            child = self.visit(ctx.getChild(i*2), depth+1)
            op = ctx.getChild(i*2-1).getText()

            if op == '*':
                result *= child
            else:
                result /= child

        return result

    def visitFactor(self, ctx,depth):

        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.VAR():
            return self.get_variable(ctx.getText())
        else:
            return self.visit(ctx.expr(), depth+1)
        


    def get_variable(self, var):
        if var in self.variables:
            return self.variables[var]
        else:
            return None

    def set_variable(self, var, value):
        self.variables[var] = value



    def get_variables(self):
        line = '-'*13
        division = '\t\033[92m+' + line + '+' + line + '+'
        result = division + '\n'
        result += '\t|%-12s | %-12s|\n' % ('id', 'value')
        result += division + '\n'

        for var in self.variables:
            result += '\t\033[92m|\033[93m%-12s\033[92m | \033[94m%-12s\033[92m|\n' % (var, self.variables[var])

        result += division + '\033[97m'

        return result





    def print_color(self, text, depth=0, color=0):

        if not self.debbuging:
            return
        
        depth += 1

        colors = {
            0: '\033[93m',  # yellow
            1: '\033[94m',  # blue
            2: '\033[92m',  # green
            3: '\033[91m',  # red
            4: '\033[97m'   # white
        }

        color = color % len(colors)
        print(colors[color] + '\t'*depth + text + '\033[0m')