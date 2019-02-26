class AssignNode(Node):

    def __init__(self):
        self.__id = None
        self.__exp = new ExpressionNode()

    def parse(self, t):
        self.__id = symbol_table[t.currentToken().key]
        t.nextToken()
        match_consume("=", t)
        self.__exp.parse(t)
        self.__id.set_value(self.__exp)

    def print(self):
        print self.__id.get_name(),
        print " , ",
        self.__exp.print()

    def execute(self):
        pass
