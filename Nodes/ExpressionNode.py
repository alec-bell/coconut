from Nodes.Node import Node
from Nodes.Evaluable import Evaluable
from Nodes.TermNode import TermNode
from Nodes.Parsing import SPECIAL_SYMBOLS

class ExpressionNode(Node, Evaluable):

    def __init__(self):
        self.__t = TermNode()
        self.__exp = None
        self.__alt = 1

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
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

    def evaluate(self):
        if self.__alt == 1:
            return self.__t.evaluate()
        elif self.__alt == 2:
            return self.__t.evaluate() + self.__exp.evaluate()
        else:
            return self.__t.evaluate() - self.__exp.evaluate()
