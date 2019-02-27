from Nodes.Node import Node
from Nodes.DeclarationNode import DeclarationNode

class DeclarationSequenceNode(Node):

    def __init__(self):
        self.__d = DeclarationNode()
        self.__ds = None

    def parse(self, t):
        self.__d.parse(t)
        if t.currentToken().value == 4: # look-ahead, 4 = int
            self.__ds = DeclarationSequenceNode()
            self.__ds.parse(t)

    def printN(self, shift=0):
        self.__d.printN(shift)
        if self.__ds != None:
            self.__ds.printN(shift)

    def execute(self):
        self.__d.execute()
        if self.__ds != None:
            self.__ds.execute()
