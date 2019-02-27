from Nodes.Node import Node
from Nodes.FacNode import FacNode
from Nodes.Match import match_consume

class TermNode(Node):

    def __init__(self):
        self.__fac = FacNode()
        self.__t = None

    def parse(self, t):
        self.__fac.parse(t)
        if t.currentToken().value == 24: # *
            match_consume("*", t)
            self.__t = TermNode()
            self.__t.parse(t)

    def printN(self, shift=0):
        self.__fac.printN()
        if self.__t is not None:
            print(" * ", end='')
            self.__t.printN()

    def execute(self):
        pass
