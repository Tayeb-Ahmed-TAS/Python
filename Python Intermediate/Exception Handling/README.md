## Python Exception Handling

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

        except:

            print("Error: Denominator cannot be 0.")

        finally:

            print("This is finally block.")

  #### Output :

        Error: Denominator cannot be 0.

        This is finally block.
