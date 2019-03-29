from Nodes.Node import Node
from Nodes.IdNode import IdNode
from Nodes.Parsing import match_consume, symbol_table, SPECIAL_SYMBOLS
from Nodes.ExpressionNode import ExpressionNode
from Tokenizer.Tokenizer import Tokenizer
from Nodes.Errors import report_error_not_an_int
import sys

class IdListNode(Node):

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self, t):
        self.__line_number = t.currentToken().line_number
        self.__id = IdNode.parse(t)
        if t.currentToken().value == SPECIAL_SYMBOLS[","]:
            match_consume(",", t)
            self.__id_list = IdListNode()
            self.__id_list.parse(t)

    def pretty_print(self, shift=0):
        print(self.__id.get_name(), end='')
        if self.__id_list is not None:
            print(", ", end='')
            self.__id_list.pretty_print()

    def parse_decl(self, t):
        self.__id = IdNode.parse_decl(t)
        if t.currentToken().value == SPECIAL_SYMBOLS[","]:
            match_consume(",", t)
            self.__id_list = IdListNode()
            self.__id_list.parse_decl(t)

    def read(self):
        val = input(self.__id.get_name() + " =? ")
        #tokenizer = Tokenizer(str=val)
        #exp = ExpressionNode()
        #exp.parse(tokenizer)
        #self.__id.set_value(exp.evaluate())
        try:
            num = int(val)
        except ValueError:
            report_error_not_an_int(self.__id, val)
        self.__id.set_value(num)
        if self.__id_list is not None:
            self.__id_list.read()

    def write(self):
        print(self.__id.get_name() + " = " + str(self.__id.get_value()))
        if self.__id_list is not None:
            self.__id_list.write()
