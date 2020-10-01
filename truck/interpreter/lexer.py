import sys
import re
from codecs import decode


class Lexer:
    def __init__(self, string):
        self.string = string
        self._clean()

        self.rules = [
            # token, pattern

            # keywords
            ['and', re.compile('and')],
            ['as', re.compile('as')],
            ['break', re.compile('break')],
            ['class', re.compile('class')],
            ['continue', re.compile('continue')],
            ['else', re.compile('else')],
            ['extends', re.compile('extends')],
            ['extern', re.compile('extern')],
            ['false', re.compile('false')],
            ['function', re.compile('function')],
            ['if', re.compile('if')],
            ['or', re.compile('or')],
            ['new', re.compile('new')],
            ['not', re.compile('not')],
            ['return', re.compile('return')],
            ['true', re.compile('true')],
            ['use', re.compile('use')],
            ['while', re.compile('while')],

            # symbols
            ['+=', re.compile('\+=')],
            ['-=', re.compile('-=')],
            ['*=', re.compile('\*=')],
            ['/=', re.compile('/=')],
            ['%=', re.compile('%=')],
            ['&=', re.compile('&=')],
            ['|=', re.compile('|=')],
            ['^=', re.compile('\^=')],
            ['==', re.compile('==')],
            ['<=', re.compile('<=')],
            ['>=', re.compile('>=')],
            ['!=', re.compile('!=')],

            ['+', re.compile('\+')],
            ['-', re.compile('-')],
            ['*', re.compile('\*')],
            ['/', re.compile('/')],
            ['%', re.compile('%')],
            ['&', re.compile('&')],
            ['|', re.compile('|')],
            ['^', re.compile('^')],
            ['=', re.compile('=')],
            ['<', re.compile('<')],
            ['>', re.compile('>')],
            ['!', re.compile('!')],

            ['(', re.compile('\(')],
            [')', re.compile('\)')],
            ['[', re.compile('\[')],
            [']', re.compile('\]')],
            ['{', re.compile('\{')],
            ['}', re.compile('\}')],

            [',', re.compile(',')],
            ['.', re.compile('\.')],
            ['~', re.compile('~')],

            # ident
            ['Ident', re.compile('[a-zA-Z_$][a-zA-Z0-9_]*')],

            # number
            ['Num', re.compile('(([1-9][0-9]*)|0)(\.[0-9]*)?(e(\+|-)?[1-9][0-9]*)?')],

            # string
            ['String', re.compile('(".*")|(\'.*\')')]
        ]

    def next(self):
        if not self.string:
            return 'Eof'

        match_list = [(r[0], r[1].match(self.string)) for r in self.rules]
        match_list = [i for i in match_list if i[1]]
        max_length = max(i[1].end() for i in match_list)
        for i in match_list:
            if i[1].end() == max_length:
                token = i[0]
                break
        self.value = self.string[:max_length]
        if not self.value:
            raise LexError("no pattern matched at `{}...`".format(self.string[:5]))

        self.string = self.string[max_length:]
        self._clean()

        if token == 'String':
            self.value = self.value[1:-1]
        return token

    def peek(self, token):
        string = self.string
        actual = self.next()
        self.string = string
        return token == actual

    def consume(self, token):
        actual = self.next()
        if token != actual:
            raise LexError("expected {}, but found {}".format(token, actual))

    def match(self, token):
        string = self.string
        actual = self.next()
        if token == actual:
            return True
        self.string = string
        return False

    def _clean(self):
        # removes whitespace and comment
        self.string = self.string.lstrip()
        comment_match = True
        while comment_match:
            comment_match = re.match('#.*', self.string)
            if comment_match:
                self.string = self.string[comment_match.end():].lstrip()


class LexError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
