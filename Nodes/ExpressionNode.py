from Nodes.Node import Node
from Nodes.TermNode import TermNode
from Nodes.Parsing import SPECIAL_SYMBOLS

class ExpressionNode(Node):

    def __init__(self):
        self.__t = TermNode()
        self.__exp = None
        self.__alt = 1

    def parse(self, t):
        self.__t.parse(t)
        if t.currentToken().value == SPECIAL_SYMBOLS["+"]:
            t.nextToken()
            self.__exp = ExpressionNode()
            self.__exp.parse(t)
            self.__alt = 2
        elif t.currentToken().value == SPECIAL_SYMBOLS["-"]:
            t.nextToken()
            self.__exp = ExpressionNode()
            self.__exp.parse(t)
            self.__alt = 3

    def pretty_print(self, shift=0):
        self.__t.pretty_print()
        if self.__exp is not None:
            if self.__alt == 2:
                print(" + ", end='')
            elif self.__alt == 3:
                print(" - ", end='')
            self.__exp.pretty_print()

    def execute(self):
        pass
