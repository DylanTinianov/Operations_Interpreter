""" TODO:
    Allow for multiple operations on a line,
    Create an array to store operations, and proceed follow a proper order of operations
    REMOVE USED TOKENS (INTS AND OPERATORS) THEN REPEAT PROCESS.
"""

from constants import *
from errors import *


class Token(object):
    def __init__(self, typ, val):
        self.type = typ
        self.value = val


class Interpreter(object):
    def __init__(self, text):
        self.input_text = text
        self.input_len = len(self.input_text)
        self.pos = 0
        self.current_token = None
        self.tokens = [Token(BOF, None)]
        self.token_spot = 0
        self.total_output = 0

        self.left = 0
        self.right = 0
        self.operator = None

    def exit_interp(self):
        return 1 if self.input_text == 'exit' else 0

    def token_advance(self):
        if self.pos != self.input_len:
            if self.input_text[self.pos] in DIGITS:
                self.current_token = Token(INT, self.input_text[self.pos])

            elif self.input_text[self.pos] in OPERATORS[0]:
                index = OPERATORS[0].index(self.input_text[self.pos])
                self.current_token = Token(OPERATORS[1][index], OPERATORS[0][index])

            elif self.input_text[self.pos] == ' ':
                self.current_token = Token(SPACE, ' ')

            else:
                symbol_error(symbol=self.input_text[self.pos])

            self.pos += 1
            return self.current_token

        return Token(typ=EOF, val=None)

    def retrieve_num(self):
        # Move left to find left num
        self.token_spot -= 1
        while self.tokens[self.token_spot].type == INT:
            self.token_spot -= 1

        # left side
        self.token_spot += 1
        num = ''
        try:
            while self.tokens[self.token_spot].type == INT:
                num += self.tokens[self.token_spot].value
                self.token_spot += 1
        except IndexError:
            pass
        self.left = int(num)

        # right side
        self.token_spot += 1
        num = ''
        try:
            while self.tokens[self.token_spot].type == INT:
                num += self.tokens[self.token_spot].value
                self.token_spot += 1
        except IndexError:
            pass
        self.right = int(num)

    def retrieve_operator(self):
        for i in range(1, len(self.tokens)):
            if self.tokens[i].type == DIVIDE:
                self.operator = DIVIDE
                self.token_spot = i
            elif self.tokens[i].type == MULTIPLY:
                self.operator = MULTIPLY
                self.token_spot = i
            elif self.tokens[i].type == MOD:
                self.operator = MOD
                self.token_spot = i
            elif self.tokens[i].type == PLUS:
                self.operator = PLUS
                self.token_spot = i
            elif self.tokens[i].type == MINUS:
                self.operator = MINUS
                self.token_spot = i

    def pass_space(self):
        while self.current_token.type is SPACE:
            self.token_advance()

    def parse_input(self):
        if self.current_token is None:
            self.current_token = self.token_advance()  # get first token

        while self.current_token.type != EOF:
            self.pass_space()
            self.tokens.append(self.current_token)
            self.current_token = self.token_advance()

    def expr(self):
        while len(self.tokens) > 2:

            if self.operator == PLUS:
                self.total_output = self.left + self.right
            elif self.operator == MINUS:
                self.total_output = self.left - self.right
            elif self.operator == MULTIPLY:
                self.total_output = self.left * self.right
            elif self.operator == DIVIDE:
                self.total_output = self.left / self.right
            elif self.operator == MOD:
                self.total_output = self.left % self.right


if __name__ == '__main__':
    interp_ = Interpreter(text=raw_input('>>> '))
    interp_.parse_input()

    interp_.retrieve_operator()
    interp_.retrieve_num()
    print interp_.left, interp_.operator, interp_.right
    interp_.expr()
    print interp_.total_output
