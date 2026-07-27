

### How Does Python’s re Module Expose Pattern and Match Types Without Defining Them? 
>This is a very advanced concept and exercise and not required to be studies by beginners.


We may call this exercise as:- The Mystery of the "Missing" Classes

This exercise will help you to understand how the re module of Python:-
-   Exposes **public APIs** over **private C implementations**
    
-   Uses **aliases** to hide internal classes
    
-   Distinguishes between **classes** and **objects**
    
-   Uses `__all__` to define what is public

##### Introduction & Context

 - In Python, we are taught that to use a class, it must be defined
   somewhere using the `class` keyword (e.g., `class MyClass:`). 
 - If you check the documentation for the `re` module, you will see references to two very important classes: **`re.Pattern`** and **`re.Match`**.
 - However, there is a technical problem: These classes are actually implemented in **C code** within the internal `_sre` engine. 
 - Because they are compiled binaries, they don't have a standard Python source code representation that you can simply "import" like a normal `.py` file.

##### The Challenge

Despite not having a `class` definition in Python, the `re` module successfully exposes these names. If you type `print(re.Pattern)` in your terminal, it works! If you use `isinstance(obj, re.Pattern)`, it works!

**Your Goal:** Investigate the `re` module's source code to discover how the developers "manufactured" these class names out of thin air.


