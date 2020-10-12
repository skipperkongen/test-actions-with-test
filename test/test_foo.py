import unittest
from foo.foo import Foo

class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.instance = Foo()

    def test_1(self):
        self.assertEquals(self.instance.foo1(1), 2)

    def test_2(self):
        self.assertEquals(self.instance.foo2(1), 2)

if __name__ == '__main__':
    unittest.main()
