from unittest import TestCase
from interpreter import *


class InterpreterTests(TestCase):
    def test_addition(self):
        interp_ = Interpreter(text='987 + 1247')
        self.assertEqual(interp_.expr(), 987+1247)

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
        interp_ = Interpreter(text='10 % 5 ')
        self.assertEqual(interp_.expr(), 10 % 5)
