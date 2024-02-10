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
        4,1,22,97,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,
        42,8,3,10,3,12,3,45,9,3,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,1,6,1,6,3,
        6,70,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,79,8,8,1,8,1,8,1,9,1,9,
        1,9,5,9,86,8,9,10,9,12,9,89,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,5,1,0,15,16,1,0,17,18,
        1,0,3,4,1,0,5,8,1,0,1,2,96,0,25,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,
        0,6,38,1,0,0,0,8,46,1,0,0,0,10,62,1,0,0,0,12,64,1,0,0,0,14,71,1,
        0,0,0,16,75,1,0,0,0,18,82,1,0,0,0,20,90,1,0,0,0,22,94,1,0,0,0,24,
        26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,
        0,28,1,1,0,0,0,29,33,3,4,2,0,30,33,3,6,3,0,31,33,3,12,6,0,32,29,
        1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,13,0,0,
        35,36,5,14,0,0,36,37,3,6,3,0,37,5,1,0,0,0,38,43,3,8,4,0,39,40,7,
        0,0,0,40,42,3,8,4,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,
        44,1,0,0,0,44,7,1,0,0,0,45,43,1,0,0,0,46,51,3,10,5,0,47,48,7,1,0,
        0,48,50,3,10,5,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,9,1,0,0,0,53,51,1,0,0,0,54,63,5,19,0,0,55,63,5,13,0,0,
        56,57,5,20,0,0,57,58,3,6,3,0,58,59,5,21,0,0,59,63,1,0,0,0,60,63,
        5,1,0,0,61,63,5,2,0,0,62,54,1,0,0,0,62,55,1,0,0,0,62,56,1,0,0,0,
        62,60,1,0,0,0,62,61,1,0,0,0,63,11,1,0,0,0,64,65,5,9,0,0,65,66,3,
        16,8,0,66,69,3,14,7,0,67,68,5,10,0,0,68,70,3,14,7,0,69,67,1,0,0,
        0,69,70,1,0,0,0,70,13,1,0,0,0,71,72,5,11,0,0,72,73,3,0,0,0,73,74,
        5,12,0,0,74,15,1,0,0,0,75,78,5,20,0,0,76,79,3,18,9,0,77,79,3,20,
        10,0,78,76,1,0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,81,5,21,0,0,81,
        17,1,0,0,0,82,87,3,22,11,0,83,84,7,2,0,0,84,86,3,22,11,0,85,83,1,
        0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,19,1,0,0,0,89,
        87,1,0,0,0,90,91,3,6,3,0,91,92,7,3,0,0,92,93,3,6,3,0,93,21,1,0,0,
        0,94,95,7,4,0,0,95,23,1,0,0,0,8,27,32,43,51,62,69,78,87
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'&'", "'|'", "'>'", 
                     "'<'", "'=='", "'!='", "'if'", "'else'", "'{'", "'}'", 
                     "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "AND", "OR", "GTHAN", 
                      "LTHAN", "EQUALS", "NEQUALS", "IF", "ELSE", "BEGIN", 
                      "END", "VAR", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "INT", "LPAREN", "RPAREN", "WS" ]

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
    RULE_comparison_expr = 10
    RULE_boolean = 11

    ruleNames =  [ "program", "statement", "assignment", "expr", "term", 
                   "factor", "if_statement", "block", "condition", "boolean_expr", 
                   "comparison_expr", "boolean" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    AND=3
    OR=4
    GTHAN=5
    LTHAN=6
    EQUALS=7
    NEQUALS=8
    IF=9
    ELSE=10
    BEGIN=11
    END=12
    VAR=13
    ASSIGN=14
    PLUS=15
    MINUS=16
    MUL=17
    DIV=18
    INT=19
    LPAREN=20
    RPAREN=21
    WS=22

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1581574) != 0)):
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
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
            self.state = 34
            self.match(ArithmeticParser.VAR)
            self.state = 35
            self.match(ArithmeticParser.ASSIGN)
            self.state = 36
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
            self.state = 38
            self.term()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 39
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.term()
                self.state = 45
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
            self.state = 46
            self.factor()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.factor()
                self.state = 53
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

        def TRUE(self):
            return self.getToken(ArithmeticParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ArithmeticParser.FALSE, 0)

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
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(ArithmeticParser.INT)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(ArithmeticParser.VAR)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(ArithmeticParser.LPAREN)
                self.state = 57
                self.expr()
                self.state = 58
                self.match(ArithmeticParser.RPAREN)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.match(ArithmeticParser.TRUE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(ArithmeticParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 64
            self.match(ArithmeticParser.IF)
            self.state = 65
            self.condition()
            self.state = 66
            self.block()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 67
                self.match(ArithmeticParser.ELSE)
                self.state = 68
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
            self.state = 71
            self.match(ArithmeticParser.BEGIN)
            self.state = 72
            self.program()
            self.state = 73
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

        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def boolean_expr(self):
            return self.getTypedRuleContext(ArithmeticParser.Boolean_exprContext,0)


        def comparison_expr(self):
            return self.getTypedRuleContext(ArithmeticParser.Comparison_exprContext,0)


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
            self.state = 75
            self.match(ArithmeticParser.LPAREN)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 76
                self.boolean_expr()
                pass

            elif la_ == 2:
                self.state = 77
                self.comparison_expr()
                pass


            self.state = 80
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

        def boolean(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.BooleanContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.BooleanContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.AND)
            else:
                return self.getToken(ArithmeticParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.OR)
            else:
                return self.getToken(ArithmeticParser.OR, i)

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
            self.state = 82
            self.boolean()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 83
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 84
                self.boolean()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.ExprContext,i)


        def GTHAN(self):
            return self.getToken(ArithmeticParser.GTHAN, 0)

        def LTHAN(self):
            return self.getToken(ArithmeticParser.LTHAN, 0)

        def EQUALS(self):
            return self.getToken(ArithmeticParser.EQUALS, 0)

        def NEQUALS(self):
            return self.getToken(ArithmeticParser.NEQUALS, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_comparison_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_expr" ):
                listener.enterComparison_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_expr" ):
                listener.exitComparison_expr(self)




    def comparison_expr(self):

        localctx = ArithmeticParser.Comparison_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparison_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.expr()
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 92
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ArithmeticParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ArithmeticParser.FALSE, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)




    def boolean(self):

        localctx = ArithmeticParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





