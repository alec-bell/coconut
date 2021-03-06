import sys
import re
from Tokenizer.Token import Token
from Tokenizer.Errors import report_error_invalid_id

class Tokenizer:
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

    REGEX_INTEGER = "\d{1,8}$"
    REGEX_IDENTIFIER = "(?=.{1,8}$)^[A-Z][A-Z]{0,7}[0-9]{0,7}$"
    REGEX_WHITESPACE = "\s"

    TOKEN_VALUE_INTEGER = 31
    TOKEN_VALUE_IDENTIFIER = 32
    TOKEN_VALUE_EOF = 33

    def __init__(self, file=None, str=None):
        if file is not None:
            self.file = file
            self.alt = 1
        elif str is not None:
            self.str = str
            self.alt = 2
        self.line_number = 1 # Counter to keep track of current line number.
        self.current_char = self.currentChar()
        self.nextToken()

    def nextTokenKey(self):
        """Return the next possible token string of non-whitespace characters from the input stream."""

        if self.current_char == '':
            return ''

        # Move to next non-whitespace character
        while re.match(self.REGEX_WHITESPACE, self.current_char):
            if self.current_char == '\n':
                self.line_number += 1
            self.current_char = self.currentChar()

        key = ""
        # Special symbols
        if self.current_char in self.SPECIAL_SYMBOLS:
            key += self.current_char
            self.current_char = self.file.read(1)
            if key + self.current_char in self.SPECIAL_SYMBOLS:
                key += self.current_char
                self.current_char = self.currentChar()
        # All other possible tokens
        else:
            while not re.match(self.REGEX_WHITESPACE, self.current_char) and self.current_char not in self.SPECIAL_SYMBOLS and self.current_char != '':
                key += self.current_char
                self.current_char = self.currentChar()

        return key

    def currentChar(self):
        if self.alt == 1:
            return self.file.read(1)
        else:
            if len(self.str) > 0:
                char = self.str[0]
                self.str = self.str[1:]
            else:
                char = ''
            return char

    def currentToken(self):
        """Return the current token object."""
        return self.token

    def nextToken(self):
        """If valid, store the next valid token object, otherwise output error and terminate."""
        key = self.nextTokenKey()

        if key in self.RESERVED_WORDS:
            self.token = Token(key, self.RESERVED_WORDS[key], self.line_number)
        elif key in self.SPECIAL_SYMBOLS:
            self.token = Token(key, self.SPECIAL_SYMBOLS[key], self.line_number)
        elif re.match(self.REGEX_INTEGER, key):
            self.token = Token(key, self.TOKEN_VALUE_INTEGER, self.line_number)
        elif re.match(self.REGEX_IDENTIFIER, key):
            self.token = Token(key, self.TOKEN_VALUE_IDENTIFIER, self.line_number)
        elif key == '':
            self.token = Token(key, self.TOKEN_VALUE_EOF, self.line_number)
        else:
            report_error_invalid_id(self, key)
