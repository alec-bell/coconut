class ExpressionNode(Node):

    def __init__(self):
        self.__t = new TermNode()
        self.__exp = None
        self.__alt = 1

    def parse(self, t):
        self.__t.parse(t)
        if t.currentToken().value == 22: # +
            t.nextToken()
            self.__exp = new ExpressionNode()
            self.__exp.parse(t)
            self.__alt = 2
        elif t.currentToken().value == 23: # -
            t.nextToken()
            self.__exp = new ExpressionNode()
            self.__exp.parse(t)
            self.__alt = 3

    def print(self):
        self.__t.print(),
        if self.__exp is not None:
            if self.__alt == 2:
                print " + ",
            elif self.__alt == 3:
                print " - ",
            self.__exp.print(),

    def execute(self):
        pass
