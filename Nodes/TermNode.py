from Nodes.Node import Node
from Nodes.Evaluable import Evaluable
from Nodes.FacNode import FacNode
from Nodes.Parsing import match_consume, SPECIAL_SYMBOLS

class TermNode(Node, Evaluable):

    def __init__(self):
        self.__fac = FacNode()
        self.__t = None

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        self.__fac.parse(t)
        if t.currentToken().value == SPECIAL_SYMBOLS["*"]:
            match_consume("*", t)
            self.__t = TermNode()
            self.__t.parse(t)

    def pretty_print(self, shift=0):
        self.__fac.pretty_print()
        if self.__t is not None:
            print(" * ", end='')
            self.__t.pretty_print()

    def evaluate(self):
        if self.__t is None:
            return self.__fac.evaluate()
        else:
            return self.__fac.evaluate() * self.__t.evaluate()
