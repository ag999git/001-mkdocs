

### Task 1 — Investigate a Real Python Library Function

The plotting function in **Matplotlib** has the following simplified form:

`plot(x, y, *args, **kwargs)`

#### Research Question

Explain why the designers of Matplotlib chose to use `*args` and `**kwargs` in this function instead of defining a very long list of parameters.

Your explanation should address the following points:

1.  What are the **mandatory arguments** in `plot()`?
2.  What types of values can be passed using **`*args`**?
3.  What types of options are typically passed using **`**kwargs`**?
4.  Why is this design useful when a library **adds new features in later versions**?
5.  How does this design help **old programs continue to run without modification**?


#### Model Answers Task 1 — Investigate a Real Python Library Function

You can access Matplotlib documentation [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

Function signature (simplified):

`plot(x, y, *args, **kwargs)`

#### A. Mandatory arguments of the function

The **mandatory arguments** of the function are:

-   `x` → list/array of x-coordinates
    
-   `y` → list/array of y-coordinates
    

Example:

`plt.plot(x, y)`

These specify the **data points that must be plotted**. If you dont provide the data points, then obviously, the points cannot be plotted

----------

#### B. What can be passed using `*args`

`*args` allows additional **positional arguments**.

In Matplotlib, these are usually **formatting strings** that control:

-   color
    
-   marker style
    
-   line style
    

Example:

`plt.plot(x, y, "ro--")`


  
Meaning: 

| Symbol | Meaning |
| --- | --- |
| r | red color |
| o | circle marker |
| -- | dashed line |

So `*args` allows **compact style specifications**.

But providing *args is optional. If you dont provide any *args, then the library will use the default values

#### C. What can be passed using `**kwargs`

`**kwargs` allows **keyword arguments** for many optional settings.

Examples:

`plt.plot(x, y, color="green", linewidth=3, marker="o")`

Common keyword parameters include:

  

| Parameter | Purpose |
| --- | --- |
| color | Line color |
| linewidth | Line thickness |
| marker | Marker shape |
| linestyle | Line pattern |
| label | Legend label |

These options make the plot **highly customizable**.

----------

#### D. Why this design helps when libraries add new features

If a library developer adds a new option such as:

`alpha=0.5`

the function can still accept it through `**kwargs`.

Old code like:

`plt.plot(x,y)`

continues to work without modification.

Thus `**kwargs` allows **future extension of the library**.

----------

#### E. How this helps backward compatibility

Backward compatibility means **old programs continue to run after library updates**.

Example: Old program:

`plt.plot(x,y)`

Later library version adds new parameter:

`plt.plot(x,y,alpha=0.7)`

Old programs still work because the new parameters are **optional keyword arguments stored in `**kwargs`**.





### Task 2 — Documentation Investigation


Visit the official Matplotlib documentation for:


`matplotlib.pyplot.plot()`	

You can access Matplotlib documentation [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

Find and list **five keyword arguments** that can be passed to the function.

Example format:



| Keyword Argument | Purpose |
| --- | --- |
| color | Sets line color |
| linewidth | Sets thickness |
| marker | Controls point markers |
| linestyle | Controls line style |
| label | Text for legend |

#### Model solution Task 2 — Documentation Investigation

Example keyword arguments for `matplotlib.pyplot.plot()`:


| Keyword Argument | Purpose |
| --- | --- |
| color | Sets the color of the line |
| linewidth | Controls thickness of the line |
| marker | Specifies the marker symbol |
| linestyle | Defines the pattern of the line |
| label | Provides a label used in the legend |
| alpha | Controls transparency |
| markersize | Size of markers |
| markerfacecolor | Color inside markers |

Example usage:

`plt.plot(x, y, color="red", linewidth=2, marker="o")`

----------
### Task 3 — Programming Experiment

Write a Python program that calls `plot()` in **three different ways**:

1.  Using only **mandatory arguments**
    
2.  Using **`*args` formatting string**
    
3.  Using **`**kwargs` options**
    

Example template:

```python

import  matplotlib.pyplot  as  plt  
  
x  = [1,2,3,4]  
y  = [1,4,9,16]  
  
# Case 1: Mandatory arguments only  
plt.plot(x,y)  
  
# Case 2: Using *args formatting  
plt.plot(x,y,"ro--")  
  
# Case 3: Using **kwargs  
plt.plot(x,y,color="green",linewidth=3)  
  
plt.show()
```

Explain how each version changes the appearance of the plot.
#### Model solution Task 3 — Programming Experiment

Example script:

```python

import  matplotlib.pyplot  as  plt  
  
x  = [1,2,3,4]  
y  = [1,4,9,16]  
  
# Case 1: Mandatory arguments only  
plt.plot(x, y)  
  
# Case 2: Using *args formatting string  
plt.plot(x, y, "ro--")  

# Case 3: Using **kwargs  
plt.plot(x, y, color="green", linewidth=3)  
  
plt.show()
```

##### Explanation

| Case | Code | Result |
| --- | --- | --- |
| 1 | plt.plot(x,y) | Default blue line |
| 2 | plt.plot(x,y,"ro--") | Red dashed line with circle markers |
| 3 | plt.plot(x,y,color="green",linewidth=3) | Thick green line |

Observations:

-   `*args` provides **short style formatting**
    
-   `**kwargs` provides **detailed customization**
    

----------
### Task 4 — API Design Thinking

Suppose you are designing a library function for plotting data.

You could define the function in two ways.

##### Version A (Rigid)

`def  plot(x, y, color="blue", linewidth=1, marker=None,  
  linestyle="-", label=None, grid=False):`

##### Version B (Flexible)

`def  plot(x, y, *args, **kwargs):`

##### Question

Explain why **Version B is often preferred in large libraries** ?.

Discuss the following:

-   flexibility
    
-   future extension
    
-   backward compatibility
    
-   readability of documentation




#### Model Solution Task 4 — API Design Thinking

Two possible designs:

##### Version A (Rigid)


```python

def  plot(x, y, color="blue", linewidth=1, marker=None,  
  linestyle="-", label=None, grid=False):

```

##### Version B (Flexible)

`def  plot(x, y, *args, **kwargs):`

----------

##### Why Version B is preferred in large libraries

  

  

| Feature | Version A | Version B |
| --- | --- | --- |
| Flexibility | Limited | Very high |
| Future extension | Difficult | Easy |
| Backward compatibility | Harder | Easier |
| Parameter count | Fixed | Unlimited |



### Task 5: Endianness in Computer Systems
In computer architecture, endianness refers to the order in which bytes are stored in memory when representing multi-byte data such as integers. Two common conventions are: (1) Big-endian – the most significant byte (MSB) is stored first. (2) Little-endian – the least significant byte (LSB) is stored first.
Your Tasks:- (1) Study the concepts big-endian and little-endian byte ordering. (2) Explain the difference between these two formats with the help of a small example (for instance, how the number 0x12345678 would be stored in memory). (3) Use Python to determine the endianness of your computer system using the sys module. (4) Write a short Python script that: (a) Prints the system’s byte order. (b) Demonstrates how a number is stored in both little-endian and big-endian formats.
Hint: The sys module contains an attribute called byteorder.

#### Answer

The `sys` module contains an attribute called `byteorder`.

`sys.byteorder`

Possible values are:

`"little"`  
`"big"`


#### A. Conceptual Explanation

When computers store numbers larger than one byte, they must decide **which byte goes first in memory**.

Suppose we want to store the **32-bit hexadecimal number**

`0x12345678`

This number contains **4 bytes**:

12   34   56   78

#### B. Big-Endian Representation

In **big-endian systems**, the **most significant byte is stored first**.

Memory order:

`12   34   56   78`

This format is sometimes called **network byte order** and is commonly used in network protocols.

----------

#### C. Little-Endian Representation

In **little-endian systems**, the **least significant byte is stored first**.

Memory order:

`78   56   34   12`

Most modern processors such as **Intel x86 and AMD** use **little-endian format**.

----------

#### D. How to Detect Endianness in Python

Python provides the attribute:

`sys.byteorder`

This returns either:

`"little"`

or

`"big"`

depending on the architecture of the computer.

----------

#### E. Python Demonstration Script

This script demonstrates both the **system byte order** and **how integers are stored in different endian formats**.

```python

# Demonstration of Endianness in Python

import sys

print("System Byte Order:", sys.byteorder)  # Shows the byte order of the system (either 'little' or 'big')
print("-" * 40)

# Example integer (32-bit number)
number = 0x12345678

print("Original number (hex):", hex(number))

# Convert integer into bytes using big-endian format
big_endian_bytes = number.to_bytes(4, byteorder='big')  # 4 bytes for a 32-bit integer

# Convert integer into bytes using little-endian format
little_endian_bytes = number.to_bytes(4, byteorder='little')  # 4 bytes for a 32-bit integer

print("Big-endian byte order:")  # In big-endian, the most significant byte (MSB) is stored first.
print(list(big_endian_bytes))  # Output will show the byte values in big-endian order

print("Little-endian byte order:")  # In little-endian, the least significant byte (LSB) is stored first.
print(list(little_endian_bytes))  # Output will show the byte values in little-endian order

# Display hexadecimal representation
print("Big-endian (hex):", big_endian_bytes.hex())  # Hexadecimal representation of big-endian bytes
print("Little-endian (hex):", little_endian_bytes.hex())  # Hexadecimal representation of little-endian bytes


```

### 6. Research Task: Implementing a Pseudo Random Number Generator in Python

Most programming languages provide built-in functions for generating random numbers. However, these numbers are not truly random; they are generated using algorithms called **Pseudo Random Number Generators (PRNGs)**. One of the earliest and simplest PRNG algorithms is the **Linear Congruential Generator (LCG)**. The algorithm generates a sequence of integers using the recurrence relation:

$$
X_{n+1} = (a \cdot X_n + c) \pmod m
$$

**Where:**
* $X$ is the sequence of pseudorandom values.
* $a$ is the multiplier, where $0 < a < m$.
* $c$ is the increment, where $0 < c < m$.
* $X_0$ is the start value (the seed).
* $m$ is the modulus.

Typical parameter values used in many systems are: 
(1) m = 2^31 
(2) a = 1103515245 
(3) c = 12345

(This problem uses OOP concept of Class, so you may do this after studying the chapter on OOP)

**Your Tasks: 
- (1)** Study the concept of **Pseudo Random Number Generators (PRNG)**. 
- (2) Understand how the **Linear Congruential Generator (LCG)** produces a sequence of numbers. 
- (3) Write a **Python class** that: 
    - (a) Stores the seed value. 
    - (b) Generates the next pseudorandom number using the LCG formula. 
- (4) Add a method that **scales the result to a floating-point number between 0 and 1**. 
- (5) Demonstrate the generator by printing the first **few values of the sequence**.

**Questions to Think About: (1)** What happens if the **seed value changes**? (2) Why are these numbers called **pseudo-random** instead of truly random?

#### Script which implements this task

Given below is a script which implements this task


```python

# Linear Congruential Generator (LCG)
# A simple pseudo-random number generator algorithm


class LinearCongruentialGenerator:
    """
    This class implements the Linear Congruential Generator algorithm.

    Formula:
        X(n+1) = (a * X(n) + c) mod m

    where:
        X(n) = current state (seed)
        a    = multiplier
        c    = increment
        m    = modulus
    """

    def __init__(self, seed=1):
        """
        Constructor initializes the generator parameters
        and starting seed.
        """

        # Standard parameters used in many C libraries
        self.a = 1103515245       # multiplier
        self.c = 12345            # increment
        self.m = 2**31            # modulus

        # Initial seed (starting value)
        self.state = seed

    def next_int(self):
        """
        Generate the next pseudorandom integer.
        Updates the internal state.
        """

        # Apply LCG formula
        self.state = (self.a * self.state + self.c) % self.m

        # Return the new value
        return self.state

    def next_float(self):
        """
        Convert the generated integer into a floating-point
        number between 0 and 1.
        """

        # Generate next integer
        value = self.next_int()

        # Scale result to [0, 1)
        return value / self.m


# Demonstration of the generator
print("Demonstrating Linear Congruential Generator")

# Create generator object with a seed
lcg = LinearCongruentialGenerator(seed=123456)

print("\nFirst 5 pseudorandom integers:")

for i in range(5):
    print(f"X_{i+1} =", lcg.next_int())


# Demonstrate floating-point random numbers
print("Random numbers scaled to range [0,1):")
lcg2 = LinearCongruentialGenerator(seed=100)

for i in range(5):
    print(lcg2.next_float())


```

#### Key Concepts 

#### A. Deterministic randomness

If the **seed is the same**, the **sequence will always be the same**.

Example:

`LinearCongruentialGenerator(seed=10)`

always produces the **same sequence**.

----------

#### B. Why the generator is called "pseudo-random"

The numbers **look random**, but they are actually produced by a **deterministic formula**.

----------

#### C. Role of each parameter
The following table summarizes the role of various parameters used in the equation to generate PRNG

  

| Parameter | Role |
| --- | --- |
| seed | starting value |
| a | multiplier |
| c | increment |
| m | modulus controlling range |


### 7. Research Task: Unpacking of Iterables in Python

In Python, it is possible to **unpack elements of an iterable (such as a list or tuple) directly into variables**. Normally, the number of variables must exactly match the number of elements in the iterable.

However, Python provides a powerful feature called **Partial Unpacking** that allows one variable to collect the remaining elements of the iterable. This is done using the **asterisk (`*`) operator**, sometimes called a **star expression**.

When a variable is prefixed with `*`, it collects **all remaining unassigned elements** from the iterable.

#### A. Important Characteristics

1.  The variable prefixed with `*` collects **multiple elements**.
    
2.  The collected elements are stored as a **list**.
    
3.  Only **one starred variable** can appear in a single unpacking operation.
    
4.  The starred variable can appear **at the beginning, middle, or end** of the assignment.
    

#### B. Research Tasks

1.  Study how **iterable unpacking** works in Python.
    
2.  Explain the concept of **partial unpacking using the `*` operator**.
    
3.  Write Python examples demonstrating:
    
    -   capturing elements at the **end**
        
    -   capturing elements in the **middle**
        
    -   capturing elements at the **beginning**
        
4.  Observe the **type of the variable that collects the remaining elements**.
    

----------

#### C. Script which implements the above task


```python

# Demonstration of Partial Unpacking of Iterables in Python

# Example 1: Catching elements at the end
print("Example 1: Catching elements at the end")

# The first two variables get the first two elements
# The starred variable collects the remaining elements
first, second, *tail = [10, 20, 30, 40, 50]  # The list has 5 elements. first=10, second=20, tail=[30, 40, 50]

print("first =", first, "second =", second, "tail =", tail)  # Output will show the values of first, second, and tail

print("-----------------------------------")

# Example 2: Catching elements in the middle
print("Example 2: Catching elements in the middle")

# First variable takes the first element
# Last variable takes the last element
# Starred variable collects everything in between
start, *middle, last = [1, 2, 3, 4, 5, 6]

print("start =", start, "middle =", middle, "last =", last)

print("-----------------------------------")

# Example 3: Catching elements at the beginning
print("Example 3: Catching elements at the beginning")

# Starred variable collects elements at the beginning
*beginning, second_last, last = [100, 200, 300, 400, 500]

print("beginning =", beginning, "second_last =", second_last, "last =", last)

print("-----------------------------------")

# Example 4: Using partial unpacking with tuples
print("Example 4: Using partial unpacking with tuples")

data = (11, 22, 33, 44, 55)

a, *b = data

print("a =", a, "b =", b)
print("Type of b:", type(b))  # Always a list

print("-----------------------------------")

# Example 5: Star variable collecting zero elements
print("Example 5: Star variable collecting zero elements")

x, y, *rest = [5, 10]

print("x =", x, "y =", y, "rest =", rest)  #

```


### 8. Task: Implementing the Brute-Force String Searching Algorithm in Python

Searching for a **substring (pattern)** inside a larger **string (text)** is a common problem in computer science.

One of the simplest methods to perform this task is the **Brute-Force String Searching Algorithm**.

The algorithm works by **checking every possible alignment** of the pattern within the text.

#### Basic Idea

Suppose:

-   **Text (T)** has length **m**
    
-   **Pattern (P)** has length **n**
    

The algorithm works as follows:

1.  Align the beginning of **P** with the first character of **T**.
    
2.  Compare characters of **P** with corresponding characters of **T**.
    
3.  If all characters match → the pattern is found.
    
4.  If a mismatch occurs → slide the pattern **one position to the right**.
    
5.  Repeat until:
    
    -   the pattern is found, or
        
    -   all possible positions have been checked.
        

### Tasks

1.  Study the **Brute-Force string searching algorithm**.
    
2.  Explain how the **pattern slides over the text**.
    
3.  Write a Python function that:
    
    -   takes **text** and **pattern** as inputs
        
    -   returns the **starting index of the match**
        
    -   returns **-1 if the pattern is not found**
        
4.  Test your program with a few example strings.
    

----------

#### The following table shows how the matching takes place.
The script implementing the problem is as follows

In the following script, the text given is `text1 = "acdabcdacabcd"`
The pattern given is `pattern1 = "cdac"`



  

  

  

  

| Index | Match found? | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| String |  | a | c | d | a | b | c | d | a | c | a | b | c | d |
| Pattern (Initially 0) | No | c | d | a | c |  |  |  |  |  |  |  |  |  |
| 1 | No |  | c | d | a | c |  |  |  |  |  |  |  |  |
| 2 | No |  |  | c | d | a | c |  |  |  |  |  |  |  |
| 3 | No |  |  |  | c | d | a | c |  |  |  |  |  |  |
| 4 | No |  |  |  |  | c | d | a | c |  |  |  |  |  |
| 5 | Yes |  |  |  |  |  | c | d | a | c |  |  |  |  |




#### The script implementing the problem is as follows


```python

# Brute Force String Search Algorithm

def brute_force_search(text, pattern):
    """
    Searches for 'pattern' inside 'text' using the brute force method.

    Parameters
    ----------
    text : str
        The larger string in which we search.

    pattern : str
        The substring we want to find.

    Returns
    -------
    int
        Starting index of the pattern if found.
        Returns -1 if pattern is not present.
    """

    # Length of text and pattern
    m = len(text)  # Length of the text string
    n = len(pattern)  # Length of the pattern string

    # Try every possible alignment of pattern in text
    for i in range(m - n + 1):

        print(f"\nChecking alignment starting at text index {i}")

        match = True  # Assume match unless mismatch found

        # Compare characters one by one
        for j in range(n):  # Loop through each character in the pattern

            print(f"Comparing text[{i+j}]='{text[i+j]}' with pattern[{j}]='{pattern[j]}'")  # Show the characters being compared

            if text[i + j] != pattern[j]:  # If characters do not match
                print("Mismatch found → shift pattern to the right")
                match = False  # Set match to False if a mismatch is found
                break

        # If all characters matched
        if match:  # If we completed the inner loop without breaking, it means we found a match
            print("Pattern found!")
            return i  # Return the starting index of the pattern in the text

    # Pattern not found
    return -1


# Test Examples

text1 = "acdabcdacabcd"
pattern1 = "cdac"

result = brute_force_search(text1, pattern1)

print("\nFinal Result:")
print("Pattern found at index:", result)


```

The output to above script is 


```python

Checking alignment starting at text index 0
Comparing text[0]='a' with pattern[0]='c'
Mismatch found → shift pattern to the right

Checking alignment starting at text index 1
Comparing text[1]='c' with pattern[0]='c'
Comparing text[2]='d' with pattern[1]='d'
Comparing text[3]='a' with pattern[2]='a'
Comparing text[4]='b' with pattern[3]='c'
Mismatch found → shift pattern to the right

Checking alignment starting at text index 2
Comparing text[2]='d' with pattern[0]='c'
Mismatch found → shift pattern to the right

Checking alignment starting at text index 3
Comparing text[3]='a' with pattern[0]='c'
Mismatch found → shift pattern to the right

Checking alignment starting at text index 4
Comparing text[4]='b' with pattern[0]='c'
Mismatch found → shift pattern to the right

Checking alignment starting at text index 5
Comparing text[5]='c' with pattern[0]='c'
Comparing text[6]='d' with pattern[1]='d'
Comparing text[7]='a' with pattern[2]='a'
Comparing text[8]='c' with pattern[3]='c'
Pattern found!

Final Result:
Pattern found at index: 5


```




















