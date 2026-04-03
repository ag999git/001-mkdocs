



### Research Question: The "Single Root" Architecture of Python

**Part A: Universal Ancestry and Implicit Inheritance** Investigate the role of the `object` class as the ultimate base class in Python's type hierarchy. How does the "Implicit Inheritance" of `object` provide every Python entity—whether a user-defined class or a primitive type like `int` and `str`—with its fundamental capabilities (such as identity, string representation, and memory allocation)?

**Part B: Programmatic Proof and the MRO** How do the `__mro__` (Method Resolution Order) attribute and the `issubclass()` function prove this architecture? Explain why Python 3 made inheritance from `object` implicit and identify which essential "dunder" methods are inherited even by an empty class.

----------

#### Discussion/ Solution

#### **Part A: The Foundation of Every Entity**

In Python, **everything is an object**. To make this possible, Python 3 utilizes a "Single Root" hierarchy where the built-in class `object` sits at the very top.

-   **Fundamental Capabilities:** By inheriting from `object`, every class automatically gains "low-level" logic. For instance, `__new__` handles the physical creation of the object in RAM, and `__repr__` provides a default way to display the object (e.g., `<__main__.Cat object at 0x...>`).
    
-   **Consistency:** This architecture ensures that integers, strings, and custom pets all share a common "DNA," allowing the Python interpreter to treat them uniformly in memory.
    

#### **Part B: Proving the Hierarchy**

-   **The MRO Proof:** The `__mro__` attribute (or `.mro()` method) lists the search path Python follows to find methods. No matter how complex the inheritance, the last stop is always `<class 'object'>`.
    
-   **Implicit Inheritance:** Python 3 introduced "New-Style Classes." Writing `class Cat:` is now shorthand for `class Cat(object):`. This was done to simplify syntax and ensure all classes benefit from modern OOP features like properties and descriptors.
    
-   **Inherited Dunder Methods:** An empty class still possesses over 20 methods inherited from `object`, including `__dir__` (to list attributes), `__eq__` (for equality checks), and `__init__` (the constructor).
    

----------

#### Script

This script gives a clear, "Level-based" view of ancestry.

```python

class Dog(object): pass  # Explicit
class Cat: pass         # Implicit

def deep_dive_ancestry(cls):  # A function to deeply analyze the ancestry of a class
    print(f"--- Deep Dive: {cls.__name__} ---")
    # 1. Show Parents
    print(f"Direct Parents (__bases__): {cls.__bases__}")
    
    # 2. Show Full Ancestry (MRO)
    print("Full MRO Path:")
    for i, ancestor in enumerate(cls.mro()):
        print(f"  Level {i}: {ancestor}")
    
    # 3. Boolean Proof of Inheritance
    print(f"Is it a descendant of 'object'? {issubclass(cls, object)}")
    # Output: Is it a descendant of 'object'? True
    
    # 4. Show the 'Inherited DNA' from object
    if cls == object:
        print(f"Total methods in 'object' root: {len(dir(cls))}")
    print("-" * 40)
    # Note: We won't show the actual methods here to avoid overwhelming output, but you can uncomment the next line to see them.
    # print(f"Methods inherited from object: {dir(object)}")

# 1. Test custom classes to confirm they inherit from object
deep_dive_ancestry(Dog)  # This will show that Dog inherits from object
# 1(A). --- Deep Dive: Dog ---
deep_dive_ancestry(Dog)
# Output: --- Deep Dive: Dog ---
# Direct Parents (__bases__): (<class 'object'>,)   
# Full MRO Path:
#   Level 0: <class '__main__.Dog'>
#   Level 1: <class 'object'>
# Is it a descendant of 'object'? True
# ----------------------------------------

# 1(B). --- Deep Dive: Cat ---
deep_dive_ancestry(Cat)  # This will show that Cat also inherits from object
# Output: --- Deep Dive: Cat ---
# Direct Parents (__bases__): (<class 'object'>,)
# Full MRO Path:
#   Level 0: <class '__main__.Cat'>
#   Level 1: <class 'object'>
# Is it a descendant of 'object'? True
# ----------------------------------------


# 2(A). --- Deep Dive: int ---
deep_dive_ancestry(int) # This will show that int inherits from object
# Output: --- Deep Dive: int ---
# Direct Parents (__bases__): (<class 'object'>,)
# Full MRO Path:
#   Level 0: <class 'int'>
#   Level 1: <class 'object'>
# Is it a descendant of 'object'? True
# ----------------------------------------
# 2(B). --- Deep Dive: str ---
deep_dive_ancestry(str)  # This will show that str inherits from object
# Output: --- Deep Dive: str ---
# Direct Parents (__bases__): (<class 'object'>,)
# Full MRO Path:
#   Level 0: <class 'str'>
#   Level 1: <class 'object'>
# Is it a descendant of 'object'? True
# ----------------------------------------


# 3. Test the root itself
deep_dive_ancestry(object)  # This will show that object is the root of all classes
# Output: --- Deep Dive: object ---
# Direct Parents (__bases__): ()
# Full MRO Path:
#   Level 0: <class 'object'>
# Is it a descendant of 'object'? True
# ----------------------------------------


```

#### The diagram

The following flowchart shows the hierarchy of some inbuilt and user created classes.
Note:- Exceptions as a class are discussed in the chapter on exceptions

![Diagram](/resources/ch-7-oop-object-base.png)









