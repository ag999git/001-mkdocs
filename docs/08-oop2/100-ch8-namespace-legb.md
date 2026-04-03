




### **What is `__dict__`?**

-   In Python, most objects store their attributes in a special attribute called:

`__dict__`

-   It is a **dictionary** that contains:
    -   Attribute names → keys
    -   Attribute values → values

In simple words:

> `__dict__` is the **actual namespace dictionary of an object**

----------

### Key Idea

`object.attribute  ⇔  object.__dict__['attribute']`

Both refer to the same data.

----------

### Example 1: Instance Namespace

```python

# __dict__ Demonstration
# Every object in Python has a __dict__ attribute that stores its attributes and their values in a 
# dictionary format. This allows us to see the internal state of an object and how its attributes 
# are organized.    # In this example, we define a class called Pet with an __init__ method that 
# initializes the name and type attributes. When we create an instance of the Pet class and 
# print its __dict__, we can see the attributes and their corresponding values stored in a dictionary format.  
#
class Pet:
    def __init__(self, name):
        self.name = name
        self.type = "Animal"

p = Pet("Dog")

print(p.__dict__)
# Output: {'name': 'Dog', 'type': 'Animal'}


```


#### Example 2 script


```python

# A. CLASS DEFINITION
class Dog:
    species = "Pet"  # Class attribute 

    def __init__(self, name):
        self.name = name  # Instance attribute

# B. OBJECT CREATION
d = Dog("Tommy")  

# C. NAMESPACE DISPLAY
print("Class Namespace:->", Dog.__dict__)
# Output: Class Namespace:-> {'__module__': '__main__', 'species': 'Pet',....}
print("Instance Namespace:->", d.__dict__)
# Output: Instance Namespace:-> {'name': 'Tommy'}

# D. ADD NEW ATTRIBUTE by directly modifying the instance's __dict__
d.__dict__["color"] = "Brown"
print("Added attribute 'color':->", d.color)  # Added attribute 'color':-> Brown

# E. MODIFY ATTRIBUTE by directly modifying the instance's __dict__
d.__dict__["name"] = "Bruno"  # Modifying the 'name' attribute using __dict__
print("Modified name:->", d.name)  # Modified name:-> Bruno



```



### Explanatory Note: Understanding `__dict__` using Class and Object

-   This script demonstrates how Python internally stores attributes of a **class** and its **objects (instances)** using the special attribute `__dict__`.

#### 1. Class Definition

-   The class `Dog` contains:
    -   A **class attribute** → `species = "Pet"`
    -   An **instance attribute** → `name` (created inside `__init__()`)

**Important idea:**

-   Class attributes belong to the **class namespace**
-   Instance attributes belong to the **object (instance) namespace**


#### 2. Object Creation

`d  =  Dog("Tommy")`

-   When the object `d` is created:
    -   Python first creates the object
    -   Then calls `__init__()`
    -   The attribute `name = "Tommy"` is stored in the **instance namespace**

#### 3. Viewing Namespaces using `__dict__`

`Dog.__dict__`

-   Shows the **class namespace**
-   Contains:
    -   Class variables (`species`)
    -   Methods (`__init__`)
    -   Other built-in attributes

`d.__dict__`

-   Shows the **instance namespace**
-   Contains only:
    -   `{'name': 'Tommy'}`

**Point to be noted:**

> Class and instance maintain **separate namespaces**


#### 4. Adding Attribute using `__dict__`

`d.__dict__["color"] =  "Brown"`

-   Adds a new attribute `color` to the object `d`
-   This attribute is stored in the **instance namespace**

**The above statement is equivalent to:**

`d.color =  "Brown"`

#### 5. Modifying Attribute using `__dict__`

`d.__dict__["name"] =  "Bruno"`

-   Updates the existing attribute `name`
-   Since `name` is in the instance namespace, it gets modified there

**The Output confirms:**

`Bruno`



#### 6. Key Concepts Demonstrated by the script

-   `__dict__` is a **dictionary representing namespace**
-   Class and instance have **different `__dict__`**
-   Attributes can be:
    -   **Added dynamically**
    -   **Modified dynamically**
-   Attribute access:
    
   ` d.name ⇔  d.__dict__['name']`
    

----------

#### Conclusion

> The `__dict__` attribute is the internal storage mechanism that Python uses to manage attributes of classes and objects. By accessing it directly, we can see and even manipulate how Python stores data inside objects.








