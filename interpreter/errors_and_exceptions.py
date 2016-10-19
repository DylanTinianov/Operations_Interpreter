def symbol_error(symbol):
    raise SymbolException(symbol=symbol)


def type_error(type_):
    raise TypeException(type_=type_)


def operator_error():
    raise OperatorException()


class SymbolException(Exception):
    def __init__(self, symbol):
        self.symbol = symbol
        self.__str__()

    def __str__(self):
        print 'Symbol', self.symbol, ' usage not allowed'


class TypeException(Exception):
    def __init__(self, type_):
        self.type_ = type_
        self.__str__()

    def __str__(self):
        print 'Incorrect usage of type:', self.type_


class OperatorException(Exception):
    def __init__(self):
        self.__str__()

    def __str__(self):
        print 'No operator was entered'
