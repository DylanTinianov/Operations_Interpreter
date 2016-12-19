import pytest
from interpreter import *
from tests.test_cases import *


class TestOperator:

    def test_addition(self):
        interp_ = Interpreter(text='987 + 1247')
        interp_.parse_input()
        while len(interp_.tokens) > 2:
            interp_.retrieve_operator()
            interp_.retrieve_num()
            interp_.expr()
        assert interp_.total_output == 987 + 1247

    def test_subtraction(self):
        interp_ = Interpreter(text='987 - 1247')
        interp_.parse_input()
        while len(interp_.tokens) > 2:
            interp_.retrieve_operator()
            interp_.retrieve_num()
            interp_.expr()
        assert interp_.total_output == 987 - 1247

    def test_multiplication(self):
        interp_ = Interpreter(text='987 * 1247')
        interp_.parse_input()
        while len(interp_.tokens) > 2:
            interp_.retrieve_operator()
            interp_.retrieve_num()
            interp_.expr()
        assert interp_.total_output == 987 * 1247

    def test_division(self):
        interp_ = Interpreter(text='10 / 5')
        interp_.parse_input()
        while len(interp_.tokens) > 2:
            interp_.retrieve_operator()
            interp_.retrieve_num()
            interp_.expr()
        assert interp_.total_output == 10 / 5

    def test_modulo(self):
        interp_ = Interpreter(text='100 % 5')
        interp_.parse_input()
        while len(interp_.tokens) > 2:
            interp_.retrieve_operator()
            interp_.retrieve_num()
            interp_.expr()
        assert interp_.total_output == 100 % 5

    def test_spacing(self):
        for case in TEST_SPACING:
            interp_ = Interpreter(text=case)
            interp_.parse_input()
            while len(interp_.tokens) > 2:
                interp_.retrieve_operator()
                interp_.retrieve_num()
                interp_.expr()

    def test_exit(self):
        interp_ = Interpreter(text="exit")
        assert interp_.exit_interp()
