import reporter
from environ import Environ

class Program:
    def __init__(self):
        self.statements = []

    def eval(self, environ):
        for statement in self.statements:
            statement.eval(environ)


class Block:
    def __init__(self):
        self.statements = []

    def eval(self, environ):
        environ = Environ(environ)
        for statement in self.statements:
            statement.eval(environ)


class Declaration:
    def __init__(self, ident, expression):
        self.ident = ident
        self.expression = expression

    def eval(self, environ):
        result = self.expression.eval(environ) if self.expression else None
        environ.set(self.ident, result)


class IfStatement:
    def __init__(self, cond, then, otherwise=None):
        self.cond = cond
        self.then = then
        self.otherwise = otherwise

    def eval(self, environ):
        if self.cond.eval(environ):
            self.then.eval(environ)
        elif self.otherwise:
            self.otherwise.eval(environ)


class WhileStatement:
    def __init__(self, cond, then):
        self.cond = cond
        self.then = then

    def eval(self, environ):
        while self.cond.eval(environ):
            self.then.eval(environ)


class PrintStatement:
    def __init__(self, expr):
        self.expr = expr

    def eval(self, environ):
        print(self.expr.eval(environ))


class Assign:
    def __init__(self, ident, expr):
        self.ident = ident
        self.expr = expr

    def eval(self, environ):
        environ.update(self.ident, self.expr.eval(environ))


class Expression:
    def __init__(self, left, right, oper):
        self.left = left
        self.right = right
        self.oper = oper

    def eval(self, environ):
        left = self.left.eval(environ)
        right = self.right.eval(environ)
        return self.oper(left, right, environ)


class Lambda:
    def __init__(self, params, block):
        self.params = params
        self.block = block

    def eval(self, environ):
        def func(args, environ):
            environ = Environ(environ)
            args = zip(self.params, args)
            for (p, a) in args:
                environ.set(p, a.eval(environ))
            return self.block.eval(environ)
        return func


class Variable:
    def __init__(self, ident):
        self.ident = ident

    def eval(self, environ):
        value = environ.get(self.ident)
        if value is None:
            reporter.report_error(f'unknown variable {self.ident}')
        return value


class Data:
    def __init__(self, data):
        self.data = data

    def eval(self, environ):
        return self.data

