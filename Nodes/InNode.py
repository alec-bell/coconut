from Nodes.Node import Node
from Nodes.Executable import Executable
from Nodes.IdListNode import IdListNode
from Nodes.Parsing import match_consume

class InNode(Node, Executable):

    def __init__(self):
        self.__id_list = IdListNode()

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        match_consume("read", t)
        self.__id_list.parse(t)
        match_consume(";", t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + "read ", end='')
        self.__id_list.pretty_print()
        print(";")

    def execute(self):
        self.__id_list.read()
