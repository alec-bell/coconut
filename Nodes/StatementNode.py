from Nodes.Node import Node
from Nodes.AssignNode import AssignNode
from Nodes.IfNode import IfNode
from Nodes.LoopNode import LoopNode
from Nodes.InNode import InNode
from Nodes.OutNode import OutNode
from Nodes.Match import match_consume

class StatementNode(Node):

    def __init__(self):
        self.__n = None

    def parse(self, t):
        token = t.currentToken().value
        if token == 32: # ID
            self.__n = AssignNode()
        elif token == 5: # if
            self.__n = IfNode()
        elif token == 8: # while
            self.__n = LoopNode()
        elif token == 10: # in
            self.__n = InNode()
        elif token == 11: # out
            self.__n = OutNode()
        else:
            print("Parse Error: [Line " + str(t.currentToken().line_number) + "] Expected statement but got: '" + t.currentToken().key + "'")
            exit()

        self.__n.parse(t)

    def printN(self, shift=0):
        self.__n.printN(shift)

    def execute(self):
        pass
