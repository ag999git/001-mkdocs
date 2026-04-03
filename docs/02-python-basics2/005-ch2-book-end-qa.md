


## **a. What is the difference between a numeric literal and a numeric variable?**

### Answer:

-   A **numeric literal** is an actual number written _directly_ in the program.
    
-   A **numeric variable** is a _name_ that refers to a number stored in memory.
    

### Example:

```python

x = 42  # x is a numeric variable
# 42 is a numeric literal

``` 

----------

## **b. How does one convert a number to a string?**

Use the built-in **`str()`** constructor.

```python

num = 55
text = str(num)
print(text) # Output: '55'
print(type(text)) # Output: <class 'str'>

``` 

----------

## **c. How does one modify a string in place?**

### **Answer:**

You **cannot** modify a string in place because **strings are immutable**.

To “modify” a string, you must create a **new** one.

### Example:


```python

s = "hello"
# s[0] = "H"
# TypeError: strings are immutable
# Correct way:
s = "H" + s[1:]
print(s) # "Hello"

``` 

----------

## **d. Best practices for using `import` in a module + Recommended import order**

### **Recommended order (PEP 8):**

1.  **Standard library modules**
    
2.  **Third-party modules** (installed via pip)
    
3.  **Local/project modules**
    

### Example:

```python

# 1. Standard library
import os
import sys
# 2. Third-party libraries
import numpy as np
import requests
# 3. Local modules
import my_utils
import student_database

``` 

### Additional Best Practices:

-   Avoid `from module import *`
    
-   Use explicit imports for clarity
    
-   Group imports at the **top of the file**
    
-   Keep imports alphabetically sorted (optional but recommended)
    

----------

## **e. Explain type casting, implicit & explicit casting, narrow & wide casting. Give example of data loss.**

### **Type Casting**

Converting one data type to another.

----------

### **Explicit Casting** (done by programmer)

```python

x = "123"
y = int(x)
# Explicit cast string → int

``` 

----------

### **Implicit Casting** (done automatically by Python)

```python

x = 5  # x is of type int
y = 2.0  # y is float 
float z = (x + y)
# x remains as 5 ie an int
# But in the expression (x + y), x is promoted to float first and then added to y 
print(z) # Gives a float 7.0

``` 

----------

### ** Give example of Narrow Casting (possible data loss)**

```python
val = int(9.78)
print(val) # 9 → decimal part lost

``` 

----------

### **Wide Casting (no data loss)**

```python
val = float(5)
print(val) # 5.0

``` 

----------

## **f. What is the type of data when you divide an integer by another integer?**

### **Always → float**

`print(type(7 / 2)) # <class 'float'>` 

----------

## **g. What are circular dependencies and circular imports?**

### **Circular dependency**

Module A requires Module B  
Module B requires Module A

### **Circular import example:**

`a.py`

```
import b    # importing b in a.py
```

`b.py`

```python
import a    # importing a in b.py
``` 

This causes Python to get stuck during import.

### **Avoid by:**

-   Moving imports inside functions
    
-   Redesigning modules
    
-   Combining modules
    

----------

## **h. What are command-line applications? How do you run them? Examples?**

### **Answer:**

A **command-line application** is a program executed in a terminal window.

Examples:

-   `pip`
    
-   `python`
    
-   `git`
    
-   `conda`
    
-   `ipconfig` / `ping`
    

----------

### **Run in Anaconda Prompt:**

`python myscript.py`

```python
pip install numpy
``` 

----------

### **Run in Jupyter Notebook:**

Prefix commands with `!`

```python
!pip install numpy
!python myscript.py
``` 

----------

## **i. What is the value of the None type data type?**

`None` represents **no value**, **empty**, or **missing data**.

`x = None  print(type(x)) # <class 'NoneType'>` 

----------

## **j. Sequenced vs Non-sequenced containers in Python**

### **Sequenced Containers**

-   Order is maintained
    
-   Items can be accessed by index
    

Examples:

