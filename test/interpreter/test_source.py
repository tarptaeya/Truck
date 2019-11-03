from unittest import TestCase
from truck.interpreter import Source

class TestSource(TestCase):
    def test_length(self):
        s = Source("hello")
        self.assertEqual(len(s), 5)

        s = Source("hello\nworld")
        self.assertEqual(len(s), 11)

    def test_index(self):
        s = Source("hello")
        self.assertEqual(s[1], "e")
        self.assertEqual(s[4], "o")
        self.assertEqual(s[5], None)
