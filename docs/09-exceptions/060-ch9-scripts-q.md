



40 script-based questions focused on exceptions


1. Write a script that attempts to add a string and an integer. Wrap this in a try-except block to catch the specific exception and print a helpful message.

```python

try:
    # Attempting to add incompatible types
    result = "
```python
" + 3 
except TypeError as e:
    # Handling the mismatch between string and integer
    print(f"Error caught: {e}. You cannot add a string to an integer directly.")

```
2. Create a script that asks a user for their age. Use the raise statement to trigger a ValueError if the age is less than 0, and handle it.

```python

try:
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        # Manually triggering an exception for invalid data
        raise ValueError("Age cannot be a negative number.")
    print(f"Age recorded: {user_age}")
except ValueError as e:
    # Printing the message provided in the raise statement
    print(f"Validation Error: {e}")

```
3. Demonstrate the difference between a Syntax Error and an Exception by writing a script that attempts to divide by zero. Explain via comments why this is an Exception and not a Syntax Error.

```python

# A Syntax Error would prevent this code from even starting (e.g., missing ':').
# This code is syntactically correct, so it compiles and runs.
try:
    # The error happens at 'runtime' when the instruction is executed.
    calculation = 10 / 0
except ZeroDivisionError:
    # This is an Exception because the logic failed during execution.
    print("Logic Error: You cannot divide a number by zero.")

```
4. Write a script using try, except, and else. The script should divide two numbers; the else block should print the result only if no error occurred.

```python

try:
    num1 = 10
    num2 = 2
    ans = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    # This runs only if the try block completes without errors
    print(f"Division successful! The result is: {ans}")

```
5. Create a script that tries to access a non-existent file. Handle both `FileNotFoundError` and `PermissionError` separately.

```python

