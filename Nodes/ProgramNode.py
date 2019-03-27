from Nodes.Node import Node
from Nodes.Executable import Executable
from Nodes.DeclarationSequenceNode import DeclarationSequenceNode
from Nodes.StatementSequenceNode import StatementSequenceNode
from Nodes.Parsing import match_consume, symbol_table, TOKEN_VALUE_EOF
from Nodes.Errors import report_error_expected_eof

class ProgramNode(Node, Executable):

    def __init__(self):
        self.__ds = DeclarationSequenceNode()
        self.__ss = StatementSequenceNode()

    def parse(self, t):
        match_consume("program", t)
        self.__ds.parse(t)
        match_consume("begin", t)
        self.__ss.parse(t)
        match_consume("end", t)
        if t.currentToken().value != TOKEN_VALUE_EOF:
            report_error_expected_eof(t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + "program ")
        self.__ds.pretty_print(shift + 1)
        print((shift + 1)*'  ' + "begin")
        self.__ss.pretty_print(shift + 2)
        print((shift + 1)*'  ' + "end")

    def execute(self):
        self.__ss.execute()
