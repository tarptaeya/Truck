import sys
from codecs import decode

class Lexer:
    def __init__(self, source):
        self.source = source
        self.index = 0
        self.previous = 0
        self.value = None

        self.keywords = {
            "and", "as", "break", "class", "continue",
            "else", "extends", "extern", "false",
            "function", "if", "or", "new", "not",
            "return", "true", "use", "while",
        }

    def consume(self, token):
        actual = self.next()
        if actual != token:
            raise LexError("expected {}, but found {}\n".format(token, actual))

    def match(self, token):
        actual = self.next()
        if actual == token:
            return True
        self.rollback()
        return False

    def next(self):
        self.previous = self.index

        current = self.source[self.index]
        if current is None:
            return "Eof"

        # comment
        if current == "#":
            while current not in ["\n", None]:
                self.index += 1
                current = self.source[self.index]
            self.index += 1
            return self.next()

        # symobol=
        if current in {"+", "-", "*", "/", "%", "&", "|", "^", "=", "<", ">", "!"}:
            self.value = current
            self.index += 1
            current = self.source[self.index]
            if current == "=":
                self.value += current
                self.index += 1
            return self.value

        # symbol
        if current in {"(", ")", "[", "]", "{", "}", ",", ".", "~"}:
            self.value = current
            self.index += 1
            return self.value

        # ident or keyword
        if current.isalpha() or current == "_":
            self.value = ""
            while current and current.isalnum() or current == "_":
                self.value += current
                self.index += 1
                current = self.source[self.index]
            if self.value in self.keywords:
                return self.value
            return "Ident"

        # number
        if current.isdigit():
            value = 0
            decimal = 0
            exponent = 0
            while current and current.isdigit():
                value = value * 10 + int(current)
                self.index += 1
                current = self.source[self.index]
            if current == ".":
                self.index += 1
                current = self.source[self.index]

                place = 1
                while current and current.isdigit():
                    decimal = decimal + int(current) / 10 ** place
                    place += 1
                    self.index += 1
                    current = self.source[self.index]
            if current == "e" or current == "E":
                self.index += 1
                current = self.source[self.index]

                negative = False
                if current == "+":
                    self.index += 1
                    current = self.source[self.index]
                elif current == "-":
                    negative = True
                    self.index += 1
                    current = self.source[self.index]

                power = 0
                if current is None:
                    raise LexError("unexpected EOF while reading number")
                while current and current.isdigit():
                    power = power * 10 + int(current)
                    self.index += 1
                    current = self.source[self.index]
                exponent = -power if negative else power
            self.value = (value + decimal) * 10 ** exponent
            return "Num"

        # string
        if current in ["\""]:
            self.value = ""
            self.index += 1
            current = self.source[self.index]
            while current != "\"":
                if current == "\\":
                    self.index += 1
                    current = "\\" + self.source[self.index]
                self.value += current
                self.index += 1
                current = self.source[self.index]
            self.value = decode(self.value, "unicode-escape")
            self.index += 1
            return "String"

        self.index += 1
        return self.next()

    def peek(self, token):
        actual = self.next()
        self.rollback()
        return actual == token

    def rollback(self):
        self.index = self.previous


class LexError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
