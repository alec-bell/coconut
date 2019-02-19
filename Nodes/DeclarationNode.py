class DeclarationNode(Node):

    def __init__(self):
        self.__id_list = new IdListNode()

    def parse(self, t):
        match_consume("int", t)
        self.__id_list.parse(t)
        match_consume(";", t)

    def print(self):
        print "int ",
        self.__id_list.print()
        print ";"

    def execute(self):
        self.__id_list.execute()
