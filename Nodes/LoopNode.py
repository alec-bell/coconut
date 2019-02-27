from Nodes.Node import Node
from Nodes.ConditionNode import ConditionNode
#from Nodes.StatementSequenceNode import StatementSequenceNode
from Nodes.Match import match_consume

class LoopNode(Node):

    def __init__(self):
        self.__cond = ConditionNode()
        self.__ss = StatementSequenceNode()

    def parse(self, t):
        match_consume("while", t)
        self.__cond.parse(t)
        match_consume("loop", t)
        self.__ss.parse(t)
        match_consume("end", t)
        match_consume(";", t)

    def printN(self):
        print("while ", end='')
        self.__cond.printN()
        print(" loop")
        self.__ss.printN()
        print("end;")

    def execute(self):
        pass
