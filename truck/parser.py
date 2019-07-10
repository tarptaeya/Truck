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
        if self.lexer.peek('return'):
            return self._return()
        if self.lexer.match('break'):
            return Break()
        if self.lexer.match('continue'):
            return Continue()
        if self.lexer.peek('{'):
            return self._block()
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
        otherwise = None
        if self.lexer.match('else'):
            otherwise = self._block()
        return IfStatement(cond,then, otherwise)

    def _while(self):
        self.lexer.consume('while')
        cond = self._expression()
        then = self._block()
        return WhileStatement(cond, then)

    def _return(self):
        self.lexer.consume('return')
        return ReturnStatement(self._expression())

    def _assign(self):
        self.lexer.consume('ident')
        ident = self.lexer.value
        self.lexer.consume('=')
        return Assign(ident, self._expression())

    def _expression(self):
        if self.lexer.peek('fn'):
            return self._lambda()
        return self._or()

    def _lambda(self):
        self.lexer.consume('fn')
        self.lexer.consume('(')
        params = []
        if self.lexer.match('ident'):
            params.append(self.lexer.value)
            while self.lexer.match(','):
                self.lexer.consume('ident')
                params.append(self.lexer.value)
        self.lexer.consume(')')
        block = self._block()
        return Lambda(params, block)

    def _or(self):
        expr = self._and()
        while True:
            if self.lexer.match('or'):
                expr = Expression(expr, self._and(), lambda x, y, e: x or y)
            else:
                break
        return expr

    def _and(self):
        expr = self._equality()
        while True:
            if self.lexer.match('and'):
                expr = Expression(expr, self._equality(), lambda x, y, e: x and y)
            else:
                break
        return expr

    def _equality(self):
        expr = self._comparision()
        while True:
            if self.lexer.match('=='):
                expr = Expression(expr, self._comparision, lambda x, y, e: x == y)
            elif self.lexer.match('!='):
                expr = Expression(expr, self._comparision, lambda x, y, e: x != y)
            else:
                break
        return expr

    def _comparision(self):
        expr = self._addition()
        while True:
            if self.lexer.match('>='):
                expr = Expression(expr, self._addition(), lambda x, y, e: x >= y)
            elif self.lexer.match('<='):
                expr = Expression(expr, self._addition(), lambda x, y, e: x <= y)
            elif self.lexer.match('<'):
                expr = Expression(expr, self._addition(), lambda x, y, e: x < y)
            elif self.lexer.match('>'):
                expr = Expression(expr, self._addition(), lambda x, y, e: x > y)
            else:
                break
        return expr

    def _addition(self):
        expr = self._multiplication()
        while True:
            if self.lexer.match('+'):
                expr = Expression(expr, self._multiplication(), lambda x, y, e: x + y)
            elif self.lexer.match('-'):
                expr = Expression(expr, self._multiplication(), lambda x, y, e: x - y)
            else:
                break
        return expr

    def _multiplication(self):
        expr = self._unary()
        while True:
            if self.lexer.match('*'):
                expr = Expression(expr, self._unary(), lambda x, y, e: x * y)
            elif self.lexer.match('/'):
                expr = Expression(expr, self._unary(), lambda x, y, e: x // y)
            else:
                break
        return expr

    def _unary(self):
        if self.lexer.peek('not'):
            return self._not()
        if self.lexer.peek('-'):
            return self._uminus()
        mark = self.lexer.index
        if self.lexer.match('ident'):
            if self.lexer.peek('('):
                self.lexer.index = mark
                return self._funcall()
        self.lexer.index = mark
        return self._primary()

    def _not(self):
        self.lexer.consume('not')
        expr = self._unary()
        return Expression(expr, None, lambda x, y, e: not x)

    def _uminus(self):
        self.lexer.consume('-')
        expr = self._unary()
        return Expression(expr, None, lambda x, y, e: -x)

    def _funcall(self):
        self.lexer.consume('ident')
        ident = self.lexer.value
        self.lexer.consume('(')
        args = []
        if not self.lexer.peek(')'):
            args.append(self._expression())
            while self.lexer.match(','):
                args.append(self._expression())
        self.lexer.consume(')')
        func = Variable(ident)
        return Expression(func, Data(args), lambda f, a, e: f(a, e))

    def _primary(self):
        if self.lexer.match('true'):
            return Data(True)
        if self.lexer.match('false'):
            return Data(False)
        if self.lexer.match('num'):
            return Data(self.lexer.value)
        if self.lexer.match('string'):
            return Data(self.lexer.value)
        if self.lexer.match('('):
            expr = self._expression()
            self.lexer.consume(')')
            return expr
        self.lexer.consume('ident')
        return Variable(self.lexer.value)

