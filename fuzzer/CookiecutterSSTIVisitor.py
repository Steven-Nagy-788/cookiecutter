# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterSSTI.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CookiecutterSSTIParser import CookiecutterSSTIParser
else:
    from CookiecutterSSTIParser import CookiecutterSSTIParser

# This class defines a complete generic visitor for a parse tree produced by CookiecutterSSTIParser.

class CookiecutterSSTIVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CookiecutterSSTIParser#start.
    def visitStart(self, ctx:CookiecutterSSTIParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#sstiCookiecutter.
    def visitSstiCookiecutter(self, ctx:CookiecutterSSTIParser.SstiCookiecutterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#projectPair.
    def visitProjectPair(self, ctx:CookiecutterSSTIParser.ProjectPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#payload1Pair.
    def visitPayload1Pair(self, ctx:CookiecutterSSTIParser.Payload1PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#payload2Pair.
    def visitPayload2Pair(self, ctx:CookiecutterSSTIParser.Payload2PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#payload3Pair.
    def visitPayload3Pair(self, ctx:CookiecutterSSTIParser.Payload3PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#payloadCurl.
    def visitPayloadCurl(self, ctx:CookiecutterSSTIParser.PayloadCurlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#payloadMath.
    def visitPayloadMath(self, ctx:CookiecutterSSTIParser.PayloadMathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterSSTIParser#payloadAbort.
    def visitPayloadAbort(self, ctx:CookiecutterSSTIParser.PayloadAbortContext):
        return self.visitChildren(ctx)



del CookiecutterSSTIParser