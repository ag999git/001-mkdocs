


## Research / Project Question

### Handling Uncaught Exceptions in Tkinter

Normally, Python programs display a **traceback error** and may stop execution when an exception is not handled using: `try-except`

However, GUI applications often require a more user-friendly way to handle unexpected errors.

Research how Python handles **uncaught exceptions** and investigate the role of: `sys.excepthook` in overriding Python’s default error-handling behavior.

### Your Task

### Part A — Theory

Research and explain the following:

1.  What is an **uncaught exception**?
2.  How does Python normally respond to exceptions that are not handled using `try-except`?
3.  What is: `sys.excepthook` and what is its purpose?

4.  Explain the difference between:

    -    Local Exception Handling: `try-except`
    -    Global Exception Handling: `sys.excepthook`

5.  Why might GUI applications prefer a **friendly popup message** instead of a traceback?

----------

### Part B — Script Writing

Write a Tkinter program that:

1.  Creates a GUI window.
2.  Displays a scrolling log area (`Text` widget).
3.  Uses: `logging` to save errors to a file named: `error_log.txt`

4.  Defines a custom function to handle uncaught exceptions.
5.  Overrides Python’s default exception route using: `sys.excepthook`
6.  Adds a button with label: `Trigger NameError`
7.  Intentionally creates an uncaught exception when the button is clicked.
8.  Displays a friendly popup message instead of crashing.

----------

### Part C — Reflection

Answer the following:

> What would happen if: `sys.excepthook` were not overridden? Explain briefly.

### Expected Learning Outcome

After completing this task, students should be able to:

 - explain uncaught exceptions.
 - distinguish between local and global error handling. 
 - understand how `sys.excepthook` works. 
 - build safer Tkinter applications.
 - create user-friendly error reporting


## Model Theory Solution

### 1. What is an Uncaught Exception?

An **exception** is an error that occurs while a program is running.

Examples include:

```python
NameError
ValueError
ZeroDivisionError
IndexError
```

Normally, programmers handle exceptions using: `try-except`

However, when an exception is **not handled**, it becomes an:

> **uncaught exception**

Example: `print(undefined_variable)`

Here: `undefined_variable` does not exist, so Python raises: `NameError` . Further, if no: `try-except`block catches it, the exception becomes **uncaught**.

----------

### 2. How Does Python Normally Respond to Unhandled Exceptions?

By default, Python follows this sequence:

```python
Error occurs
↓
Python prints traceback
↓
Program stops (crashes)
```

Example:

```python
x = 10 / 0
# Output
Traceback (most recent call last):...ZeroDivisionError:division by zero
```

This detailed error report is called a: `traceback`.

A traceback contains:

-   type of error,
-   error message,
-   line number,
-   sequence of function calls.

Although useful for programmers, traceback messages may confuse normal users.

----------

### 3. What is `sys.excepthook` and What is Its Purpose?

Python provides a built-in mechanism called: `sys.excepthook`. It controls:

> **what Python should do when an uncaught exception occurs**

By default: 
```python
uncaught error
↓
traceback shown
↓
program crashes
```

However, programmers can replace Python’s default behavior.

Example:

```python
sys.excepthook =handle_uncaught
```

Now, instead of showing an ugly traceback: `custom_function()` runs
This function can:

-   display a friendly popup,
-   save errors to a log file,
-   notify the user,
-   prevent abrupt crashes.

Thus:

> `sys.excepthook` provides **global exception handling**.

----------

### 4. Difference Between Local and Global Exception Handling

| Feature | Local Exception Handling | Global Exception Handling |
| --- | --- | --- |
| Method | try-except | sys.excepthook |
| Scope | One specific block of code | Entire application |
| Purpose | Handle expected errors locally | Catch uncaught errors |
| Programmer control | Explicitly written around risky code | Runs automatically |
| Example | File reading, division | Unexpected program failures |

### Local Exception Handling (`try-except`)

`try-except` catches errors in a specific part of the program.

Example:

```python
try:    
    age = int(text)
except ValueError:    
    print("Invalid input")
```
Only this section (Which is fenced in a try-except block) is protected. This is called:

> **local exception handling**

because it works only in one location.

----------

### Global Exception Handling (`sys.excepthook`)

`sys.excepthook` catches errors that were **not handled anywhere else**.

Example:

```python
sys.excepthook =handle_uncaught
```

Whenever an uncaught error occurs: Python automatically calls `handle_uncaught()`. This protects the entire application. But you as a programmer are expected to write this function `handle_uncaught()`

Hence:

