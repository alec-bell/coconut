from Nodes.Node import Node
from Nodes.ConditionNode import ConditionNode
from Nodes.Parsing import match_consume, RESERVED_WORDS

class IfNode(Node):

    def __init__(self):
        self.__cond = ConditionNode()
        from Nodes.StatementSequenceNode import StatementSequenceNode
        self.__ss_true = StatementSequenceNode()
        self.__ss_false = None

    def parse(self, t):
        match_consume("if", t)
        self.__cond.parse(t)
        match_consume("then", t)
        self.__ss_true.parse(t)
        if t.currentToken().value == RESERVED_WORDS["else"]:
            match_consume("else", t)
            from Nodes.StatementSequenceNode import StatementSequenceNode
            self.__ss_false = StatementSequenceNode()
            self.__ss_false.parse(t)
        match_consume("end", t)
        match_consume(";", t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + "if ", end='')
        self.__cond.pretty_print()
        print(" then")
        self.__ss_true.pretty_print(shift + 1)
        if self.__ss_false is not None:
            print(shift*'  ' + "else")
            self.__ss_false.pretty_print(shift + 1)
        print(shift*'  ' + "end;")

    def execute(self):
        pass
