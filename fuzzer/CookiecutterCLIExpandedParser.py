# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterCLIExpanded.g4 by ANTLR 4.13.1
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
        4,1,25,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,3,2,42,
        8,2,1,3,1,3,1,3,1,3,3,3,48,8,3,1,4,1,4,1,4,1,4,3,4,54,8,4,1,5,1,
        5,1,5,1,5,3,5,60,8,5,1,6,1,6,1,6,1,7,1,7,4,7,67,8,7,11,7,12,7,68,
        1,8,1,8,4,8,73,8,8,11,8,12,8,74,1,9,1,9,1,10,1,10,1,11,1,11,1,12,
        1,12,1,13,1,13,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,0,4,1,0,4,5,2,0,4,12,18,23,1,0,5,10,1,0,13,15,82,0,30,
        1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,43,1,0,0,0,8,49,1,0,0,0,10,55,
        1,0,0,0,12,61,1,0,0,0,14,66,1,0,0,0,16,72,1,0,0,0,18,76,1,0,0,0,
        20,78,1,0,0,0,22,80,1,0,0,0,24,82,1,0,0,0,26,84,1,0,0,0,28,86,1,
        0,0,0,30,31,3,2,1,0,31,32,5,0,0,1,32,1,1,0,0,0,33,38,3,4,2,0,34,
        38,3,6,3,0,35,38,3,8,4,0,36,38,3,10,5,0,37,33,1,0,0,0,37,34,1,0,
        0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,41,5,1,0,0,40,42,
        3,12,6,0,41,40,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,44,3,24,12,
        0,44,45,5,24,0,0,45,47,5,2,0,0,46,48,3,14,7,0,47,46,1,0,0,0,47,48,
        1,0,0,0,48,7,1,0,0,0,49,50,3,26,13,0,50,51,5,24,0,0,51,53,5,2,0,
        0,52,54,3,14,7,0,53,52,1,0,0,0,53,54,1,0,0,0,54,9,1,0,0,0,55,56,
        3,28,14,0,56,57,5,24,0,0,57,59,5,3,0,0,58,60,3,16,8,0,59,58,1,0,
        0,0,59,60,1,0,0,0,60,11,1,0,0,0,61,62,5,24,0,0,62,63,3,18,9,0,63,
        13,1,0,0,0,64,65,5,24,0,0,65,67,3,20,10,0,66,64,1,0,0,0,67,68,1,
        0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,15,1,0,0,0,70,71,5,24,0,0,71,
        73,3,22,11,0,72,70,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,1,0,
        0,0,75,17,1,0,0,0,76,77,7,0,0,0,77,19,1,0,0,0,78,79,7,1,0,0,79,21,
        1,0,0,0,80,81,7,2,0,0,81,23,1,0,0,0,82,83,7,3,0,0,83,25,1,0,0,0,
        84,85,5,16,0,0,85,27,1,0,0,0,86,87,5,17,0,0,87,29,1,0,0,0,7,37,41,
        47,53,59,68,74
    ]

