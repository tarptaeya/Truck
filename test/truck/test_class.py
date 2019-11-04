from unittest import TestCase
from truck import truck

class TestClass(TestCase):
    def test_normal(self):
        res = truck.execute("""
        class TestMath {
            power(x, p) {
                r = 1
                while p > 0 {
                    r = r * x
                    p = p - 1
                }
                return r
            }
        }

        t = TestMath()
        t.power(2, 10)
        """)

        self.assertEqual(res, 2 ** 10)

    def test_constructor(self):
        res = truck.execute("""
        class Person {
            constructor(name, age) {
                this.name = name
                this.age = age
            }
        }

        p = Person("truck", 1)
        p.name
        """)

        self.assertEqual(res, "truck")

    def test_instance(self):
        res = truck.execute("""
        class A { constructor() { this.x = 1 } }
        class B extends A { constructor() { super.constructor() } update() { this.x = this.x * 2 } }

        x = B()
        y = B()

        x.update()
        x.update()

        y.x
        """)

        self.assertEqual(res, 1)

    def test_inheritance(self):
        res = truck.execute("""
        class Base {
            greet() {
                return "Hello from base class"
            }
        }

        class Derived extends Base {
        }

        d = Derived()
        d.greet()
        """)

        self.assertEqual(res, "Hello from base class")