> **global exception handling**.

----------

### Visual Difference
**LOCAL**
```python
LOCAL:Error
↓
try-except
↓
Handled here
```
**GLOBAL**
```python
GLOBAL:Error
↓
No try-except found
↓
sys.excepthook
↓
Global handler runs
```

----------

### 5. Why Do GUI Applications Prefer Friendly Popup Messages?

GUI applications are designed for: `normal users`. Most users may not understand: `tracebacks technical error details`

Instead, GUI applications prefer: friendly popup dialogs.

Example: 
```python
Error:Something went wrong.
Please try again.
```

## Flowchart showing the execution of the script
![Flowchart handling global exceptions](/resources/ch14-tkinter-exceptions.png)

## Script

```python

import tkinter as tk
from tkinter import messagebox
import logging
import sys

# 1. CONFIGURE LOGGING
# logging.basicConfig() sets up logging to a file.
# Create log file: error_log.txt. Errors will be saved here.
# Log level: ERROR (only errors, not info/debug)
log_level = logging.ERROR
# Format: timestamp, log level, message
log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="error_log.txt", level=log_level, format=log_format)

# 2. CREATE MAIN WINDOW
root = tk.Tk()
root.title("Global Hook Demo")
root.geometry("420x300")

# 3. CREATE LIVE LOG PANEL
# Text widget behaves like a mini console window.
# It shows: (1) what user did, (2) errors, (3) global hook activity
log_box = tk.Text(root, height=8, width=45)

log_box.pack(padx=10, pady=10)

# 4. DEFINE write_log()
# Purpose: Display messages inside GUI log window.
def write_log(message):
    # Add message to log panel in the GUI window at the end
    log_box.insert(tk.END, message + "\n")

    # Auto-scroll to latest line. Without this, the log would keep adding lines
    # but the user would not see them unless they manually scroll down.
    log_box.see(tk.END)

# 5. DEFINE GLOBAL HANDLER
# Purpose: Catch uncaught errors. Log them, show popup, and update log panel.
# Example: (1) NameError (2) ZeroDivisionError
# Instead of ugly crash we have: (1) → log error (2) → update log panel (3) → show popup
# exc_type, exc_value, exc_traceback are the error details that Python passes to this 
# function when an uncaught error occurs.
# exec_type is the type of error (e.g. NameError), 
# exc_value is the error message, and 
# exc_traceback contains the stack trace. We don't use exc_traceback in this function, but it's available if we wanted to log it or show it in the popup.

def handle_uncaught(exc_type, exc_value, exc_traceback):
    # Create readable error message named error_msg from the error details.
    error_msg = (f"{exc_type.__name__}: " f"{exc_value}")

    # Show steps in log panel in the GUI window.
    write_log( "Global hook activated")
    write_log(f"ERROR → {error_msg}")

    # Also save error to file named error_log.txt using logging.error()
    logging.error(error_msg)

    write_log("Error saved to file")  # Update log panel to show that error was saved to file.

    # Show popup message
    messagebox.showerror( "Unexpected Error", error_msg)

# 6. OVERRIDE PYTHON'S #    DEFAULT ERROR ROUTE
# Normally: Error→ Traceback→ Program crashes
# We replace that route with OUR function.
# sys.excepthook is the function Python calls when an error is not caught by any try-except block. 
# By assigning our handle_uncaught function to sys.excepthook, we ensure that any uncaught error 
# will be handled by our custom function instead of crashing the program.
# sys.excepthook takes parameters exc_type, exc_value, exc_traceback which 
# contain details about the error that occurred.
sys.excepthook = (handle_uncaught)

write_log("Global hook installed")  # Update log panel to show that global hook is active.

# 7. DEFINE DELIBERATE ERROR
# Purpose: # Intentionally create → uncaught NameError.
# Global hook should catch it.
def trigger_error():
    write_log("Button clicked")  # Update log panel to show that button was clicked.
    write_log("Triggering NameError")  # Update log panel to show that NameError is being triggered.

    # Deliberate error
    print(undefined_variable)  # This will raise a NameError because 'undefined_variable' is not defined. No try-except, so it will be caught by our global handler instead of crashing the program.

# 8. CREATE BUTTON
# Button to trigger the error. It will call trigger_error() when clicked, which 
# will raise a NameError that is not caught by any try-except block, so it will 
# be handled by our global exception handler instead of crashing the program.
tk.Button(root, text="Trigger NameError", command=trigger_error).pack(pady=10)

# 9. START GUI LOOP
# Program waits for # user interaction.
root.mainloop()

```










