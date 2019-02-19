class ProgramNode(Node):

    def __init__(self):
        self.__ds = new DeclarationSequenceNode()
        self.__ss = new StatementSequenceNode()

    def parse(self, t):
        match_consume("program", t)
        self.__ds.parse(t)
        match_consume("begin", t)
        self.__ss.parse(t)
        match_consume("end", t)

    def print(self):
        print "program"
        self.__ds.print()
        print "begin"
        self.__ss.print()
        print "end"

    def execute(self):
        self.__ds.execute()
        self.__ss.execute()
