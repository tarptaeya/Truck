from unittest import TestCase
from truck.interpreter import *
from truck.interpreter.ast import *

class TestParser(TestCase):
    def test_if(self):
        p = Parser(Lexer(Source("""
        if 5 > 2 { 
            print(4)
        }
        """)))
        r = Program()
        i = If()
        i.cond = Expr(Const(5), Const(2), ">")
        i.then = Block()
        i.then.add(Expr(Ident("print"), Params(Const(4)), "()"))
        r.add(i)
        self.assertEqual(p.parse().__repr__(), r.__repr__())

    def test_if_else(self):
        p = Parser(Lexer(Source("""
        if 5 > 2 {
            print(4)
        } else {
            print(2)
        }
        """)))
        r = Program()
        i = If()
        i.cond = Expr(Const(5), Const(2), ">")
        i.then = Block()
        i.then.add(Expr(Ident("print"), Params(Const(4)), "()"))
        i.otherwise = Block()
        i.otherwise.add(Expr(Ident("print"), Params(Const(2)), "()"))
        r.add(i)
        self.assertEqual(p.parse().__repr__(), r.__repr__())

    def test_while(self):
        p = Parser(Lexer(Source("""
        while 2 > 1 {
            x = x * 2
            if x > 100 {
                break
            }
        }
        """)))
        r = Program()
        w = While()
        w.cond = Expr(Const(2), Const(1), ">")
        w.block = Block()
        w.block.add(Assign(Ident("x"), Expr(Ident("x"), Const(2), "*")))
        i = If()
        i.cond = Expr(Ident("x"), Const(100), ">")
        i.then = Block()
        i.then.add(Break())
        w.block.add(i)
        r.add(w)
        self.assertEqual(p.parse().__repr__(), r.__repr__())

    def test_expr(self):
        p = Parser(Lexer(Source("5 + 20 / 10 - 3 * 2")))
        r = Program()
        e = Expr(
                5,
                Expr(
                    Expr(Const(20), Const(10), "/"),
                    Expr(Const(3), Const(2), "*"),
                    "-"),
                "+")
        r.add(e)
        self.assertEqual(p.parse().__repr__(), r.__repr__())

    def test_attrib(self):
        p = Parser(Lexer(Source("number.add(10 * 2, 5 + a).result.addTo(4)")))
        r = Program()
        e = Expr(
                Ident("number"),
                Expr(
                    Expr(
                        Ident("add"),
                        Params(
                            Expr(Const(10), Const(2), "*"),
                            Expr(Const(5), Ident("a"), "+")),
                        "()"),
                    Expr(
                        Ident("result"),
                        Expr(
                            Ident("addTo"),
                            Params(Const(4)),
                            "()"),
                        "."),
                    "."),
                ".")
        r.add(e)
        self.assertEqual(p.parse().__repr__(), r.__repr__())
