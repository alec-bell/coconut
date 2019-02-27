from Nodes.Node import Node
from Nodes.IdListNode import IdListNode
from Nodes.Match import match_consume

class OutNode(Node):

    def __init__(self):
        self.__id_list = IdListNode()

    def parse(self, t):
        match_consume("write", t)
        self.__id_list.parse(t)
        match_consume(";", t)

    def printN(self, shift=0):
        print(shift*'  ' + "write ", end='')
        self.__id_list.printN()
        print(";")

    def execute(self):
        pass
