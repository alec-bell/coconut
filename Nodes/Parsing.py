from Nodes.Errors import report_error_match_consume

symbol_table = dict()

RESERVED_WORDS = {
    "program": 1,
    "begin": 2,
    "end": 3,
    "int": 4,
    "if": 5,
    "then": 6,
    "else": 7,
    "while": 8,
    "loop": 9,
    "read": 10,
    "write": 11,
    "and": 12,
    "or": 13
}

SPECIAL_SYMBOLS = {
    ";": 14,
    ",": 15,
    "=": 16,
    "!": 17,
    "[": 18,
    "]": 19,
    "(": 20,
    ")": 21,
    "+": 22,
    "-": 23,
    "*": 24,
    "!=": 25,
    "==": 26,
    ">=": 27,
    "<=": 28,
    ">": 29,
    "<": 30
}

TOKEN_VALUE_INTEGER = 31
TOKEN_VALUE_IDENTIFIER = 32
TOKEN_VALUE_EOF = 33

def match_consume(expected, t):
    if expected in RESERVED_WORDS and RESERVED_WORDS[expected] == t.currentToken().value:
        t.nextToken()
    elif expected in SPECIAL_SYMBOLS and SPECIAL_SYMBOLS[expected] == t.currentToken().value:
        t.nextToken()
    else:
        report_error_match_consume(expected, t)
