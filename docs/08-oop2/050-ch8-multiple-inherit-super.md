





## `super()` in Multiple Inheritance (Advanced Notes)

----------

### Core Idea

In single inheritance:

>In single inheritance, `super()` usually calls the immediate parent, because the MRO is simple.

In multiple inheritance:

> `super()` → calls the **next class in MRO**

----------

### Why This Matters

-   Ensures **each class runs exactly once**
    
-   Avoids duplicate calls (especially in diamond structure)
    
-   Enables **cooperative inheritance**
    


**Cooperative inheritance** means every class participates in the chain by calling `super()` so that all classes get executed exactly once.

----------

### Diamond Structure
```python

       Pet  
     /     \  
 Walker  Swimmer  
     \     /  
      Dog
```

Both `Walker` and `Swimmer` inherit from `Pet`  
`Dog` inherits from both

----------


### Correct Way Using `super()` (Cooperative Design)

**Key Rules of `super()` in Multiple Inheritance**

----------

#### Rule 1: It follows MRO, not hierarchy tree

Not “parent” → but **next in line**

----------

#### Rule 2: All classes must cooperate

Every class must call:

`super().__init__()`

If one class skips → chain breaks

----------

#### Rule 3: Method should exist in all classes (if chaining)

If a method uses `super()` for chaining, then every class in the MRO should either:

-  implement that method, OR

-  safely allow the chain to continue (by calling `super(`))


Otherwise:

`AttributeError`

**Why does this rule exist?**

Because `super()` keeps doing: "Call the next class in MRO"

-  It does NOT check whether the method exists later
-  It simply tries to call it

**What happens if method is missing?**

If at any step you call: `super().action()`

and the next class does NOT have `action()`

Python raises:

`AttributeError: 'super' object has no attribute 'action'`


----------

#### Rule 4: Avoid direct parent calls

Don't do (Bad):

`Pet.__init__(self)`

Do instead (Good):

`super().__init__()`



----------


<details>

<summary> Problem statement and solution to use of `super()` and MRO in Multiple Inheritance </summary>



### Problem statement and solution to use of `super()` and MRO in Multiple Inheritance 

----------

### Problem Statement

You are required to design a Python program to demonstrate how `super()` works in **multiple inheritance**, and how Python uses **Method Resolution Order (MRO)** to control execution.

----------

#### Part A: Class Design

Create the following class hierarchy:

1.  A base class `Pet` with:
    
    -   A constructor that prints: `"Pet constructor"`
        
    -   A method `action()` that prints: `"Pet action"`
        

----------

2.  Two parent classes:
    

#### (a) `Walker`

-   Inherits from `Pet`
    
-   Constructor should:
    
    -   Print `"Walker constructor"`
        
    -   Call parent constructor using `super()`
        
-   Method `action()`:
    
    -   Print `"Walking..."`
        
    -   Call next method using `super()`
        

----------

#### (b) `Swimmer`

-   Same structure as `Walker`
    
-   Replace output with `"Swimming..."`
    

----------

### Part B: Multiple Inheritance

Create two child classes:

#### (a) `Dog1`

-   Inherits from `Walker, Swimmer`
    
-   Constructor:
    
    -   Print `"Dog1 constructor"`
        
    -   Call `super()`
        
-   Method `action()`:
    
    -   Print `"Dog1 action"`
        
    -   Call `super()`
        

----------

#### (b) `Dog2`

-   Inherits from `Swimmer, Walker`
    
-   Same structure as `Dog1`
    

----------

### Part C: Execution

Write code to:

1.  Print MRO of both classes:
    
    Dog1.__mro__  
    Dog2.__mro__
    
2.  Create objects:
    
    -   `d1 = Dog1()`
        
    -   `d2 = Dog2()`
        
3.  Call:
    
    d1.action()  
    d2.action()

</details>





----------

#### Script 


