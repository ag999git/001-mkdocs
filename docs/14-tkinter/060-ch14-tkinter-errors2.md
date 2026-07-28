




# Research / Project Question

## Tkinter Delayed Tasks, Safe Callbacks and Multiple Windows

In many GUI applications, some tasks do not run immediately. Instead, they run **after a delay**.

Examples:

```python
Show reminder after 5 seconds
Auto-save after some time
Load data after startup
Display notification later
```

Tkinter provides the: `after()` method for scheduling delayed actions.

However, delayed tasks may sometimes fail and cause errors. Therefore, programmers must use **safe callbacks** with proper **error handling**.

Tkinter also allows programs to open **multiple windows** using: `toplevel()` instead of creating multiple `Tk()` windows.

----------

## Project Objectives

Research and explain how Tkinter handles:

1.  Delayed execution using `after()`
2.  Safe callbacks using `try-except`
3.  Additional windows using `Toplevel()`
4.  Error handling in delayed tasks

----------

## Part A — Theory. Research and explain the following:

### 1. `after()` Method

Explain:

-   What is `after()`?
-   Why is it useful in GUI applications?
-   Syntax of `after()`
-   Difference between:

```
root.after(2000, func)
```

and:

```
time.sleep(2)
```

Why is `after()` preferred in Tkinter?

### 2. Callback Functions

Explain:

-   What is a callback function?
-   Why does `after()` require a callback?
-   Give one practical example.


### 3. Safe Delayed Callback

Explain:

-   Why delayed tasks may fail
-   Why `try-except` should be used
-   How user-friendly error handling improves GUI programs

----------

### 4. `Toplevel()` Window

Explain:

-   Purpose of `Toplevel()`
-   Difference between `Tk()` and `Toplevel()`
-   Why multiple `Tk()` windows are not recommended

----------

### 5. Best Practices

Write at least **five rules/best practices** for using:

```
after()
Toplevel()
safe callbacks
```

----------

## Part B — Script Writing

Write a Tkinter program that performs the following:

### Main Window

The main window must contain:

1.  A heading label.
2.  A button named:

```
Open Task Window
```

### Child Window (`Toplevel()`)

When the button is clicked:

1.  A new `Toplevel()` window must open.
2.  It should contain:

    -   an `Entry` widget,
    -   a button: `Start Delayed Task`

3.  User enters a number.

----------

### Delayed Processing (`after()`)

When button is clicked:

1.  Program waits **3 seconds** using: `after()`

2.  Then processes the entered value.

----------

### Safe Callback Requirements

The delayed task must:

-   safely convert input to integer,
-   use `try-except`,
-   show error message for invalid input,
-   show success message for valid input.

----------

### Input Rules

Valid: `0–100`

Invalid: `lettersnegative valuesnumbers above 100empty input`

----------

### Output Requirements

Valid input: `Success message appears`

Invalid input: `Friendly error message appears`

The GUI must never crash.

----------

## Theory Answer

### 1. `after()` Method

The `after()` method is used to run a function after a specified delay.

### Syntax

```python
widget.after(milliseconds,function_name)
```

Example:

```python
root.after(3000, task)
```

This runs: `task()` after **3000 milliseconds (3 seconds)**.

### Why Not `time.sleep()`?

Because `time.sleep()` freezes the GUI.

But: `after()` keeps the GUI responsive.


## 2. Callback Functions

A callback function is a function passed to another function and executed later.

Example: `root.after(3000, process_data)`

Here: `process_data` is the callback.



## 3. Safe Delayed Callback

Delayed tasks may fail due to:

```python
invalid input
missing data
runtime errors
```

Therefore: `try-except`  should be used. Instead of crashing, the program shows: `friendly messagebox error`



## 4. `Toplevel()`

`Toplevel()` creates an additional child window.

Example: `win = tk.Toplevel(root)`

Only **one `Tk()` window** should normally exist.

Additional windows should use: `Toplevel()`

----------

## Best Practices

1.  Prefer `after()` over `time.sleep()` in Tkinter.
2.  Always use `try-except` in delayed tasks.
3.  Use `Toplevel()` for extra windows.
4.  Validate input before processing.
5.  Show friendly errors using `messagebox`.

----------

# Model Script Solution

```python

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()  # Create main window
root.title("Delayed Task Demo")
root.geometry("300x180")

# Open child window
def open_window():
    # Create Toplevel window
    win_top = tk.Toplevel(root)
    win_top.title("Task Window")
    win_top.geometry("280x180")

    tk.Label(win_top, text="Enter a number (0-100)").pack(pady=5) # Label widget
    entry = tk.Entry(win_top) # Entry widget for user input
    entry.pack(pady=5)

    status = tk.Label(win_top, text="Waiting...") # Status label to show messages
    status.pack(pady=5)
    # Safe delayed task
    def process_number():  # Function to run after delay
        try:
            num = int(entry.get()) # Convert input to integer
            if num < 0: # Raise error for negative numbers
                raise ValueError("Negative number not allowed")
            if num > 100: # Raise error for numbers greater than 100
                raise ValueError("Number must be ≤ 100")

        except ValueError as e:
            # Show error message
            messagebox.showerror("Error", str(e))

            status.config(text="Invalid input")

        else:
            messagebox.showinfo("Success", f"Number = {num}")  # Success message

            status.config(text="Task completed")

    # Schedule delayed task
    def start_task():
        status.config(text="Waiting 3 seconds...")

        # Run function after 3 sec
        win_top.after(3000, process_number)

    # Start button
    tk.Button(win_top, text="Start Delayed Task", command=start_task).pack(pady=10)

# Main button
tk.Button(root, text="Open Task Window", command=open_window).pack(pady=40)

root.mainloop()

```









