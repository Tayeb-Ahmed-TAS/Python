## Python Exception Handling

### Exception :

- The exception is a **Runtime Error**.

- It can happen for **Incorrect Input** or **Incorrect Code**.

### Python try...except Block :

- The try...except block is used to handle exceptions in Python

  #### Syntax :

        try:

            # code that may cause exception

        except exception_name:

            # code to run when exception occurs

### Python try...finally :

- In Python, the finally block is always executed no matter whether there is an exception or not.

- The finally block is optional. And, for each try block, there can be only one finally block.

  #### Example :

        try:

            numerator = 10

            denominator = 0

            result = numerator/denominator

            print(result)

        except exception_name:

            print("Error: Denominator cannot be 0.")

        finally:

            print("This is finally block.")

  #### Output :

        Error: Denominator cannot be 0.

        This is finally block.

  ### Python Built-in Exceptions :

        print(dir(locals()['__builtins__']))

- We can view all the built-in exceptions using the built-in local() function.

### Some of the common built-in exceptions :

| Exception             | Cause of Error                                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| AssertionError        | Raised when an assert statement fails.                                                                                     |
| AttributeError        | Raised when attribute assignment or reference fails.                                                                       |
| EOFError              | Raised when the input() function hits end-of-file condition.                                                               |
| FloatingPointError    | Raised when a floating point operation fails.                                                                              |
| GeneratorExit         | Raise when a generator's close() method is called.                                                                         |
| ImportError           | Raised when the imported module is not found.                                                                              |
| IndexError            | Raised when the index of a sequence is out of range.                                                                       |
| KeyError              | Raised when a key is not found in a dictionary.                                                                            |
| KeyboardInterrupt     | Raised when the user hits the interrupt key (Ctrl+C or Delete).                                                            |
| MemoryError           | Raised when an operation runs out of memory.                                                                               |
| NameError             | Raised when a variable is not found in local or global scope.                                                              |
| NotImplementedError   | Raised by abstract methods.                                                                                                |
| OSError               | Raised when system operation causes system related error.                                                                  |
| OverflowError         | Raised when the result of an arithmetic operation is too large to be represented.                                          |
| ReferenceError        | Raised when a weak reference proxy is used to access a garbage collected referent.                                         |
| RuntimeError          | Raised when an error does not fall under any other category.                                                               |
| StopIteration         | Raised by next() function to indicate that there is no further item to be returned by iterator.                            |
| SyntaxError           | Raised by parser when syntax error is encountered.                                                                         |
| IndentationError      | Raised when there is incorrect indentation.                                                                                |
| TabError              | Raised when indentation consists of inconsistent tabs and spaces.                                                          |
| SystemError           | Raised when interpreter detects internal error.                                                                            |
| SystemExit            | Raised by sys.exit() function.                                                                                             |
| TypeError             | Raised when a function or operation is applied to an object of incorrect type.                                             |
| UnboundLocalError     | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| UnicodeError          | Raised when a Unicode-related encoding or decoding error occurs.                                                           |
| UnicodeEncodeError    | Raised when a Unicode-related error occurs during encoding.                                                                |
| UnicodeDecodeError    | Raised when a Unicode-related error occurs during decoding.                                                                |
| UnicodeTranslateError | Raised when a Unicode-related error occurs during translating.                                                             |
| ValueError            | Raised when a function gets an argument of correct type but improper value.                                                |
| ZeroDivisionError     | Raised when the second operand of division or modulo operation is zero.                                                    |
