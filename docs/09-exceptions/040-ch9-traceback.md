




## PROJECT: Study of Exceptions using `sys` and `traceback`



### RESEARCH QUESTION: “How does Python internally represent exceptions, and how can the `sys` and `traceback` modules be used to extract, analyze, and present detailed information about errors?”



### Details of the problem:

1.  What is an **exception object**
2.  Role of:
    -   `sys.exc_info()`
    -   `traceback` module
3.  Structure of:
    -   Exception type
    -   Exception value
    -   Traceback object
4.  How Python builds a **stack trace**
5.  Difference between:
    -   Basic error message (`str(e)`)
    -   Full traceback
6.  Practical uses:
    -   Debugging
    -   Error reporting

----------

## ANSWER

### 1. Exception Representation in Python

-   Exceptions are **objects created from classes**
-   When an error occurs:
    -   Python creates an **exception object**
    -   Stores:
        -   Type
        -   Message
        -   Traceback

----------

### 2. sys.exc_info()
`sys.exc_info()` gives a tuple of 3 components in form of a tuple as shown below:
`(type, value, traceback) =  sys.exc_info()`


  The meaning of each component is shown in table below:

| Component | Meaning |
| --- | --- |
| Type | Exception class |
| Value | Exception object |
| Traceback | Call stack info |




### 3. traceback Module

-   It is used to extract and format stack traces

### Important Functions of traceback module are:

  

| Function | Purpose |
| --- | --- |
| extract_tb() | Structured traceback |
| format_exc() | Full formatted string |
| print_exc() | Print traceback |


### 4. Stack Trace Concept

-   A stack trace shows:
    -   Sequence of function calls
    -   Where error occurred



### 5. Basic vs Detailed Error
`str(e)` cannot give as much details as the `traceback` module. The difference beyween the two is shown in table below:
  

| Feature | str(e) | traceback |
| --- | --- | --- |
| Detail level | Low | High |
| Shows location | No | Yes |
| Shows call stack | No | Yes |

## PART 2: SCRIPT QUESTION

> Write a Python program that:
> 
> 1.  Defines at least **two nested functions**
> 2.  Intentionally generates an exception (e.g., division by zero)
> 3.  Uses:
>     -   `try-except`
>     -   `sys.exc_info()`
>     -   `traceback.extract_tb()`
> 4.  Prints:
>     -   Exception type
>     -   Exception message
>     -   File name
>     -   Line number
>     -   Function name
>     -   Code line causing error
> 5.  Also prints the **full formatted traceback**
> 6.  Ensures program continues after handling the exception



## SCRIPT (ANSWER)

```python

import sys
import traceback

# Function 1 calls Function 2, which calls Function 3 where the error occurs.
def level1():
    print("1. Inside level1()")
    level2()

# Function 2
def level2():
    print("2. Inside level2()")
    level3()

# Function 3 (Error occurs here)
def level3():
    print("3. Inside level3()")
    x = 10 / 0   # ZeroDivisionError

# Main execution
try:
    print("1. Starting program")
    level1()

except Exception as e:
    print("4. Exception caught in except block")

    # Get exception details using sys.exc_info()
    e_type, e_value, e_tb = sys.exc_info()

    print("Type:", e_type)  # Output: <class 'ZeroDivisionError'>
    print("Message:", e_value)  # Output: division by zero

    # -------- Structured Traceback --------
    print("5. Extracted Traceback Details:")
    # traceback.extract_tb() returns a list of FrameSummary objects 
    # representing the call stack at the point where the exception occurred.
    tb_list = traceback.extract_tb(e_tb)  
    print("6. Printing traceback details for each frame:")
    for frame in tb_list:  # Each frame contains details about the file, line number, function name, and code text
        filename, lineno, func_name, text = frame
        print("File:", filename)  # Output: the file name where the error occurred
        print("Line:", lineno)  # Output: the line number where the error occurred
        print("Function:", func_name)  # Output: the function name where the error occurred
        print("Code:", text)  # Output: the line of code that caused the error
        print("-" * 40)

    # -------- Full Traceback --------
    print("7. Full Traceback:")
    print(traceback.format_exc())  # Output: full traceback as a string

finally:
    print("8. Program continues after exception handling")

```



## PART 3: EXPLANATION OF SCRIPT**

----------

### Execution Flow

1.  `level1()` → calls `level2()`
2.  `level2()` → calls `level3()`
3.  `level3()` → error occurs
4.  Control jumps to `except`
5.  Exception info is extracted and displayed


### Key Concepts Explained

#### A. Nested Calls

-   Creates a **call stack**
-   Helps demonstrate traceback clearly

----------

#### B. `sys.exc_info()`

-   Captures:
    -   Type → `ZeroDivisionError`
    -   Value → message
    -   Traceback → execution path

----------

#### C.  `traceback.extract_tb()`

-   Breaks traceback into:
    -   File
    -   Line
    -   Function
    -   Code

----------

#### D. `traceback.format_exc()`

-   Gives **complete formatted traceback**

----------

### PART 4: COMPARISON TABLES

----------

### **`sys` vs `traceback`**

  

| Feature | sys.exc_info() | traceback |
| --- | --- | --- |
| Output type | Tuple | Structured / formatted |
| Detail level | Medium | High |
| Ease of use | Moderate | Easy to display |
| Use case | Internal inspection | Debugging |


**Types of Exception Information**

  

| Level | Tool | Output |
| --- | --- | --- |
| Basic | `str(e)` | Message |
| Medium | `sys.exc_info()` | Type + object |
| Detailed | `traceback` | Full call stack |
























