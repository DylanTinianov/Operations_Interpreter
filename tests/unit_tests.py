import unittest
from interpreter import *
from test_cases import *


class OperatorTests(unittest.TestCase):

    def test_addition(self):
        interp_ = Interpreter(text='987 + 1247')
        self.assertEqual(interp_.expr(), 987 + 1247)

    def test_subtraction(self):
        interp_ = Interpreter(text='987 - 1247')
        self.assertEqual(interp_.expr(), 987 - 1247)

    def test_multiplication(self):
        interp_ = Interpreter(text='987 * 1247')
        self.assertEqual(interp_.expr(), 987 * 1247)

    def test_division(self):
        interp_ = Interpreter(text='10 / 5 ')
        self.assertEqual(interp_.expr(), 10 / 5)

    def test_modulo(self):
        interp_ = Interpreter(text='100 % 5 ')
        self.assertEqual(interp_.expr(), 100 % 5)

    def test_spacing(self):
        for case in TEST_SPACING:
            interp_ = Interpreter(text=case)
            interp_.expr()


if __name__ == '__main__':
    unittest.main(exit=False)
