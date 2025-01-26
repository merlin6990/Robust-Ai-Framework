# Generated from E:/7-Semester/Compiler/Robust-Ai-Framework/RAF_Compiler/grammar/RAF.g4 by ANTLR 4.13.1
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
        4,1,25,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,3,0,40,8,0,1,
        1,4,1,43,8,1,11,1,12,1,44,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,3,1,3,
        1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,
        71,8,7,11,7,12,7,72,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,4,10,83,8,
        10,11,10,12,10,84,1,11,1,11,1,12,1,12,3,12,91,8,12,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,3,14,100,8,14,4,14,102,8,14,11,14,12,14,103,
        1,15,1,15,1,16,1,16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,0,5,1,0,1,2,1,0,3,4,1,0,5,6,1,0,13,15,
        1,0,17,19,101,0,36,1,0,0,0,2,42,1,0,0,0,4,50,1,0,0,0,6,53,1,0,0,
        0,8,55,1,0,0,0,10,57,1,0,0,0,12,59,1,0,0,0,14,61,1,0,0,0,16,76,1,
        0,0,0,18,78,1,0,0,0,20,80,1,0,0,0,22,86,1,0,0,0,24,90,1,0,0,0,26,
        92,1,0,0,0,28,101,1,0,0,0,30,105,1,0,0,0,32,107,1,0,0,0,34,109,1,
        0,0,0,36,37,3,2,1,0,37,39,3,12,6,0,38,40,3,20,10,0,39,38,1,0,0,0,
        39,40,1,0,0,0,40,1,1,0,0,0,41,43,3,4,2,0,42,41,1,0,0,0,43,44,1,0,
        0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,48,3,8,4,0,47,49,
        3,24,12,0,48,47,1,0,0,0,48,49,1,0,0,0,49,3,1,0,0,0,50,51,3,10,5,
        0,51,52,3,6,3,0,52,5,1,0,0,0,53,54,7,0,0,0,54,7,1,0,0,0,55,56,7,
        1,0,0,56,9,1,0,0,0,57,58,7,2,0,0,58,11,1,0,0,0,59,60,3,14,7,0,60,
        13,1,0,0,0,61,62,5,7,0,0,62,63,5,8,0,0,63,70,3,16,8,0,64,65,5,9,
        0,0,65,66,3,16,8,0,66,67,5,10,0,0,67,68,3,18,9,0,68,69,5,11,0,0,
        69,71,1,0,0,0,70,64,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,
        0,0,0,73,74,1,0,0,0,74,75,5,12,0,0,75,15,1,0,0,0,76,77,5,24,0,0,
        77,17,1,0,0,0,78,79,7,3,0,0,79,19,1,0,0,0,80,82,5,16,0,0,81,83,3,
        22,11,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,
        85,21,1,0,0,0,86,87,7,4,0,0,87,23,1,0,0,0,88,91,3,26,13,0,89,91,
        3,30,15,0,90,88,1,0,0,0,90,89,1,0,0,0,91,25,1,0,0,0,92,93,5,20,0,
        0,93,94,3,28,14,0,94,27,1,0,0,0,95,96,3,34,17,0,96,97,5,21,0,0,97,
        99,3,34,17,0,98,100,5,10,0,0,99,98,1,0,0,0,99,100,1,0,0,0,100,102,
        1,0,0,0,101,95,1,0,0,0,102,103,1,0,0,0,103,101,1,0,0,0,103,104,1,
        0,0,0,104,29,1,0,0,0,105,106,3,32,16,0,106,31,1,0,0,0,107,108,5,
        22,0,0,108,33,1,0,0,0,109,110,5,25,0,0,110,35,1,0,0,0,8,39,44,48,
        72,84,90,99,103
    ]

