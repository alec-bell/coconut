class LoopNode(Node):

    def __init__(self):
        self.__cond = new ConditionNode()
        self.__ss = new StatementSequenceNode()

    def parse(self, t):
        match_consume("while", t)
        self.__cond.parse(t)
        match_consume("loop", t)
        self.__ss.parse(t)
        match_consume("end", t)
        match_consume(";", t)

    def print(self):
        print "while ",
        self.__cond.print(),
        print " loop"
        self.__ss.print()
        print "end;"

    def execute(self):
        pass
