from Nodes.Node import Node
from Nodes.Evaluable import Evaluable
from Nodes.FacNode import FacNode
from Nodes.Parsing import match_consume, SPECIAL_SYMBOLS

class ComparisonNode(Node, Evaluable):

    def __init__(self):
        self.__fac1 = FacNode()
        self.__fac2 = FacNode()
        self.__alt = 1

    def parse(self, t):
        match_consume("(", t)
        self.__fac1.parse(t)
        if t.currentToken().value == SPECIAL_SYMBOLS["!="]:
            match_consume("!=", t)
            self.__alt = 1
        elif t.currentToken().value == SPECIAL_SYMBOLS["=="]:
            match_consume("==", t)
            self.__alt = 2
        elif t.currentToken().value == SPECIAL_SYMBOLS["<"]:
            match_consume("<", t)
            self.__alt = 3
        elif t.currentToken().value == SPECIAL_SYMBOLS[">"]:
            match_consume(">", t)
            self.__alt = 4
        elif t.currentToken().value == SPECIAL_SYMBOLS["<="]:
            match_consume("<=", t)
            self.__alt = 5
        elif t.currentToken().value == SPECIAL_SYMBOLS[">="]:
            match_consume(">=", t)
            self.__alt = 6
        self.__fac2.parse(t)
        match_consume(")", t)

    def pretty_print(self, shift=0):
        print("( ", end='')
        self.__fac1.pretty_print()
        if self.__alt == 1:
            print(" != ", end='')
        elif self.__alt == 2:
            print(" == ", end='')
        elif self.__alt == 3:
            print(" < ", end='')
        elif self.__alt == 4:
            print(" > ", end='')
        elif self.__alt == 5:
            print(" <= ", end='')
        elif self.__alt == 6:
            print(" >= ", end='')
        self.__fac2.pretty_print()
        print(" )", end='')

    def evaluate(self):
        if self.__alt == 1:
            return self.__fac1.evaluate() != self.__fac2.evaluate()
        elif self.__alt == 2:
            return self.__fac1.evaluate() == self.__fac2.evaluate()
        elif self.__alt == 3:
            return self.__fac1.evaluate() < self.__fac2.evaluate()
        elif self.__alt == 4:
            return self.__fac1.evaluate() > self.__fac2.evaluate()
        elif self.__alt == 5:
            return self.__fac1.evaluate() <= self.__fac2.evaluate()
        elif self.__alt == 6:
            return self.__fac1.evaluate() >= self.__fac2.evaluate()
