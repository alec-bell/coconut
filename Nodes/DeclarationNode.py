from Nodes.Node import Node
from Nodes.IdListNode import IdListNode
from Nodes.Parsing import match_consume

class DeclarationNode(Node):

    def __init__(self):
        self.__id_list = IdListNode()

    def parse(self, t):
        match_consume("int", t)
        self.__id_list.parse(t)
        match_consume(";", t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + "int ", end='')
        self.__id_list.pretty_print()
        print(";")

    def execute(self):
        self.__id_list.execute()
