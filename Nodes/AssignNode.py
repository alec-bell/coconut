from Nodes.Node import Node
from Nodes.Executable import Executable
from Nodes.ExpressionNode import ExpressionNode
from Nodes.Parsing import match_consume, symbol_table
from Nodes.Errors import report_error_undeclared_identifier

class AssignNode(Node, Executable):

    def __init__(self):
        self.__id = None
        self.__exp = ExpressionNode()

    def parse(self, t):
        if t.currentToken().key not in symbol_table:
            report_error_undeclared_identifier(t)
        self.__id = symbol_table[t.currentToken().key]
        t.nextToken()
        match_consume("=", t)
        self.__exp.parse(t)
        match_consume(";", t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + self.__id.get_name(), end='')
        print(" = ", end='')
        self.__exp.pretty_print()
        print(";")

    def execute(self):
        self.__id.set_value(self.__exp.evaluate())
