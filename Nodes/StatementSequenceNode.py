from Nodes.Node import Node
from Nodes.StatementNode import StatementNode
from Nodes.Match import match_consume

class StatementSequenceNode(Node):

    def __init__(self):
        self.__s = StatementNode()
        self.__ss = None

    def parse(self, t):
        self.__s.parse(t)
        if t.currentToken().value != 3 and t.currentToken().value != 7: # look-ahead, 3 = end, 7 = else
            self.__ss = StatementSequenceNode()
            self.__ss.parse(t)

    def printN(self):
        self.__s.printN()
        if self.__ss != None:
            self.__ss.printN()

    def execute(self):
        pass
