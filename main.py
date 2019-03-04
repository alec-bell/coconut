import sys
from Tokenizer.Token import Token
from Tokenizer.Tokenizer import Tokenizer
from Nodes.ProgramNode import ProgramNode

f = open(sys.argv[1],"r")
tokenizer = Tokenizer(f)
program = ProgramNode()
program.parse(tokenizer)
program.pretty_print()
