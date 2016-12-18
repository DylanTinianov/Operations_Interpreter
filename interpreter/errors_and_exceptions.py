def symbol_error(symbol):
    raise SymbolException(symbol=symbol)


def type_error(type_):
    raise TypeException(type_=type_)


def operator_error():
    raise OperatorException()


class SymbolException(Exception):

    def __init__(self, symbol):
        print 'Symbol', symbol, ' usage not allowed'


class TypeException(Exception):

    def __init__(self, type_):
        print 'Incorrect usage of type:', type_


class OperatorException(Exception):

    def __init__(self):
        print 'No operator was entered'
