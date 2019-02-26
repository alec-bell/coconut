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

    def print(self):
        if self.__alt == 1:
            print "!=",
        elif self.__alt == 2:
            print "==",
        elif self.__alt == 3:
            print "<",
        elif self.__alt == 4:
            print ">",
        elif self.__alt == 5:
            print "<=",
        elif self.__alt == 6:
            print ">=",

    def execute(self):
        pass
