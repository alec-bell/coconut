from Nodes.Node import Node
from Nodes.DeclarationNode import DeclarationNode
from Nodes.Parsing import RESERVED_WORDS

class DeclarationSequenceNode(Node):

    def __init__(self):
        self.__d = DeclarationNode()
        self.__ds = None

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        self.__d.parse(t)
        if t.currentToken().value == RESERVED_WORDS["int"]:
            self.__ds = DeclarationSequenceNode()
            self.__ds.parse(t)

    def pretty_print(self, shift=0):
        self.__d.pretty_print(shift)
        if self.__ds != None:
            self.__ds.pretty_print(shift)
