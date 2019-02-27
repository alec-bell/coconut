from Nodes.Node import Node
from Nodes.ExpressionNode import ExpressionNode
from Nodes.Match import match_consume, symbol_table

class AssignNode(Node):

    def __init__(self):
        self.__id = None
        self.__exp = ExpressionNode()

    def parse(self, t):
        self.__id = symbol_table[t.currentToken().key]
        t.nextToken()
        match_consume("=", t)
        self.__exp.parse(t)
        self.__id.set_value(self.__exp)
        match_consume(";", t)

    def printN(self, shift=0):
        print(shift*'  ' + self.__id.get_name(), end='')
        print(" = ", end='')
        self.__exp.printN()
        print(";")

    def execute(self):
        pass
