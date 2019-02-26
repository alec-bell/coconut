class StatementSequenceNode(Node):

    def __init__(self):
        self.__s = new SequenceNode()
        self.__ss = None

    def parse(self, t):
        self.__s.parse(t)
        if t.currentToken().value != 3: # look-ahead, 3 = end
            self.__ss = new StatementSequenceNode()
            self.__ss.parse(t)

    def print(self):
        self.__s.print()
        if self.__ss != None:
            self.__ss.print()

    def execute(self):
        pass
