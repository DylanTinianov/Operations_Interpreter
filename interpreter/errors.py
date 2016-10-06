def parsing_error():
    raise Exception('Error parsing input')


def symbol_error(symbol):
    raise Exception('Symbol', symbol, ' usage not allowed')


def type_error(type_):
    raise Exception('Incorrect usage of type:', type_)
