from Nodes.Node import Node
from Nodes.FacNode import FacNode
from Nodes.ComparisonOperatorNode import ComparisonOperatorNode
from Nodes.Match import match_consume

class ComparisonNode(Node):

    def __init__(self):
        self.__fac1 = FacNode()
        self.__fac2 = FacNode()
        self.__comp_op = ComparisonOperatorNode()

    def parse(self, t):
        match_consume("(", t)
        self.__fac1.parse(t)
        self.__comp_op.parse(t)
        self.__fac2.parse(t)
        match_consume(")", t)

    def printN(self):
        print("( ", end='')
        self.__fac1.printN()
        self.__comp_op.printN()
        self.__fac2.printN()
        print(" )", end='')

    def execute(self):
        pass
