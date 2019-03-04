from Nodes.Node import Node
from Nodes.AssignNode import AssignNode
from Nodes.IfNode import IfNode
from Nodes.LoopNode import LoopNode
from Nodes.InNode import InNode
from Nodes.OutNode import OutNode
from Nodes.Parsing import match_consume, TOKEN_VALUE_IDENTIFIER, RESERVED_WORDS
from Nodes.Errors import report_error_expected_statement

class StatementNode(Node):

    def __init__(self):
        self.__n = None

    def parse(self, t):
        token = t.currentToken().value
        if token == TOKEN_VALUE_IDENTIFIER:
            self.__n = AssignNode()
        elif token == RESERVED_WORDS["if"]:
            self.__n = IfNode()
        elif token == RESERVED_WORDS["while"]:
            self.__n = LoopNode()
        elif token == RESERVED_WORDS["read"]:
            self.__n = InNode()
        elif token == RESERVED_WORDS["write"]:
            self.__n = OutNode()
        else:
            report_error_expected_statement(t)

        self.__n.parse(t)

    def pretty_print(self, shift=0):
        self.__n.pretty_print(shift)

    def execute(self):
        pass