class RAFParser ( Parser ):

    grammarFileName = "RAF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MNIST'", "'CIFAR'", "'use_json'", "'use_default'", 
                     "'Load'", "'Save'", "'MLP'", "'Layer_Size={'", "',('", 
                     "','", "')'", "'}'", "'\"relu\"'", "'\"sigmoid\"'", 
                     "'\"softmax\"'", "'plot'", "'val_acc'", "'confusion_matrix'", 
                     "'accuracy'", "'flip_poison'", "'->'", "'sample'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "INTEGER", 
                      "String" ]

    RULE_start = 0
    RULE_data_statement = 1
    RULE_data = 2
    RULE_dataset = 3
    RULE_json = 4
    RULE_action = 5
    RULE_model_statement = 6
    RULE_mlp = 7
    RULE_size = 8
    RULE_activation = 9
    RULE_plot_statement = 10
    RULE_metric = 11
    RULE_poison_statement = 12
    RULE_label_flip = 13
    RULE_flip_statement = 14
    RULE_backdoor = 15
    RULE_backdoor_type = 16
    RULE_label = 17

    ruleNames =  [ "start", "data_statement", "data", "dataset", "json", 
                   "action", "model_statement", "mlp", "size", "activation", 
                   "plot_statement", "metric", "poison_statement", "label_flip", 
                   "flip_statement", "backdoor", "backdoor_type", "label" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    WS=23
    INTEGER=24
    String=25

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

        def data_statement(self):
            return self.getTypedRuleContext(RAFParser.Data_statementContext,0)


        def model_statement(self):
            return self.getTypedRuleContext(RAFParser.Model_statementContext,0)


        def plot_statement(self):
            return self.getTypedRuleContext(RAFParser.Plot_statementContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_start

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

        localctx = RAFParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.data_statement()
            self.state = 37
            self.model_statement()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 38
                self.plot_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def json(self):
            return self.getTypedRuleContext(RAFParser.JsonContext,0)


        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RAFParser.DataContext)
            else:
                return self.getTypedRuleContext(RAFParser.DataContext,i)


        def poison_statement(self):
            return self.getTypedRuleContext(RAFParser.Poison_statementContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_data_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_statement" ):
                listener.enterData_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_statement" ):
                listener.exitData_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_statement" ):
                return visitor.visitData_statement(self)
            else:
                return visitor.visitChildren(self)




    def data_statement(self):

        localctx = RAFParser.Data_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.data()
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
                    break

            self.state = 46
            self.json()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==22:
                self.state = 47
                self.poison_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(RAFParser.ActionContext,0)


        def dataset(self):
            return self.getTypedRuleContext(RAFParser.DatasetContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = RAFParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.action()
            self.state = 51
            self.dataset()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatasetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RAFParser.RULE_dataset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataset" ):
                listener.enterDataset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataset" ):
                listener.exitDataset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataset" ):
                return visitor.visitDataset(self)
            else:
                return visitor.visitChildren(self)




    def dataset(self):

        localctx = RAFParser.DatasetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dataset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RAFParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = RAFParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_json)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RAFParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = RAFParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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


    class Model_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mlp(self):
            return self.getTypedRuleContext(RAFParser.MlpContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_model_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_statement" ):
                listener.enterModel_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_statement" ):
                listener.exitModel_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel_statement" ):
                return visitor.visitModel_statement(self)
            else:
                return visitor.visitChildren(self)




    def model_statement(self):

        localctx = RAFParser.Model_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_model_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.mlp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MlpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RAFParser.SizeContext)
            else:
                return self.getTypedRuleContext(RAFParser.SizeContext,i)


        def activation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RAFParser.ActivationContext)
            else:
                return self.getTypedRuleContext(RAFParser.ActivationContext,i)


        def getRuleIndex(self):
            return RAFParser.RULE_mlp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMlp" ):
                listener.enterMlp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMlp" ):
                listener.exitMlp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlp" ):
                return visitor.visitMlp(self)
            else:
                return visitor.visitChildren(self)




    def mlp(self):

        localctx = RAFParser.MlpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mlp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(RAFParser.T__6)
            self.state = 62
            self.match(RAFParser.T__7)
            self.state = 63
            self.size()
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.match(RAFParser.T__8)
                self.state = 65
                self.size()
                self.state = 66
                self.match(RAFParser.T__9)
                self.state = 67
                self.activation()
                self.state = 68
                self.match(RAFParser.T__10)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 74
            self.match(RAFParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(RAFParser.INTEGER, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = RAFParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(RAFParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActivationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RAFParser.RULE_activation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActivation" ):
                listener.enterActivation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActivation" ):
                listener.exitActivation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActivation" ):
                return visitor.visitActivation(self)
            else:
                return visitor.visitChildren(self)




    def activation(self):

        localctx = RAFParser.ActivationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_activation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
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


    class Plot_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metric(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RAFParser.MetricContext)
            else:
                return self.getTypedRuleContext(RAFParser.MetricContext,i)


        def getRuleIndex(self):
            return RAFParser.RULE_plot_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlot_statement" ):
                listener.enterPlot_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlot_statement" ):
                listener.exitPlot_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot_statement" ):
                return visitor.visitPlot_statement(self)
            else:
                return visitor.visitChildren(self)




    def plot_statement(self):

        localctx = RAFParser.Plot_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_plot_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(RAFParser.T__15)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.metric()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RAFParser.RULE_metric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetric" ):
                listener.enterMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetric" ):
                listener.exitMetric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetric" ):
                return visitor.visitMetric(self)
            else:
                return visitor.visitChildren(self)




    def metric(self):

        localctx = RAFParser.MetricContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_metric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
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


    class Poison_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.datatype = str()


        def getRuleIndex(self):
            return RAFParser.RULE_poison_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.datatype = ctx.datatype



    class Label_functionContext(Poison_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RAFParser.Poison_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label_flip(self):
            return self.getTypedRuleContext(RAFParser.Label_flipContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_function" ):
                listener.enterLabel_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_function" ):
                listener.exitLabel_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_function" ):
                return visitor.visitLabel_function(self)
            else:
                return visitor.visitChildren(self)


    class Backdoor_functionContext(Poison_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RAFParser.Poison_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def backdoor(self):
            return self.getTypedRuleContext(RAFParser.BackdoorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackdoor_function" ):
                listener.enterBackdoor_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackdoor_function" ):
                listener.exitBackdoor_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackdoor_function" ):
                return visitor.visitBackdoor_function(self)
            else:
                return visitor.visitChildren(self)



    def poison_statement(self):

        localctx = RAFParser.Poison_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_poison_statement)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = RAFParser.Label_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.label_flip()
                pass
            elif token in [22]:
                localctx = RAFParser.Backdoor_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.backdoor()
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


    class Label_flipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def flip_statement(self):
            return self.getTypedRuleContext(RAFParser.Flip_statementContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_label_flip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_flip" ):
                listener.enterLabel_flip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_flip" ):
                listener.exitLabel_flip(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_flip" ):
                return visitor.visitLabel_flip(self)
            else:
                return visitor.visitChildren(self)




    def label_flip(self):

        localctx = RAFParser.Label_flipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_label_flip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(RAFParser.T__19)
            self.state = 93
            self.flip_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flip_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RAFParser.LabelContext)
            else:
                return self.getTypedRuleContext(RAFParser.LabelContext,i)


        def getRuleIndex(self):
            return RAFParser.RULE_flip_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlip_statement" ):
                listener.enterFlip_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlip_statement" ):
                listener.exitFlip_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlip_statement" ):
                return visitor.visitFlip_statement(self)
            else:
                return visitor.visitChildren(self)




    def flip_statement(self):

        localctx = RAFParser.Flip_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_flip_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 95
                self.label()
                self.state = 96
                self.match(RAFParser.T__20)
                self.state = 97
                self.label()

                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 98
                    self.match(RAFParser.T__9)


                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackdoorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def backdoor_type(self):
            return self.getTypedRuleContext(RAFParser.Backdoor_typeContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_backdoor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackdoor" ):
                listener.enterBackdoor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackdoor" ):
                listener.exitBackdoor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackdoor" ):
                return visitor.visitBackdoor(self)
            else:
                return visitor.visitChildren(self)




    def backdoor(self):

        localctx = RAFParser.BackdoorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_backdoor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.backdoor_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Backdoor_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RAFParser.RULE_backdoor_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackdoor_type" ):
                listener.enterBackdoor_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackdoor_type" ):
                listener.exitBackdoor_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackdoor_type" ):
                return visitor.visitBackdoor_type(self)
            else:
                return visitor.visitChildren(self)




    def backdoor_type(self):

        localctx = RAFParser.Backdoor_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_backdoor_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(RAFParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def String(self):
            return self.getToken(RAFParser.String, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = RAFParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(RAFParser.String)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





