import sys
from Tokenizer.Token import Token
from Tokenizer.Tokenizer import Tokenizer
from Nodes.ProgramNode import ProgramNode

try:
    f = open(sys.argv[1],"r")
except IOError:
    print("Error: " + sys.argv[1] + " does not exist")
    exit()

tokenizer = Tokenizer(file=f)
program = ProgramNode()
program.parse(tokenizer)
program.execute()
