from Nodes.Node import Node
from Nodes.IdListNode import IdListNode
from Nodes.Parsing import match_consume

class DeclarationNode(Node):

    def __init__(self):
        self.__id_list = IdListNode()

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        match_consume("int", t)
        self.__id_list.parse_decl(t)
        match_consume(";", t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + "int ", end='')
        self.__id_list.pretty_print()
        print(";")
