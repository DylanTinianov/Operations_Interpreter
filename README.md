# Operations Interpreter  [![Build Status](https://travis-ci.org/DylanTinianov/Operations_Interpreter.svg?branch=master)](https://travis-ci.org/DylanTinianov/Operations_Interpreter)
This Software is a continuously running interpreter capable of computing and printing multiple integer operations

### Operations
This Interpreter can compute the following: (listed in order of precedence)
```
/ * % + -
```
Standard order of operations will be followed

### Syntax Guide
Input can be placed in any order, and spaces are ignored

No limit to the number of operations per line or number size

Simple example:

<img src="https://github.com/DylanTinianov/Images/blob/master/Interpreter/example.png" width="200" height="100" />

To exit the program, simply type 'exit': 
```
>>> exit
```

### Syntax Error Handling
The program will be polite about incorrect inputs

#### Types of Errors
<pre>
Symbol Error:   Occurs upon parsing if a character other then an integer or operator was inputted

Type Error:     Occurs when a Token type is in a non valid location within the input

Operator Error: Occurs upon operator retrieval when there is a lack of an operator
</pre>

<img src="https://github.com/DylanTinianov/Images/blob/master/Interpreter/error_handling.png" width="200" height="200" />

This is accomplished through creating custom errors and exceptions

##### In code example:
``` Python
def symbol_error(symbol):
    raise SymbolException(symbol=symbol)

class SymbolException(Exception):
    def __init__(self, symbol):
        print 'Symbol', symbol, ' usage not allowed'
```

### Linux
To run the interpreter, run the following in project root
```bash
$ ./scripts/run.sh
```