try:
    # Attempting to open a file that likely doesn't exist
    with open("ghost_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    # Specific handler for missing files
    print("The system could not find the specified file.")
except PermissionError:
    # Specific handler for access rights issues
    print("You do not have the required permissions to read this file.")

```
6. Write a script that uses a `finally` block to ensure a "Cleanup Complete" message prints regardless of whether a `ValueError` occurs during a string-to-int conversion.

```python

try:
    # Risky conversion
    val = int("abc")
except ValueError:
    print("Conversion failed: Invalid literal for integer.")
finally:
    # This block executes no matter what happened above
    print("Cleanup Complete: Releasing resources and closing sessions.")

```
7. Demonstrate the "Generic Exception" safety net. Write a script with a specific except for `IndexError` and a generic except Exception as `e` for any other unforeseen errors.

```python

try:
    my_list = [1, 2, 3]
    # This will trigger an IndexError
    print(my_list[10])
except IndexError:
    print("Specific Error: Index is out of range.")
except Exception as e:
    # Fallback for any error not caught by specific blocks
    print(f"An unexpected error occurred: {e}")

```
8. Explain the risk of a "bare" except: clause. Write a script that uses one, and add a comment explaining why catching `KeyboardInterrupt` accidentally is bad.

```python

try:
    while True:
        print("Running... (Try pressing Ctrl+C)")
        import time
        time.sleep(1)
except:
    # DANGER: This catches EVERYTHING, including KeyboardInterrupt (Ctrl+C).
    # The user might be unable to stop the program normally.
    print("Caught something, but I don't know what. This is bad practice!")

```
9. Write a script that demonstrates the as keyword. Catch a `ZeroDivisionError` and use the alias to print the arguments (args) stored inside the exception object.

```python

try:
    result = 5 / 0
except ZeroDivisionError as e:
    # 'e' is an instance of the ZeroDivisionError class
    # .args usually contains the error message string
    print(f"Exception Type: {type(e)}")
    print(f"Arguments provided to exception: {e.args}")

```
10. Use the with statement (Context Manager) to open a file. Write a comment explaining why this is safer than manual `f.close()` in terms of exceptions.

```python

try:
    # The 'with' statement automatically handles closing the file
    # even if an exception occurs inside the block.
    with open("sample.txt", "w") as f:
        f.write("Hello World")
        # If a crash happened here, 'with' would still close the file safely.
except IOError as e:
    print(f"File error: {e}")

```
11. Create a dictionary and attempt to access a missing key. Catch the `KeyError` and use the else block to confirm the data was found.

```python

data = {"name": "Alice", "role": "Admin"}

try:
    # Attempting to access a key that isn't there
    user_id = data["id"]
except KeyError as e:
    print(f"Key Error: The key {e} was not found in the dictionary.")
else:
    print(f"Data retrieved: {user_id}")

```
12. Demonstrate handling multiple exceptions in a single tuple. Catch ValueError and `TypeError` in one block for a script that processes user input.

```python

def process_input(data):
    try:
        # Potential TypeError (if data is not string) or ValueError (if not digits)
        value = int(data)
        print(f"Processed: {value}")
    except (ValueError, TypeError):
        # Grouping related errors that require the same response
        print("Input Error: Please provide a valid numeric string.")

process_input(None)
process_input("xyz")

```
13. Show the correct order of handling a Parent and Child exception. Define a custom ParentError and a `ChildError`, then catch them in the correct sequence.

```python

class ParentError(Exception): pass
class ChildError(ParentError): pass

try:
    raise ChildError("Specific problem occurred")
except ChildError:
    # Specific child must come first
    print("Caught the specific ChildError.")
except ParentError:
    # General parent comes second
    print("Caught a general ParentError.")

```
14. Show the "Incorrect" order of Parent/Child handling and explain via comments why the `ChildError` block becomes unreachable.

```python

class ParentError(Exception): pass
class ChildError(ParentError): pass

try:
    raise ChildError("Specific problem")
except ParentError:
    # This block will catch ChildError because ChildError IS a ParentError
    print("Caught by Parent block.")
except ChildError:
    # This code is unreachable! The parent above already 'swallowed' the error.
    print("Caught by Child block.")

```
15. Write a script that defines a custom exception `InsufficientFundsError` that takes balance and amount in its `__init__` method.

```python

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        # Passing a message to the base Exception class
        super().__init__(f"Attempted to withdraw {amount} with balance {balance}")

try:
    raise InsufficientFundsError(100, 500)
except InsufficientFundsError as e:
    print(f"Custom Data: Balance={e.balance}, Requested={e.amount}")

```
16. Implement the `__str__` method in a custom exception class to provide a formatted error message when the object is printed.

```python

class NetworkError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        # Custom string representation for print() and str()
        return f"[Network Error Code: {self.code}] Connection timed out."

try:
    raise NetworkError(404)
except NetworkError as e:
    # This triggers the __str__ method
    print(e)

```
17. Write a script that demonstrates `ImportError` by trying to import a non-existent module. Handle `ModuleNotFoundError` specifically.

```python

try:
    import mythical_module
except ModuleNotFoundError:
    # ModuleNotFoundError is a child of ImportError
    print("Error: The requested module 'mythical_module' does not exist.")
except ImportError:
    print("Error: A general import error occurred.")

```
18.` Illustrate AttributeError` by attempting to call a method that does not exist on a string object.

```python

text = "Hello"
try:
    # Strings do not have a 'push' method
    text.push("World")
except AttributeError as e:
    print(f"Object Error: {e}")

```
19. Demonstrate `NameError` by trying to print a variable that hasn't been defined yet.

```python

try:
    # 'secret_key' has not been assigned a value
    print(secret_key)
except NameError as e:
    print(f"Variable Error: {e}. Ensure variables are defined before use.")

```
20. Write a script that catches `IndexError` when iterating through a list and trying to access an element beyond its length.

```python

my_list = [10, 20]
try:
    # Index 2 does not exist (valid indices are 0, 1)
    item = my_list[2]
except IndexError:
    print("List Error: You are trying to access a position that doesn't exist.")

```
21. Use `raise` to re-raise an exception after logging it locally.

```python

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Logging locally: Someone tried to divide by zero.")
    # Re-raising the current exception to be handled by a higher level
    raise 

```
22. Create a script that uses `EOFError` to handle a situation where `input()` is interrupted (e.g., by pressing Ctrl+D).

```python

try:
    data = input("Enter data (or press Ctrl+D to exit): ")
    print(f"User entered: {data}")
except EOFError:
    # Triggered when the input stream ends unexpectedly
    print("\nEnd of file reached. Exiting program gracefully.")

```
23. Write a function that calculates a square root. Raise a `ValueError` if the input is negative, and catch it in the calling code.

```python

import math

def get_sqrt(n):
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(n)

try:
    print(get_sqrt(-9))
except ValueError as e:
    print(f"Math Error: {e}")

```
24. Demonstrate the hierarchy of `ArithmeticError`. Catch `ZeroDivisionError` specifically and then catch `ArithmeticError` as a fallback.

```python

try:
    # Triggering one of the arithmetic errors
    val = 10 / 0
except ZeroDivisionError:
    print("Specific: Zero Division caught.")
except ArithmeticError:
    # Catches OverflowError, FloatingPointError, etc.
    print("General: An arithmetic error occurred.")

```
25. Write a script that checks if a directory exists using `OSError`.

```python

import os

try:
    # Attempting to list contents of a restricted or non-existent path
    os.listdir("/root/hidden")
except OSError as e:
    # OSError covers system/OS level failures
    print(f"System Error: {e}")

```
26. Show how TypeError occurs when trying to iterate over an integer.

```python

number = 12345
try:
    for digit in number:
        print(digit)
except TypeError:
    # Integers are not iterable
    print("Type Error: Numbers are not iterable. Convert to string first.")

```
27. Write a script that demonstrates that `finally` runs even if a `return` statement is executed in the try block.

```python

def check_finally():
    try:
        print("Inside try block")
        return "Returning from try"
    finally:
        # This will print BEFORE the function actually returns the value
        print("Finally block executing after return statement!")

result = check_finally()
print(result)

```
28. Use a generic except to catch a `KeyboardInterrupt` and print "User aborted", but add a comment explaining why this is usually avoided.

```python

try:
    import time
    time.sleep(10)
except KeyboardInterrupt:
    # Specifically catching Ctrl+C is fine, 
    # but using 'except Exception' or 'except:' to catch it is bad.
    print("User aborted the process.")

```
29. Illustrate `IndentationError` logic. Explain via comments why this cannot be caught with `try-except`.

```python

# The following code would cause an IndentationError:
# try:
#     if True:
#     print("Missing indent")
# except IndentationError:
#     print("Caught!")

# EXPLANATION: IndentationError is a SyntaxError. 
# It is caught during 'Parsing' (Compile-time), not 'Runtime'. 
# Because the script can't even be parsed, the try-except never gets to run.

```
30. Create a script that retrieves the name of the exception class dynamically using `type(e).__name__`.

```python

try:
    int("abc")
except Exception as e:
    # Helpful for generic logging to know which error class was triggered
    error_type = type(e).__name__
    print(f"Caught an error of type: {error_type}")

```
31. (Advanced) Use Python 3.11’s `ExceptionGroup` to raise multiple exceptions at once.

```python

# ExceptionGroups allow bundling multiple errors
try:
    raise ExceptionGroup("Validation Failures", [
        ValueError("Invalid age"),
        TypeError("Invalid name type"),
        KeyError("Missing ID")
    ])
except ExceptionGroup as eg:
    print(f"Caught a group: {eg.message}")
    # Iterating through the bundled exceptions
    for e in eg.exceptions:
        print(f" - Sub-error: {e}")

```
32. (Advanced) Demonstrate the `except*` syntax to handle specific errors within an ExceptionGroup.

```python

try:
    raise ExceptionGroup("Multi-Error", [ValueError("Bad Value"), TypeError("Bad Type")])
except* ValueError as eg:
    # This syntax specifically filters out ValueErrors from the group
    print("Handled the ValueErrors from the group.")
except* TypeError as eg:
    print("Handled the TypeErrors from the group.")

```
33. (Advanced) Use the `add_note()` method to attach extra debugging information to an exception.

```python

try:
    raise ValueError("Initial Error")
except ValueError as e:
    # Adding extra context without changing the original message
    e.add_note("Context: This occurred during the database sync phase.")
    raise # Re-raising will now show the note in the traceback

```
34. (Advanced) Demonstrate "Exception Chaining" using `raise ... from`.

```python

try:
    # Low-level error
    1 / 0
except ZeroDivisionError as e:
    # Wrapping the error in a higher-level business logic exception
    # 'from e' maintains the traceback of the original error
    raise RuntimeError("Application failed to process data") from e

```
35. (Advanced) Use `raise ...` from None to suppress the context of a previous exception.

```python

try:
    int("hello")
except ValueError:
    # Using 'from None' hides the fact that a ValueError occurred
    # and only shows the new RuntimeError to the user.
    raise RuntimeError("A clean error occurred without showing context") from None

```
36. (Advanced) Use the traceback module to print the full stack trace as a string without crashing the program.

```python

import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    # Capturing the traceback into a variable for logging
    error_stack = traceback.format_exc()
    print("Program did not crash, but here is the log:")
    print(error_stack)

```
37. (Advanced) Create a custom Context Manager using a class with `__enter__` and `__exit__`.

```python

class MyResource:
    def __enter__(self):
        print("Resource Acquired")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # This handles the cleanup
        print("Resource Released")
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return True # Suppresses the exception

with MyResource():
    print("Doing work...")
    raise ValueError("Work failed")

```
38. (Advanced) Use `contextlib.suppress` to ignore a specific exception silently.

```python

from contextlib import suppress
import os

# Instead of try-except, this concisely ignores FileNotFoundError
with suppress(FileNotFoundError):
    os.remove("non_existent_file.txt")
    print("This line runs, but nothing happens if the file is missing.")

```
39. (Advanced) Demonstrate how to handle nested `try-except` blocks where an inner exception is caught and a different one is raised.

```python

try:
    try:
        # Inner risky code
        open("none.txt", "r")
    except FileNotFoundError:
        print("Inner: File missing. Raising ValueError instead.")
        raise ValueError("Configuration missing")
except ValueError as e:
    print(f"Outer: Caught converted exception: {e}")

```
40. (Advanced) Write a script that checks for "MRO" (Method Resolution Order) issues in custom exceptions when multiple inheritance is used.

```python

class Base(Exception): pass
class Mixin: pass
class CustomError(Base, Mixin): pass

try:
    raise CustomError("Testing MRO")
except CustomError as e:
    # Verifying inheritance chain
    print(f"Exception Class Hierarchy: {CustomError.mro()}")
    print("Custom Error caught successfully.")

```









