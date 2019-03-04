from Nodes.Node import Node
from Nodes.IdNode import IdNode
from Nodes.Parsing import match_consume, symbol_table, SPECIAL_SYMBOLS

class IdListNode(Node):

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self, t):
        self.__id = IdNode.parse(t)
        if t.currentToken().value == SPECIAL_SYMBOLS[","]:
            match_consume(",", t)
            self.__id_list = IdListNode()
            self.__id_list.parse(t)

    def pretty_print(self, shift=0):
        print(self.__id.get_name(), end='')
        if self.__id_list != None:
            print(", ", end='')
            self.__id_list.pretty_print()

    def execute(self):
        pass
