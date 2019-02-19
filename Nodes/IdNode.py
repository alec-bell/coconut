class Id():

    def __init__(self, name):
        self.__name = name
        self.__initialized = False
        self.__declared = False

    def set_value(self, value):
        self.__value = value
        self.__initialized = True

    def get_value(self):
        return self.__value

    def get_name(self):
        return self.__name

    def is_declared(self):
        return self.__declared

    def set_declared(self):
        self.__declared = True

    @staticmethod
    def parse(self, t):
        token = t.currentToken()
        t.nextToken()

        if token not in symbol_table:
            Id id = new IdNode(token)
            symbol_table[token] = idea
