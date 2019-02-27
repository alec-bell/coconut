from Nodes.Node import Node
from Nodes.IdNode import IdNode
from Nodes.Match import match_consume

class IdListNode(Node):

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self, t):
        self.__id = IdNode.parse(t)
        if t.currentToken().value == 15: # look-ahead, 15 = ","
            match_consume(",", t)
            self.__id_list = IdListNode()
            self.__id_list.parse(t)

    def printN(self):
        print(self.__id.get_name(), end='')
        if self.__id_list != None:
            print(", ", end='')
            self.__id_list.printN()

    def execute(self):
        pass
