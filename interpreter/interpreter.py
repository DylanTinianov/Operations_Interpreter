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

    def exit_interp(self):
        return 1 if self.input_text == 'exit' else 0

    def token_advance(self):
        if not self.pos == self.input_len:
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

        return Token(EOF, None)

    def token_match(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.token_advance()
        else:
            parsing_error()

    def retrieve_num(self):
        num = ''
        while self.current_token.type == INT:
            num += self.current_token.value
            self.token_match(token_type=INT)
        return int(num)

    def pass_space(self):
        while self.current_token.type is SPACE:
            self.token_advance()

    def expr(self):
        if self.current_token is None:
            self.current_token = self.token_advance()

            self.pass_space()
            left = self.retrieve_num()

            self.pass_space()
            operator = self.current_token
            self.token_advance()

            self.pass_space()
            right = self.retrieve_num()

            if operator.type == PLUS:
                return left + right
            elif operator.type == MINUS:
                return left - right
            elif operator.type == MULTIPLY:
                return left * right
            elif operator.type == DIVIDE:
                return left / right
            elif operator.type == MOD:
                return left % right

            operator_error(type_=operator.type)
