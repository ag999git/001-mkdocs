

# Research / Project Question

## Tkinter `after()` — Safe and Unsafe Delayed Callbacks

In GUI applications, some tasks do not run immediately. Instead, they run after a delay. Tkinter provides the: `after()` method to schedule functions to run later. However, delayed tasks may sometimes fail. Therefore, programmers must understand the difference between: `
unsafe callback` and `safe callback`.

----------

## Part A — Theory

**Research and explain the following:**

### 1. What is: `after()` and what is its purpose?

### 2. What is a callback function?

### 3. Explain: `delayed execution` with one example.

### 4. What may happen if a delayed callback contains an error?

### 5. Explain the difference between:

  
   -  Unsafe Callback (no `try-except`) and
   - Safe Callback (using `try-except`)

### 6. Why is: `time.sleep()` generally avoided in Tkinter programs?

----------

## Part B — Script Writing

Write a Tkinter program that:

1.  Creates a GUI window with a scrolling log area.
2.  Adds two buttons:

```python
Unsafe after() Error
Safe after() Error
```

3.  The first button should:

-   schedule a task after 2 seconds,
-   deliberately generate: `ZeroDivisionError`

-   allow global exception handling to catch it.

4.  The second button should:

-   schedule a task after 2 seconds,
-   safely handle the error using: `try-except`

5.  The GUI should show log messages describing what happens.



# Model Theory Solution

## 1. What is `after()`?

The: `after()` method is used to run a function after a delay.

**Syntax:** 

```python
widget.after(time_in_ms, function_name)
# function_name is the callback function
```

Example:

```python
root.after(2000, task)
# This means: run task()after 2000 milliseconds(2 seconds)
```

----------

## 2. What is a Callback Function?

A callback function is:

> a function passed to another function and executed later.

Example:

```python
root.after(2000,task)
# Here: task is the callback function.
# It will run later.
```
----------

## 3. What is Delayed Execution?

Delayed execution means:

> code runs after some waiting time instead of immediately.

Example:

```python
root.after(3000, show_message)
# This runs: show_message() after: 3 seconds
```

----------

## 4. What Happens if Delayed Callback Fails?

Sometimes delayed functions contain errors.

Example:

```python
result = 10 / 0
# creates: ZeroDivisionError
```

The important idea is:

> the error happens later, not immediately.

This can make debugging harder.

----------

## 5. Unsafe vs Safe Callback

| Feature | Unsafe Callback | Safe Callback |
| --- | --- | --- |
| try-except used | No | Yes |
| Error handling | Global hook | Local handling |
| Program safety | Less safe | Safer |
| User feedback | Crash/error popup | Friendly message |


### Unsafe Callback

Example:

```
def task():    x = 10 / 0
```

No error handling exists.

The error escapes.

Global exception handling catches it.

----------

### Safe Callback

Example:

```python
def task():
    try:
        x = 10 / 0 # Error is caught in the except block
    except ZeroDivisionError:
        print("Error handled")
```

Error is caught locally.

Program behaves safely.

----------

## 6. Why Avoid `time.sleep()`?

Using: `time.sleep()` in Tkinter freezes the GUI. Instead: `after()`
keeps GUI responsive.

----------

## Script — Unsafe vs Safe `after()` Callback

```python

import tkinter as tk
from tkinter import messagebox
import logging
import sys

# 1. LOGGING SETUP
# Save errors to file named 
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

# 2. CREATE WINDOW
root = tk.Tk()
root.title("after() Callback Demo")
root.geometry("450x350")

# 3. CREATE LOG PANEL
# Shows execution steps.
log_box = tk.Text(root, height=10, width=50)
log_box.pack(padx=10, pady=10)

# 4. write_log()
# Prints message inside GUI.
def write_log(message):
    # Add message to log panel in the GUI window at the end
    log_box.insert(tk.END, message + "\n")
    # Auto-scroll to latest line. Without this, the log would keep adding lines
    # but the user would not see them unless they manually scroll down.
    log_box.see(tk.END)

# 5. GLOBAL ERROR HANDLER
# Catches uncaught errors.
def handle_uncaught(exc_type, exc_value, exc_traceback):
    # Create readable error message named error_msg from the error details.
    error_msg = (f"{exc_type.__name__}: "f"{exc_value}")
    # Show steps in log panel in the GUI window.
    write_log("Global hook activated")
    # Also save error to file named error_log.txt using logging.error()
    write_log(f"ERROR → {error_msg}")
    # logging.error() saves the error message to the file named error_log.txt we set 
    # up in logging.basicConfig() at the beginning of the code.
    logging.error(error_msg)
    # Update log panel to show that error was saved to file.
    messagebox.showerror("Unexpected Error", error_msg)
    # Also show error in terminal for debugging purposes. 
    print(error_msg)  # 

# 6. OVERRIDE DEFAULT ROUTE
# Normally: Error→ Traceback→ Program crashes
# We replace that route with OUR function named handle_uncaught. 
# sys.excepthook is the function Python calls when an error is not caught by any try-except block. 
# By assigning our handle_uncaught function to sys.excepthook, we ensure that any uncaught error 
# will be handled by our custom function instead of crashing the program. 
# sys.excepthook takes parameters exc_type, exc_value, exc_traceback which contain details 
# about the error that occurred.
sys.excepthook = (handle_uncaught)
# Update log panel to show that global hook is active.
write_log("Global hook installed")

# 7. UNSAFE CALLBACK
# No try-except.
# Global hook catches error.
def unsafe_task():
    write_log("Unsafe task running...")
    result = 10 / 0

def start_unsafe():
    write_log("Unsafe task scheduled")
    # After 2 seconds, this will call unsafe_task which will raise a ZeroDivisionError. 
    # Since there is no try-except block, it will be caught by our global handler 
    # instead of crashing the program. So even though this will raise an error, 
    # the program will not crash. The log panel will show "Global hook activated" and 
    # "ERROR → ZeroDivisionError: division by zero". A popup will also appear showing 
    # the error message. Additionally, the error will be saved to the file named 
    # error_log.txt because of the logging.error() call in our global handler.
    # This happened because we assigned our handle_uncaught function to sys.excepthook, 
    # which is the function Python calls when an error is not caught by any try-except block.
    root.after(2000, unsafe_task)  

# 8. SAFE CALLBACK
# Error handled locally with try-except. No error reaches global handler.
def safe_task():
    write_log("Safe task running...")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        write_log("Error handled locally")
        messagebox.showwarning("Handled Error", "Division by zero")

def start_safe():
    write_log("Safe task scheduled")
    root.after(2000, safe_task)  # After 2 seconds, this will call safe_task which will raise a ZeroDivisionError. However, since there is a try-except block that catches the error, it will be handled locally and will not reach the global handler. The log panel will show "Error handled locally" and a warning popup will appear, but there will be no entry in the error_log.txt file since the error was not uncaught.

# 9. BUTTONS
# Button "Unsafe after() Error" Trigger unsafe task. Global hook will catch error. 
# Program does NOT crash, but error is logged and popup shown.
tk.Button(root, text="Unsafe after() Error", command=start_unsafe).pack(pady=5)
# Button "Safe after() Error" Trigger safe task. Error handled locally.
# No error reaches global hook. No log entry. Popup shows handled message.
tk.Button(root, text="Safe after() Error", command=start_safe).pack(pady=5)

# 10. START GUI
root.mainloop()

```

## Flowchart
The flowchart shows the steps in the execution of above script:

![Unsafe vs Safe after Callback](/resources/ch14-tkinter-safe-unsafe-after.png)

















