from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.RAFListener import RAFListener
from gen.RAFParser import RAFParser


class CustomRAFListener(RAFListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['start','label_flip','mlp']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name,keep_node=True)

    def exitStart(self, ctx):
        make_ast_subtree(self.ast, ctx, "start", keep_node=True)




