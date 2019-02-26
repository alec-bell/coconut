class StatementNode(Node):

    def __init__(self):
        self.__n = None

    def parse(self, t):
        token = t.currentToken().value
        if token == 32: # ID
            self.__n = new AssignNode()
        elif token == 5: # if
            self.__n = new IfNode()
        elif token == 9: # loop
            self.__n = new LoopNode()
        elif token == 10: # in
            self.__n = new InNode()
        elif token == 11: # out
            self.__n = new OutNode()
        else:
            print("Parse Error: [Line " + str(t.currentToken().line_number) + "] Expected statement but got: '" + t.currentToken().key + "'")
            exit()

        self.__n.parse(t)

    def print(self):
        self.__n.print()

    def execute(self):
        pass
