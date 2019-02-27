from Nodes.Node import Node
from Nodes.DeclarationSequenceNode import DeclarationSequenceNode
from Nodes.StatementSequenceNode import StatementSequenceNode
from Nodes.Match import match_consume, symbol_table

class ProgramNode(Node):

    def __init__(self):
        self.__ds = DeclarationSequenceNode()
        self.__ss = StatementSequenceNode()

    def parse(self, t):
        match_consume("program", t)
        self.__ds.parse(t)
        match_consume("begin", t)
        self.__ss.parse(t)
        match_consume("end", t)

    def printN(self, shift=0):
        print(shift*'  ' + "program")
        self.__ds.printN(shift + 1)
        print(shift*'  ' + "begin")
        self.__ss.printN(shift + 1)
        print(shift*'  ' + "end")

    def execute(self):
        self.__ds.execute()
        self.__ss.execute()
