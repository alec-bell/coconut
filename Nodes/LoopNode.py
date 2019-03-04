from Nodes.Node import Node
from Nodes.ConditionNode import ConditionNode
#from Nodes.StatementSequenceNode import StatementSequenceNode
from Nodes.Parsing import match_consume

class LoopNode(Node):

    def __init__(self):
        self.__cond = ConditionNode()
        from Nodes.StatementSequenceNode import StatementSequenceNode
        self.__ss = StatementSequenceNode()

    def parse(self, t):
        match_consume("while", t)
        self.__cond.parse(t)
        match_consume("loop", t)
        self.__ss.parse(t)
        match_consume("end", t)
        match_consume(";", t)

    def pretty_print(self, shift=0):
        print(shift*'  ' + "while ", end='')
        self.__cond.pretty_print()
        print(" loop")
        self.__ss.pretty_print(shift + 1)
        print(shift*'  ' + "end;")

    def execute(self):
        pass
