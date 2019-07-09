from nonterminals import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.root = None

    def parse(self):
        self.root = self._program()

    def _program(self):
        p = Program()
        while not self.lexer.peek('Eof'):
            p.statements.append(self._statement())
        return p

    def _block(self):
        self.lexer.consume('{')
        b = Block()
        while not self.lexer.peek('}'):
            b.statements.append(self._statement())
        self.lexer.consume('}')
        return b

    def _statement(self):
        if self.lexer.peek('var'):
            return self._declaration()
        if self.lexer.peek('if'):
            return self._if()
        if self.lexer.peek('while'):
            return self._while()
        if self.lexer.peek('print'):
            return self._print()
        mark = self.lexer.index
        if self.lexer.match('ident'):
            if self.lexer.peek('='):
                self.lexer.index = mark
                return self._assign()
            self.lexer.index = mark
        return self._expression()

    def _declaration(self):
        self.lexer.consume('var')
        self.lexer.consume('ident')
        ident = self.lexer.value
        expr = None
        if self.lexer.match('='):
            expr = self._expression()
        return Declaration(ident, expr)

    def _if(self):
        self.lexer.consume('if')
        cond = self._expression()
        then = self._block()
        if self.lexer.match('else'):
            otherwise = self._block()
        return IfStatement(cond,then, otherwise)

    def _while(self):
        self.lexer.consume('while')
        cond = self._expression()
        then = self._block()
        return WhileStatement(cond, then)

    def _print(self):
        self.lexer.consume('print')
        return PrintStatement(self._expression())

    def _assign(self):
        self.lexer.consume('ident')
        ident = self.lexer.value
        self.lexer.consume('=')
        return Assign(ident, self._expression())

    def _expression(self):
        return self._equality()

    def _equality(self):
        expr = self._comparision()
        while True:
            if self.lexer.match('=='):
                expr = Expression(expr, self._comparision, lambda x, y: x == y)
            elif self.lexer.match('!='):
                expr = Expression(expr, self._comparision, lambda x, y: x != y)
            else:
                break
        return expr

    def _comparision(self):
        expr = self._addition()
        while True:
            if self.lexer.match('>='):
                expr = Expression(expr, self._addition(), lambda x, y: x >= y)
            elif self.lexer.match('<='):
                expr = Expression(expr, self._addition(), lambda x, y: x <= y)
            elif self.lexer.match('<'):
                expr = Expression(expr, self._addition(), lambda x, y: x < y)
            elif self.lexer.match('>'):
                expr = Expression(expr, self._addition(), lambda x, y: x > y)
            else:
                break
        return expr

    def _addition(self):
        expr = self._multiplication()
        while True:
            if self.lexer.match('+'):
                expr = Expression(expr, self._multiplication(), lambda x, y: x + y)
            elif self.lexer.match('-'):
                expr = Expression(expr, self._multiplication(), lambda x, y: x - y)
            else:
                break
        return expr

    def _multiplication(self):
        expr = self._unary()
        while True:
            if self.lexer.match('*'):
                expr = Expression(expr, self._unary(), lambda x, y: x * y)
            elif self.lexer.match('/'):
                expr = Expression(expr, self._unary(), lambda x, y: x / y)
            else:
                break
        return expr

    def _unary(self):
        return self._primary()

    def _primary(self):
        if self.lexer.match('true'):
            return Boolean(True)
        if self.lexer.match('false'):
            return Boolean(False)
        if self.lexer.match('num'):
            return Number(self.lexer.value)
        self.lexer.consume('ident')
        return Variable(self.lexer.value)

