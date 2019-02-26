class IfNode(Node):

    def __init__(self):
        self.__cond = new ConditionNode()
        self.__ss_true = new StatementSequenceNode()
        self.__ss_false = None

    def parse(self, t):
        match_consume("if", t)
        self.__cond.parse(t)
        match_consume("then", t)
        self.__ss_true.parse(t)
        if t.currentToken().value == 7: # else
            match_consume("else", t)
            self.__ss_false = new StatementSequenceNode()
            self.__ss_false.parse(t)
        match_consume("end", t)
        match_consume(";", t)

    def print(self):
        print "if ",
        self.__cond.print(),
        print " then"
        self.__ss_true.print()
        if self.__ss_false is not None:
            print "else"
            self.__ss_false.print()
        print "end;"

    def execute(self):
        pass
