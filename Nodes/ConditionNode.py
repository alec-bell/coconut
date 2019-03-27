from Nodes.Node import Node
from Nodes.Evaluable import Evaluable
from Nodes.ComparisonNode import ComparisonNode
from Nodes.ExpressionNode import ExpressionNode
from Nodes.Parsing import match_consume, SPECIAL_SYMBOLS, RESERVED_WORDS

class ConditionNode(Node, Evaluable):

    def __init__(self):
        self.__comp = None
        self.__cond1 = None
        self.__cond2 = None
        self.__alt = 1

    def parse(self, t):
        if t.currentToken().value == SPECIAL_SYMBOLS["("]:
            self.__comp = ComparisonNode()
            self.__comp.parse(t)
            self.__alt = 1
        elif t.currentToken().value == SPECIAL_SYMBOLS["!"]:
            match_consume("!", t)
            self.__cond1 = ConditionNode()
            self.__cond1.parse(t)
            self.__alt = 2
        elif t.currentToken().value == SPECIAL_SYMBOLS["["]:
            match_consume("[", t)
            self.__cond1 = ConditionNode()
            self.__cond1.parse(t)
            if t.currentToken().value == RESERVED_WORDS["and"]:
                match_consume("and", t)
                self.__alt = 3
            else: # or
                match_consume("or", t)
                self.__alt = 4
            self.__cond2 = ConditionNode()
            self.__cond2.parse(t)
            match_consume("]", t)

    def pretty_print(self, shift=0):
        if self.__alt == 1:
            self.__comp.pretty_print()
        elif self.__alt == 2:
            print("!", end='')
            self.__cond1.pretty_print()
        else:
            print("[ ", end='')
            self.__cond1.pretty_print()
            if self.__alt == 3:
                print(" and ", end='')
            elif self.__alt == 4:
                print(" or ", end='')
            self.__cond2.pretty_print()
            print(" ]", end='')

    def evaluate(self):
        if self.__alt == 1:
            return self.__comp.evaluate()
        elif self.__alt == 2:
            return not self.__cond1.evaluate()
        elif self.__alt == 3:
            return self.__cond1.evaluate() and self.__cond2.evaluate()
        elif self.__alt == 4:
            return self.__cond1.evaluate() or self.__cond2.evaluate()
