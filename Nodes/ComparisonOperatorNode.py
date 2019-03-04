from Nodes.Node import Node
from Nodes.Parsing import match_consume, SPECIAL_SYMBOLS

class ComparisonOperatorNode(Node):

    def __init__(self):
        self.__alt = 1

    def parse(self, t):
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

    def pretty_print(self, shift=0):
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

    def execute(self):
        pass
