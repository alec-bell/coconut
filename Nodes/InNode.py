class InNode(Node):

    def __init__(self):
        self.__id_list = new IdList()

    def parse(self, t):
        match_consume("read", t)
        self.__id_list.parse(t)
        match_consume(";", t)

    def print(self):
        print "read ",
        self.__id_list.print(),
        print ";"

    def execute(self):
        pass
