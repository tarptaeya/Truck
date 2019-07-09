import reporter

class Lexer:
    def __init__(self, source):
        self.source = source
        self.index = 0
        self.previous = 0
        self.value = None
        self.symbols = {
                '<', '>', '=', '!', '(', ')', '{', '}',
                '[', ']', '+', '-', '*', '/', '%', ',',
                }
        self.keywords = {
                'fn', 'print', 'return', 'if', 'else',
                'while', 'break', 'continue', 'var',
                'true', 'false', 'and', 'or',
                }

    def consume(self, token):
        actual = self.next()
        if actual != token:
            reporter.report_error(f'expected {token} found {actual}')

    def match(self, token):
        actual = self.next()
        if actual == token:
            return True
        self.rollback()
        return False

    def next(self):
        self.previous = self.index

        if self.index >= len(self.source):
            return 'Eof'

        current = self.source[self.index]

        if current in self.symbols:
            self.value = current
            self.index += 1
            current = self.source[self.index]
            if current == '=':
                self.value += current
                self.index += 1
            return self.value

        if current.isalpha() or current == '_':
            self.value = ''
            while current.isalpha() or current == '_':
                self.value += current
                self.index += 1
                current = self.source[self.index]
            if self.value in self.keywords:
                return self.value
            return 'ident'

        if current.isdigit():
            self.value = 0
            while current.isdigit():
                self.value = self.value * 10 + int(current)
                self.index += 1
                current = self.source[self.index]
            return 'num'

        self.index += 1
        return self.next()

    def peek(self, token):
        actual = self.next()
        self.rollback()
        return actual == token

    def rollback(self):
        self.index = self.previous

