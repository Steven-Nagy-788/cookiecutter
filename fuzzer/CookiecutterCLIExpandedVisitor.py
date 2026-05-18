# Generated from /media/steven/MaD/projects/cookiecutter/fuzzer/CookiecutterCLIExpanded.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CookiecutterCLIExpandedParser import CookiecutterCLIExpandedParser
else:
    from CookiecutterCLIExpandedParser import CookiecutterCLIExpandedParser

# This class defines a complete generic visitor for a parse tree produced by CookiecutterCLIExpandedParser.

class CookiecutterCLIExpandedVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CookiecutterCLIExpandedParser#start.
    def visitStart(self, ctx:CookiecutterCLIExpandedParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#command.
    def visitCommand(self, ctx:CookiecutterCLIExpandedParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#list_installed_command.
    def visitList_installed_command(self, ctx:CookiecutterCLIExpandedParser.List_installed_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#render_command.
    def visitRender_command(self, ctx:CookiecutterCLIExpandedParser.Render_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#nested_command.
    def visitNested_command(self, ctx:CookiecutterCLIExpandedParser.Nested_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#replay_command.
    def visitReplay_command(self, ctx:CookiecutterCLIExpandedParser.Replay_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#list_tail.
    def visitList_tail(self, ctx:CookiecutterCLIExpandedParser.List_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#render_tail.
    def visitRender_tail(self, ctx:CookiecutterCLIExpandedParser.Render_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#replay_tail.
    def visitReplay_tail(self, ctx:CookiecutterCLIExpandedParser.Replay_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#list_item.
    def visitList_item(self, ctx:CookiecutterCLIExpandedParser.List_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#render_item.
    def visitRender_item(self, ctx:CookiecutterCLIExpandedParser.Render_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#replay_item.
    def visitReplay_item(self, ctx:CookiecutterCLIExpandedParser.Replay_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#template.
    def visitTemplate(self, ctx:CookiecutterCLIExpandedParser.TemplateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#nested_template.
    def visitNested_template(self, ctx:CookiecutterCLIExpandedParser.Nested_templateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CookiecutterCLIExpandedParser#replay_template.
    def visitReplay_template(self, ctx:CookiecutterCLIExpandedParser.Replay_templateContext):
        return self.visitChildren(ctx)



del CookiecutterCLIExpandedParser