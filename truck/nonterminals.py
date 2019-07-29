import reporter
from environ import Environ

from source import Source
from lexer import Lexer

from collections import deque

class Program:
    def __init__(self):
        self.includes = []
        self.statements = []
        self.debug = False

    def eval(self, environ):
        for incl in self.includes:
            prog = incl.eval(environ)
            prog.eval(environ)
        for statement in self.statements:
            value = statement.eval(environ)
            if value is not None and self.debug:
                value = value.__repr__()
                print(f'=> {value}')


class Include:
    def __init__(self, filename):
        self.filename = filename

    def eval(self, environ):
        import os
        from parser import Parser
        filename = f'{self.filename}.truck'
        base = environ.get('__dir__')
        if base:
            filename = os.path.abspath(os.path.join(base, filename))
        with open(filename, 'r') as f:
            string = f.read()
            source = Source(string)
            lexer = Lexer(source)
            parser = Parser(lexer)
            parser.parse()
            return parser.root


class Block:
    def __init__(self):
        self.statements = []

    def eval(self, environ):
        environ = Environ(environ)
        for statement in self.statements:
            value = statement.eval(environ)


class BreakException(Exception):
    def __init__(self):
        super(BreakException, self).__init__('cannot break without loop')


class Break:
    def eval(self, environ):
        raise BreakException()


class ContinueException(Exception):
    def __init__(self):
        super(ContinueException, self).__init__('cannot continue without loop')


class Continue:
    def eval(self, environ):
        raise ContinueException()


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
            try:
                self.then.eval(environ)
            except BreakException:
                break
            except ContinueException:
                continue


class ReturnException(Exception):
    def __init__(self, data):
        super(ReturnException, self).__init__("no toplevel function found")
        self.data = data


class ReturnStatement:
    def __init__(self, expr):
        self.expr = expr

    def eval(self, environ):
        value = self.expr.eval(environ)
        raise ReturnException(value)


class Assign:
    def __init__(self, ident, expr):
        self.ident = ident
        self.expr = expr

    def eval(self, environ):
        value = self.expr.eval(environ)
        if value is None:
            value = Data(None)
        environ.update(self.ident, value)


class Expression:
    def __init__(self, left, right, oper):
        self.left = left
        self.right = right
        self.oper = oper

    def eval(self, environ):
        left = self.left.eval(environ) if self.left else None
        right = self.right.eval(environ) if self.right else None
        return self.oper(left, right, environ)


class Lambda:
    def __init__(self, params, block):
        self.params = params
        self.block = block

    def eval(self, environ):
        def func(args, environ):
            local = Environ(environ)
            args = zip(self.params, args)
            for (p, a) in args:
                local.set(p, a.eval(environ))
            try:
                self.block.eval(local)
            except ReturnException as r:
                return r.data
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
        if isinstance(self.data, str):
            return self.data
        return self.data


class TObject:
    def __init__(self, props={}):
        self.environ = Environ()

    def eval(self, environ):
        for k in self.environ.keys():
            environ.set(k, self.environ.get(k))


class List(TObject):
    def __init__(self, elms):
        super(List, self).__init__()
        self.data = elms
        self.environ.set('push', self.push)
        self.environ.set('pop', self.pop)

    def push(self, args, environ):
        elm = args[0].eval(environ)
        self.data.append(elm)

    def pop(self, *_):
        return self.data.pop()

    def eval(self, environ):
        super(List, self).eval(environ)
        self.data = deque(map(lambda el: el.eval(environ), self.data))
        return self

    def __repr__(self):
        data = list(self.data)
        return f'{data}'


