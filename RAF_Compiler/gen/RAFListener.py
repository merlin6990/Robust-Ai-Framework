# Generated from E:/7-Semester/Compiler/Robust-Ai-Framework/RAF_Compiler/grammar/RAF.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RAFParser import RAFParser
else:
    from RAFParser import RAFParser

# This class defines a complete listener for a parse tree produced by RAFParser.
class RAFListener(ParseTreeListener):

    # Enter a parse tree produced by RAFParser#start.
    def enterStart(self, ctx:RAFParser.StartContext):
        pass

    # Exit a parse tree produced by RAFParser#start.
    def exitStart(self, ctx:RAFParser.StartContext):
        pass


    # Enter a parse tree produced by RAFParser#data_statement.
    def enterData_statement(self, ctx:RAFParser.Data_statementContext):
        pass

    # Exit a parse tree produced by RAFParser#data_statement.
    def exitData_statement(self, ctx:RAFParser.Data_statementContext):
        pass


    # Enter a parse tree produced by RAFParser#data.
    def enterData(self, ctx:RAFParser.DataContext):
        pass

    # Exit a parse tree produced by RAFParser#data.
    def exitData(self, ctx:RAFParser.DataContext):
        pass


    # Enter a parse tree produced by RAFParser#dataset.
    def enterDataset(self, ctx:RAFParser.DatasetContext):
        pass

    # Exit a parse tree produced by RAFParser#dataset.
    def exitDataset(self, ctx:RAFParser.DatasetContext):
        pass


    # Enter a parse tree produced by RAFParser#json.
    def enterJson(self, ctx:RAFParser.JsonContext):
        pass

    # Exit a parse tree produced by RAFParser#json.
    def exitJson(self, ctx:RAFParser.JsonContext):
        pass


    # Enter a parse tree produced by RAFParser#action.
    def enterAction(self, ctx:RAFParser.ActionContext):
        pass

    # Exit a parse tree produced by RAFParser#action.
    def exitAction(self, ctx:RAFParser.ActionContext):
        pass


    # Enter a parse tree produced by RAFParser#model_statement.
    def enterModel_statement(self, ctx:RAFParser.Model_statementContext):
        pass

    # Exit a parse tree produced by RAFParser#model_statement.
    def exitModel_statement(self, ctx:RAFParser.Model_statementContext):
        pass


    # Enter a parse tree produced by RAFParser#mlp.
    def enterMlp(self, ctx:RAFParser.MlpContext):
        pass

    # Exit a parse tree produced by RAFParser#mlp.
    def exitMlp(self, ctx:RAFParser.MlpContext):
        pass


    # Enter a parse tree produced by RAFParser#size.
    def enterSize(self, ctx:RAFParser.SizeContext):
        pass

    # Exit a parse tree produced by RAFParser#size.
    def exitSize(self, ctx:RAFParser.SizeContext):
        pass


    # Enter a parse tree produced by RAFParser#activation.
    def enterActivation(self, ctx:RAFParser.ActivationContext):
        pass

    # Exit a parse tree produced by RAFParser#activation.
    def exitActivation(self, ctx:RAFParser.ActivationContext):
        pass


    # Enter a parse tree produced by RAFParser#plot_statement.
    def enterPlot_statement(self, ctx:RAFParser.Plot_statementContext):
        pass

    # Exit a parse tree produced by RAFParser#plot_statement.
    def exitPlot_statement(self, ctx:RAFParser.Plot_statementContext):
        pass


    # Enter a parse tree produced by RAFParser#metric.
    def enterMetric(self, ctx:RAFParser.MetricContext):
        pass

    # Exit a parse tree produced by RAFParser#metric.
    def exitMetric(self, ctx:RAFParser.MetricContext):
        pass


    # Enter a parse tree produced by RAFParser#label_function.
    def enterLabel_function(self, ctx:RAFParser.Label_functionContext):
        pass

    # Exit a parse tree produced by RAFParser#label_function.
    def exitLabel_function(self, ctx:RAFParser.Label_functionContext):
        pass


    # Enter a parse tree produced by RAFParser#backdoor_function.
    def enterBackdoor_function(self, ctx:RAFParser.Backdoor_functionContext):
        pass

    # Exit a parse tree produced by RAFParser#backdoor_function.
    def exitBackdoor_function(self, ctx:RAFParser.Backdoor_functionContext):
        pass


    # Enter a parse tree produced by RAFParser#label_flip.
    def enterLabel_flip(self, ctx:RAFParser.Label_flipContext):
        pass

    # Exit a parse tree produced by RAFParser#label_flip.
    def exitLabel_flip(self, ctx:RAFParser.Label_flipContext):
        pass


    # Enter a parse tree produced by RAFParser#flip_statement.
    def enterFlip_statement(self, ctx:RAFParser.Flip_statementContext):
        pass

    # Exit a parse tree produced by RAFParser#flip_statement.
    def exitFlip_statement(self, ctx:RAFParser.Flip_statementContext):
        pass


    # Enter a parse tree produced by RAFParser#backdoor.
    def enterBackdoor(self, ctx:RAFParser.BackdoorContext):
        pass

    # Exit a parse tree produced by RAFParser#backdoor.
    def exitBackdoor(self, ctx:RAFParser.BackdoorContext):
        pass


    # Enter a parse tree produced by RAFParser#pattern.
    def enterPattern(self, ctx:RAFParser.PatternContext):
        pass

    # Exit a parse tree produced by RAFParser#pattern.
    def exitPattern(self, ctx:RAFParser.PatternContext):
        pass


    # Enter a parse tree produced by RAFParser#label.
    def enterLabel(self, ctx:RAFParser.LabelContext):
        pass

    # Exit a parse tree produced by RAFParser#label.
    def exitLabel(self, ctx:RAFParser.LabelContext):
        pass


    # Enter a parse tree produced by RAFParser#src.
    def enterSrc(self, ctx:RAFParser.SrcContext):
        pass

    # Exit a parse tree produced by RAFParser#src.
    def exitSrc(self, ctx:RAFParser.SrcContext):
        pass


    # Enter a parse tree produced by RAFParser#target.
    def enterTarget(self, ctx:RAFParser.TargetContext):
        pass

    # Exit a parse tree produced by RAFParser#target.
    def exitTarget(self, ctx:RAFParser.TargetContext):
        pass


    # Enter a parse tree produced by RAFParser#x.
    def enterX(self, ctx:RAFParser.XContext):
        pass

    # Exit a parse tree produced by RAFParser#x.
    def exitX(self, ctx:RAFParser.XContext):
        pass


    # Enter a parse tree produced by RAFParser#y.
    def enterY(self, ctx:RAFParser.YContext):
        pass

    # Exit a parse tree produced by RAFParser#y.
    def exitY(self, ctx:RAFParser.YContext):
        pass


    # Enter a parse tree produced by RAFParser#a.
    def enterA(self, ctx:RAFParser.AContext):
        pass

    # Exit a parse tree produced by RAFParser#a.
    def exitA(self, ctx:RAFParser.AContext):
        pass


    # Enter a parse tree produced by RAFParser#b.
    def enterB(self, ctx:RAFParser.BContext):
        pass

    # Exit a parse tree produced by RAFParser#b.
    def exitB(self, ctx:RAFParser.BContext):
        pass



del RAFParser