from Nodes.Node import Node
from Nodes.Match import match_consume

class ComparisonOperatorNode(Node):

    def __init__(self):
        self.__alt = 1

    def parse(self, t):
        if t.currentToken().value == 25: # !=
            match_consume("!=", t)
            self.__alt = 1
        elif t.currentToken().value == 26: # !=
            match_consume("==", t)
            self.__alt = 2
        elif t.currentToken().value == 30: # !=
            match_consume("<", t)
            self.__alt = 3
        elif t.currentToken().value == 29: # !=
            match_consume(">", t)
            self.__alt = 4
        elif t.currentToken().value == 28: # !=
            match_consume("<=", t)
            self.__alt = 5
        elif t.currentToken().value == 27: # !=
            match_consume(">=", t)
            self.__alt = 6

    def printN(self):
        if self.__alt == 1:
            print("!=", end='')
        elif self.__alt == 2:
            print("==", end='')
        elif self.__alt == 3:
            print("<", end='')
        elif self.__alt == 4:
            print(">", end='')
        elif self.__alt == 5:
            print("<=", end='')
        elif self.__alt == 6:
            print(">=", end='')

    def execute(self):
        pass
