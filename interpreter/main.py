from interpreter import *
from errors_and_exceptions import *


def main():
    while True:
        try:
            interp_ = Interpreter(text=raw_input('>>> '))
            if interp_.exit_interp():
                break

            interp_.parse_input()

            while len(interp_.tokens) > 2:
                interp_.retrieve_operator()
                interp_.retrieve_num()
                interp_.expr()

            print interp_.total_output

        except (SymbolException, TypeException, OperatorException):
            print 'Please use correct syntax'


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