```python

# BASE CLASS
class Pet:  # Base class for all pets
    def __init__(self):  # Constructor of Pet class is called when any subclass is instantiated
        print("Pet constructor")  

    def action(self):  # Common method that can be called by all subclasses
        print("Pet action")  

# FIRST PARENT
class Walker(Pet):  # Walker inherits from Pet
    def __init__(self):  # Constructor of Walker class is called when Walker object is instantiated
        print("Walker constructor") 
        super().__init__()   # Calls next class in MRO

    def action(self):  # Overrides Pet's action() and calls it using super()
        print("Walking...")
        super().action()     # Continue MRO chain

# SECOND PARENT
class Swimmer(Pet):  # Swimmer inherits from Pet
    def __init__(self):  # Constructor of Swimmer class is called when Swimmer object is instantiated
        print("Swimmer constructor")  
        super().__init__()   # Calls next class in MRO

    def action(self):  # Overrides Pet's action() and calls it using super()
        print("Swimming...")
        super().action()     # Continue MRO chain

# CHILD CLASS 1 (Walker first)
class Dog1(Walker, Swimmer):
    def __init__(self):  # Constructor of Dog1 class is called when Dog1 object is instantiated
        print("Dog1 constructor")  
        super().__init__()  
        # MRO: Dog1 → Walker → Swimmer → Pet → object

    def action(self):  # Overrides Walker's action() and calls it using super()
        print("Dog1 action")  # Method of Dog1 class is called when action() is invoked on Dog1 object
        super().action()
        # Flow follows MRO step-by-step

# CHILD CLASS 2 (Swimmer first)
class Dog2(Swimmer, Walker):
    def __init__(self):  # Constructor of Dog2 class is called when Dog2 object is instantiated
        print("Dog2 constructor")  
        super().__init__()
        # MRO: Dog2 → Swimmer → Walker → Pet → object

    def action(self):  # Overrides Swimmer's action() and calls it using super()
        print("Dog2 action")  # Method of Dog2 class is called when action() is invoked on Dog2 object
        super().action()
        # Flow follows MRO step-by-step


# TESTING Dog1
print("<---- Dog1 Execution ---->")

d1 = Dog1()  # Constructor chaining: Dog1 → Walker → Swimmer → Pet
# Expected Output: on object creation:
# Dog1 constructor
# Walker constructor
# Swimmer constructor
# Pet constructor

print("--- Calling action() ---")
d1.action()  
# Expected Output:
# Dog1 action
# Walking...
# Swimming...
# Pet action

print(Dog1.__mro__)  
# Output: (<class '__main__.Dog1'>, <class '__main__.Walker'>, <class '__main__.Swimmer'>, <class '__main__.Pet'>, <class 'object'>)
# MRO is Dog1 → Walker → Swimmer → Pet → object, which is different from Dog2 due to the different order of inheritance.
# Note: The order of method calls in action() for Dog1 and Dog2 is different due to the different MRO caused by the order of inheritance.


# TESTING Dog2
print("<---- Dog2 Execution ---->")

d2 = Dog2()  # Constructor chaining: Dog2 → Swimmer → Walker → Pet
# Expected Output: on object creation:
# Dog2 constructor
# Swimmer constructor
# Walker constructor
# Pet constructor

print("--- Calling action() ---")
d2.action()  # Expected Output:
# Dog2 action
# Swimming...
# Walking...
# Pet action

print(d2.__mro__)  
# Output: (<class '__main__.Dog2'>, <class '__main__.Swimmer'>, <class '__main__.Walker'>, <class '__main__.Pet'>, <class 'object'>)
# MRO is Dog2 → Swimmer → Walker → Pet → object, which is different from Dog1 due to the different order of inheritance.
# Note: The order of method calls in action() for Dog1 and Dog2 is different due to the different MRO caused by the order of inheritance.   

```

>Key Insight: `super()` does not mean “go to parent” — it means “go to next class in MRO”.


### Constructor Flow for `Dog1`

 - Dog1 constructor   
 - Walker constructor   
 - Swimmer constructor   
 - Pet constructor

#### Why this order?

Because MRO is:

Dog  →  Walker  →  Swimmer  →  Pet  →  object


### Method Flow for `Dog1`

 - Dog1 action   
 - Walking...   
 - Swimming...   
 - Pet action

Each class contributes once → **no duplication**


### Flow chart
**The following diagram shows how the MRO works for `__init__()` and `super()`

![Diagram](/resources/ch8-multiple-inherit-super2.png)













