class IdListNode(Node):

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self, t):
        self.__id = IdNode.parse(t)
        if t.currentToken().value == 15: # look-ahead, 15 = ","
            match_consume(",", t)
            self.__id_list = new IdListNode()
            self.__id_list.parse(t)

    def print(self):
        print self.__id.get_name(),
        if self.__id_list != None:
            print ", ",
            self.__id_list.print(),

    def execute(self):
        pass
