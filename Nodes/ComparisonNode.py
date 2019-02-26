class ComparisonNode(Node):

    def __init__(self):
        self.__fac1 = None
        self.__fac2 = None
        self.__comp_op = None

    def parse(self, t):
        match_consume("(", t)
        self.__fac1.parse(t)
        self.__comp_op.parse(t)
        self.__fac2.parse(t)
        match_consume(")", t)

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
