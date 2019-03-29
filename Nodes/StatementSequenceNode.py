from Nodes.Node import Node
from Nodes.Executable import Executable
from Nodes.StatementNode import StatementNode
from Nodes.Parsing import match_consume, RESERVED_WORDS

class StatementSequenceNode(Node, Executable):

    def __init__(self):
        self.__s = StatementNode()
        self.__ss = None

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        self.__s.parse(t)
        if t.currentToken().value != RESERVED_WORDS["end"] and t.currentToken().value != RESERVED_WORDS["else"]:
            self.__ss = StatementSequenceNode()
            self.__ss.parse(t)

    def pretty_print(self, shift=0):
        self.__s.pretty_print(shift)
        if self.__ss != None:
            self.__ss.pretty_print(shift)

    def execute(self):
        self.__s.execute()
        if self.__ss is not None:
            self.__ss.execute()
