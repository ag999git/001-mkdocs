




## 1. RESEARCH QUESTION (Part 1 Discussion)

> **“How does Python represent exceptions as objects in modern versions (Python 3.x), and how can the `__traceback__` attribute along with the `traceback` module be used to analyze and present detailed error information?”**

----------

### To Study

1.  Exception as an **object**
2.  Attributes of exception:
    -   `e.args`
    -   `e.__traceback__`
3.  Difference between:
    -   `sys.exc_info()` vs `e.__traceback__`
4.  Role of:
    -   `traceback.extract_tb()`
    -   `traceback.format_exc()`
5.  Stack trace concept
6.  Practical debugging use cases

----------

## 2: ANSWER (To Part 1 Discussion)

----------

### 1. Exception as an Object

-   In Python 3:
    -   Exceptions are **objects**
    -   They contain all relevant information internally

Example:

`except  Exception  as  e:`

👉 `e` itself contains:

-   Type → `type(e)`
-   Message → `str(e)`
-   Traceback → `e.__traceback__`

----------

### 2. The `__traceback__` Attribute

-   Each exception object has:

`e.__traceback__`

### It represents:

-   The **execution path** where error occurred
-   A **linked structure of stack frames**

----------

### 3. The `traceback` Module 


#### Why we need `traceback`?

-   `__traceback__` gives **raw data**
-   `traceback` converts it into:
    -   Human-readable form
    -   Structured data



#### 4. `traceback.extract_tb()`

`traceback.extract_tb(e.__traceback__)`

#### Returns:

List of:

`(filename, line number, function name, code line)`

----------

#### 5. `traceback.format_exc()`

`traceback.format_exc()`

-   Returns full traceback as a **string**
-   Useful for:
    -   Debugging
    -   Logging




#### 6. Concept Flow


```python 
Error occurs  
 ↓  
Exception object (e) created  
 ↓  
e.__traceback__ accessed  
 ↓  
traceback.extract_tb() 
 ↓  
Structured stack trace

```



## Script Question

> Write a Python program that:
> 
> 1.  Creates at least **two nested function calls**
> 2.  Generates an exception intentionally
> 3.  Uses `except Exception as e`
> 4.  Uses:
>     -   `e.__traceback__`
>     -   `traceback.extract_tb()`
>     -   `traceback.format_exc()`
> 5.  Displays:
>     -   Exception type
>     -   Message
>     -   File name
>     -   Line number
>     -   Function name
>     -   Code causing error
> 6.  Prints full formatted traceback
> 7.  Ensures program continues after handling

----------

## PART 4: Script Answer
**Before we write the script, it is helpful to see the flow of execution and the steps involved**
The following flow shows how the script works:-

```python

Error occurs
    ↓
Exception object (e) created
    ↓
e.__traceback__  → raw traceback object
    ↓
traceback.extract_tb()
    ↓
List of frames (tb_list)
    ↓
Loop through frames
    ↓
Extract file, line, function, code
    ↓
(Optional) traceback.format_exc() → full string
```



### The actual script is as follows:

```python

import traceback

# Nested functions to create stack trace
def level1():  # Function 1 calls Function 2, which calls Function 3 where the error occurs.
    print("1. Inside level1()")
    level2()

def level2():
    print("2. Inside level2()")
    level3()

def level3():
    print("3. Inside level3()")
    return 10 / 0   # ZeroDivisionError


# Main program
try:
    print("0. Starting program")
    level1()

except Exception as e:
    print("4. Exception caught")

    # -------- Basic Info --------
    print("Type:", type(e))  # Output: <class 'ZeroDivisionError'>
    print("Message:", str(e))  # Output: division by zero

    # -------- Using __traceback__ --------
    tb = e.__traceback__  # Get the traceback object from the exception instance
    print("5. Extracted Traceback Details:")

    tb_list = traceback.extract_tb(tb)  # Extracts the traceback details into a list of FrameSummary objects

    # Loop through each frame in the traceback and print details
    # Each frame contains details about the file, line number, function name, 
    # and code text where the error occurred.   
    print("6. Printing traceback details for each frame:")
    for frame in tb_list:
        filename, lineno, func_name, text = frame  # Unpack the frame details

        print("File:", filename)  # Output: the file name where the error occurred
        print("Line:", lineno)  # Output: the line number where the error occurred
        print("Function:", func_name)  # Output: the function name where the error occurred
        print("Code:", text)  # Output: the line of code that caused the error
        print("-" * 40)

    # -------- Full Traceback --------
    # traceback.format_exc() returns the full traceback as a string, which can be printed or logged.
    # It provides a complete traceback including all the frames and the error message, similar to what 
    # you see when an unhandled exception occurs.
    # This is useful for debugging and logging purposes, as it gives you the full context of the error.
    print("7. Full Traceback:")
    print(traceback.format_exc())  # Output: full traceback as a string

finally:
    print("8. Program continues after exception handling")

```



## PART 5: EXPLANATION OF KEY STEPS



### 1. Nested Functions

-   Create a **call stack**
-   Helps demonstrate traceback clearly

----------

### 2. Exception Object

`except  Exception  as  e:`

-   `e` stores everything

----------

### 3. traceback

`tb  =  e.__traceback__`

-   Raw traceback object
-   `__traceback__` is an attribute of the exception object referenced by `e`

----------

### 4. `extract_tb()`

-   Converts `__traceback__` into readable structure

----------

### 5. `format_exc()`

-   Gives full error trace (like Python error screen)

----------

## PART 6: Comparison Tables

----------

### Three Levels of Exception Handling

  

  

| Level | Tool | Output |
| --- | --- | --- |
| Basic | str(e) | Message |
| Intermediate | e.__traceback__ | Raw traceback |
| Advanced | traceback module | Structured + formatted |


### traceback Functions Comparison

| Function | Output | Use Case |
| --- | --- | --- |
| extract_tb() | Structured list | Analysis |
| format_exc() | Full string | Logging |
| print_exc() | Direct print | Quick debugging |







#### Key Insight

-    `__traceback__` gives the raw path,
-    `traceback` module makes it readable.



