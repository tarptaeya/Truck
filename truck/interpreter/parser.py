from .ast import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        root = self._program()
        return root

    def _program(self):
        # program -> (stmt)
        p = Program()
        while not self.lexer.peek("Eof"):
            s = self._stmt()
            p.add(s)
        return p

    def _stmt(self):
        # stmt -> block
        if self.lexer.peek("{"):
            return self._block()
        # stmt -> if
        if self.lexer.peek("if"):
            return self._if()
        # stmt -> while
        if self.lexer.peek("while"):
            return self._while()
        # stmt -> use
        if self.lexer.peek("use"):
            return self._use()
        # stmt -> break
        if self.lexer.peek("break"):
            return self._break()
        # stmt -> continue
        if self.lexer.peek("continue"):
            return self._continue()
        # stmt -> return
        if self.lexer.peek("return"):
            return self._return()
        # stmt -> assign
        return self._assign()

    def _block(self):
        # block -> { (stmt) }
        b = Block()
        self.lexer.consume("{")
        while not self.lexer.match("}"):
            s = self._stmt()
            b.add(s)
        return b

    def _if(self):
        # if -> if expr block [else block]?
        i = If()
        self.lexer.consume("if")
        i.cond = self._expr()
        i.then = self._block()
        if self.lexer.match("else"):
            i.otherwise = self._block()
        return i

    def _while(self):
        # while -> while expr block
        w = While()
        self.lexer.consume("while")
        w.cond = self._expr()
        w.block = self._block()
        return w

    def _use(self):
        # use -> use (.)?ident(.ident) [as ident]?
        u = Use()
        self.lexer.consume("use")

        if self.lexer.match("extern"):
            u.extern = True

        while self.lexer.match("."):
            u.path.append(".")
        self.lexer.consume("Ident")
        u.path.append(self.lexer.value)
        while self.lexer.match("."):
            self.lexer.consume("Ident")
            u.path.append(self.lexer.value)
        if self.lexer.match("as"):
            self.lexer.consume("Ident")
            u.alias = self.lexer.value
        return u

    def _break(self):
        # break -> break
        b = Break()
        self.lexer.consume("break")
        return b

    def _continue(self):
        # continue -> continue
        c = Continue()
        self.lexer.consume("continue")
        return c

    def _return(self):
        # return -> return [expr]
        r = Return()
        self.lexer.consume("return")
        r.expr = self._expr()
        return r

    def _assign(self):
        mark = self.lexer.index
        # assign -> attrib = expr
        try:
            a = Assign()
            a.lvalue = self._attrib()
            self.lexer.consume("=")
            a.rvalue = self._expr()
            return a
        # assign -> expr
        except:
            self.lexer.index = mark
            return self._expr()

    def _expr(self):
        # expr -> function
        if self.lexer.peek("function"):
            return self._function()
        # expr -> class
        if self.lexer.peek("class"):
            return self._class()
        # expr -> or
        return self._or()

    def _function(self):
        # function -> function [ident] args block
        f = Function()
        self.lexer.consume("function")
        if self.lexer.match("Ident"):
            f.ident = self.lexer.value
        f.args = self._args()
        f.body = self._block()
        return f

    def _args(self):
        # args -> "(" [ arg ("," arg) ] ")"
        a = []
        self.lexer.consume("(")
        while not self.lexer.match(")"):
            self.lexer.consume("Ident")
            a.append(self.lexer.value)
            while self.lexer.match(","):
                self.lexer.consume("Ident")
                a.append(self.lexer.value)
        return a

    def _class(self):
        # class -> class ident "{" (method) "}"
        c = Class()
        self.lexer.consume("class")
        if self.lexer.match("Ident"):
            c.ident = self.lexer.value
        if self.lexer.match("extends"):
            self.lexer.consume("Ident")
            c.base = self.lexer.value
        self.lexer.consume("{")
        while not self.lexer.match("}"):
            c.methods.append(self._method())
        return c

    def _method(self):
        # method -> ident args block
        f = Function()
        self.lexer.consume("Ident")
        f.ident = self.lexer.value
        f.args = self._args()
        f.body = self._block()
        return f

    def _or(self):
        # or -> and ("or" and)
        e = self._and()
        while self.lexer.match("or"):
            e = Expr(e, self._expr(), "or")
        return e

    def _and(self):
        # and -> equal ("and" equal)
        e = self._equal()
        while self.lexer.match("and"):
            e = Expr(e, self._expr(), "and")
        return e

    def _equal(self):
        # equal -> comparision ("==" | "!=" comparision)
        e = self._comparision()
        while True:
            if self.lexer.match("=="):
                e = Expr(e, self._comparision(), "==")
            elif self.lexer.match("!="):
                e = Expr(e, self._comparision(), "!=")
            else:
                break
        return e

    def _comparision(self):
        # comparision -> add ("<=" | ">=" | "<" | ">" add)
        e = self._add()
        while True:
            if self.lexer.match(">="):
                e = Expr(e, self._add(), ">=")
            elif self.lexer.match("<="):
                e = Expr(e, self._add(), "<=")
            elif self.lexer.match(">"):
                e = Expr(e, self._add(), ">")
            elif self.lexer.match("<"):
                e = Expr(e, self._add(), "<")
            else:
                break
        return e

    def _add(self):
        # add -> mult ("+" | "-" mult)
        e = self._mult()
        while True:
            if self.lexer.match("+"):
                e = Expr(e, self._mult(), "+")
            elif self.lexer.match("-"):
                e = Expr(e, self._mult(), "-")
            else:
                break
        return e

    def _mult(self):
        # mult -> bit_or ("*" | "/" | "%" bit_or)
        e = self._bit_or()
        while True:
            if self.lexer.match("*"):
                e = Expr(e, self._bit_or(), "*")
            elif self.lexer.match("/"):
                e = Expr(e, self._bit_or(), "/")
            elif self.lexer.match("%"):
                e = Expr(e, self._bit_or(), "%")
            else:
                break
        return e

    def _bit_or(self):
        # bit_or -> bit_and ("|" bit_and)
        e = self._bit_and()
        while self.lexer.match("|"):
            e = Expr(e, self._bit_and(), "|")
        return e

    def _bit_and(self):
        # bit_and -> unary ("&" unary)
        e = self._unary()
        while self.lexer.match("&"):
            e = Expr(e, self._unary(), "&")
        return e

    def _unary(self):
        # unary -> ("-" | "~" | "not") unary
        # TODO: not and ~ ^
        if self.lexer.match("-"):
            return Expr(Const(0), self._unary(), "-")
        #unary -> attrib
        return self._attrib()

    def _attrib(self):
        # attrib -> primary ("()") ("." primary ("()"))
        e = self._primary()
        while True:
            if self.lexer.match("."):
                e = Expr(e, self._primary(), ".")
            elif self.lexer.peek("("):
                e = Expr(e, self._params(), "()")
            else:
                break
        return e

    def _params(self):
        # params -> "(" [expr ("," expr)] ")"
        p = Params()
        self.lexer.consume("(")
        while not self.lexer.match(")"):
            p.add(self._expr())
            while self.lexer.match(","):
                p.add(self._expr())
        return p

    def _primary(self):
        # primary -> Num
        if self.lexer.match("Num"):
            return Const(self.lexer.value)
        # primary -> String
        if self.lexer.match("String"):
            return Const(self.lexer.value)
        # primary -> true
        if self.lexer.match("true"):
            return Const(True)
        # primary -> false
        if self.lexer.match("false"):
            return Const(False)
        # primary -> "(" expr ")"
        if self.lexer.match("("):
            e = self._expr()
            self.lexer.consume(")")
            return e
        if self.lexer.match("Ident"):
            return Ident(self.lexer.value)
        raise ParseError("unable to reduce to primary")


class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
