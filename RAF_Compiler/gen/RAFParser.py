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
        4,1,31,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,3,0,52,8,0,1,1,4,
        1,55,8,1,11,1,12,1,56,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,83,8,
        7,11,7,12,7,84,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,4,10,95,8,10,11,
        10,12,10,96,1,11,1,11,1,12,1,12,3,12,103,8,12,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,3,14,112,8,14,4,14,114,8,14,11,14,12,14,115,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,4,15,129,8,15,
        11,15,12,15,130,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,
        1,22,1,22,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,1,2,1,0,3,4,1,0,5,6,1,0,
        13,15,1,0,17,19,144,0,48,1,0,0,0,2,54,1,0,0,0,4,62,1,0,0,0,6,65,
        1,0,0,0,8,67,1,0,0,0,10,69,1,0,0,0,12,71,1,0,0,0,14,73,1,0,0,0,16,
        88,1,0,0,0,18,90,1,0,0,0,20,92,1,0,0,0,22,98,1,0,0,0,24,102,1,0,
        0,0,26,104,1,0,0,0,28,113,1,0,0,0,30,117,1,0,0,0,32,134,1,0,0,0,
        34,145,1,0,0,0,36,147,1,0,0,0,38,149,1,0,0,0,40,151,1,0,0,0,42,153,
        1,0,0,0,44,155,1,0,0,0,46,157,1,0,0,0,48,49,3,2,1,0,49,51,3,12,6,
        0,50,52,3,20,10,0,51,50,1,0,0,0,51,52,1,0,0,0,52,1,1,0,0,0,53,55,
        3,4,2,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,
        57,58,1,0,0,0,58,60,3,8,4,0,59,61,3,24,12,0,60,59,1,0,0,0,60,61,
        1,0,0,0,61,3,1,0,0,0,62,63,3,10,5,0,63,64,3,6,3,0,64,5,1,0,0,0,65,
        66,7,0,0,0,66,7,1,0,0,0,67,68,7,1,0,0,68,9,1,0,0,0,69,70,7,2,0,0,
        70,11,1,0,0,0,71,72,3,14,7,0,72,13,1,0,0,0,73,74,5,7,0,0,74,75,5,
        8,0,0,75,82,3,16,8,0,76,77,5,9,0,0,77,78,3,16,8,0,78,79,5,10,0,0,
        79,80,3,18,9,0,80,81,5,11,0,0,81,83,1,0,0,0,82,76,1,0,0,0,83,84,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,12,0,0,
        87,15,1,0,0,0,88,89,5,30,0,0,89,17,1,0,0,0,90,91,7,3,0,0,91,19,1,
        0,0,0,92,94,5,16,0,0,93,95,3,22,11,0,94,93,1,0,0,0,95,96,1,0,0,0,
        96,94,1,0,0,0,96,97,1,0,0,0,97,21,1,0,0,0,98,99,7,4,0,0,99,23,1,
        0,0,0,100,103,3,26,13,0,101,103,3,30,15,0,102,100,1,0,0,0,102,101,
        1,0,0,0,103,25,1,0,0,0,104,105,5,20,0,0,105,106,3,28,14,0,106,27,
        1,0,0,0,107,108,3,34,17,0,108,109,5,21,0,0,109,111,3,34,17,0,110,
        112,5,10,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,
        107,1,0,0,0,114,115,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,
        29,1,0,0,0,117,118,5,22,0,0,118,119,5,23,0,0,119,120,5,24,0,0,120,
        121,5,25,0,0,121,122,5,26,0,0,122,123,3,36,18,0,123,124,5,10,0,0,
        124,125,5,27,0,0,125,126,5,26,0,0,126,128,3,38,19,0,127,129,3,32,
        16,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,
        0,0,131,132,1,0,0,0,132,133,5,12,0,0,133,31,1,0,0,0,134,135,5,10,
        0,0,135,136,5,28,0,0,136,137,3,40,20,0,137,138,5,10,0,0,138,139,
        3,42,21,0,139,140,5,10,0,0,140,141,3,44,22,0,141,142,5,10,0,0,142,
        143,3,46,23,0,143,144,5,11,0,0,144,33,1,0,0,0,145,146,5,31,0,0,146,
        35,1,0,0,0,147,148,5,31,0,0,148,37,1,0,0,0,149,150,5,31,0,0,150,
        39,1,0,0,0,151,152,5,30,0,0,152,41,1,0,0,0,153,154,5,30,0,0,154,
        43,1,0,0,0,155,156,5,30,0,0,156,45,1,0,0,0,157,158,5,30,0,0,158,
        47,1,0,0,0,9,51,56,60,84,96,102,111,115,130
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
                     "'accuracy'", "'flip_poison'", "'->'", "'backdoor'", 
                     "':='", "'{'", "'src_class'", "':'", "'target_class'", 
                     "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "INTEGER", "String" ]

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
    RULE_pattern = 16
    RULE_label = 17
    RULE_src = 18
    RULE_target = 19
    RULE_x = 20
    RULE_y = 21
    RULE_a = 22
    RULE_b = 23

    ruleNames =  [ "start", "data_statement", "data", "dataset", "json", 
                   "action", "model_statement", "mlp", "size", "activation", 
                   "plot_statement", "metric", "poison_statement", "label_flip", 
                   "flip_statement", "backdoor", "pattern", "label", "src", 
                   "target", "x", "y", "a", "b" ]

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
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    WS=29
    INTEGER=30
    String=31

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
            self.state = 48
            self.data_statement()
            self.state = 49
            self.model_statement()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 50
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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.data()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
                    break

            self.state = 58
            self.json()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==22:
                self.state = 59
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
            self.state = 62
            self.action()
            self.state = 63
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
            self.state = 65
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
            self.state = 67
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
            self.state = 69
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
            self.state = 71
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
            self.state = 73
            self.match(RAFParser.T__6)
            self.state = 74
            self.match(RAFParser.T__7)
            self.state = 75
            self.size()
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.match(RAFParser.T__8)
                self.state = 77
                self.size()
                self.state = 78
                self.match(RAFParser.T__9)
                self.state = 79
                self.activation()
                self.state = 80
                self.match(RAFParser.T__10)
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 86
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
            self.state = 88
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
            self.state = 90
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
            self.state = 92
            self.match(RAFParser.T__15)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.metric()
                self.state = 96 
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
            self.state = 98
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = RAFParser.Label_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.label_flip()
                pass
            elif token in [22]:
                localctx = RAFParser.Backdoor_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 101
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
            self.state = 104
            self.match(RAFParser.T__19)
            self.state = 105
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
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.label()
                self.state = 108
                self.match(RAFParser.T__20)
                self.state = 109
                self.label()

                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 110
                    self.match(RAFParser.T__9)


                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
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

        def src(self):
            return self.getTypedRuleContext(RAFParser.SrcContext,0)


        def target(self):
            return self.getTypedRuleContext(RAFParser.TargetContext,0)


        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RAFParser.PatternContext)
            else:
                return self.getTypedRuleContext(RAFParser.PatternContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(RAFParser.T__21)
            self.state = 118
            self.match(RAFParser.T__22)
            self.state = 119
            self.match(RAFParser.T__23)
            self.state = 120
            self.match(RAFParser.T__24)
            self.state = 121
            self.match(RAFParser.T__25)
            self.state = 122
            self.src()
            self.state = 123
            self.match(RAFParser.T__9)
            self.state = 124
            self.match(RAFParser.T__26)
            self.state = 125
            self.match(RAFParser.T__25)
            self.state = 126
            self.target()
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.pattern()
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 132
            self.match(RAFParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def x(self):
            return self.getTypedRuleContext(RAFParser.XContext,0)


        def y(self):
            return self.getTypedRuleContext(RAFParser.YContext,0)


        def a(self):
            return self.getTypedRuleContext(RAFParser.AContext,0)


        def b(self):
            return self.getTypedRuleContext(RAFParser.BContext,0)


        def getRuleIndex(self):
            return RAFParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = RAFParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(RAFParser.T__9)
            self.state = 135
            self.match(RAFParser.T__27)
            self.state = 136
            self.x()
            self.state = 137
            self.match(RAFParser.T__9)
            self.state = 138
            self.y()
            self.state = 139
            self.match(RAFParser.T__9)
            self.state = 140
            self.a()
            self.state = 141
            self.match(RAFParser.T__9)
            self.state = 142
            self.b()
            self.state = 143
            self.match(RAFParser.T__10)
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
            self.state = 145
            self.match(RAFParser.String)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SrcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def String(self):
            return self.getToken(RAFParser.String, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_src

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSrc" ):
                listener.enterSrc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSrc" ):
                listener.exitSrc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSrc" ):
                return visitor.visitSrc(self)
            else:
                return visitor.visitChildren(self)




    def src(self):

        localctx = RAFParser.SrcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_src)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(RAFParser.String)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def String(self):
            return self.getToken(RAFParser.String, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget" ):
                listener.enterTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget" ):
                listener.exitTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget" ):
                return visitor.visitTarget(self)
            else:
                return visitor.visitChildren(self)




    def target(self):

        localctx = RAFParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(RAFParser.String)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(RAFParser.INTEGER, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_x

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX" ):
                listener.enterX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX" ):
                listener.exitX(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitX" ):
                return visitor.visitX(self)
            else:
                return visitor.visitChildren(self)




    def x(self):

        localctx = RAFParser.XContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_x)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(RAFParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(RAFParser.INTEGER, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_y

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterY" ):
                listener.enterY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitY" ):
                listener.exitY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitY" ):
                return visitor.visitY(self)
            else:
                return visitor.visitChildren(self)




    def y(self):

        localctx = RAFParser.YContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_y)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(RAFParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(RAFParser.INTEGER, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA" ):
                return visitor.visitA(self)
            else:
                return visitor.visitChildren(self)




    def a(self):

        localctx = RAFParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_a)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(RAFParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(RAFParser.INTEGER, 0)

        def getRuleIndex(self):
            return RAFParser.RULE_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB" ):
                listener.enterB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB" ):
                listener.exitB(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB" ):
                return visitor.visitB(self)
            else:
                return visitor.visitChildren(self)




    def b(self):

        localctx = RAFParser.BContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_b)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(RAFParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





