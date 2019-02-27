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

    def printN(self):
        print("program")
        self.__ds.printN()
        print("begin")
        self.__ss.printN()
        print("end")

    def execute(self):
        self.__ds.execute()
        self.__ss.execute()