[Link to source code of `__init__()__` file of re module](https://github.com/python/cpython/blob/main/Lib/re/__init__.py)

(Can click this also: https://github.com/python/cpython/blob/main/Lib/re/__init__.py  )
----------

#### How to study this

##### **Step 1: The Namespace Mystery**

Run the following code in your Python interpreter:

Python

```python
# Demonstration of re.Pattern and re.Match types in Python's re module
import  re

# Create Pattern and Match objects
pattern = re.compile(r'\d+')
match = pattern.match('123') 

# 1. Print the objects and confirm that they are of the correct types
print("Pattern object:", pattern) # Output: Pattern object: re.compile('\\d+')
print("Match object :", match) # Output: Match object : <re.Match object; span=(0, 3), match='123'>

# 2. Print their types and verify they match re.Pattern and re.Match
print(type(pattern)) # Output: <class 're.Pattern'>
print(type(match)) # Output: <class 're.Match'>

# 3. Use 'is' operator to compare types
print(type(pattern) is  re.Pattern) # Output: True
print(type(match) is  re.Match) # Output: True

```

**Observation:** You will see `<class 're.Pattern'>`, and `<class 're.Match'>`, But if you search the `re.py` file for the text `class Pattern:`, or `class Match`, you will find **zero** results.

#### **Step 2: Github Research**

Navigate to the [official CPython GitHub repository](https://github.com/python/cpython/blob/main/Lib/re/__init__.py).

-   Look for the `__all__` list to confirm `Pattern` and `Match` are listed as public symbols.
    
-   Then, search the file for the lines where `Pattern` and `Match` are actually assigned their values. (Note that Pattern begins with capital P and Match begins with capital M. So do a case sensitive search)
    

##### **Step 3: Analyze the "Hack"**

Find these two specific lines in the source code:

[Link to following 2 lines in the source code ](https://github.com/python/cpython/blob/a4086d7f89e5d388e4ffcdb13e4fba0255234286/Lib/re/__init__.py#L310)

```python
Pattern = type(_compiler.compile('', 0))
Match = type(_compiler.compile('', 0).match(''))
```

----------

##### **Questions for the Student**

1.  **The Extraction:** In your own words, explain what `type(_compiler.compile('', 0))` is doing. Why did the developer use an empty string `''`?
    
2.  **The Variable vs. The Class:** In Python, we usually use lowercase for variables (`x = 10`) and Capitalized names for classes. Why did the developers use a capital **P** in `Pattern = ...` even though it looks like a variable assignment?
    
3.  **The Benefit:** Why go through all this trouble? Why didn't the developers just leave these types as hidden internal C-structures? (Hint: Think about `isinstance()` and Type Hinting).
    
4.  **The Experiment:** What happens if you try to call `re.Pattern()` directly in your code like a normal constructor? Why does it fail?
    

----------

#### The "Cheat Sheet"

-   **The Hack:** Since the perople who wrote the re module could not import the _blueprint_ (the C-class), they created a _product_ (an instance) using `_compiler.compile` and then use the `type()` function to "steal" the blueprint from that product. So in effect, they created a dummy empty Pattern object and a dummy empty Match object as follows:-
```python
Pattern = type(_compiler.compile('', 0))
Match = type(_compiler.compile('', 0).match(''))
```
- They named these objects as Pattern and Match and exposed them as public symbols through the `__all__`. So even though the class Pattern and Match are not defined in the traditional way using keyword class in the `__init__()` file of the re module. 
    
-   **Encapsulation:** This creates a **Type Alias**. It maps a friendly, public Python name (`re.Pattern`) to a cryptic, private C-name (`_sre.SRE_Pattern`). Similarly it maps a friendly public name `re.Match` to a private C-name (`_sre.SRE_Match`.)

| Internal         | Public     |
| ---------------- | ---------- |
| _sre.SRE_Pattern | re.Pattern |
| _sre.SRE_Match   | re.Match   |


#### Some additional learning points from this exercise

```python
Pattern = type(_compiler.compile('', 0))
Match = type(_compiler.compile('', 0).match(''))
```
At first glance, this looks strange.
-  Why compile an empty regex?
-  Why immediately match it?
-  Why use `type()` instead of importing classes?

To answer these questions, we need to understand the following
-   The actual implementation of regex in Python is written in **C**
   -   It lives inside a private module called **`_sre`**
    -   The classes for **compiled regex objects** and **match objects** are **not normal Python classes**
    
Now, suppose you want to check whether an object is of type Pattern.
How to do this?
The code writers of the re library found a hack. They created two objects and on purpose **named their types as `Pattern` and `Match`**
Therefore:

#### The key idea behind the hack

> **If you can’t import the class, create an instance and ask Python what its type is.**
> The hack “Creates a regex object, then capture the **class** of that object and assign it the public name `Pattern`.”
> `re.Pattern` is a public alias for a C-implemented class called `_sre.SRE_Pattern`.

So yes — `Pattern` becomes a **reference to the same class**.

#### Let us discuss the given code line by line.
The lines of code are:-

```python
Pattern = type(_compiler.compile('', 0))
Match = type(_compiler.compile('', 0).match(''))
```


##### Step 1: `_compiler.compile('', 0)`

`_compiler.compile('', 0)` 

What does this do?

-   Compiles an **empty regex pattern**
    
-   Uses flags `0` (no flags)
    
-   Returns a **compiled regex object**
    

This object is:

-   Created by the **C-based `_sre` engine**
    
-   An instance of the internal **Pattern type**
    

----------

### Step 2: `type(_compiler.compile('', 0))`

`Pattern = type(_compiler.compile('', 0))` 

This line:

-   Takes the compiled regex object
    
-   Asks Python: _“What is your class?”_
    

So now:

`Pattern == <class  '_sre.SRE_Pattern'>` 

This class is **not directly importable**, but it **exists**.

We now have a reference to the **Pattern class**.

----------



### Step 3: `.match('')`. Getting the Match type

`_compiler.compile('', 0).match('')` 

What happens here?

-   `.match('')` attempts to match the empty pattern against an empty string
    
-   This always succeeds
    
-   Returns a **match object**
    

Internally:

`match_obj = <_sre.SRE_Match object>` 

----------

##### Step 4: `type(...)`

`Match = type(_compiler.compile('', 0).match(''))` 

This line:

-   Extracts the **class** of the match object
    
-   Stores it in `Match`
    

Now:

`Match == <class  '_sre.SRE_Match'>` 

----------

##### Why is this called a “hack”?

Because:

-   The classes are **implemented in C**
    
-   They are **not directly exposed**
    
-   Python “discovers” them indirectly by:
    
    -   Creating instances
        
    -   Extracting their types
        

This is sometimes called:

-   **Type extraction by instantiation**
    
-   **Reflection-based discovery**
    

----------

##### Why doesn’t Python expose these classes normally?

Because:

-   They are **engine internals**
    
-   They were historically not meant to be public API
    
-   The `re` module abstracts them away
    

Later versions of Python _did_ expose:

`re.Pattern
re.Match` 

But internally, this hack (or something very similar) is still used.

----------

##### Why does the `re` module need these types?

###  1. `isinstance()` checks

`isinstance(obj, re.Pattern) isinstance(obj, re.Match)` 

### 2. Type annotations

`def  func(p: re.Pattern) -> re.Match:
    ...` 

### 3. Clean public API

Users see:

```python
re.Pattern
re.Match
``` 

But internally:

```python
_sre.SRE_Pattern
_sre.SRE_Match
``` 

----------

##### Why empty strings are used

Using `''` is:

-   Safe
    
-   Fast
    
-   Guaranteed to compile
    
-   Guaranteed to match
    

This avoids:

-   Errors
    
-   Edge cases
    
-   Performance cost
    

----------

----------

##### Key Takeaways

-   Python regex objects are **not pure Python classes**
    
-   They come from a **C extension**
    
-   You cannot import their classes directly
    
-   Python uses **reflection** to obtain their types
    
-   This enables:
    
    -   Type checking
        
    -   Public APIs
        
    -   Backward compatibility
        

----------

##### One-Sentence Summary 

> **When a class cannot be imported, Python creates an instance and asks it who it is.**
    