class CookiecutterCLIExpandedParser ( Parser ):

    grammarFileName = "CookiecutterCLIExpanded.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-l'", "'--no-input'", "'--replay --replay-file tests/test-replay/valid_replay.json'", 
                     "'--default-config'", "'--config-file tests/test-config/valid-config.yaml'", 
                     "'--config-file tests/test-config/valid-partial-config.yaml'", 
                     "'--overwrite-if-exists'", "'--skip-if-file-exists'", 
                     "'--keep-project-on-failure'", "'-v'", "'--accept-hooks=yes'", 
                     "'--accept-hooks=no'", "'tests/fake-repo-pre/'", "'tests/fake-repo-tmpl/'", 
                     "'tests/fake-repo-dict/'", "'tests/fake-nested-templates/'", 
                     "'tests/fake-repo-replay/'", "'repo_name=fuzz-project'", 
                     "'project_name=Fuzz_Project'", "'project_short_description=Expanded_fuzzing'", 
                     "'full_name=Fuzz_User'", "'email=fuzz@example.com'", 
                     "'github_username=fuzz_user'", "' '" ]

    symbolicNames = [ "<INVALID>", "LIST_INSTALLED", "NO_INPUT", "REPLAY", 
                      "DEFAULT_CONFIG", "VALID_CONFIG", "PARTIAL_CONFIG", 
                      "OVERWRITE", "SKIP_ARG", "KEEP", "VERBOSE", "ACCEPT_YES", 
                      "ACCEPT_NO", "FAKE_REPO_PRE", "FAKE_REPO_TMPL", "FAKE_REPO_DICT", 
                      "FAKE_NESTED", "FAKE_REPO_REPLAY", "EXTRA_REPO_NAME", 
                      "EXTRA_PROJECT_NAME", "EXTRA_SHORT_DESC", "EXTRA_FULL_NAME", 
                      "EXTRA_EMAIL", "EXTRA_GITHUB", "SP", "WS" ]

    RULE_start = 0
    RULE_command = 1
    RULE_list_installed_command = 2
    RULE_render_command = 3
    RULE_nested_command = 4
    RULE_replay_command = 5
    RULE_list_tail = 6
    RULE_render_tail = 7
    RULE_replay_tail = 8
    RULE_list_item = 9
    RULE_render_item = 10
    RULE_replay_item = 11
    RULE_template = 12
    RULE_nested_template = 13
    RULE_replay_template = 14

    ruleNames =  [ "start", "command", "list_installed_command", "render_command", 
                   "nested_command", "replay_command", "list_tail", "render_tail", 
                   "replay_tail", "list_item", "render_item", "replay_item", 
                   "template", "nested_template", "replay_template" ]

    EOF = Token.EOF
    LIST_INSTALLED=1
    NO_INPUT=2
    REPLAY=3
    DEFAULT_CONFIG=4
    VALID_CONFIG=5
    PARTIAL_CONFIG=6
    OVERWRITE=7
    SKIP_ARG=8
    KEEP=9
    VERBOSE=10
    ACCEPT_YES=11
    ACCEPT_NO=12
    FAKE_REPO_PRE=13
    FAKE_REPO_TMPL=14
    FAKE_REPO_DICT=15
    FAKE_NESTED=16
    FAKE_REPO_REPLAY=17
    EXTRA_REPO_NAME=18
    EXTRA_PROJECT_NAME=19
    EXTRA_SHORT_DESC=20
    EXTRA_FULL_NAME=21
    EXTRA_EMAIL=22
    EXTRA_GITHUB=23
    SP=24
    WS=25

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

        def command(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.CommandContext,0)


        def EOF(self):
            return self.getToken(CookiecutterCLIExpandedParser.EOF, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_start

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

        localctx = CookiecutterCLIExpandedParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.command()
            self.state = 31
            self.match(CookiecutterCLIExpandedParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_installed_command(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.List_installed_commandContext,0)


        def render_command(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Render_commandContext,0)


        def nested_command(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Nested_commandContext,0)


        def replay_command(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Replay_commandContext,0)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = CookiecutterCLIExpandedParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.list_installed_command()
                pass
            elif token in [13, 14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.render_command()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.nested_command()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.replay_command()
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


    class List_installed_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_INSTALLED(self):
            return self.getToken(CookiecutterCLIExpandedParser.LIST_INSTALLED, 0)

        def list_tail(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.List_tailContext,0)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_list_installed_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_installed_command" ):
                listener.enterList_installed_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_installed_command" ):
                listener.exitList_installed_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_installed_command" ):
                return visitor.visitList_installed_command(self)
            else:
                return visitor.visitChildren(self)




    def list_installed_command(self):

        localctx = CookiecutterCLIExpandedParser.List_installed_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_installed_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CookiecutterCLIExpandedParser.LIST_INSTALLED)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 40
                self.list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Render_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def template(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.TemplateContext,0)


        def SP(self):
            return self.getToken(CookiecutterCLIExpandedParser.SP, 0)

        def NO_INPUT(self):
            return self.getToken(CookiecutterCLIExpandedParser.NO_INPUT, 0)

        def render_tail(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Render_tailContext,0)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_render_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRender_command" ):
                listener.enterRender_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRender_command" ):
                listener.exitRender_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRender_command" ):
                return visitor.visitRender_command(self)
            else:
                return visitor.visitChildren(self)




    def render_command(self):

        localctx = CookiecutterCLIExpandedParser.Render_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_render_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.template()
            self.state = 44
            self.match(CookiecutterCLIExpandedParser.SP)
            self.state = 45
            self.match(CookiecutterCLIExpandedParser.NO_INPUT)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 46
                self.render_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nested_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nested_template(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Nested_templateContext,0)


        def SP(self):
            return self.getToken(CookiecutterCLIExpandedParser.SP, 0)

        def NO_INPUT(self):
            return self.getToken(CookiecutterCLIExpandedParser.NO_INPUT, 0)

        def render_tail(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Render_tailContext,0)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_nested_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNested_command" ):
                listener.enterNested_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNested_command" ):
                listener.exitNested_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested_command" ):
                return visitor.visitNested_command(self)
            else:
                return visitor.visitChildren(self)




    def nested_command(self):

        localctx = CookiecutterCLIExpandedParser.Nested_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nested_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.nested_template()
            self.state = 50
            self.match(CookiecutterCLIExpandedParser.SP)
            self.state = 51
            self.match(CookiecutterCLIExpandedParser.NO_INPUT)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 52
                self.render_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Replay_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def replay_template(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Replay_templateContext,0)


        def SP(self):
            return self.getToken(CookiecutterCLIExpandedParser.SP, 0)

        def REPLAY(self):
            return self.getToken(CookiecutterCLIExpandedParser.REPLAY, 0)

        def replay_tail(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Replay_tailContext,0)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_replay_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplay_command" ):
                listener.enterReplay_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplay_command" ):
                listener.exitReplay_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplay_command" ):
                return visitor.visitReplay_command(self)
            else:
                return visitor.visitChildren(self)




    def replay_command(self):

        localctx = CookiecutterCLIExpandedParser.Replay_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_replay_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.replay_template()
            self.state = 56
            self.match(CookiecutterCLIExpandedParser.SP)
            self.state = 57
            self.match(CookiecutterCLIExpandedParser.REPLAY)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 58
                self.replay_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SP(self):
            return self.getToken(CookiecutterCLIExpandedParser.SP, 0)

        def list_item(self):
            return self.getTypedRuleContext(CookiecutterCLIExpandedParser.List_itemContext,0)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_list_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_tail" ):
                listener.enterList_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_tail" ):
                listener.exitList_tail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_tail" ):
                return visitor.visitList_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_tail(self):

        localctx = CookiecutterCLIExpandedParser.List_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(CookiecutterCLIExpandedParser.SP)
            self.state = 62
            self.list_item()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Render_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SP(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterCLIExpandedParser.SP)
            else:
                return self.getToken(CookiecutterCLIExpandedParser.SP, i)

        def render_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CookiecutterCLIExpandedParser.Render_itemContext)
            else:
                return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Render_itemContext,i)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_render_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRender_tail" ):
                listener.enterRender_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRender_tail" ):
                listener.exitRender_tail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRender_tail" ):
                return visitor.visitRender_tail(self)
            else:
                return visitor.visitChildren(self)




    def render_tail(self):

        localctx = CookiecutterCLIExpandedParser.Render_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_render_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.match(CookiecutterCLIExpandedParser.SP)
                self.state = 65
                self.render_item()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Replay_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SP(self, i:int=None):
            if i is None:
                return self.getTokens(CookiecutterCLIExpandedParser.SP)
            else:
                return self.getToken(CookiecutterCLIExpandedParser.SP, i)

        def replay_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CookiecutterCLIExpandedParser.Replay_itemContext)
            else:
                return self.getTypedRuleContext(CookiecutterCLIExpandedParser.Replay_itemContext,i)


        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_replay_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplay_tail" ):
                listener.enterReplay_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplay_tail" ):
                listener.exitReplay_tail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplay_tail" ):
                return visitor.visitReplay_tail(self)
            else:
                return visitor.visitChildren(self)




    def replay_tail(self):

        localctx = CookiecutterCLIExpandedParser.Replay_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_replay_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.match(CookiecutterCLIExpandedParser.SP)
                self.state = 71
                self.replay_item()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.DEFAULT_CONFIG, 0)

        def VALID_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.VALID_CONFIG, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_list_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_item" ):
                listener.enterList_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_item" ):
                listener.exitList_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_item" ):
                return visitor.visitList_item(self)
            else:
                return visitor.visitChildren(self)




    def list_item(self):

        localctx = CookiecutterCLIExpandedParser.List_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class Render_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.DEFAULT_CONFIG, 0)

        def VALID_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.VALID_CONFIG, 0)

        def PARTIAL_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.PARTIAL_CONFIG, 0)

        def OVERWRITE(self):
            return self.getToken(CookiecutterCLIExpandedParser.OVERWRITE, 0)

        def SKIP_ARG(self):
            return self.getToken(CookiecutterCLIExpandedParser.SKIP_ARG, 0)

        def KEEP(self):
            return self.getToken(CookiecutterCLIExpandedParser.KEEP, 0)

        def VERBOSE(self):
            return self.getToken(CookiecutterCLIExpandedParser.VERBOSE, 0)

        def ACCEPT_YES(self):
            return self.getToken(CookiecutterCLIExpandedParser.ACCEPT_YES, 0)

        def ACCEPT_NO(self):
            return self.getToken(CookiecutterCLIExpandedParser.ACCEPT_NO, 0)

        def EXTRA_REPO_NAME(self):
            return self.getToken(CookiecutterCLIExpandedParser.EXTRA_REPO_NAME, 0)

        def EXTRA_PROJECT_NAME(self):
            return self.getToken(CookiecutterCLIExpandedParser.EXTRA_PROJECT_NAME, 0)

        def EXTRA_SHORT_DESC(self):
            return self.getToken(CookiecutterCLIExpandedParser.EXTRA_SHORT_DESC, 0)

        def EXTRA_FULL_NAME(self):
            return self.getToken(CookiecutterCLIExpandedParser.EXTRA_FULL_NAME, 0)

        def EXTRA_EMAIL(self):
            return self.getToken(CookiecutterCLIExpandedParser.EXTRA_EMAIL, 0)

        def EXTRA_GITHUB(self):
            return self.getToken(CookiecutterCLIExpandedParser.EXTRA_GITHUB, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_render_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRender_item" ):
                listener.enterRender_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRender_item" ):
                listener.exitRender_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRender_item" ):
                return visitor.visitRender_item(self)
            else:
                return visitor.visitChildren(self)




    def render_item(self):

        localctx = CookiecutterCLIExpandedParser.Render_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_render_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16523248) != 0)):
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


    class Replay_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALID_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.VALID_CONFIG, 0)

        def PARTIAL_CONFIG(self):
            return self.getToken(CookiecutterCLIExpandedParser.PARTIAL_CONFIG, 0)

        def OVERWRITE(self):
            return self.getToken(CookiecutterCLIExpandedParser.OVERWRITE, 0)

        def SKIP_ARG(self):
            return self.getToken(CookiecutterCLIExpandedParser.SKIP_ARG, 0)

        def KEEP(self):
            return self.getToken(CookiecutterCLIExpandedParser.KEEP, 0)

        def VERBOSE(self):
            return self.getToken(CookiecutterCLIExpandedParser.VERBOSE, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_replay_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplay_item" ):
                listener.enterReplay_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplay_item" ):
                listener.exitReplay_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplay_item" ):
                return visitor.visitReplay_item(self)
            else:
                return visitor.visitChildren(self)




    def replay_item(self):

        localctx = CookiecutterCLIExpandedParser.Replay_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_replay_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
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


    class TemplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FAKE_REPO_PRE(self):
            return self.getToken(CookiecutterCLIExpandedParser.FAKE_REPO_PRE, 0)

        def FAKE_REPO_TMPL(self):
            return self.getToken(CookiecutterCLIExpandedParser.FAKE_REPO_TMPL, 0)

        def FAKE_REPO_DICT(self):
            return self.getToken(CookiecutterCLIExpandedParser.FAKE_REPO_DICT, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate" ):
                listener.enterTemplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate" ):
                listener.exitTemplate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate" ):
                return visitor.visitTemplate(self)
            else:
                return visitor.visitChildren(self)




    def template(self):

        localctx = CookiecutterCLIExpandedParser.TemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_template)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
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


    class Nested_templateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FAKE_NESTED(self):
            return self.getToken(CookiecutterCLIExpandedParser.FAKE_NESTED, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_nested_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNested_template" ):
                listener.enterNested_template(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNested_template" ):
                listener.exitNested_template(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested_template" ):
                return visitor.visitNested_template(self)
            else:
                return visitor.visitChildren(self)




    def nested_template(self):

        localctx = CookiecutterCLIExpandedParser.Nested_templateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_nested_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(CookiecutterCLIExpandedParser.FAKE_NESTED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Replay_templateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FAKE_REPO_REPLAY(self):
            return self.getToken(CookiecutterCLIExpandedParser.FAKE_REPO_REPLAY, 0)

        def getRuleIndex(self):
            return CookiecutterCLIExpandedParser.RULE_replay_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplay_template" ):
                listener.enterReplay_template(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplay_template" ):
                listener.exitReplay_template(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplay_template" ):
                return visitor.visitReplay_template(self)
            else:
                return visitor.visitChildren(self)




    def replay_template(self):

        localctx = CookiecutterCLIExpandedParser.Replay_templateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_replay_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(CookiecutterCLIExpandedParser.FAKE_REPO_REPLAY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





