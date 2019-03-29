from Nodes.Parsing import symbol_table
from Nodes.Errors import report_error_uninitialized_identifier, report_error_undeclared_identifier, report_error_not_an_int, report_error_duplicate_identifier

class IdNode():

    def __init__(self, name):
        self.__name = name
        self.__initialized = False
        self.__declared = False

    def set_value(self, value):
        self.__value = value
        self.__initialized = True

    def get_value(self):
        if self.__initialized is False:
            report_error_uninitialized_identifier(self)
        return self.__value

    def get_name(self):
        return self.__name

    def is_declared(self):
        return self.__declared

    def set_declared(self):
        self.__declared = True

    @staticmethod
    def parse(t):
        if t.currentToken().key not in symbol_table:
            report_error_undeclared_identifier(t)

        token = t.currentToken()
        t.nextToken()

        return symbol_table[token.key]

    @staticmethod
    def parse_decl(t):
        if t.currentToken().key in symbol_table:
            report_error_duplicate_identifier(t)

        id = IdNode(t.currentToken().key)
        id.set_declared()
        symbol_table[t.currentToken().key] = id
        t.nextToken()

        return id
