# Interpreter
This Software is a continuously running interpreter capable of computing and printing multiple integer operations

### Operations
This Interpreter can compute the following: (listed in order of precedence)
```
/ * % + -
```
Standard order of operations will be followed

### Elegant Error Handling
The program will be polite about incorrect inputs

<img src="https://github.com/DylanTinianov/Images/blob/master/Interpreter/error_handling.png" width="200" height="200" />

This is accomplished through creating custom errors and exceptions

For example:

``` Python
def symbol_error(symbol):
    raise SymbolException(symbol=symbol)

class SymbolException(Exception):
    def __init__(self, symbol):
        self.symbol = symbol
        self.__str__()

    def __str__(self):
        print 'Symbol', self.symbol, ' usage not allowed'
```
### Linux
To run the interpreter, run the following in project root
```bash
$ ./scripts/run.sh
```
To exit the program, simply type 'exit': 
```
>>> exit
```

### Example Usage
Input can be placed in any order, and spaces are ignored

No limit to the number of operations per line

<img src="https://github.com/DylanTinianov/Images/blob/master/Interpreter/example.png" width="200" height="100" />
