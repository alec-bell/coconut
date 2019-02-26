class TermNode(Node):

    def __init__(self):
        self.__fac = new FacNode()
        self.__t = None

    def parse(self, t):
        self.__fac.parse(t)
        if t.currentToken().value == 24: # *
            match_consume("*", t)
            self.__t = new TermNode()
            self.__t.parse(t)

    def print(self):
        self.__fac.print()
        if self.__t is not None:
            print " * ",
            self.__t.print()

    def execute(self):
        pass
