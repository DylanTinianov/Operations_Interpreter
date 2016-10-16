from interpreter import *


def main():
    while True:
        interp_ = Interpreter(text=raw_input('>>> '))
        if interp_.exit_interp():
            break

        interp_.parse_input()

        while len(interp_.tokens) > 2:
            interp_.retrieve_operator()
            interp_.retrieve_num()
            interp_.expr()

        print interp_.total_output


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
