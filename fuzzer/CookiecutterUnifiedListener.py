# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterUnified.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CookiecutterUnifiedParser import CookiecutterUnifiedParser
else:
    from CookiecutterUnifiedParser import CookiecutterUnifiedParser

# This class defines a complete listener for a parse tree produced by CookiecutterUnifiedParser.
class CookiecutterUnifiedListener(ParseTreeListener):

    # Enter a parse tree produced by CookiecutterUnifiedParser#start.
    def enterStart(self, ctx:CookiecutterUnifiedParser.StartContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#start.
    def exitStart(self, ctx:CookiecutterUnifiedParser.StartContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#json_start.
    def enterJson_start(self, ctx:CookiecutterUnifiedParser.Json_startContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#json_start.
    def exitJson_start(self, ctx:CookiecutterUnifiedParser.Json_startContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#json_object.
    def enterJson_object(self, ctx:CookiecutterUnifiedParser.Json_objectContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#json_object.
    def exitJson_object(self, ctx:CookiecutterUnifiedParser.Json_objectContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#pair.
    def enterPair(self, ctx:CookiecutterUnifiedParser.PairContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#pair.
    def exitPair(self, ctx:CookiecutterUnifiedParser.PairContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#key.
    def enterKey(self, ctx:CookiecutterUnifiedParser.KeyContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#key.
    def exitKey(self, ctx:CookiecutterUnifiedParser.KeyContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#value.
    def enterValue(self, ctx:CookiecutterUnifiedParser.ValueContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#value.
    def exitValue(self, ctx:CookiecutterUnifiedParser.ValueContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#array.
    def enterArray(self, ctx:CookiecutterUnifiedParser.ArrayContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#array.
    def exitArray(self, ctx:CookiecutterUnifiedParser.ArrayContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#string.
    def enterString(self, ctx:CookiecutterUnifiedParser.StringContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#string.
    def exitString(self, ctx:CookiecutterUnifiedParser.StringContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#stringBody.
    def enterStringBody(self, ctx:CookiecutterUnifiedParser.StringBodyContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#stringBody.
    def exitStringBody(self, ctx:CookiecutterUnifiedParser.StringBodyContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#textAtom.
    def enterTextAtom(self, ctx:CookiecutterUnifiedParser.TextAtomContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#textAtom.
    def exitTextAtom(self, ctx:CookiecutterUnifiedParser.TextAtomContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#jinjaExpr.
    def enterJinjaExpr(self, ctx:CookiecutterUnifiedParser.JinjaExprContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#jinjaExpr.
    def exitJinjaExpr(self, ctx:CookiecutterUnifiedParser.JinjaExprContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#jinjaInner.
    def enterJinjaInner(self, ctx:CookiecutterUnifiedParser.JinjaInnerContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#jinjaInner.
    def exitJinjaInner(self, ctx:CookiecutterUnifiedParser.JinjaInnerContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#number.
    def enterNumber(self, ctx:CookiecutterUnifiedParser.NumberContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#number.
    def exitNumber(self, ctx:CookiecutterUnifiedParser.NumberContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#json_bool.
    def enterJson_bool(self, ctx:CookiecutterUnifiedParser.Json_boolContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#json_bool.
    def exitJson_bool(self, ctx:CookiecutterUnifiedParser.Json_boolContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#nullValue.
    def enterNullValue(self, ctx:CookiecutterUnifiedParser.NullValueContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#nullValue.
    def exitNullValue(self, ctx:CookiecutterUnifiedParser.NullValueContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#ssti_start.
    def enterSsti_start(self, ctx:CookiecutterUnifiedParser.Ssti_startContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#ssti_start.
    def exitSsti_start(self, ctx:CookiecutterUnifiedParser.Ssti_startContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#sstiCookiecutter.
    def enterSstiCookiecutter(self, ctx:CookiecutterUnifiedParser.SstiCookiecutterContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#sstiCookiecutter.
    def exitSstiCookiecutter(self, ctx:CookiecutterUnifiedParser.SstiCookiecutterContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#projectPair.
    def enterProjectPair(self, ctx:CookiecutterUnifiedParser.ProjectPairContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#projectPair.
    def exitProjectPair(self, ctx:CookiecutterUnifiedParser.ProjectPairContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#payload1Pair.
    def enterPayload1Pair(self, ctx:CookiecutterUnifiedParser.Payload1PairContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#payload1Pair.
    def exitPayload1Pair(self, ctx:CookiecutterUnifiedParser.Payload1PairContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#payload2Pair.
    def enterPayload2Pair(self, ctx:CookiecutterUnifiedParser.Payload2PairContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#payload2Pair.
    def exitPayload2Pair(self, ctx:CookiecutterUnifiedParser.Payload2PairContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#payload3Pair.
    def enterPayload3Pair(self, ctx:CookiecutterUnifiedParser.Payload3PairContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#payload3Pair.
    def exitPayload3Pair(self, ctx:CookiecutterUnifiedParser.Payload3PairContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#payloadCurl.
    def enterPayloadCurl(self, ctx:CookiecutterUnifiedParser.PayloadCurlContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#payloadCurl.
    def exitPayloadCurl(self, ctx:CookiecutterUnifiedParser.PayloadCurlContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#payloadMath.
    def enterPayloadMath(self, ctx:CookiecutterUnifiedParser.PayloadMathContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#payloadMath.
    def exitPayloadMath(self, ctx:CookiecutterUnifiedParser.PayloadMathContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#payloadAbort.
    def enterPayloadAbort(self, ctx:CookiecutterUnifiedParser.PayloadAbortContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#payloadAbort.
    def exitPayloadAbort(self, ctx:CookiecutterUnifiedParser.PayloadAbortContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#cli_start.
    def enterCli_start(self, ctx:CookiecutterUnifiedParser.Cli_startContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#cli_start.
    def exitCli_start(self, ctx:CookiecutterUnifiedParser.Cli_startContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#command.
    def enterCommand(self, ctx:CookiecutterUnifiedParser.CommandContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#command.
    def exitCommand(self, ctx:CookiecutterUnifiedParser.CommandContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#list_installed_command.
    def enterList_installed_command(self, ctx:CookiecutterUnifiedParser.List_installed_commandContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#list_installed_command.
    def exitList_installed_command(self, ctx:CookiecutterUnifiedParser.List_installed_commandContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#render_command.
    def enterRender_command(self, ctx:CookiecutterUnifiedParser.Render_commandContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#render_command.
    def exitRender_command(self, ctx:CookiecutterUnifiedParser.Render_commandContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#nested_command.
    def enterNested_command(self, ctx:CookiecutterUnifiedParser.Nested_commandContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#nested_command.
    def exitNested_command(self, ctx:CookiecutterUnifiedParser.Nested_commandContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#replay_command.
    def enterReplay_command(self, ctx:CookiecutterUnifiedParser.Replay_commandContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#replay_command.
    def exitReplay_command(self, ctx:CookiecutterUnifiedParser.Replay_commandContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#list_tail.
    def enterList_tail(self, ctx:CookiecutterUnifiedParser.List_tailContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#list_tail.
    def exitList_tail(self, ctx:CookiecutterUnifiedParser.List_tailContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#render_tail.
    def enterRender_tail(self, ctx:CookiecutterUnifiedParser.Render_tailContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#render_tail.
    def exitRender_tail(self, ctx:CookiecutterUnifiedParser.Render_tailContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#replay_tail.
    def enterReplay_tail(self, ctx:CookiecutterUnifiedParser.Replay_tailContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#replay_tail.
    def exitReplay_tail(self, ctx:CookiecutterUnifiedParser.Replay_tailContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#list_item.
    def enterList_item(self, ctx:CookiecutterUnifiedParser.List_itemContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#list_item.
    def exitList_item(self, ctx:CookiecutterUnifiedParser.List_itemContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#render_item.
    def enterRender_item(self, ctx:CookiecutterUnifiedParser.Render_itemContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#render_item.
    def exitRender_item(self, ctx:CookiecutterUnifiedParser.Render_itemContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#replay_item.
    def enterReplay_item(self, ctx:CookiecutterUnifiedParser.Replay_itemContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#replay_item.
    def exitReplay_item(self, ctx:CookiecutterUnifiedParser.Replay_itemContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#template.
    def enterTemplate(self, ctx:CookiecutterUnifiedParser.TemplateContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#template.
    def exitTemplate(self, ctx:CookiecutterUnifiedParser.TemplateContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#nested_template.
    def enterNested_template(self, ctx:CookiecutterUnifiedParser.Nested_templateContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#nested_template.
    def exitNested_template(self, ctx:CookiecutterUnifiedParser.Nested_templateContext):
        pass


    # Enter a parse tree produced by CookiecutterUnifiedParser#replay_template.
    def enterReplay_template(self, ctx:CookiecutterUnifiedParser.Replay_templateContext):
        pass

    # Exit a parse tree produced by CookiecutterUnifiedParser#replay_template.
    def exitReplay_template(self, ctx:CookiecutterUnifiedParser.Replay_templateContext):
        pass



del CookiecutterUnifiedParser