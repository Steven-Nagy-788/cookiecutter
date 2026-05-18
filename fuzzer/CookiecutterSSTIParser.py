# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterSSTI.g4 by ANTLR 4.13.1
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
        4,1,28,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,89,0,18,1,
        0,0,0,2,21,1,0,0,0,4,31,1,0,0,0,6,37,1,0,0,0,8,43,1,0,0,0,10,49,
        1,0,0,0,12,55,1,0,0,0,14,77,1,0,0,0,16,83,1,0,0,0,18,19,3,2,1,0,
        19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,1,0,0,22,23,3,4,2,0,23,24,5,6,
        0,0,24,25,3,6,3,0,25,26,5,6,0,0,26,27,3,8,4,0,27,28,5,6,0,0,28,29,
        3,10,5,0,29,30,5,2,0,0,30,3,1,0,0,0,31,32,5,15,0,0,32,33,5,5,0,0,
        33,34,5,7,0,0,34,35,5,19,0,0,35,36,5,7,0,0,36,5,1,0,0,0,37,38,5,
        16,0,0,38,39,5,5,0,0,39,40,5,7,0,0,40,41,3,12,6,0,41,42,5,7,0,0,
        42,7,1,0,0,0,43,44,5,17,0,0,44,45,5,5,0,0,45,46,5,7,0,0,46,47,3,
        14,7,0,47,48,5,7,0,0,48,9,1,0,0,0,49,50,5,18,0,0,50,51,5,5,0,0,51,
        52,5,7,0,0,52,53,3,16,8,0,53,54,5,7,0,0,54,11,1,0,0,0,55,56,5,13,
        0,0,56,57,5,20,0,0,57,58,5,9,0,0,58,59,5,21,0,0,59,60,5,3,0,0,60,
        61,5,8,0,0,61,62,5,22,0,0,62,63,5,8,0,0,63,64,5,4,0,0,64,65,5,9,
        0,0,65,66,5,23,0,0,66,67,5,10,0,0,67,68,5,8,0,0,68,69,5,26,0,0,69,
        70,5,8,0,0,70,71,5,11,0,0,71,72,5,9,0,0,72,73,5,24,0,0,73,74,5,10,
        0,0,74,75,5,11,0,0,75,76,5,14,0,0,76,13,1,0,0,0,77,78,5,13,0,0,78,
        79,5,27,0,0,79,80,5,12,0,0,80,81,5,27,0,0,81,82,5,14,0,0,82,15,1,
        0,0,0,83,84,5,13,0,0,84,85,5,20,0,0,85,86,5,9,0,0,86,87,5,21,0,0,
        87,88,5,3,0,0,88,89,5,8,0,0,89,90,5,22,0,0,90,91,5,8,0,0,91,92,5,
        4,0,0,92,93,5,9,0,0,93,94,5,25,0,0,94,95,5,10,0,0,95,96,5,11,0,0,
        96,97,5,14,0,0,97,17,1,0,0,0,0
    ]

