from Nodes.Node import Node
from Nodes.TermNode import TermNode

class ExpressionNode(Node):

    def __init__(self):
        self.__t = TermNode()
        self.__exp = None
        self.__alt = 1

    def parse(self, t):
        self.__t.parse(t)
        if t.currentToken().value == 22: # +
            t.nextToken()
            self.__exp = ExpressionNode()
            self.__exp.parse(t)
            self.__alt = 2
        elif t.currentToken().value == 23: # -
            t.nextToken()
            self.__exp = ExpressionNode()
            self.__exp.parse(t)
            self.__alt = 3

    def printN(self, shift=0):
        self.__t.printN()
        if self.__exp is not None:
            if self.__alt == 2:
                print(" + ", end='')
            elif self.__alt == 3:
                print(" - ", end='')
            self.__exp.printN()

    def execute(self):
        pass
