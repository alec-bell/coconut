from Nodes.Node import Node
from Nodes.FacNode import FacNode
from Nodes.ComparisonOperatorNode import ComparisonOperatorNode
from Nodes.Parsing import match_consume

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

    def pretty_print(self, shift=0):
        print("( ", end='')
        self.__fac1.pretty_print()
        self.__comp_op.pretty_print()
        self.__fac2.pretty_print()
        print(" )", end='')

    def execute(self):
        pass
