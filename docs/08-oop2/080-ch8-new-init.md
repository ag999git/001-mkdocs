




## `__new__()` versus `__init__()`



-   Object creation in Python happens in **two steps**:
- Step 1: `__new__()` → creates the object.
- Step 2: `__init__()` → initializes the object

----------

### Simple Definition

-   `__new__()`:
    
    > Creates and returns a **new object (instance)**
    
-   `__init__()`:
    
    > Initializes the **attributes of the object**


### Comparative table

  

| Feature | `__new__()` | `__init__()` |
| --- | --- | --- |
| Purpose | Creates object | Initializes object |
| Type | Static-like method | Instance method |
| First parameter | cls (class) | self (object) |
| Called when | Before object exists | After object exists |
| Return value | Must return object | Must return None |
| Controls | Object creation | Object customization |
| Called first? | Yes | No |
| Can skip next step? | Yes. Calling `__new__()` can skip calling `__init__()` | No. Since `__init__()` is called after `__new__()`, so cannot skip it |


### Flow of Execution

```python

(1) Call ClassName()
      ↓
(2) __new__(cls)
      ↓
(3) returns object
      ↓
(4) __init__(self)

```

### The following script shows the use of `__new__()` and `__init__()`

```python

# Basic demonstration of __new__ and __init__

class Pet:

    # __init__() always gets called after an object is created. It is responsible for initializing the attributes of the object. 
    # If __new__() does not return an instance of the class, then __init__() will not be called, and the object will not be initialized properly. 
    # Therefore, it is crucial to call super().__new__(cls) within the __new__() method to ensure that an object is created before any initialization logic is executed in __init__(). This allows us to have control over the object creation process while still ensuring that the necessary initialization steps are performed correctly.
    
    def __init__(self):  # (initializer method)
        print("Step 2: __init__() called")
        self.name = "Default Pet"
    
    # __new__() always gets called before __init__() when an object is created. 
    # It is responsible for creating and returning a new instance of the class. If __new__() does not return an instance of the class, then __init__() will not be called, and the object will not be initialized properly. Therefore, it is crucial to call super().__new__(cls) within the __new__() method to ensure that an object is created before any initialization logic is executed in __init__(). This allows us to have control over the object creation process while still ensuring that the necessary initialization steps are performed correctly.
    
    def __new__(cls):  # (object creation method)
        print("Step 1: __new__() called")
        # If you want to create an object, you must call the __new__() method of the parent class (object) to actually create the object. 
        # This is done using super().__new__(cls), which ensures that the object is created properly according to the class hierarchy and memory management rules of Python. 
        # If you do not call super().__new__(cls), no object will be created, and you will not be able to initialize it with __init__() or use it in any meaningful way.
        obj = super().__new__(cls)  # Create object. 
        return obj  # Must return object

# Create object
p = Pet()  
# Output:
# Step 1: __new__() called
# Step 2: __init__() called

```


### Important Concept

-   `__new__()` creates object → returns it
    
-   That returned object becomes `self` in `__init__()`
    

----------

### Very Important Rule

> If `__new__()` does not return an object → `__init__()` will not run

----------

### Script in which `super()` is not called
In the following script, the line of script with `super()` is commented out.
As a result, `__init__()` is not called and object is not created.
>If you want to override `__new__()`, you must call super() on `__new__(cls)` using the `cls` attribute.


```python

class Pet:

    def __new__(cls):
        print("__new__ called")
        # super() not called → no object created
        # obj = super().__new__(cls)  # No object created because super() is not called, so __init__() will not be called either, and the object will not be initialized properly.
        # return obj  
        return None

    def __init__(self):
        print("__init__ called")

p = Pet()
# Output:
# __new__ called

print(p)  # p is None because __new__() returned None, so no object was created and initialized, resulting in p being assigned the value None.
# Output: None


```



### Using `__new__()` to ensure that only 1 instance of a class can be created

-   This script demonstrates how `__new__()` can be used to **control object creation**
    
-   Normally:
    
    -   Every call to a class creates a **new object**
        
-   But in some cases, we want:
    
    > Only **one object** of a class to exist (Singleton pattern)
    

----------

#### How This Script Ensures Only One Object

-   A class variable `_instance` stores the created object
    
-   In `__new__()`:
    
    -   If `_instance` is `None` → create a new object
        
    -   If `_instance` already exists → return the same object
        
-   Since `__new__()` controls object creation:
    
    -   No new object is created after the first one
        

----------

#### Key Idea

> `__new__()` decides whether to create a new object or reuse an existing one


### Script implementing singleton design pattern


```python

# Singleton using __new__()

class SingletonPet:
    _instance = None                              # (class attribute to store single object)

    def __new__(cls):                             # (object creation method)
        if cls._instance is None:                 # Check if object already exists
            print("Creating object")
            cls._instance = super().__new__(cls)  # Create object using super() to ensure proper object creation. This is crucial for the singleton pattern to work correctly, as it allows us to control the instantiation process and ensure that only one instance of the class is created throughout the program.
        else:  # If object already exists, return existing object
            print("Using existing object")
        return cls._instance

    def __init__(self):                            # (initializer method)
        print("Initializing object")

# Test the singleton implementation

s1 = SingletonPet()  # This will create a new object since _instance is initially None
# Output:
# Creating object
s2 = SingletonPet()  # s2 won't create a new object, it will return the existing object s1
# Output:
# Using existing object

print("Are both objects same?", s1 is s2)
# Output:
# Are both objects same? True


```






### The Lifecycle of Object Creation: `__new__()` vs `__init__()`

1.  **The Two-Step Process:** Object creation is a dual-stage sequence: first **`__new__()`** (Allocation) and then **`__init__()`** (Initialization).
    
2.  **Creation vs. Setup:** `__new__()` is the **constructor** that creates and returns a raw, empty instance; `__init__()` is the **initializer** that populates that instance with data.
    
3.  **Arguments:** `__new__()` receives `cls` (the class itself) as its first argument, while `__init__()` receives `self` (the instance created by `__new__()`).
    
4.  **The Silent Ancestor:** Every class inherits a default `__new__()` from the base `object` class, which handles the low-level memory allocation.
    
5.  **The Return Requirement:** If you override `__new__()`, you **must** return an instance, typically by calling `super().__new__(cls)`.
    
6.  **The Dependency:** `__init__()` is only triggered if `__new__()` returns an instance of that specific class (or a subclass).
    
7.  **Return Types:** `__new__()` must return the instance; conversely, `__init__()` must always return `None`.
    
8.  **The Orchestrator:** Classes are "callable" because their metaclass (`type`) implements `__call__`.
    
9.  **The Hidden Sequence:** When you call `MyClass()`, `type.__call__` is what actually executes the `__new__()` → `__init__()` sequence behind the scenes.
    
10.  **Immutable Types:** `__new__()` is the only way to customize the creation of immutable types (like `tuple`, `str`, or `int`), because by the time `__init__()` runs, the object is already "frozen."
    
11.  **Use Cases for `__new__()`:** Use it for advanced patterns like **Singletons**, Intercepting object creation in **Metaclasses**, or inheriting from **Immutable built-ins**.
    
12.  **Use Cases for `__init__()`:** Use it for **99% of tasks**, such as setting instance attributes and initial state.























