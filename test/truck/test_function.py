from unittest import TestCase
from truck import truck

class TestFunction(TestCase):
    def test_normal(self):
        res = truck.execute("""
        function addNums(x, y) {
            return x + y
        }

        addNums(5, 2 * 3)
        """)

        self.assertEqual(res, 5 + 2 * 3)

    def test_recursive(self):
        from math import factorial
        res = truck.execute("""
        function factorial(n) {
            if n < 1 {
                return 1
            }

            return n * factorial(n - 1)
        }

        factorial(100)
        """)

        self.assertEqual(res, factorial(100))

    def test_closure(self):
        res = truck.execute("""
        function outer(x, y) {
            z = x + y

            return function(p) {
                return p * z
            }
        }

        f = outer(2, 3)
        f(10)
        """)

        self.assertEqual(res, 10 * (2 + 3))

