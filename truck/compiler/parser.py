from .ast import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        root = self._parse()
        return root

    def _parse(self):
        return None
