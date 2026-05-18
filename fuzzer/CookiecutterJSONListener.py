# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterJSON.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CookiecutterJSONParser import CookiecutterJSONParser
else:
    from CookiecutterJSONParser import CookiecutterJSONParser

# This class defines a complete listener for a parse tree produced by CookiecutterJSONParser.
class CookiecutterJSONListener(ParseTreeListener):

    # Enter a parse tree produced by CookiecutterJSONParser#start.
    def enterStart(self, ctx:CookiecutterJSONParser.StartContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#start.
    def exitStart(self, ctx:CookiecutterJSONParser.StartContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#object.
    def enterObject(self, ctx:CookiecutterJSONParser.ObjectContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#object.
    def exitObject(self, ctx:CookiecutterJSONParser.ObjectContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#pair.
    def enterPair(self, ctx:CookiecutterJSONParser.PairContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#pair.
    def exitPair(self, ctx:CookiecutterJSONParser.PairContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#key.
    def enterKey(self, ctx:CookiecutterJSONParser.KeyContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#key.
    def exitKey(self, ctx:CookiecutterJSONParser.KeyContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#value.
    def enterValue(self, ctx:CookiecutterJSONParser.ValueContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#value.
    def exitValue(self, ctx:CookiecutterJSONParser.ValueContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#array.
    def enterArray(self, ctx:CookiecutterJSONParser.ArrayContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#array.
    def exitArray(self, ctx:CookiecutterJSONParser.ArrayContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#string.
    def enterString(self, ctx:CookiecutterJSONParser.StringContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#string.
    def exitString(self, ctx:CookiecutterJSONParser.StringContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#stringBody.
    def enterStringBody(self, ctx:CookiecutterJSONParser.StringBodyContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#stringBody.
    def exitStringBody(self, ctx:CookiecutterJSONParser.StringBodyContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#textAtom.
    def enterTextAtom(self, ctx:CookiecutterJSONParser.TextAtomContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#textAtom.
    def exitTextAtom(self, ctx:CookiecutterJSONParser.TextAtomContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#jinjaExpr.
    def enterJinjaExpr(self, ctx:CookiecutterJSONParser.JinjaExprContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#jinjaExpr.
    def exitJinjaExpr(self, ctx:CookiecutterJSONParser.JinjaExprContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#jinjaInner.
    def enterJinjaInner(self, ctx:CookiecutterJSONParser.JinjaInnerContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#jinjaInner.
    def exitJinjaInner(self, ctx:CookiecutterJSONParser.JinjaInnerContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#number.
    def enterNumber(self, ctx:CookiecutterJSONParser.NumberContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#number.
    def exitNumber(self, ctx:CookiecutterJSONParser.NumberContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#bool.
    def enterBool(self, ctx:CookiecutterJSONParser.BoolContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#bool.
    def exitBool(self, ctx:CookiecutterJSONParser.BoolContext):
        pass


    # Enter a parse tree produced by CookiecutterJSONParser#nullValue.
    def enterNullValue(self, ctx:CookiecutterJSONParser.NullValueContext):
        pass

    # Exit a parse tree produced by CookiecutterJSONParser#nullValue.
    def exitNullValue(self, ctx:CookiecutterJSONParser.NullValueContext):
        pass



del CookiecutterJSONParser