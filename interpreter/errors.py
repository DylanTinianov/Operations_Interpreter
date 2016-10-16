def parsing_error():
    raise Exception('Error parsing input')


def symbol_error(symbol):
    raise Exception('Symbol', symbol, ' usage not allowed')


def type_error(type_):
    raise Exception('Incorrect usage of type:', type_)


def operator_error(type_):
    raise Exception('Incorrect operator type:', type_)


def bracket_error(open_close):
    if open_close == 'close':
        raise Exception('No closing bracket')
    else:
        raise Exception('No opening bracket')
