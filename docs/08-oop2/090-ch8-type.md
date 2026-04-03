



## PART 1: Basic concepts of metaclasses

----------

### 1. What is a Metaclass? (Simple Definition)

-   A **metaclass** is:
    
    > A class that **creates other classes**
    

----------

### 2. Understanding the Hierarchy

(1) Metaclass → creates → Class   
(2) Class → creates → Object 

----------

### What happens behind the scene when you create a class in Python

Suppose you dont use metaclasses but simply create a class as follows:


### 3. Basic Example

#### Explanation of the script given below:





-   This script demonstrates that in Python, **classes can be created in two ways**:
    
    -   Using the `class` keyword (normal way)
        
    -   Using the built-in `type()` function (advanced way)
        

----------

**Core Idea**

-   Python internally uses `type()` to create classes
    
-   The `class` keyword is simply a **simplified and readable way** of doing the same thing
    

----------
**What This Script Will Show**

1.  How a simple class (like `Dog`) is **converted internally** into a `type()` call
    
2.  How we can **manually create a class** using `type()`
    
3.  How to:
    
    -   Add **attributes** (like `sound`, `breed`)
        
    -   Add **methods** (like `speak()`)
        
4.  How to create an **object from the dynamically created class**
    

----------

**Important Concepts Used**

-   `type(class_name, bases, dictionary)`
    
    -   `class_name` → Name of the class
        
    -   `bases` → Parent classes (empty tuple means no inheritance)
        
    -   `dictionary` → Attributes and methods of the class
        

----------

**Why This is Important**

-   Helps understand how Python works **internally**
    
-   Used in:
    
    -   Frameworks
        
    -   Dynamic class creation
        
    -   Advanced programming
        

----------

**Logic of the Script**

-   First, we define a normal class and show its equivalent `type()` version
    
-   Then, we:
    
    -   Add attributes using a dictionary
        
    -   Add methods using functions
        
    -   Combine them into a class
        
-   Finally, we create an object and call its method
    

----------

**Key Takeaway**

> A class in Python is just an object created by `type()`, and we can create it manually if needed


#### Creating a Python class "normally" that is without using "type"

```python

class Dog:  # Define a simple class named Dog
    sound = "Woof"

```

#### Creating a Python class using "type"


```python

# In Python, you can create classes dynamically using the `type()` function. This allows you 
# to define a class at runtime, which can be useful in certain scenarios where you need to 
# generate classes based on user input, configuration, or other dynamic factors. 

# The `type()` function takes three arguments: 
# 1. the name of the class as a string, 
# 2. a tuple of base classes (for inheritance), and 
# 3. a dictionary of attributes and methods for the class.

Dog = type("Dog", (), {"sound": "Woof"})  # type() is a built-in function that can be used to create classes dynamically.   
print(Dog.sound)  # Output: Woof
# We created a class named "Dog" with no base classes (empty tuple) and a class attribute "sound" with the value "Woof".

# You can add attributes to the class as well
dict_attributes = {"sound": "Woof", "breed": "Labrador"}
Dog = type("Dog", (), dict_attributes)
print(Dog.sound)  # Output: Woof
print(Dog.breed)  # Output: Labrador

# You can also add methods to the class
# Define a method to be added to the class
def speak(self):
    return f"{self.sound}!"

dict_methods = {"speak": speak}  # Dictionary of methods to be added to the class
dict_merged = {**dict_attributes, **dict_methods}  # Merge attributes and methods into one dictionary
Dog = type("Dog", (), dict_merged)  # Use the merged dictionary
dog_instance = Dog()
print(dog_instance.speak())  # Output: Woof!



```

### Diagram showing the flow of execution of above script


![Diagram](/resources/ch-8-type-explain.png)


### What does the above script do?

-   You are **directly calling the metaclass**
-   You are **manually creating a class**
-   This is used in:
    -   Dynamic class creation
    -   Frameworks
    -   Advanced programming

### Comparison table

  

|  | Feature | Implicit (class keyword) | Explicit (type) |
| --- | --- | --- | --- |
| 1 | Syntax | class Dog: | type("Dog", ...) |
| 2 | Ease of use | Very easy | Less readable |
| 3 | Control | Limited | Full control |
| 4 | Usage | Normal programming | Advanced / dynamic cases |

### Important Insight

> Both approaches create **exactly the same kind of class object**



### The following table summarizes the two different routes followed 


  

| Step No. | Step Name | Normal Route (Default type) | Metaclass Route (PetMeta) | Key Insight |
| --- | --- | --- | --- | --- |
| 1 | Class Definition Encountered | Python sees class Dog: | Python sees class Dog(metaclass=PetMeta): | This is where the path diverges |
| 2 | Decide Class Creator | Uses default metaclass → type | Uses custom metaclass → PetMeta | Every class is created by a metaclass |
| 3 | Prepare Class Components | Collects name, bases, and dictionary (__dict__) | Same: name, bases, dct collected | Both routes start identically |
| 4 | Call Class Constructor | type(name, bases, dct) is called | PetMeta(name, bases, dct) is called | Metaclass replaces type |
| 5 | Execute __new__() of Metaclass | type.__new__() runs silently | PetMeta.__new__() runs (custom logic) | Control point for customization |
| 6 | Modify Class (Optional) | No modification (default behavior) | Can modify dct (e.g., add category) | This is where "magic" happens |
| 7 | Create Class Object | Class Dog is created normally | Class Dog is created with modifications | Output is still a class object |
| 8 | Class Ready | Dog has only defined attributes | Dog has auto-added attributes | Behavior difference appears here |
| 9 | Object Creation | dog = Dog() | dog = Dog() | Object creation is SAME in both |
| 10 | Call __new__() (instance) | Dog.__new__() runs | Same | Metaclass does NOT affect instance creation directly |
| 11 | Call __init__() | Initializes object | Same | Object-level logic unchanged |
| 12 | Final Object | Normal object | Object of modified class | Difference comes from class design |














