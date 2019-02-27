import sys
from Token import Token

from Nodes.ProgramNode import ProgramNode

from Tokenizer import Tokenizer

f = open(sys.argv[1],"r")
tokenizer = Tokenizer(f)
program = ProgramNode()
program.parse(tokenizer)
program.printN()
