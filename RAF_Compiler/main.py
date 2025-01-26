from antlr4 import *
import argparse
from RAFCustomListener import CustomRAFListener
from Repository.ast_to_networkx_graph import show_ast
from gen.RAFLexer import RAFLexer
from gen.RAFParser import RAFParser
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from RAFCodeGenerator import RAFCodeGenerator


def main(arguments):
	stream = FileStream(arguments.input, encoding='utf8')
	lexer = RAFLexer(stream)
	token_stream = CommonTokenStream(lexer)
	parser = RAFParser(token_stream)
	parse_tree = parser.start()
	ast_builder_listener = CustomRAFListener(parser.ruleNames)
	walker = ParseTreeWalker()
	walker.walk(t=parse_tree, listener=ast_builder_listener)
	ast = ast_builder_listener.ast
	show_ast(ast.root)
	post_order_ast_traverser = PostOrderASTTraverser()
	post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
	traversal = post_order_ast_traverser.traverse_ast(ast.root)
	code_generator = RAFCodeGenerator()
	generated_code = code_generator.generate_code(traversal)
	with open(arguments.output, 'w') as output_file:
		output_file.write(generated_code)


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'test2.raf')
	argparser.add_argument('-o', '--output', help='Output path', default=r'output.py')
	args = argparser.parse_args()
	main(args)
