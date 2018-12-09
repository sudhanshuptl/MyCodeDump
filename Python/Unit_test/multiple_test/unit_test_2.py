import unittest
from code_to_test import add, subtract, divide


class TestExceptions(unittest.TestCase):

    def test_divide_ex(self):
        with self.assertRaises(TypeError):
            divide(5,'dg')

        with self.assertRaises(ValueError):
            divide(5,0)

    def test_sbtract_ex(self):
        with self.assertRaises(TypeError):
            subtract(5, '546')


if __name__ == '__main__':
    unittest.main()