class CookiecutterSSTIParser ( Parser ):

    grammarFileName = "CookiecutterSSTI.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "']'", "':'", "','", 
                     "'\"'", "'''", "'.'", "'('", "')'", "'+'", "'{{'", 
                     "'}}'", "'\"project_name\"'", "'\"ssti_payload1\"'", 
                     "'\"ssti_payload2\"'", "'\"ssti_payload3\"'", "<INVALID>", 
                     "'lipsum'", "'__globals__'", "'os'", "'popen'", "'read'", 
                     "'abort'", "'curl -s https://api.restful-api.dev/objects'" ]

    symbolicNames = [ "<INVALID>", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "COLON", "COMMA", "QUOTE", "SQUOTE", "DOT", "LPAREN", 
                      "RPAREN", "PLUS", "J2_OPEN", "J2_CLOSE", "PROJECT_NAME", 
                      "SSTI_PAYLOAD1", "SSTI_PAYLOAD2", "SSTI_PAYLOAD3", 
                      "SAFE_NAME", "LIPSUM", "GLOBALS", "OS", "POPEN", "READ", 
                      "ABORT", "CURL_CMD", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_sstiCookiecutter = 1
    RULE_projectPair = 2
    RULE_payload1Pair = 3
    RULE_payload2Pair = 4
    RULE_payload3Pair = 5
    RULE_payloadCurl = 6
    RULE_payloadMath = 7
    RULE_payloadAbort = 8

    ruleNames =  [ "start", "sstiCookiecutter", "projectPair", "payload1Pair", 
                   "payload2Pair", "payload3Pair", "payloadCurl", "payloadMath", 
                   "payloadAbort" ]

    EOF = Token.EOF
    LBRACE=1
    RBRACE=2
    LBRACK=3
    RBRACK=4
    COLON=5
    COMMA=6
    QUOTE=7
    SQUOTE=8
    DOT=9
    LPAREN=10
    RPAREN=11
    PLUS=12
    J2_OPEN=13
    J2_CLOSE=14
    PROJECT_NAME=15
    SSTI_PAYLOAD1=16
    SSTI_PAYLOAD2=17
    SSTI_PAYLOAD3=18
    SAFE_NAME=19
    LIPSUM=20
    GLOBALS=21
    OS=22
    POPEN=23
    READ=24
    ABORT=25
    CURL_CMD=26
    NUMBER=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sstiCookiecutter(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.SstiCookiecutterContext,0)


        def EOF(self):
            return self.getToken(CookiecutterSSTIParser.EOF, 0)

        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = CookiecutterSSTIParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.sstiCookiecutter()
            self.state = 19
            self.match(CookiecutterSSTIParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SstiCookiecutterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CookiecutterSSTIParser.LBRACE, 0)

        def projectPair(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.ProjectPairContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.COMMA)
            else:
                return self.getToken(CookiecutterSSTIParser.COMMA, i)

        def payload1Pair(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.Payload1PairContext,0)


        def payload2Pair(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.Payload2PairContext,0)


        def payload3Pair(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.Payload3PairContext,0)


        def RBRACE(self):
            return self.getToken(CookiecutterSSTIParser.RBRACE, 0)

        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_sstiCookiecutter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSstiCookiecutter" ):
                listener.enterSstiCookiecutter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSstiCookiecutter" ):
                listener.exitSstiCookiecutter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSstiCookiecutter" ):
                return visitor.visitSstiCookiecutter(self)
            else:
                return visitor.visitChildren(self)




    def sstiCookiecutter(self):

        localctx = CookiecutterSSTIParser.SstiCookiecutterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sstiCookiecutter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(CookiecutterSSTIParser.LBRACE)
            self.state = 22
            self.projectPair()
            self.state = 23
            self.match(CookiecutterSSTIParser.COMMA)
            self.state = 24
            self.payload1Pair()
            self.state = 25
            self.match(CookiecutterSSTIParser.COMMA)
            self.state = 26
            self.payload2Pair()
            self.state = 27
            self.match(CookiecutterSSTIParser.COMMA)
            self.state = 28
            self.payload3Pair()
            self.state = 29
            self.match(CookiecutterSSTIParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProjectPairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROJECT_NAME(self):
            return self.getToken(CookiecutterSSTIParser.PROJECT_NAME, 0)

        def COLON(self):
            return self.getToken(CookiecutterSSTIParser.COLON, 0)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.QUOTE)
            else:
                return self.getToken(CookiecutterSSTIParser.QUOTE, i)

        def SAFE_NAME(self):
            return self.getToken(CookiecutterSSTIParser.SAFE_NAME, 0)

        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_projectPair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProjectPair" ):
                listener.enterProjectPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProjectPair" ):
                listener.exitProjectPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProjectPair" ):
                return visitor.visitProjectPair(self)
            else:
                return visitor.visitChildren(self)




    def projectPair(self):

        localctx = CookiecutterSSTIParser.ProjectPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_projectPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CookiecutterSSTIParser.PROJECT_NAME)
            self.state = 32
            self.match(CookiecutterSSTIParser.COLON)
            self.state = 33
            self.match(CookiecutterSSTIParser.QUOTE)
            self.state = 34
            self.match(CookiecutterSSTIParser.SAFE_NAME)
            self.state = 35
            self.match(CookiecutterSSTIParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Payload1PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SSTI_PAYLOAD1(self):
            return self.getToken(CookiecutterSSTIParser.SSTI_PAYLOAD1, 0)

        def COLON(self):
            return self.getToken(CookiecutterSSTIParser.COLON, 0)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.QUOTE)
            else:
                return self.getToken(CookiecutterSSTIParser.QUOTE, i)

        def payloadCurl(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.PayloadCurlContext,0)


        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_payload1Pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayload1Pair" ):
                listener.enterPayload1Pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayload1Pair" ):
                listener.exitPayload1Pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayload1Pair" ):
                return visitor.visitPayload1Pair(self)
            else:
                return visitor.visitChildren(self)




    def payload1Pair(self):

        localctx = CookiecutterSSTIParser.Payload1PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_payload1Pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(CookiecutterSSTIParser.SSTI_PAYLOAD1)
            self.state = 38
            self.match(CookiecutterSSTIParser.COLON)
            self.state = 39
            self.match(CookiecutterSSTIParser.QUOTE)
            self.state = 40
            self.payloadCurl()
            self.state = 41
            self.match(CookiecutterSSTIParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Payload2PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SSTI_PAYLOAD2(self):
            return self.getToken(CookiecutterSSTIParser.SSTI_PAYLOAD2, 0)

        def COLON(self):
            return self.getToken(CookiecutterSSTIParser.COLON, 0)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.QUOTE)
            else:
                return self.getToken(CookiecutterSSTIParser.QUOTE, i)

        def payloadMath(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.PayloadMathContext,0)


        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_payload2Pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayload2Pair" ):
                listener.enterPayload2Pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayload2Pair" ):
                listener.exitPayload2Pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayload2Pair" ):
                return visitor.visitPayload2Pair(self)
            else:
                return visitor.visitChildren(self)




    def payload2Pair(self):

        localctx = CookiecutterSSTIParser.Payload2PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_payload2Pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(CookiecutterSSTIParser.SSTI_PAYLOAD2)
            self.state = 44
            self.match(CookiecutterSSTIParser.COLON)
            self.state = 45
            self.match(CookiecutterSSTIParser.QUOTE)
            self.state = 46
            self.payloadMath()
            self.state = 47
            self.match(CookiecutterSSTIParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Payload3PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SSTI_PAYLOAD3(self):
            return self.getToken(CookiecutterSSTIParser.SSTI_PAYLOAD3, 0)

        def COLON(self):
            return self.getToken(CookiecutterSSTIParser.COLON, 0)

        def QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.QUOTE)
            else:
                return self.getToken(CookiecutterSSTIParser.QUOTE, i)

        def payloadAbort(self):
            return self.getTypedRuleContext(CookiecutterSSTIParser.PayloadAbortContext,0)


        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_payload3Pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayload3Pair" ):
                listener.enterPayload3Pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayload3Pair" ):
                listener.exitPayload3Pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayload3Pair" ):
                return visitor.visitPayload3Pair(self)
            else:
                return visitor.visitChildren(self)




    def payload3Pair(self):

        localctx = CookiecutterSSTIParser.Payload3PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_payload3Pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CookiecutterSSTIParser.SSTI_PAYLOAD3)
            self.state = 50
            self.match(CookiecutterSSTIParser.COLON)
            self.state = 51
            self.match(CookiecutterSSTIParser.QUOTE)
            self.state = 52
            self.payloadAbort()
            self.state = 53
            self.match(CookiecutterSSTIParser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayloadCurlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def J2_OPEN(self):
            return self.getToken(CookiecutterSSTIParser.J2_OPEN, 0)

        def LIPSUM(self):
            return self.getToken(CookiecutterSSTIParser.LIPSUM, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.DOT)
            else:
                return self.getToken(CookiecutterSSTIParser.DOT, i)

        def GLOBALS(self):
            return self.getToken(CookiecutterSSTIParser.GLOBALS, 0)

        def LBRACK(self):
            return self.getToken(CookiecutterSSTIParser.LBRACK, 0)

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.SQUOTE)
            else:
                return self.getToken(CookiecutterSSTIParser.SQUOTE, i)

        def OS(self):
            return self.getToken(CookiecutterSSTIParser.OS, 0)

        def RBRACK(self):
            return self.getToken(CookiecutterSSTIParser.RBRACK, 0)

        def POPEN(self):
            return self.getToken(CookiecutterSSTIParser.POPEN, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.LPAREN)
            else:
                return self.getToken(CookiecutterSSTIParser.LPAREN, i)

        def CURL_CMD(self):
            return self.getToken(CookiecutterSSTIParser.CURL_CMD, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.RPAREN)
            else:
                return self.getToken(CookiecutterSSTIParser.RPAREN, i)

        def READ(self):
            return self.getToken(CookiecutterSSTIParser.READ, 0)

        def J2_CLOSE(self):
            return self.getToken(CookiecutterSSTIParser.J2_CLOSE, 0)

        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_payloadCurl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayloadCurl" ):
                listener.enterPayloadCurl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayloadCurl" ):
                listener.exitPayloadCurl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayloadCurl" ):
                return visitor.visitPayloadCurl(self)
            else:
                return visitor.visitChildren(self)




    def payloadCurl(self):

        localctx = CookiecutterSSTIParser.PayloadCurlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_payloadCurl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(CookiecutterSSTIParser.J2_OPEN)
            self.state = 56
            self.match(CookiecutterSSTIParser.LIPSUM)
            self.state = 57
            self.match(CookiecutterSSTIParser.DOT)
            self.state = 58
            self.match(CookiecutterSSTIParser.GLOBALS)
            self.state = 59
            self.match(CookiecutterSSTIParser.LBRACK)
            self.state = 60
            self.match(CookiecutterSSTIParser.SQUOTE)
            self.state = 61
            self.match(CookiecutterSSTIParser.OS)
            self.state = 62
            self.match(CookiecutterSSTIParser.SQUOTE)
            self.state = 63
            self.match(CookiecutterSSTIParser.RBRACK)
            self.state = 64
            self.match(CookiecutterSSTIParser.DOT)
            self.state = 65
            self.match(CookiecutterSSTIParser.POPEN)
            self.state = 66
            self.match(CookiecutterSSTIParser.LPAREN)
            self.state = 67
            self.match(CookiecutterSSTIParser.SQUOTE)
            self.state = 68
            self.match(CookiecutterSSTIParser.CURL_CMD)
            self.state = 69
            self.match(CookiecutterSSTIParser.SQUOTE)
            self.state = 70
            self.match(CookiecutterSSTIParser.RPAREN)
            self.state = 71
            self.match(CookiecutterSSTIParser.DOT)
            self.state = 72
            self.match(CookiecutterSSTIParser.READ)
            self.state = 73
            self.match(CookiecutterSSTIParser.LPAREN)
            self.state = 74
            self.match(CookiecutterSSTIParser.RPAREN)
            self.state = 75
            self.match(CookiecutterSSTIParser.J2_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayloadMathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def J2_OPEN(self):
            return self.getToken(CookiecutterSSTIParser.J2_OPEN, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.NUMBER)
            else:
                return self.getToken(CookiecutterSSTIParser.NUMBER, i)

        def PLUS(self):
            return self.getToken(CookiecutterSSTIParser.PLUS, 0)

        def J2_CLOSE(self):
            return self.getToken(CookiecutterSSTIParser.J2_CLOSE, 0)

        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_payloadMath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayloadMath" ):
                listener.enterPayloadMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayloadMath" ):
                listener.exitPayloadMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayloadMath" ):
                return visitor.visitPayloadMath(self)
            else:
                return visitor.visitChildren(self)




    def payloadMath(self):

        localctx = CookiecutterSSTIParser.PayloadMathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_payloadMath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(CookiecutterSSTIParser.J2_OPEN)
            self.state = 78
            self.match(CookiecutterSSTIParser.NUMBER)
            self.state = 79
            self.match(CookiecutterSSTIParser.PLUS)
            self.state = 80
            self.match(CookiecutterSSTIParser.NUMBER)
            self.state = 81
            self.match(CookiecutterSSTIParser.J2_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayloadAbortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def J2_OPEN(self):
            return self.getToken(CookiecutterSSTIParser.J2_OPEN, 0)

        def LIPSUM(self):
            return self.getToken(CookiecutterSSTIParser.LIPSUM, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.DOT)
            else:
                return self.getToken(CookiecutterSSTIParser.DOT, i)

        def GLOBALS(self):
            return self.getToken(CookiecutterSSTIParser.GLOBALS, 0)

        def LBRACK(self):
            return self.getToken(CookiecutterSSTIParser.LBRACK, 0)

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterSSTIParser.SQUOTE)
            else:
                return self.getToken(CookiecutterSSTIParser.SQUOTE, i)

        def OS(self):
            return self.getToken(CookiecutterSSTIParser.OS, 0)

        def RBRACK(self):
            return self.getToken(CookiecutterSSTIParser.RBRACK, 0)

        def ABORT(self):
            return self.getToken(CookiecutterSSTIParser.ABORT, 0)

        def LPAREN(self):
            return self.getToken(CookiecutterSSTIParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CookiecutterSSTIParser.RPAREN, 0)

        def J2_CLOSE(self):
            return self.getToken(CookiecutterSSTIParser.J2_CLOSE, 0)

        def getRuleIndex(self):
            return CookiecutterSSTIParser.RULE_payloadAbort

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayloadAbort" ):
                listener.enterPayloadAbort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayloadAbort" ):
                listener.exitPayloadAbort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayloadAbort" ):
                return visitor.visitPayloadAbort(self)
            else:
                return visitor.visitChildren(self)




    def payloadAbort(self):

        localctx = CookiecutterSSTIParser.PayloadAbortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_payloadAbort)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(CookiecutterSSTIParser.J2_OPEN)
            self.state = 84
            self.match(CookiecutterSSTIParser.LIPSUM)
            self.state = 85
            self.match(CookiecutterSSTIParser.DOT)
            self.state = 86
            self.match(CookiecutterSSTIParser.GLOBALS)
            self.state = 87
            self.match(CookiecutterSSTIParser.LBRACK)
            self.state = 88
            self.match(CookiecutterSSTIParser.SQUOTE)
            self.state = 89
            self.match(CookiecutterSSTIParser.OS)
            self.state = 90
            self.match(CookiecutterSSTIParser.SQUOTE)
            self.state = 91
            self.match(CookiecutterSSTIParser.RBRACK)
            self.state = 92
            self.match(CookiecutterSSTIParser.DOT)
            self.state = 93
            self.match(CookiecutterSSTIParser.ABORT)
            self.state = 94
            self.match(CookiecutterSSTIParser.LPAREN)
            self.state = 95
            self.match(CookiecutterSSTIParser.RPAREN)
            self.state = 96
            self.match(CookiecutterSSTIParser.J2_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





