class IdListNode(Node):

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self, t):
        match_consume("int", t)
        self.id_list.parse(t)
        match_consume(";", t)
        self.__id = Id.parse()

    def print(self):
        print "int ",
        self.id_list.print()
        print ";"

    def execute(self):
        self.id_list.execute()
