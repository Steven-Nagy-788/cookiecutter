# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterJSON.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CookiecutterJSONParser import CookiecutterJSONParser
else:
    from CookiecutterJSONParser import CookiecutterJSONParser

# This class defines a complete generic visitor for a parse tree produced by CookiecutterJSONParser.

class CookiecutterJSONVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CookiecutterJSONParser#start.
    def visitStart(self, ctx:CookiecutterJSONParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#object.
    def visitObject(self, ctx:CookiecutterJSONParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#pair.
    def visitPair(self, ctx:CookiecutterJSONParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#key.
    def visitKey(self, ctx:CookiecutterJSONParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#value.
    def visitValue(self, ctx:CookiecutterJSONParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#array.
    def visitArray(self, ctx:CookiecutterJSONParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#string.
    def visitString(self, ctx:CookiecutterJSONParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#stringBody.
    def visitStringBody(self, ctx:CookiecutterJSONParser.StringBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#textAtom.
    def visitTextAtom(self, ctx:CookiecutterJSONParser.TextAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#jinjaExpr.
    def visitJinjaExpr(self, ctx:CookiecutterJSONParser.JinjaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#jinjaInner.
    def visitJinjaInner(self, ctx:CookiecutterJSONParser.JinjaInnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#number.
    def visitNumber(self, ctx:CookiecutterJSONParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#bool.
    def visitBool(self, ctx:CookiecutterJSONParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterJSONParser#nullValue.
    def visitNullValue(self, ctx:CookiecutterJSONParser.NullValueContext):
        return self.visitChildren(ctx)



del CookiecutterJSONParser