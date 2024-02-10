# Generated from Arithmetic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,41,
        9,3,1,4,1,4,1,4,5,4,46,8,4,10,4,12,4,49,9,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,62,8,5,1,6,1,6,1,6,1,6,1,6,3,6,69,8,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,82,8,9,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,16,17,1,0,18,19,1,0,4,9,84,0,
        21,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,34,1,0,0,0,8,42,1,0,0,0,10,
        61,1,0,0,0,12,63,1,0,0,0,14,70,1,0,0,0,16,74,1,0,0,0,18,78,1,0,0,
        0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,1,1,0,0,0,25,29,3,4,2,0,26,29,3,6,3,0,27,29,3,12,6,0,
        28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,14,
        0,0,31,32,5,15,0,0,32,33,3,6,3,0,33,5,1,0,0,0,34,39,3,8,4,0,35,36,
        7,0,0,0,36,38,3,8,4,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,
        39,40,1,0,0,0,40,7,1,0,0,0,41,39,1,0,0,0,42,47,3,10,5,0,43,44,7,
        1,0,0,44,46,3,10,5,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,
        48,1,0,0,0,48,9,1,0,0,0,49,47,1,0,0,0,50,62,5,20,0,0,51,62,5,14,
        0,0,52,53,5,21,0,0,53,54,3,6,3,0,54,55,5,22,0,0,55,62,1,0,0,0,56,
        62,5,1,0,0,57,58,5,21,0,0,58,59,3,18,9,0,59,60,5,22,0,0,60,62,1,
        0,0,0,61,50,1,0,0,0,61,51,1,0,0,0,61,52,1,0,0,0,61,56,1,0,0,0,61,
        57,1,0,0,0,62,11,1,0,0,0,63,64,5,10,0,0,64,65,3,16,8,0,65,68,3,14,
        7,0,66,67,5,11,0,0,67,69,3,14,7,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        13,1,0,0,0,70,71,5,12,0,0,71,72,3,0,0,0,72,73,5,13,0,0,73,15,1,0,
        0,0,74,75,5,21,0,0,75,76,3,18,9,0,76,77,5,22,0,0,77,17,1,0,0,0,78,
        81,3,8,4,0,79,80,7,2,0,0,80,82,3,18,9,0,81,79,1,0,0,0,81,82,1,0,
        0,0,82,19,1,0,0,0,7,23,28,39,47,61,68,81
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'true'", "'false'", "'&'", 
                     "'|'", "'>'", "'<'", "'=='", "'!='", "'if'", "'else'", 
                     "'{'", "'}'", "<INVALID>", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "TRUE", "FALSE", "AND", "OR", 
                      "GTHAN", "LTHAN", "EQUALS", "NEQUALS", "IF", "ELSE", 
                      "BEGIN", "END", "VAR", "ASSIGN", "PLUS", "MINUS", 
                      "MUL", "DIV", "INT", "LPAREN", "RPAREN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_if_statement = 6
    RULE_block = 7
    RULE_condition = 8
    RULE_boolean_expr = 9

    ruleNames =  [ "program", "statement", "assignment", "expr", "term", 
                   "factor", "if_statement", "block", "condition", "boolean_expr" ]

    EOF = Token.EOF
    BOOLEAN=1
    TRUE=2
    FALSE=3
    AND=4
    OR=5
    GTHAN=6
    LTHAN=7
    EQUALS=8
    NEQUALS=9
    IF=10
    ELSE=11
    BEGIN=12
    END=13
    VAR=14
    ASSIGN=15
    PLUS=16
    MINUS=17
    MUL=18
    DIV=19
    INT=20
    LPAREN=21
    RPAREN=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArithmeticParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3163138) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ArithmeticParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ArithmeticParser.If_statementContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ArithmeticParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(ArithmeticParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ArithmeticParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ArithmeticParser.VAR)
            self.state = 31
            self.match(ArithmeticParser.ASSIGN)
            self.state = 32
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.PLUS)
            else:
                return self.getToken(ArithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MINUS)
            else:
                return self.getToken(ArithmeticParser.MINUS, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ArithmeticParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.term()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 35
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.term()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.FactorContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MUL)
            else:
                return self.getToken(ArithmeticParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIV)
            else:
                return self.getToken(ArithmeticParser.DIV, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.factor()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.factor()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ArithmeticParser.INT, 0)

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def BOOLEAN(self):
            return self.getToken(ArithmeticParser.BOOLEAN, 0)

        def boolean_expr(self):
            return self.getTypedRuleContext(ArithmeticParser.Boolean_exprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(ArithmeticParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(ArithmeticParser.VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(ArithmeticParser.LPAREN)
                self.state = 53
                self.expr()
                self.state = 54
                self.match(ArithmeticParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(ArithmeticParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(ArithmeticParser.LPAREN)
                self.state = 58
                self.boolean_expr()
                self.state = 59
                self.match(ArithmeticParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ArithmeticParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(ArithmeticParser.ConditionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.BlockContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ArithmeticParser.ELSE, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = ArithmeticParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ArithmeticParser.IF)
            self.state = 64
            self.condition()
            self.state = 65
            self.block()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 66
                self.match(ArithmeticParser.ELSE)
                self.state = 67
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ArithmeticParser.BEGIN, 0)

        def program(self):
            return self.getTypedRuleContext(ArithmeticParser.ProgramContext,0)


        def END(self):
            return self.getToken(ArithmeticParser.END, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ArithmeticParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ArithmeticParser.BEGIN)
            self.state = 71
            self.program()
            self.state = 72
            self.match(ArithmeticParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)

        def boolean_expr(self):
            return self.getTypedRuleContext(ArithmeticParser.Boolean_exprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ArithmeticParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ArithmeticParser.LPAREN)
            self.state = 75
            self.boolean_expr()
            self.state = 76
            self.match(ArithmeticParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def boolean_expr(self):
            return self.getTypedRuleContext(ArithmeticParser.Boolean_exprContext,0)


        def GTHAN(self):
            return self.getToken(ArithmeticParser.GTHAN, 0)

        def LTHAN(self):
            return self.getToken(ArithmeticParser.LTHAN, 0)

        def EQUALS(self):
            return self.getToken(ArithmeticParser.EQUALS, 0)

        def NEQUALS(self):
            return self.getToken(ArithmeticParser.NEQUALS, 0)

        def AND(self):
            return self.getToken(ArithmeticParser.AND, 0)

        def OR(self):
            return self.getToken(ArithmeticParser.OR, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_boolean_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_expr" ):
                listener.enterBoolean_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_expr" ):
                listener.exitBoolean_expr(self)




    def boolean_expr(self):

        localctx = ArithmeticParser.Boolean_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolean_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.term()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                self.state = 79
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 80
                self.boolean_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





