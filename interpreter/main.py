from interpreter import *


def main():
    while True:
        interp_ = Interpreter(text=raw_input('>>> '))
        if interp_.exit_interp():
            return
        print(interp_.expr())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
