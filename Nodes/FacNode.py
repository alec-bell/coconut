from Nodes.Node import Node
from Nodes.IdNode import IdNode
#from Nodes.ExpressionNode import ExpressionNode
from Nodes.Match import match_consume, symbol_table

class FacNode(Node):

    def __init__(self):
        self.__int = None
        self.__id = None
        self.__exp = None
        self.__alt = 1

    def parse(self, t):
        if t.currentToken().value == 31: # int
            self.__int = int(t.currentToken().key)
            t.nextToken()
            self.__alt = 1
        elif t.currentToken().value == 32: # ID
            self.__id = symbol_table[t.currentToken().key]
            t.nextToken()
            self.__alt = 2
        elif t.currentToken().value == 20: # (
            match_consume("(", t)
            self.__exp = ExpressionNode()
            self.__exp.parse(t)
            match_consume(")", t)
            self.__alt = 3

    def printN(self):
        if self.__alt == 1:
            print(str(self.__int), end='')
        elif self.__alt == 2:
            print(self.__id.get_name(), end='')
        elif self.__alt == 3:
            print("( ", end='')
            self.__exp.printN()
            print(" )")

    def execute(self):
        pass
