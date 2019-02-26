class ConditionNode(Node):

    def __init__(self):
        self.__comp = None
        self.__cond1 = None
        self.__cond2 = None
        self.__alt = 1

    def parse(self, t):
        if t.currentToken().value == 20: # (
            self.__comp = new ComparisonNode()
            self.__comp.parse(t)
            self.__alt = 1
        elif t.currentToken().value == 17: # !
            self.__cond1 = new ConditionNode()
            self.__cond1.parse(t)
            self.__alt = 2
        elif t.currentToken().value == 18: # [
            match_consume("[", t)
            self.__cond1 = new ExpressionNode()
            self.__cond1.parse(t)
            if t.currentToken().value == 12: # and
                match_consume("and", t)
                self.__alt = 3
            else: # or
                match_consume("or", t)
                self.__alt = 4
            self.__cond2 = new ExpressionNode()
            self.__cond2.parse(t)
            match_consume("]", t)

    def print(self):
        if self.__alt == 1:
            self.__comp.print()
        elif self.__alt == 2:
            print "!",
            self.__cond1.print()
        else:
            print "[ ",
            self.__cond1.print()
            if self.__alt == 3:
                print " and ",
            elif self.__alt == 4:
                print " or ",
            self.__cond2.print()
            print " ]",

    def execute(self):
        pass
