from interpreter import *


def main():
    while True:
        interp_ = Interpreter(text=raw_input('>>> '))
        if interp_.exit_interp():
            return
        interp_.parse_input()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