-   `list`
    
-   `tuple`
    
-   `str`
    
-   `range`
    

### **Non-sequenced Containers**

-   No inherent ordering
    
-   Cannot access by index
    

Examples:

-   `dict`
    
-   `set`
    

----------

## **k. Why can we think of a tuple as a “read-only list”?**

Because:

-   Tuples are ordered like lists 
-   Tuples support indexing 
-   Tuples support iteration 
-   But tuples **cannot be modified  → immutable**
    

----------

## **l. Why must dictionary keys be unique?**

Because dictionaries look up values by **key**, and lookup must return **exactly one** value.

If duplicate keys existed:  
Python wouldn’t know which value to return.

----------

## **m. Why is a Python dictionary called a “mapping”?**

Because it **maps**:

`key →  value` 

Just like mathematical mapping:

`f(x) = y` 

----------

## **n. Why can’t you get a key from a value in a dictionary?**

Because:

-   Values may **not be unique**
    
-   Reverse lookup would be **ambiguous**
    
-   Values do not have to be hashable or searchable
    

### Example:

`d = {"a": 10, "b": 10}` 

Which key corresponds to value 10?  
There are **two** values of 10 each → ambiguous.

----------

## **o. What are mutable and immutable objects?**

### **Mutable objects** (can change)

-   `list`
    
-   `dict`
    
-   `set`
    

`lst = [1,2]
lst.append(3) # allowed` 

----------

### **Immutable objects** (cannot change)

-   `int`
    
-   `float`
    
-   `str`
    
-   `tuple`
    

`s = "hello"  # s[0] = "H"   # ❌ Not allowed` 

----------

## **p. What do “modular programming” and “runnable code” mean?**

### **Modular Programming**

Breaking a big program into smaller reusable files called **modules**.

### **Runnable Code**

Code that executes immediately when a module is imported.

Example:

Suppose you have a file:-
`mymodule.py`
whose contents are as follows:-
```python
# Inside mymodule.py
print("Hello World!")
```
Now in another file say `test.py` you import the module `mymodule.py` as follows:-
```python
# Inside test.py
import mymodule
```
The moment you import `mymodule`, the line `print("Hello World!") will be executed and you will get an output as follows:-
`Hello World!`



----------

## **q. Difference between attributes/methods of a module vs normal variables/functions**

### **Inside a module:**

```python
import math
print(math.pi) # pi is attribute of math module
print(math.sqrt(25)) # sqrt() is method of math module
```

### **Difference:**

-   They are _namespaced_ → accessed using dot notation
-   Loaded through import system
-   Can be in separate files
    
Normal variables and functions exist only within the program where they're defined.

----------

## **r. Difference between literal string and string variable**

### Literal string:

`"Hello    # literal string"` 

### String variable:

`msg = "Hello"    # msg is a string variable` 

Both are strings — difference is just **how they appear in code**.

----------

## **s. Explain positive and negative indexing in strings. What does index -1 mean?**

### **Positive indexing** (left → right)

```python
H e  l  l  o
0 1  2  3  4
``` 

### **Negative indexing** (right → left)

```python
 H  e  l  l  o
-5 -4 -3 -2 -1
``` 

-   Index `-1` → **last character**
    

```python
s = "Hello"
print(s[-1]) # gives o which is the last character at index [-1]
``` 

----------

## **t. What are binary literals in Python?**

Numbers written with prefix **`0b`** or **`0B`**.

```python
print(0b1010) # 10
print(bin(10)) # '0b1010'    # So binary 0b1010 is same as decimal 10
``` 

----------

## **u. What is “dead code” or “unreachable code”?**

Code that **will never execute**.

Example:

```python
def  f():
    return
    print("I will never run") # dead code
``` 

----------

## **v. What is the `pip` command used for?**

### **pip = Python Package Installer**

Used to install, update, and remove Python packages.

Examples:

```python
pip install numpy
pip install requests
pip uninstall pandas
pip list
``` 

----------