### LEGB

 - While the idea of a namespace as a dictionary is very useful for
   understanding, it is important to note that Python does not simply
   store values — it stores **references to objects**. 
   
 - This means that when we write a statement like `x = 10`, the name `x` does not    “contain” the value 10; instead, it **refers to an object** (with its    own unique `id`) that represents the integer 10. 
 - This explains many    important Python behaviors such as multiple variables referring to    the same object, object mutability, and memory efficiency.
 - Further, namespaces are **dynamic** in nature — entries can be added,    modified, or removed during program execution. This is why Python    provides functions like `locals()` and `globals()` to inspect these    mappings at runtime.
 - While a namespace can be understood as a simple dictionary mapping names to objects, it is important to realise that **Python does not search all namespaces at once**. 
 - Instead, it follows a **specific resolution order called the LEGB rule (Local → Enclosing → Global → Built-in)**. 
 - Whenever a variable is used, Python looks for its name step-by-step through these nested namespaces until it finds a match. This process is called **name resolution**. 
 - If the same variable name exists in multiple namespaces, the one found first in this order is used, leading to the concept of **shadowing**, where an inner variable hides an outer one. 
 - Also, assignment behaves differently from access—when you assign a value to a variable inside a function, Python by default creates a **new local variable**, unless explicitly instructed using keywords like `global` or `nonlocal`. 
 - Understanding this dynamic lookup and binding mechanism is crucial, because it explains many subtle behaviors in Python such as variable scope errors, closures, and function behavior.


#### Summary table


  

|  | Feature | Local (L) | Enclosing (E) | Global (G) | Built-in (B) |
| --- | --- | --- | --- | --- | --- |
| 1 | Where defined? | Inside a function | Inside outer (enclosing) function | At module (file) level | Inside Python (predefined) |
| 2 | Created when? | Function is called | Outer function is called | Script starts | Python interpreter starts |
| 3 | Scope visibility | Only within that function | Available to inner functions | Available everywhere in module | Available everywhere |
| 4 | Access priority | 1st (highest) | 2nd | 3rd | 4th (lowest) |
| 5 | Lifetime | Till function execution ends | Till outer function exists | Entire program execution | Entire Python session |
| 6 | Stored in | Local namespace (locals()) | Enclosing namespace | Global namespace (globals()) | Built-in namespace (__builtins__) |
| 7 | Example (Pet) | pet = "Local Pet" | pet = "Enclosing Pet" | pet = "Global Pet" | len(), print() (Functions are also objects) |
| 8 | Accessed from inner function? | Yes | Yes | Yes | Yes |
| 9 | Accessed from outer function? | No | No | Yes | Yes |
| 10 | Can modify directly? | Yes | No (use nonlocal). | No (use global) | No |
| 11 | Keyword required to modify | No | nonlocal | global | Not allowed |
| 12 | Common use | Temporary variables | Closures, nested functions | Shared data/config | Standard functions |
| 13 | Shadowing possible? | Yes | Yes | Yes | Yes (dangerous) |
| 14 | Common mistake | Assuming it affects global | Forgetting nonlocal | Forgetting global | Overriding built-ins |
| 15 | Error if not found? | Checks next scope | Checks next scope | Checks next scope | NameError |



### Script


