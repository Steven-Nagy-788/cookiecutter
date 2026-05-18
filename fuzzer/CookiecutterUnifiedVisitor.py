# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterUnified.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CookiecutterUnifiedParser import CookiecutterUnifiedParser
else:
    from CookiecutterUnifiedParser import CookiecutterUnifiedParser

# This class defines a complete generic visitor for a parse tree produced by CookiecutterUnifiedParser.

class CookiecutterUnifiedVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CookiecutterUnifiedParser#start.
    def visitStart(self, ctx:CookiecutterUnifiedParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#json_start.
    def visitJson_start(self, ctx:CookiecutterUnifiedParser.Json_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#json_object.
    def visitJson_object(self, ctx:CookiecutterUnifiedParser.Json_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#pair.
    def visitPair(self, ctx:CookiecutterUnifiedParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#key.
    def visitKey(self, ctx:CookiecutterUnifiedParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#value.
    def visitValue(self, ctx:CookiecutterUnifiedParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#array.
    def visitArray(self, ctx:CookiecutterUnifiedParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#string.
    def visitString(self, ctx:CookiecutterUnifiedParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#stringBody.
    def visitStringBody(self, ctx:CookiecutterUnifiedParser.StringBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#textAtom.
    def visitTextAtom(self, ctx:CookiecutterUnifiedParser.TextAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#jinjaExpr.
    def visitJinjaExpr(self, ctx:CookiecutterUnifiedParser.JinjaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#jinjaInner.
    def visitJinjaInner(self, ctx:CookiecutterUnifiedParser.JinjaInnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#number.
    def visitNumber(self, ctx:CookiecutterUnifiedParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#json_bool.
    def visitJson_bool(self, ctx:CookiecutterUnifiedParser.Json_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#nullValue.
    def visitNullValue(self, ctx:CookiecutterUnifiedParser.NullValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#ssti_start.
    def visitSsti_start(self, ctx:CookiecutterUnifiedParser.Ssti_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#sstiCookiecutter.
    def visitSstiCookiecutter(self, ctx:CookiecutterUnifiedParser.SstiCookiecutterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#projectPair.
    def visitProjectPair(self, ctx:CookiecutterUnifiedParser.ProjectPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#payload1Pair.
    def visitPayload1Pair(self, ctx:CookiecutterUnifiedParser.Payload1PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#payload2Pair.
    def visitPayload2Pair(self, ctx:CookiecutterUnifiedParser.Payload2PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#payload3Pair.
    def visitPayload3Pair(self, ctx:CookiecutterUnifiedParser.Payload3PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#payloadCurl.
    def visitPayloadCurl(self, ctx:CookiecutterUnifiedParser.PayloadCurlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#payloadMath.
    def visitPayloadMath(self, ctx:CookiecutterUnifiedParser.PayloadMathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#payloadAbort.
    def visitPayloadAbort(self, ctx:CookiecutterUnifiedParser.PayloadAbortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#cli_start.
    def visitCli_start(self, ctx:CookiecutterUnifiedParser.Cli_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#command.
    def visitCommand(self, ctx:CookiecutterUnifiedParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#list_installed_command.
    def visitList_installed_command(self, ctx:CookiecutterUnifiedParser.List_installed_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#render_command.
    def visitRender_command(self, ctx:CookiecutterUnifiedParser.Render_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#nested_command.
    def visitNested_command(self, ctx:CookiecutterUnifiedParser.Nested_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#replay_command.
    def visitReplay_command(self, ctx:CookiecutterUnifiedParser.Replay_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#list_tail.
    def visitList_tail(self, ctx:CookiecutterUnifiedParser.List_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#render_tail.
    def visitRender_tail(self, ctx:CookiecutterUnifiedParser.Render_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#replay_tail.
    def visitReplay_tail(self, ctx:CookiecutterUnifiedParser.Replay_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#list_item.
    def visitList_item(self, ctx:CookiecutterUnifiedParser.List_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#render_item.
    def visitRender_item(self, ctx:CookiecutterUnifiedParser.Render_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#replay_item.
    def visitReplay_item(self, ctx:CookiecutterUnifiedParser.Replay_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#template.
    def visitTemplate(self, ctx:CookiecutterUnifiedParser.TemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#nested_template.
    def visitNested_template(self, ctx:CookiecutterUnifiedParser.Nested_templateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterUnifiedParser#replay_template.
    def visitReplay_template(self, ctx:CookiecutterUnifiedParser.Replay_templateContext):
        return self.visitChildren(ctx)



del CookiecutterUnifiedParser