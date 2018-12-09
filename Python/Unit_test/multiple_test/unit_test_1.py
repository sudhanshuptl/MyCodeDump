import unittest
from code_to_test import add, subtract, divide


class TestBasic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add('sudh','anshu'),'sudhanshu')

    def test_subtract(self):
        self.assertEqual(subtract(7,3),4)

    def test_divide(self):
        self.assertEqual(divide(10,5),2)


if __name__ == '__main__':
    unittest.main()