```python

# LEGB RULE DEMONSTRATION
# L → Local, E → Enclosing, G → Global, B → Built-in
# Python looks for variable in this order:
# 1. Local: inside current function
# 2. Enclosing: in any enclosing function (if nested)
# 3. Global: at module level
# 4. Built-in: Python's built-in names (like len, print)

# (1) GLOBAL SCOPE
# This variable is defined at the top level (module level)
# It is accessible everywhere unless shadowed

pet = "Global Pet"  # This variable belongs to the GLOBAL scope


# (2) BUILT-IN SCOPE
# Built-in functions like len() and print() are always available
# These names exist in Python's built-in namespace

print("Built-in len():", len([1, 2, 3]))  # This uses the built-in len() function to get the length of the list [1, 2, 3], which returns 3. The print() function is also a built-in that outputs the result to the console.

# (3) ENCLOSING + LOCAL SCOPE
# This demonstrates Local and Enclosing scopes

def outer_function():  # This is the outer function that defines an enclosing scope for the inner function.
    # This variable belongs to ENCLOSING scope
    pet = "Enclosing Pet"

    def inner_function():  # This is the inner function that defines a local scope. It can access variables from its own local scope, the enclosing scope (outer_function), and the global scope.
        # This variable belongs to LOCAL scope
        pet = "Local Pet"  # This variable shadows the 'pet' variable in the enclosing scope. When we refer to 'pet' inside this inner function, it will use this local variable instead of the one in the enclosing scope.

        # LEGB: Local → Enclosing → Global → Built-in
        # Python finds 'pet' in LOCAL first
        print("Inner (Local):", pet)  # Output: Inner (Local): Local Pet

    inner_function()  # This line calls the inner_function, which will execute the code inside it and print the value of 'pet' from the local scope.

    # Here LOCAL (inner) is gone → Enclosing is used
    print("Outer (Enclosing):", pet)  # Output: Outer (Enclosing): Enclosing Pet


outer_function()  # This line calls the outer_function, which will execute the code inside it, including the call to inner_function, and print the values of 'pet' from both the local and enclosing scopes.

# (4) ACCESS PRIORITY (LEGB RULE)
# If a variable is not found in Local or Enclosing,
# Python searches Global

def check_legb():  # This function demonstrates the LEGB rule by trying to access the variable 'pet'. Since there is no local variable named 'pet' in this function, and there is no enclosing function with a variable named 'pet', Python will look for 'pet' in the global scope. It will find the global variable 'pet' that we defined at the beginning of the code, which has the value "Global Pet", and print it.
    # No local 'pet', no enclosing 'pet'
    # So Python uses GLOBAL 'pet'
    print("LEGB uses Global:", pet)

check_legb()  # This line calls the check_legb function, which will execute the code inside it and print the value of 'pet' from the global scope, demonstrating the LEGB rule.

# (5) SHADOWING (VERY IMPORTANT CONCEPT)
# A variable in inner scope can "hide" (shadow) outer variable

pet = "Global Dog"  # This variable is defined in the global scope and will be shadowed by any local variable named 'pet' in a function.

def shadow_test():  # This function demonstrates variable shadowing. Inside this function, we define a local variable named 'pet' that has the same name as the global variable 'pet'. This local variable will shadow the global variable within the scope of this function, meaning that any reference to 'pet' inside this function will refer to the local variable instead of the global one.
    pet = "Local Cat"   # This shadows global 'pet'
    print("Inside function (Local):", pet)  # Output: Inside function (Local): Local Cat

shadow_test()  # This line calls the shadow_test function, which will execute the code inside it and print the value of 'pet' from the local scope, demonstrating variable shadowing.

# Global variable is NOT changed
print("Outside function (Global):", pet)  # Output: Outside function (Global): Global Dog

# (6) MODIFYING GLOBAL VARIABLE
# By default, assignment creates LOCAL variable
# To modify global variable → use 'global'

def modify_global():  # This function demonstrates how to modify a global variable from within a function. By using the 'global' keyword, we tell Python that we want to use the global variable 'pet' instead of creating a new local variable. This allows us to change the value of the global variable 'pet' from inside this function.
    global pet   # Tell Python: use global variable
    pet = "Modified Global Pet"  # This line modifies the global variable 'pet' to have the new value "Modified Global Pet".

modify_global()  # This line calls the modify_global function, which will execute the code inside it and modify the global variable 'pet'.

print("After global modification:", pet)  # Output: After global modification: Modified Global Pet
# This line prints the value of 'pet' after it has been modified by the modify_global function, demonstrating that the global variable has been successfully changed.

# (7) ERROR CASE: MODIFY WITHOUT 'global'
# Uncomment to see error

"""
def wrong_modify_global():  # This function demonstrates what happens when you try to modify a global variable without using the 'global' keyword. In this case, Python will treat 'pet' as a local variable because we are assigning a new value to it. However, since there is no local variable named 'pet' defined before the assignment, Python will raise an UnboundLocalError when it tries to read the value of 'pet' before it has been assigned in the local scope.
    pet = "Modified Global Pet"  # This line attempts to assign a new value to 'pet', but since 'pet' is not declared as global, Python treats it as a local variable. When the function tries to execute this line, it will raise an UnboundLocalError because it tries to read the value of 'pet' before it has been assigned in the local scope.
    # ERROR: Python thinks 'pet' is local (due to assignment)
    # But we are trying to read it before assignment → UnboundLocalError

wrong_modify_global()  # This line calls the wrong_modify_global function, which will execute the code inside it and raise an UnboundLocalError due to the attempt to modify a global variable without using the 'global' keyword.
"""

# (8) MODIFYING ENCLOSING VARIABLE
# To modify enclosing variable → use 'nonlocal'

def outer_modify():
    pet = "Outer Pet"

    def inner_modify():
        nonlocal pet   # Refers to enclosing variable
        pet = "Modified Enclosing Pet"

    inner_modify()
    print("After nonlocal modification:", pet)

outer_modify()


# (9) ERROR CASE: MODIFY ENCLOSING WITHOUT 'nonlocal'
# Uncomment to see behavior

"""
def wrong_enclosing():
    pet = "Outer Pet"

    def inner():
        pet = "New Value"  
        # This creates a NEW LOCAL variable
        # It does NOT modify enclosing variable

    inner()
    print("Still Outer:", pet)  # Output remains unchanged

wrong_enclosing()
"""


# (10) BUILT-IN SHADOWING (DANGEROUS)
# You can override built-in names, but it is a BAD practice

len_backup = len   # Save original function

len = 100  # Shadowing built-in function

# Uncomment below to see error
# print(len([1,2,3]))
# ERROR: 'int' object is not callable
# Because len is now an integer, not a function

# Restore built-in
len = len_backup

# (11) ERROR IF VARIABLE NOT FOUND
# If Python cannot find variable in LEGB → NameError

def error_demo():
    try:
        print(unknown_variable)
    except NameError as e:
        print("NameError occurred:", e)

error_demo()

# (12) LOCALS() AND GLOBALS()
# These functions show namespace dictionaries

def show_namespaces():
    local_var = "I am local"

    # locals() → dictionary of local variables
    print("locals():", locals())

show_namespaces()

# globals() → dictionary of global variables
print("Sample globals keys:", list(globals().keys())[:5])

# (13) BUILT-IN NAMESPACE ACCESS
# Built-ins are stored in __builtins__

print("Type of __builtins__:", type(__builtins__))

# (14) FINAL SUMMARY DEMO
# This shows full LEGB chain clearly

pet = "Global Final"

def outer_final():
    pet = "Enclosing Final"

    def inner_final():
        pet = "Local Final"
        print("Local:", pet)   # Local

    inner_final()
    print("Enclosing:", pet)   # Enclosing

outer_final()

print("Global:", pet)  # Global

```

