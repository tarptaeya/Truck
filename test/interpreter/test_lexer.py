from unittest import TestCase
from truck.interpreter import Lexer, Source
from truck.interpreter.lexer import LexError

class TestLexer(TestCase):
    def test_ident(self):
        self._check("ident", [("Ident", "ident"), "Eof"])
        self._check("__xyz__", [("Ident", "__xyz__"), "Eof"])
        self._check("x_3_y", [("Ident", "x_3_y"), "Eof"])

    def test_number_int(self):
        self._check("0", [("Num", 0), "Eof"])
        self._check("123", [("Num", 123), "Eof"])
        self._check("5", [("Num", 5), "Eof"])

    def test_number_real(self):
        self._check("0.51", [("Num", 0.51), "Eof"])
        self._check("32.", [("Num", 32), "Eof"])
        self._check("3.045", [("Num", 3.045), "Eof"])
        self._check("2.99e+8", [("Num", 2.99e8), "Eof"])
        self._check("0.02e-1", [("Num", 0.02e-1), "Eof"])

        self.assertRaises(LexError, lambda: self._get_tokens("1.6e+"))
        self.assertRaises(LexError, lambda: self._get_tokens("3.4e"))

    def test_string(self):
        self._check("\"hello world\"", [("String", "hello world"), "Eof"])
        self._check('"Ram said, \\"Hello!\\""', [("String", 'Ram said, "Hello!"'), "Eof"])

    def _check(self, s, r):
        ts = self._get_tokens(s)
        self.assertEqual(ts, r)

    def _get_tokens(self, s):
        l = Lexer(Source(s))
        ts = []
        while True:
            t = l.next()
            if t in ["Ident", "Num", "String"]:
                ts.append((t, l.value))
            else:
                ts.append(t)
            if t == "Eof":
                break
        return ts
