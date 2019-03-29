from Nodes.Node import Node
from Nodes.Evaluable import Evaluable
from Nodes.IdNode import IdNode
from Nodes.Parsing import match_consume, symbol_table, TOKEN_VALUE_INTEGER, TOKEN_VALUE_IDENTIFIER, SPECIAL_SYMBOLS
from Nodes.Errors import report_error_expected_expresion

class FacNode(Node, Evaluable):

    def __init__(self):
        self.__int = None
        self.__id = None
        self.__exp = None
        self.__alt = 1

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        if t.currentToken().value == TOKEN_VALUE_INTEGER:
            self.__int = int(t.currentToken().key)
            t.nextToken()
            self.__alt = 1
        elif t.currentToken().value == TOKEN_VALUE_IDENTIFIER:
            self.__id = symbol_table[t.currentToken().key]
            t.nextToken()
            self.__alt = 2
        elif t.currentToken().value == SPECIAL_SYMBOLS["("]:
            match_consume("(", t)
            from Nodes.ExpressionNode import ExpressionNode
            self.__exp = ExpressionNode()
            self.__exp.parse(t)
            match_consume(")", t)
            self.__alt = 3
        else:
            report_error_expected_expresion(t)

    def pretty_print(self, shift=0):
        if self.__alt == 1:
            print(str(self.__int), end='')
        elif self.__alt == 2:
            print(self.__id.get_name(), end='')
        elif self.__alt == 3:
            print("( ", end='')
            self.__exp.pretty_print()
            print(" )", end='')

    def evaluate(self):
        if self.__alt == 1:
            return self.__int
        elif self.__alt == 2:
            return self.__id.get_value()
        elif self.__alt == 3:
            return self.__exp.evaluate()
