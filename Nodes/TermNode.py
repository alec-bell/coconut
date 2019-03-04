from Nodes.Node import Node
from Nodes.FacNode import FacNode
from Nodes.Parsing import match_consume, SPECIAL_SYMBOLS

class TermNode(Node):

    def __init__(self):
        self.__fac = FacNode()
        self.__t = None

    def parse(self, t):
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

    def execute(self):
        pass
