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
        self.left_spot = 0
        self.last_operator = None

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
        self.left_spot = self.token_spot
        num = ''
        try:
            while self.tokens[self.token_spot].type == INT:
                num += str(self.tokens[self.token_spot].value)
                self.tokens.pop(self.token_spot)
        except IndexError:
            pass

        try:
            self.left = int(num)
        except ValueError:
            raise type_error(type_=self.tokens[self.token_spot].value)

        # right side
        self.token_spot += 1
        num = ''
        try:
            while self.tokens[self.token_spot].type == INT:
                num += str(self.tokens[self.token_spot].value)
                self.tokens.pop(self.token_spot)
        except IndexError:
            pass

        try:
            self.right = int(num)
        except ValueError:
            raise type_error(type_=self.tokens[self.token_spot].value)

    def find_token_types(self):
        token_types = list()
        for i in self.tokens:
            token_types.append(i.type)
        return token_types

    def retrieve_operator(self):
        token_types = self.find_token_types()
        is_operator = False

        for i in range(1, len(self.tokens)):
            if self.tokens[i].type in OPERATORS[1]:
                is_operator = True

                if self.tokens[i].type == DIVIDE:
                    self.operator = DIVIDE
                    self.token_spot = i
                    break

                elif self.tokens[i].type == MULTIPLY:
                    self.operator = MULTIPLY
                    self.token_spot = i
                    if DIVIDE in token_types:
                        continue
                    else:
                        break

                elif self.tokens[i].type == MOD:
                    self.operator = MOD
                    self.token_spot = i
                    cont = False
                    for typ in [DIVIDE, MULTIPLY]:
                        if typ in token_types:
                            cont = True
                    if cont:
                        continue
                    else:
                        break

                elif self.tokens[i].type == PLUS:
                    self.operator = PLUS
                    self.token_spot = i
                    cont = False
                    for typ in [DIVIDE, MULTIPLY, MOD]:
                        if typ in token_types:
                            cont = True
                    if cont:
                        continue
                    else:
                        break

                elif self.tokens[i].type == MINUS:
                    self.operator = MINUS
                    self.token_spot = i
                    cont = False
                    for typ in [DIVIDE, MULTIPLY, MOD, PLUS]:
                        if typ in token_types:
                            cont = True
                    if cont:
                        continue
                    else:
                        break

        if is_operator is False:
            raise operator_error(type_='NO OPERATOR')

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
        if self.operator == PLUS:
            self.total_output += self.left + self.right
        elif self.operator == MINUS:
            self.total_output += (self.left - self.right)
        elif self.operator == MULTIPLY:
            self.total_output += (self.left * self.right)
        elif self.operator == DIVIDE:
            self.total_output += (self.left / self.right)
        elif self.operator == MOD:
            self.total_output += (self.left % self.right)

        if len(self.tokens) > 2:
            token_types = self.find_token_types()
            num_ops = 0
            for i in token_types:
                if i in OPERATORS[1]:
                    num_ops += 1

            self.tokens.pop(self.left_spot)     # pop out operator
            self.tokens.insert(self.left_spot, Token(typ=INT, val=self.total_output))   # insert new total
            if len(self.tokens) >= 4:
                self.total_output = 0
