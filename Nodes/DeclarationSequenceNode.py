class DeclarationSequenceNode(Node):

    def __init__(self):
        self.__d = new DeclarationNode()
        self.__ds = None

    def parse(self, t):
        self.__d.parse(t)
        if t.currentToken().value == 4: # look-ahead, 4 = int
            self.__ds = new DeclarationSequenceNode();
            self.__ds.parse(t)

    def print(self):
        self.__d.print()
        if self.__ds != None:
            self.__ds.print()

    def execute(self):
        self.__d.execute()
        if self.__ds != None:
            self.__ds.execute()
