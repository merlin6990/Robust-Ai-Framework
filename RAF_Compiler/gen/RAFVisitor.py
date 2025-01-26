# Generated from E:/7-Semester/Compiler/Robust-Ai-Framework/RAF_Compiler/grammar/RAF.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RAFParser import RAFParser
else:
    from RAFParser import RAFParser

# This class defines a complete generic visitor for a parse tree produced by RAFParser.

class RAFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RAFParser#start.
    def visitStart(self, ctx:RAFParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#data_statement.
    def visitData_statement(self, ctx:RAFParser.Data_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#data.
    def visitData(self, ctx:RAFParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#dataset.
    def visitDataset(self, ctx:RAFParser.DatasetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#json.
    def visitJson(self, ctx:RAFParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#action.
    def visitAction(self, ctx:RAFParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#model_statement.
    def visitModel_statement(self, ctx:RAFParser.Model_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#mlp.
    def visitMlp(self, ctx:RAFParser.MlpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#size.
    def visitSize(self, ctx:RAFParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#activation.
    def visitActivation(self, ctx:RAFParser.ActivationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#plot_statement.
    def visitPlot_statement(self, ctx:RAFParser.Plot_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#metric.
    def visitMetric(self, ctx:RAFParser.MetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#label_function.
    def visitLabel_function(self, ctx:RAFParser.Label_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#backdoor_function.
    def visitBackdoor_function(self, ctx:RAFParser.Backdoor_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#label_flip.
    def visitLabel_flip(self, ctx:RAFParser.Label_flipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#flip_statement.
    def visitFlip_statement(self, ctx:RAFParser.Flip_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#backdoor.
    def visitBackdoor(self, ctx:RAFParser.BackdoorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#pattern.
    def visitPattern(self, ctx:RAFParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#label.
    def visitLabel(self, ctx:RAFParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#src.
    def visitSrc(self, ctx:RAFParser.SrcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#target.
    def visitTarget(self, ctx:RAFParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#x.
    def visitX(self, ctx:RAFParser.XContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#y.
    def visitY(self, ctx:RAFParser.YContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#a.
    def visitA(self, ctx:RAFParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RAFParser#b.
    def visitB(self, ctx:RAFParser.BContext):
        return self.visitChildren(ctx)



del RAFParser