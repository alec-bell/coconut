from Nodes.Node import Node
from Nodes.ComparisonNode import ComparisonNode
from Nodes.ExpressionNode import ExpressionNode
from Nodes.Match import match_consume

class ConditionNode(Node):

    def __init__(self):
        self.__comp = None
        self.__cond1 = None
        self.__cond2 = None
        self.__alt = 1

    def parse(self, t):
        if t.currentToken().value == 20: # (
            self.__comp = ComparisonNode()
            self.__comp.parse(t)
            self.__alt = 1
        elif t.currentToken().value == 17: # !
            self.__cond1 = ConditionNode()
            self.__cond1.parse(t)
            self.__alt = 2
        elif t.currentToken().value == 18: # [
            match_consume("[", t)
            self.__cond1 = ExpressionNode()
            self.__cond1.parse(t)
            if t.currentToken().value == 12: # and
                match_consume("and", t)
                self.__alt = 3
            else: # or
                match_consume("or", t)
                self.__alt = 4
            self.__cond2 = ExpressionNode()
            self.__cond2.parse(t)
            match_consume("]", t)

    def printN(self):
        if self.__alt == 1:
            self.__comp.printN()
        elif self.__alt == 2:
            print("!", end='')
            self.__cond1.printN()
        else:
            print("[ ", end='')
            self.__cond1.printN()
            if self.__alt == 3:
                print(" and ", end='')
            elif self.__alt == 4:
                print(" or ", end='')
            self.__cond2.printN()
            print(" ]", end='')

    def execute(self):
        pass