#### Explanation of the script

#### Explanatory Note: Understanding LEGB Rule through the Script

-   This script demonstrates how Python **resolves variable names** using the **LEGB rule**:
    -   **L → Local**
    -   **E → Enclosing**
    -   **G → Global**
    -   **B → Built-in**

Whenever a variable is used, Python **searches step-by-step in this order** and stops when it finds the variable.

----------

#### 1. Global and Built-in Scope

-   The script begins by defining a **global variable** `pet = "Global Pet"`.
-   It also demonstrates **built-in functions** like `len()` and `print()`.

**Points to be noted**

-   Built-in names are always available.
-   Global variables are accessible unless **shadowed**.



#### Enclosing and Local Scope (Nested Functions)

-   The function `outer_function()` creates an **enclosing scope**.
-   Inside it, `inner_function()` creates a **local scope**.

**Important behavior:**

-   The variable `pet` exists in **three levels**:
    -   Local → `"Local Pet"`
    -   Enclosing → `"Enclosing Pet"`
    -   Global → `"Global Pet"`

**The Python Interpreter chooses:**

-   **Local first**, then **Enclosing**, then **Global**

----------

#### 3. LEGB Search in Action

-   In `check_legb()`:
    -   No local or enclosing variable exists
    -   So Python uses the **global variable**

**This shows:**

> If a name is not found, Python moves outward step-by-step

----------

#### 4. Shadowing Concept

-   Inside `shadow_test()`:
    -   A local variable `pet` hides the global variable

**Note**

-   Shadowing does **not modify** the outer variable
-   It only **hides it temporarily**



#### 5. Modifying Global Variables

-   By default, assignment inside a function creates a **local variable**
-   To modify a global variable, we must use: `global  pet`

Without `global`, Python assumes a new local variable

----------

#### 6. Common Error: UnboundLocalError

-   If we try to modify a global variable **without `global`**, Python:
    -   Treats it as `local`
    -   But tries to read it before assignment

**This causes:**

`UnboundLocalError`


#### 7. Modifying Enclosing Variables

-   To modify a variable in an enclosing function, we use: `nonlocal  pet`

This allows inner functions to modify outer variables

----------

#### 8. Common Behavior without `nonlocal`

-   Without `nonlocal`:
    -   A new local variable is created
    -   Enclosing variable remains unchanged

----------

#### 9. Built-in Shadowing (Dangerous)

-   The script shows that built-in names like `len` can be overridden:

`len  =  100`

This breaks normal behavior:

-   `len()` stops working

**Note:- Always avoid using built-in names as variables**

----------

#### 10. Name Resolution Failure

-   If a variable is not found in any scope (L → E → G → B):

**Python raises:**  `NameError`



#### 11. Namespace Inspection

-   The script uses:
    -   `locals()` → shows local variables
    -   `globals()` → shows global variables

These return **`dictionaries (namespaces)`**

----------

#### 12. Built-in Namespace Access

-   Built-in names are stored in: `__builtins__`



#### 13. Final Demonstration

-   The last part shows all three scopes together:
    -   Local → used inside inner function
    -   Enclosing → used in outer function
    -   Global → used outside

This clearly shows the **complete LEGB chain**

----------

#### Conclusion

-   Python does **not search all variables at once**
-   It follows a **strict order (LEGB)**
-   Inner scopes can access outer scopes, but not vice versa
-   Assignment rules are different from access rules

















